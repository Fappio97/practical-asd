import sys, re


def read_input(file_path) -> list:
    value = []
    f = open(file_path, "r")
    row = f.readline()
    while row != "":
        value.append(row)
        row = f.readline()
    f.close()
    return value


class SHA_1:
    def __init__(self, sha):
        self.commit = []
        self.sha = sha

    def business_logic(self, value: list):
        for i in value:
            x = re.match(r"^commit\s+(.*)", i)
            if bool(x) and self.sha in x.groups()[0]:
                self.commit.append(x.groups()[0])

        print(self.commit)


if __name__ == "__main__":
    SHA_1(sys.argv[1]).business_logic(read_input(sys.argv[2]))
