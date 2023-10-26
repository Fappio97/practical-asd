import sys, re


class Authors:
    def __init__(self):
        self.authors = {}

    def business_logic(self, file_path):
        f = open(file_path, "r")
        row = f.readline()
        while row != "":
            # print(row)
            x = re.match(r"^Author:\s+(\w+\s*\w*)\s+<", row)
            if bool(x) and x.groups()[0]:
                if x.groups()[0] in self.authors:
                    self.authors[x.groups()[0]] += 1
                else:
                    self.authors[x.groups()[0]] = 1
            row = f.readline()
        f.close()

        for i in self.authors.keys():
            print(i + " " + str(self.authors[i]))


if __name__ == "__main__":
    Authors().business_logic(sys.argv[1])
