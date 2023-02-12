probAge1 = 0.138613
utilAge1 = [60, 25, 15]
probAge2 = 0.138613
utilAge2 = [20, 50, 30]
probAge3 = 0.267326
utilAge3 = [5, 20, 75]

probCp1 = 0.280528
utilCp1 = [75, 15, 10]
probCp2 = 0.135313
utilCp2 = [21, 50, 29]
probCp3 = 0.128712
utilCp3 = [7, 28, 65]

probChol1 = 0.099009
utilChol1 = [70, 20, 10]
probChol2 = 0.194719
utilChol2 = [20, 50, 30]
probChol3 = 0.250825
utilChol3 = [5, 15, 120]

probFbs1 = 0.468646
utilFbs1 = [10, 15, 3]
probFbs2 = 0.759075
utilFbs2 = [3, 10, 15]

result = []


def bigger(list):
    big_value = -1
    index_list = -1

    for i in range(len(list)):
        max_value = max(list[i])
        if max_value > big_value:
            big_value = max_value
            index_list = i
    return index_list


class Dados:

    def __init__(self, age, cp, chol, fbs):
        self.age = age
        self.cp = cp
        self.chol = chol
        self.fbs = fbs
        self.classAge = None
        self.classCp = None
        self.classChol = None
        self.classFbs = None

    def setClassAge(self):
        if self.age < 45:
            result = [probAge1 * utilAge1[0], probAge1 *
                      utilAge1[1], probAge1 * utilAge1[2]]
            self.classAge = 1
            return result
        elif self.age < 53:
            result = [probAge2 * utilAge2[0], probAge2 *
                      utilAge2[1], probAge2 * utilAge2[2]]
            self.classAge = 2
            return result
        else:
            result = [probAge3 * utilAge3[0], probAge3 *
                      utilAge3[1], probAge3 * utilAge3[2]]
            self.classAge = 3
            return result

    def setClassCp(self):
        if self.cp >= 2:
            result = [probCp1 * utilCp1[0], probCp1 *
                      utilCp1[1], probCp1 * utilCp1[2]]
            self.classCp = 1
            return result
        elif self.cp == 1:
            result = [probCp2 * utilCp2[0], probCp2 *
                      utilCp2[1], probCp2 * utilCp2[2]]
            self.classCp = 2
            return result
        else:
            result = [probCp3 * utilCp3[0], probCp3 *
                      utilCp3[1], probCp3 * utilCp3[2]]
            self.classCp = 3
            return result

    def setClassChol(self):
        if self.chol < 200:
            result = [probChol1 * utilChol1[0], probChol1 *
                      utilChol1[1], probChol1 * utilChol1[2]]
            self.classChol = 1
            return result
        elif self.chol < 240:
            result = [probChol2 * utilChol2[0], probChol2 *
                      utilChol2[1], probChol2 * utilChol2[2]]
            self.classChol = 2
            return result
        else:
            result = [probChol3 * utilChol3[0], probChol3 *
                      utilChol3[1], probChol3 * utilChol3[2]]
            self.classChol = 3
            return result

    def setClassFbs(self):
        if self.fbs == 0:
            result = [probFbs1 * utilFbs1[0], probFbs1 *
                      utilFbs1[1], probFbs1 * utilFbs1[2]]
            self.classFbs = 1
            return result
        else:
            result = [probFbs2 * utilFbs2[0], probFbs2 *
                      utilFbs2[1], probFbs2 * utilFbs2[2]]
            self.classFbs = 2
            return result


idade = int(input("Digite uma idade: "))
dor = int(input("Dor no peito (Escala de 0 a 3): "))
colesterol = int(input("Colesterol: "))
sugar = int(
    input("Açucar no sangue é maior que 120 (1 = Verdade, 0 = Mentira): "))

d = Dados(idade, dor, colesterol, sugar)
resultAge = d.setClassAge()
resultCp = d.setClassCp()
resultChol = d.setClassChol()
resultFbs = d.setClassFbs()

results = [resultAge, resultCp, resultChol, resultFbs]

index_list = bigger(results)

if index_list == 0:
    if d.classAge == 1:
        print("Coração ta saudável, sem problemas de saúde.")
    elif d.classAge == 2:
        print("É recomendável melhorar sua alimentação.")
    else:
        print("Procure um médico imediatamente.")
elif index_list == 1:
    if d.classCp == 1:
        print("Coração ta saudável, sem problemas de saúde.")
    elif d.classCp == 2:
        print("É recomendável melhorar sua alimentação.")
    else:
        print("Procure um médico imediatamente.")
elif index_list == 2:
    if d.classChol == 1:
        print("Coração ta saudável, sem problemas de saúde.")
    elif d.classChol == 2:
        print("É recomendável melhorar sua alimentação.")
    else:
        print("Procure um médico imediatamente.")
else:
    if d.classFbs == 1:
        print("Coração ta saudável, sem problemas de saúde.")
    else:
        print("É recomendável melhorar sua alimentação.")
