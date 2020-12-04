import re

data = open("/content/drive/MyDrive/Datasets/AdventOfCode/passport.txt").read().split("\n\n")[:]


class Validate():
    def __init__(self, data):
        self.data = data
        self.primary_validated = []
        self.secondary_validated = []
        self.count = 0
        self.requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        
    def primary_validation(self):
        for i in self.data:
            self.match = True
            for j in self.requirements:
                if j not in i:
                    self.match = False
            if self.match:
                self.primary_validated.append(i)
                self.count += 1

        return self.primary_validated

    
    def validate_birth_year(self, id):
        return re.search('byr:19[2-9][0-9]|byr:200[0-2]', id)

    def validate_issue_year(self, id):
        return re.search('iyr:201[0-9]|iyr:2020', id)
    
    def validate_expiration_year(self, id):
        return re.search('eyr:202[0-9]|eyr:2030', id)
    
    def validate_height(self, id):
        if re.search('cm', id):
            return re.search('hgt:1[5-8][0-9]|hgt:19[0-3]', id)
        elif re.search('in', id):
            return re.search('hgt:59|hgt:6[0-9]|hgt:7[0-6]', id)
        else:
            return None
    
    def validate_hair_colour(self, id):
        return re.search('#[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]', id)
    
    def validate_eye_colour(self, id):
        return re.search('ecl:amb|ecl:blu|ecl:brn|ecl:gry|ecl:grn|ecl:hzl|ecl:oth', id)

    def validate_passport_id(self, id):
        return re.search('pid:\d{9}', id)

    def secondary_validation(self):
        self.primary_validated = self.primary_validation()
        bc = 0
        for i in self.primary_validated:
            self.match = True
            if not self.validate_birth_year(i):
                print(i, "\n-----")
                self.match = False
                continue

            if not self.validate_issue_year(i):
                self.match = False
                continue
                
            if not self.validate_expiration_year(i):
                self.match = False
                continue
            
            if not self.validate_height(i):
                
                self.match = False
                continue
            
            if not self.validate_hair_colour(i):
                self.match = False
                continue
            
            if not self.validate_eye_colour(i):
                self.match = False
                continue
            
            if not self.validate_passport_id(i):
                self.match = False
                continue

            if self.match:
                self.secondary_validated.append(i)
            self.match = True

        print(len(self.secondary_validated))
        return len(self.secondary_validated)
validate = Validate(data)
print(validate.secondary_validation())
