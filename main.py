import numpy as np
import skfuzzy as fuzzy
import skfuzzy.control as ctrl
from IPython.display import Image

maths = ctrl.Antecedent(np.arange(0, 11, 1), 'Maths')
coding = ctrl.Antecedent(np.arange(0, 11, 1), 'Coding')
networking = ctrl.Antecedent(np.arange(0, 11, 1), 'Networking')
embedded_sys = ctrl.Antecedent(np.arange(0, 11, 1), 'Embedded')
database = ctrl.Antecedent(np.arange(0, 11, 1), 'DataBase')

crypto = ctrl.Consequent(np.arange(0, 101, 1), 'Crypto')
ml = ctrl.Consequent(np.arange(0, 101, 1), 'Machine Learning')
embedded_design = ctrl.Consequent(np.arange(0, 101, 1), 'embedded design')
cloud_computing = ctrl.Consequent(np.arange(0, 101, 1), 'Cloud computing')
iot = ctrl.Consequent(np.arange(0, 101, 1), 'IOT')

low = [-2, 0, 3, 7.5]
medium_pre = [3, 5, 7]
high = [2.5, 7, 10, 11]

not_recommend = [-1, 0, 15, 50]
recommend = [50, 85, 100, 101]
medium_res = [20, 50, 80]

for item in [maths, coding, networking, embedded_sys, database]:
    item['low'] = fuzzy.trapmf(x=item.universe, abcd=low)
    item['medium'] = fuzzy.trimf(x=item.universe, abc=medium_pre)
    item['high'] = fuzzy.trapmf(x=item.universe, abcd=high)

for item in [crypto, ml, embedded_design, cloud_computing, iot]:
    item['Not_Recommend'] = fuzzy.trapmf(x=item.universe, abcd=not_recommend)
    item['Recommend'] = fuzzy.trapmf(x=item.universe, abcd=recommend)
    item['Medium'] = fuzzy.trimf(x=item.universe, abc=medium_res)

maths.view()
coding.view()
networking.view()
embedded_sys.view()
database.view()

crypto.view()
ml.view()
embedded_design.view()
iot.view()
cloud_computing.view()

ml_rule1 = ctrl.Rule(maths['low'] & coding['low'], ml['Not_Recommend'])
ml_rule2 = ctrl.Rule(maths['low'] & coding['medium'], ml['Not_Recommend'])
ml_rule3 = ctrl.Rule(maths['low'] & coding['high'], ml['Medium'])
ml_rule4 = ctrl.Rule(maths['medium'] & coding['low'], ml['Not_Recommend'])
ml_rule5 = ctrl.Rule(maths['medium'] & coding['medium'], ml['Medium'])
ml_rule6 = ctrl.Rule(maths['medium'] & coding['high'], ml['Recommend'])
ml_rule7 = ctrl.Rule(maths['high'] & coding['low'], ml['Medium'])
ml_rule8 = ctrl.Rule(maths['high'] & coding['medium'], ml['Recommend'])
ml_rule9 = ctrl.Rule(maths['high'] & coding['high'], ml['Recommend'])

ml_rule1.view()

crypto_rule1 = ctrl.Rule(maths['low'] & networking['low'], crypto['Not_Recommend'])
crypto_rule2 = ctrl.Rule(maths['low'] & networking['medium'], crypto['Not_Recommend'])
crypto_rule3 = ctrl.Rule(maths['low'] & networking['high'], crypto['Medium'])
crypto_rule4 = ctrl.Rule(maths['medium'] & networking['low'], crypto['Not_Recommend'])
crypto_rule5 = ctrl.Rule(maths['medium'] & networking['medium'], crypto['Medium'])
crypto_rule6 = ctrl.Rule(maths['medium'] & networking['high'], crypto['Recommend'])
crypto_rule7 = ctrl.Rule(maths['high'] & networking['low'], crypto['Medium'])
crypto_rule8 = ctrl.Rule(maths['high'] & networking['medium'], crypto['Recommend'])
crypto_rule9 = ctrl.Rule(maths['high'] & networking['high'], crypto['Recommend'])

