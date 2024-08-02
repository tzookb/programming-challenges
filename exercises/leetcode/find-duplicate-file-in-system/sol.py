class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_contents = {}

        for pathsrow in paths:
            items = pathsrow.split(" ")
            folder = items[0]
            file_names_content = items[1:]
            for fnc in file_names_content:
                file_name, content = fnc.split("(")
                content = content[0:-1]
                full_path = folder + "/" + file_name
                file_contents[full_path] = content
        
        content_to_file = {}

        for filename in file_contents:
            content = file_contents[filename]
            if content not in content_to_file:
                content_to_file[content] = []
            content_to_file[content].append(filename)


        final = []
        for contentKey in content_to_file:
            if len(content_to_file[contentKey]) <= 1:
                continue
            final.append(content_to_file[contentKey])

        return final