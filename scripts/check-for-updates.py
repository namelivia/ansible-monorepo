import os
import subprocess
import requests
import semver

class TagsRequestResponse:
    def __init__(self, count, next, previous, results):
        self.count = count
        self.next = next
        self.previous = previous
        self.results = results

class ImageDeclaration:
    def __init__(self, file, line, content):
        self.file = file
        self.line = line
        self.content = content
        self.image = content.split("\"")[1]

    def __str__(self):
        return f"{self.file}:{self.line} - {self.content} > {self.image}"

class UpdateProposal:
    def __init__(self, image_declaration, current_version, latest_version):
        self.image_declaration = image_declaration
        self.current_version = current_version
        self.latest_version = latest_version
        self.approved = False

    def approve(self):
        self.approved = True

    def apply(self):
        file = self.image_declaration.file
        line = self.image_declaration.line
        old_content = self.image_declaration.content
        new_content = old_content.replace(str(self.current_version), str(self.latest_version))
        print(f"In file {file} at line {line}")
        print(f"Old content: {old_content}")
        print(f"New content: {new_content}")


class Tag:
    def __init__(
        self,
        creator,
        id,
        images,
        last_updated,
        last_updater,
        last_updater_username,
        name,
        repository,
        full_size,
        v2,
        tag_status,
        tag_last_pulled,
        tag_last_pushed,
        media_type,
        content_type,
        digest = None
    ):
        self.creator = creator
        self.id = id
        self.images = images
        self.last_updated = last_updated
        self.last_updater = last_updater
        self.last_updater_username = last_updater_username
        self.name = name
        self.repository = repository
        self.full_size = full_size
        self.v2 = v2
        self.tag_status = tag_status
        self.tag_last_pulled = tag_last_pulled
        self.tag_last_pushed = tag_last_pushed
        self.media_type = media_type
        self.content_type = content_type
        self.digest = digest


def parse_docker_image(image):
    namespace = image.split('/')[0]
    if namespace == image:
        namespace = "library"
        name = image.split(':')[0]
    else:
        name = image.split('/')[1].split(':')[0]
    tag = image.split(':')[1]
    return namespace, name, tag

EXCLUSIONS = "roles/ansible-pleroma"  # This image is directly built from the source code
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(BASE_DIR)

up_to_date = []
outdated = []
cant_check = []

def find_image_declarations():
    image_declarations = []
    roles_folders = os.listdir(os.path.join(BASE_DIR, "roles"))
    for role_folder in roles_folders:
        main_task_yml = os.path.join(BASE_DIR, "roles", role_folder, "tasks", "main.yml")
        if os.path.exists(main_task_yml):
            with open(main_task_yml, "r") as f:
                for number, line in enumerate(f.readlines()):
                    if "image: \"" in line:
                        image_declarations.append(ImageDeclaration(main_task_yml, number, line))
    return image_declarations
                        

image_declarations = find_image_declarations()

proposals = []
for image_declaration in image_declarations:
    namespace, name, current_tag = parse_docker_image(image_declaration.image)
    try:
        current_tag = semver.VersionInfo.parse(current_tag)
    except ValueError:
        #print(f"Skipping {image} as it is not a valid semver tag")
        cant_check.append(image_declaration.image)
        continue
    response = requests.get(f"https://hub.docker.com/v2/namespaces/{namespace}/repositories/{name}/tags?page_size=100")
    if response.ok:
        response = TagsRequestResponse(**response.json())
        tags = [Tag(**tag) for tag in response.results]
        parsed_tags = []
        for tag in tags:
            try:
                parsed_tags.append(semver.VersionInfo.parse(tag.name))
            except ValueError:
                continue
        latest_tag = max(parsed_tags)
        if latest_tag > current_tag:
            proposal = UpdateProposal(image_declaration, current_tag, latest_tag)
            proposals.append(proposal)
            outdated.append(image_declaration.image)
        else:
            #print(f"{namespace}/{name} is up to date")
            up_to_date.append(image_declaration.image)

    else:
        #print(f"Failed to fetch tags for {namespace}/{name}")
        continue

for proposal in proposals:
    proposal.apply()
