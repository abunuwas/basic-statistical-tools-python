
class Bayesian:
    def __init__(self, prior_probability, sensitivity, specificity,
        testResult):
        self.prior_probability = prior_probability
        self.sensitivity = sensitivity
        self.specificity = specificity
        self.p_not_c = 1-prior_probability
        self.p_neg_c = 1-sensitivity
        self.pos_notC = 1-specificity
        self.testResult = testResult
        self.test = testResult[0:3].title()
        print('''
P(C) = {0:1.3f}  -  P(¬C) = {1:1.3f}
P(Pos|C) = {2:1.3f}  -  P(Neg|C) = {3:1.3f}
P(Neg|¬C) = {4:1.3f}  -  P(Pos|¬C) = {5:1.3f}
'''.format(self.prior_probability, self.p_not_c,
           self.sensitivity, self.p_neg_c,
           self.specificity, self.pos_notC))

    def jointProbability(self):
        if self.testResult == 'positive':
            parameter1 = self.sensitivity
            parameter2 = self.pos_notC
        if self.testResult == 'negative':
            parameter1 = self.p_neg_c
            parameter2 = self.specificity
        p_c = self.prior_probability * parameter1
        p_notC = self.p_not_c * parameter2
        print('''
P(C, {2}) = {0:1.3f}
P(¬C, {3}) = {1:1.3f}
'''.format(p_c, p_notC, self.test, self.test))
        return p_c, p_notC

    def normalize(self, p_c_neg, p_notC_neg):
        p_c, p_notC = self.jointProbability()
        normalizer = p_c + p_notC
        print('''
P({1}) = {0:1.3f}
'''.format(normalizer, self.test))
        return normalizer

    def posteriorProbability(self):
        p_c, p_notC = self.jointProbability()
        normalizer = self.normalize(p_c, p_notC)
        posterior_c = p_c/normalizer
        posterior_notC = p_notC/normalizer
        print('''
P(C|{2}) = {0:1.4f}
P(¬C|{3}) = {1:1.4f}
'''.format(posterior_c, posterior_notC, self.test, self.test))
        return posterior_c, posterior_notC

## Example of use
prob1 = Bayesian(0.9, 0.9, 0.8, 'positive')
p_c, p_notC = prob1.jointProbability()
prob1.normalize(p_c, p_notC)
prob1.posteriorProbability()