crypto_rule1.view()

iot_rule1 = ctrl.Rule(coding['low'] & networking['low'] & embedded_sys['low'], iot['Not_Recommend'])
iot_rule2 = ctrl.Rule(coding['low'] & networking['low'] & embedded_sys['medium'], iot['Not_Recommend'])
iot_rule3 = ctrl.Rule(coding['low'] & networking['low'] & embedded_sys['high'], iot['Medium'])
iot_rule4 = ctrl.Rule(coding['low'] & networking['medium'] & embedded_sys['low'], iot['Not_Recommend'])
iot_rule5 = ctrl.Rule(coding['low'] & networking['medium'] & embedded_sys['medium'], iot['Medium'])
iot_rule6 = ctrl.Rule(coding['low'] & networking['medium'] & embedded_sys['high'], iot['Medium'])
iot_rule7 = ctrl.Rule(coding['low'] & networking['high'] & embedded_sys['low'], iot['Medium'])
iot_rule8 = ctrl.Rule(coding['low'] & networking['high'] & embedded_sys['medium'], iot['Medium'])
iot_rule9 = ctrl.Rule(coding['low'] & networking['high'] & embedded_sys['high'], iot['Medium'])
iot_rule10 = ctrl.Rule(coding['medium'] & networking['low'] & embedded_sys['low'], iot['Not_Recommend'])
iot_rule11 = ctrl.Rule(coding['medium'] & networking['low'] & embedded_sys['medium'], iot['Medium'])
iot_rule12 = ctrl.Rule(coding['medium'] & networking['low'] & embedded_sys['high'], iot['Medium'])
iot_rule13 = ctrl.Rule(coding['medium'] & networking['medium'] & embedded_sys['low'], iot['Medium'])
iot_rule14 = ctrl.Rule(coding['medium'] & networking['medium'] & embedded_sys['medium'], iot['Medium'])
iot_rule15 = ctrl.Rule(coding['medium'] & networking['medium'] & embedded_sys['high'], iot['Medium'])
iot_rule16 = ctrl.Rule(coding['medium'] & networking['high'] & embedded_sys['low'], iot['Medium'])
iot_rule17 = ctrl.Rule(coding['medium'] & networking['high'] & embedded_sys['medium'], iot['Medium'])
iot_rule18 = ctrl.Rule(coding['medium'] & networking['high'] & embedded_sys['high'], iot['Recommend'])
iot_rule19 = ctrl.Rule(coding['high'] & networking['low'] & embedded_sys['low'], iot['Medium'])
iot_rule20 = ctrl.Rule(coding['high'] & networking['low'] & embedded_sys['medium'], iot['Medium'])
iot_rule21 = ctrl.Rule(coding['high'] & networking['low'] & embedded_sys['high'], iot['Medium'])
iot_rule22 = ctrl.Rule(coding['high'] & networking['medium'] & embedded_sys['low'], iot['Medium'])
iot_rule23 = ctrl.Rule(coding['high'] & networking['medium'] & embedded_sys['medium'], iot['Medium'])
iot_rule24 = ctrl.Rule(coding['high'] & networking['medium'] & embedded_sys['high'], iot['Recommend'])
iot_rule25 = ctrl.Rule(coding['high'] & networking['high'] & embedded_sys['low'], iot['Medium'])
iot_rule26 = ctrl.Rule(coding['high'] & networking['high'] & embedded_sys['medium'], iot['Recommend'])
iot_rule27 = ctrl.Rule(coding['high'] & networking['high'] & embedded_sys['high'], iot['Recommend'])

iot_rule1.view()

