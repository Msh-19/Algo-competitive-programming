class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_address = defaultdict(list)
        for i in range(len(paths)):
            files = paths[i].split(" ")
            directory = files[0]

            for file in files[1:]:
                name, content = file.split("(")
                content_address[content[:-1]].append(directory + '/' + name)

        return [content_address[content] for content in content_address if len(content_address[content]) > 1]