embedded_rule1 = ctrl.Rule(coding['low'] & embedded_sys['low'], embedded_design['Not_Recommend'])
embedded_rule2 = ctrl.Rule(coding['low'] & embedded_sys['medium'], embedded_design['Not_Recommend'])
embedded_rule3 = ctrl.Rule(coding['low'] & embedded_sys['high'], embedded_design['Medium'])
embedded_rule4 = ctrl.Rule(coding['medium'] & embedded_sys['low'], embedded_design['Not_Recommend'])
embedded_rule5 = ctrl.Rule(coding['medium'] & embedded_sys['medium'], embedded_design['Medium'])
embedded_rule6 = ctrl.Rule(coding['medium'] & embedded_sys['high'], embedded_design['Recommend'])
embedded_rule7 = ctrl.Rule(coding['high'] & embedded_sys['low'], embedded_design['Medium'])
embedded_rule8 = ctrl.Rule(coding['high'] & embedded_sys['medium'], embedded_design['Recommend'])
embedded_rule9 = ctrl.Rule(coding['high'] & embedded_sys['high'], embedded_design['Recommend'])

embedded_rule1.view()

cc_rule1 = ctrl.Rule(networking['low'] & database['low'], cloud_computing['Not_Recommend'])
cc_rule2 = ctrl.Rule(networking['low'] & database['medium'], cloud_computing['Not_Recommend'])
cc_rule3 = ctrl.Rule(networking['low'] & database['high'], cloud_computing['Medium'])
cc_rule4 = ctrl.Rule(networking['medium'] & database['low'], cloud_computing['Not_Recommend'])
cc_rule5 = ctrl.Rule(networking['medium'] & database['medium'], cloud_computing['Medium'])
cc_rule6 = ctrl.Rule(networking['medium'] & database['high'], cloud_computing['Recommend'])
cc_rule7 = ctrl.Rule(networking['high'] & database['low'], cloud_computing['Medium'])
cc_rule8 = ctrl.Rule(networking['high'] & database['medium'], cloud_computing['Recommend'])
cc_rule9 = ctrl.Rule(networking['high'] & database['high'], cloud_computing['Recommend'])

cc_rule1.view()

recommender_ctrl = ctrl.ControlSystem(rules=[ml_rule1, ml_rule2, ml_rule3, ml_rule4, ml_rule5, ml_rule6, ml_rule7, ml_rule8, ml_rule9,
                                             crypto_rule1, crypto_rule2, crypto_rule3, crypto_rule4, crypto_rule5, crypto_rule6, crypto_rule7, crypto_rule8, crypto_rule9,
                                             iot_rule1, iot_rule2, iot_rule3, iot_rule4, iot_rule5, iot_rule6, iot_rule7, iot_rule8, iot_rule9, iot_rule10, iot_rule11,
                                             iot_rule12, iot_rule13, iot_rule14, iot_rule15, iot_rule16, iot_rule17, iot_rule18, iot_rule19, iot_rule20, iot_rule21,
                                             iot_rule22, iot_rule23, iot_rule24, iot_rule25, iot_rule26, iot_rule27,
                                             cc_rule1, cc_rule2, cc_rule3, cc_rule4, cc_rule5, cc_rule6, cc_rule7, cc_rule8, cc_rule9,
                                             embedded_rule1, embedded_rule2, embedded_rule3, embedded_rule4, embedded_rule5, embedded_rule6, embedded_rule7, embedded_rule8, embedded_rule9])
simulation = ctrl.ControlSystemSimulation(control_system=recommender_ctrl)

simulation.input['Maths'] = 8
simulation.input['Coding'] = 7
simulation.input['Networking'] = 4
simulation.input['Embedded'] = 8
simulation.input['DataBase'] = 5

simulation.compute()
print(simulation.output['Crypto'])
print(simulation.output['Machine Learning'])
print(simulation.output['embedded design'])
print(simulation.output['Cloud computing'])
print(simulation.output['IOT'])
crypto.view(sim=simulation)
ml.view(sim=simulation)
embedded_design.view(sim=simulation)
cloud_computing.view(sim=simulation)
iot.view(sim=simulation)