#print("Droplet removal size of liquid in the gas phase (microns):")
#dm_liquid = float(input())
dm_liquid = 140

#print("oil density (lb/ft^3): ")
#oil_density = float(input())
oil_density = 54.67
#print("Pressure (psia):")
#p = float(input())
p = 1000
#print("Temperature (ͦR):")
#t = float(input())
t = 600
#print("SG of gas:")
#SGgas = float(input())
SGgas = 0.6

TemperatureList = [-100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
PList = [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000]

if(p == 0):
    ViscosityList = [0.007, 0.0099, 0.012, 0.0145, 0.0165, 0.017, 0.0185, 0.0195, 0.02, 0.0215, 0.023, 0.024]
elif(p == 500):
    ViscosityList = [0.009, 0.011, 0.013, 0.0155, 0.017, 0.018, 0.019, 0.02, 0.021, 0.022, 0.024, 0.025]
elif(p == 750):
    ViscosityList = [0.017, 0.0135, 0.016, 0.018, 0.019, 0.02]
elif(p == 1000):
    ViscosityList = [0.031, 0.0155, 0.017, 0.0185, 0.0195, 0.02, 0.0215, 0.022, 0.024, 0.0255, 0.0275, 0.029]
elif(p == 1500):
    ViscosityList = [0.04, 0.018, 0.018, 0.019, 0.02]
elif(p == 2000):
    ViscosityList = [0.048, 0.023, 0.021, 0.019, 0.0205, 0.021, 0.022, 0.0235, 0.025, 0.0255, 0.0265, 0.028]
elif(p == 3000):
    ViscosityList = [0.056, 0.029, 0.023, 0.0225, 0.022, 0.0223, 0.0235, 0.0245, 0.0255, 0.0265, 0.0285, 0.03]

j = 0

for i in range(12):
    if TemperatureList[i]==t:
        j=i

print("Viscosity of gas = ", ViscosityList[j], "cp")

miu = ViscosityList[j]


if(SGgas == 0.55):
    if(t == -100):
        ZfactorList = [1.020, 0.89, 0.75, 0.59, 'not defined', 'not defined', 'not defined', 0.42, 0.46, 0.5, 0.54, 0.57, 0.63, 0.67, 0.72, 0.75, 0.78, 0.83, 0.86, 0.89, 0.93]
    elif(t == -50):
        ZfactorList = [1.020, 0.92, 0.83, 0.74, 0.66, 0.59, 0.55, 0.54, 0.56, 0.58, 0.6, 0.63, 0.65, 0.68, 0.72, 0.75, 0.8, 0.84, 0.88, 0.92, 0.96]
    elif(t == 0):
        ZfactorList = [1.020, 0.94, 0.87, 0.81, 0.76, 0.73, 0.69, 0.68, 0.67, 0.67, 0.68, 0.69, 0.72, 0.74, 0.76, 0.78, 0.83, 0.85, 0.88, 0.92, 0.95, 0.96]
    elif(t == 25):
        ZfactorList = [1.020, 0.95, 0.9, 0.85, 0.81, 0.77, 0.75, 0.74, 0.73, 0.73, 0.735, 0.74, 0.75, 0.77, 0.79, 0.82, 0.84, 0.87, 0.89, 0.93, 0.95]
    elif(t == 50):
        ZfactorList = [1.020, 0.97, 0.93, 0.89, 0.85, 0.83, 0.8, 0.79, 0.78, 0.77, 0.78, 0.79, 0.81, 0.83, 0.84, 0.86, 0.88, 0.9, 0.92, 0.95, 0.97]
    elif(t == 75):
        ZfactorList = [1.020, 0.98, 0.95, 0.92, 0.88, 0.86, 0.85, 0.84, 0.83, 0.83, 0.835, 0.84, 0.845, 0.86, 0.87, 0.89, 0.91, 0.93, 0.94, 0.96, 0.98]
    elif(t == 100):
        ZfactorList = [1.020, 0.99, 0.97, 0.94, 0.92, 0.89, 0.87, 0.865, 0.865, 0.87, 0.875, 0.88, 0.885, 0.89, 0.91, 0.92, 0.93, 0.94, 0.96, 0.975, 0.99]
    elif(t == 150):
        ZfactorList = [1.020, 1.00, 0.98, 0.96, 0.94, 0.93, 0.92, 0.91, 0.9, 0.905, 0.91, 0.915, 0.92, 0.93, 0.94, 0.95, 0.96, 0.975, 0.99, 1.00, 1.010]
    elif(t == 200):
        ZfactorList = [1.020, 1.005, 0.99, 0.98, 0.97, 0.96, 0.945, 0.94, 0.93, 0.93, 0.94, 0.945, 0.95, 0.96, 0.965, 0.975, 0.98, 1.010, 1.010, 1.020, 1.030]
    elif(t == 250):
        ZfactorList = [1.020, 1.010, 0.995, 0.985, 0.98, 0.975, 0.965, 0.965, 0.963, 0.965, 0.97, 0.973, 0.98, 0.985, 0.99, 1.000, 1.010, 1.020, 1.030, 1.040, 1.050]
    elif(t == 300):
        ZfactorList = [1.020, 1.010, 1.005, 0.995, 0.99, 0.985, 0.98, 0.975, 0.975, 0.98, 0.985, 0.99, 1.000, 1.005, 1.020, 1.030, 1.035, 1.040, 1.050, 1.060, 1.070]
    elif(t == 400):
        ZfactorList = [1.020, 1.013, 1.010, 1.005, 1.004, 1.003, 1.001, 1.002, 1.005, 1.010, 1.020, 1.025, 1.030, 1.035, 1.040, 1.045, 1.050, 1.060, 1.070, 1.080, 1.090]
    elif(t == 600):
        ZfactorList = [1.020, 1.014, 1.011, 1.008, 1.005, 1.007, 1.010, 1.015, 1.020, 1.025, 1.030, 1.035, 1.040, 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined']
    elif(t == 800):
        ZfactorList = [1.020, 1.017, 1.013, 1.015, 1.017, 1.019, 1.020, 1.021, 1.024, 1.030, 1.035, 1.045, 1.060, 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined']
    elif(t == 1000):
        ZfactorList = [1.020, 1.020, 1.019, 1.018, 1.019, 1.020, 1.022, 1.025, 1.030, 1.035, 1.050, 1.070, 1.090, 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined']


elif(SGgas == 0.6):
    if(t == 0):
        ZfactorList = [1, 0.92, 0.85, 0.79, 0.73, 0.67, 0.64, 0.61, 0.59, 0.61, 0.63, 0.65, 0.67, 0.69, 0.72, 0.75, 0.78, 0.82, 0.85, 0.88, 0.92]
    elif(t == 25):
        ZfactorList = [1, 0.94, 0.88, 0.83, 0.78, 0.73, 0.68, 0.66, 0.65, 0.66, 0.67, 0.68, 0.69, 0.72, 0.74, 0.76, 0.79, 0.83, 0.86, 0.89, 0.93]
    elif(t == 50):
        ZfactorList = [1, 0.95, 0.9, 0.85, 0.82, 0.77, 0.73, 0.71, 0.7, 0.71, 0.72, 0.725, 0.73, 0.75, 0.77, 0.8, 0.82, 0.85, 0.88, 0.91, 0.93]
    elif(t == 75):
        ZfactorList = [1, 0.96, 0.92, 0.88, 0.85, 0.82, 0.78, 0.76, 0.75, 0.753, 0.755, 0.76, 0.765, 0.78, 0.8, 0.825, 0.84, 0.87, 0.895, 0.93, 0.95]
    elif(t == 100):
        ZfactorList = [1, 0.965, 0.935, 0.9, 0.87, 0.84, 0.82, 0.79, 0.78, 0.78, 0.785, 0.79, 0.8, 0.815, 0.83, 0.845, 0.865, 0.885, 0.91, 0.945, 0.965]
    elif(t == 150):
        ZfactorList = [1, 0.975, 0.95, 0.935, 0.915, 0.89, 0.875, 0.87, 0.865, 0.86, 0.855, 0.858, 0.86, 0.87, 0.88, 0.895, 0.91, 0.93, 0.95, 0.97, 0.99]
    elif(t == 200):
        ZfactorList = [1, 0.985, 0.97, 0.955, 0.94, 0.93, 0.92, 0.91, 0.905, 0.9, 0.905, 0.91, 0.92, 0.925, 0.935, 0.945, 0.95, 0.97, 0.98, 0.995, 1.010]
    elif(t == 300):
        ZfactorList = [1, 0.99, 0.985, 0.98, 0.975, 0.97, 0.965, 0.96, 0.96, 0.963, 0.965, 0.97, 0.975, 0.98, 0.985, 0.995, 1.010, 1.020, 1.030, 1.045, 1.060]
    elif(t == 400):
        ZfactorList = [1, 0.995, 0.99, 0.987, 0.983, 0.982, 0.981, 0.982, 0.983, 0.984, 0.985, 0.99, 1.000, 1.010, 1.015, 1.025, 1.030, 1.040, 1.050, 1.065, 1.073]
    elif(t == 500):
        ZfactorList = [1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.003, 1.005, 1.010, 1.020, 1.025, 1.030, 1.035, 1.045, 1.055, 1.060, 1.070, 1.080, 1.085]
    elif(t == 600):
        ZfactorList = [1, 1.005, 1.006, 1.007, 1.008, 1.009, 1.010, 1.011, 1.012, 1.015, 1.020, 1.030, 1.035, 1.045, 1.050, 1.060, 1.070, 1.075, 1.080, 1.088, 1.095]

elif(SGgas == 0.65):
    if(t == 10):
        ZfactorList = [1, 0.918, 0.84, 0.76, 0.68, 0.6, 0.55, 0.53, 0.545, 0.57, 0.593, 0.62, 0.655, 0.69, 0.72, 0.755, 0.79, 0.82, 0.86, 0.9, 0.94]
    elif(t == 25):
        ZfactorList = [1, 0.94, 0.87, 0.81, 0.74, 0.68, 0.65, 0.61, 0.6, 0.62, 0.64, 0.66, 0.69, 0.71, 0.74, 0.77, 0.81, 0.84, 0.87, 0.9, 0.94]
    elif(t == 50):
        ZfactorList = [1, 0.93, 0.878, 0.812, 0.79, 0.75, 0.71, 0.69, 0.67, 0.66, 0.67, 0.69, 0.71, 0.73, 0.76, 0.79, 0.81, 0.84, 0.88, 0.91, 0.94]
    elif(t == 75):
        ZfactorList = [1, 0.96, 0.91, 0.86, 0.82, 0.78, 0.75, 0.72, 0.71, 0.7, 0.7, 0.72, 0.74, 0.75, 0.77, 0.8, 0.83, 0.86, 0.89, 0.92, 0.94]
    elif(t == 100):
        ZfactorList = [1, 0.96, 0.92, 0.89, 0.85, 0.82, 0.79, 0.77, 0.76, 0.757, 0.76, 0.77, 0.78, 0.79, 0.81, 0.83, 0.85, 0.87, 0.89, 0.92, 0.94]
    elif(t == 150):
        ZfactorList = [1, 0.97, 0.95, 0.92, 0.89, 0.87, 0.85, 0.84, 0.82, 0.82, 0.826, 0.83, 0.84, 0.85, 0.86, 0.87, 0.89, 0.91, 0.92, 0.95, 0.97]
    elif(t == 200):
        ZfactorList = [1, 0.98, 0.96, 0.94, 0.93, 0.917, 0.89, 0.88, 0.87, 0.86, 0.865, 0.871, 0.878, 0.88, 0.89, 0.91, 0.926, 0.94, 0.96, 0.97, 0.98]
    elif(t == 300):
        ZfactorList = [1, 0.99, 0.98, 0.97, 0.96, 0.95, 0.94, 0.946, 0.935, 0.93, 0.936, 0.94, 0.945, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.03]
    elif(t == 400):
        ZfactorList = [1, 0.997, 0.99, 0.98, 0.98, 0.97, 0.97, 0.96, 0.96, 0.956, 0.96, 0.97, 0.98, 0.98, 0.99, 1, 1.01, 1.03, 1.04, 1.05, 1.06]
    elif(t == 500):
        ZfactorList = [1, 0.998, 0.99, 0.99, 0.98, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 1, 1.01, 1.02, 1.03, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08]
    elif(t == 650):
        ZfactorList = [1, 1, 1, 1.005, 1.007, 1.008, 1.009, 1.01, 1.02, 1.03, 1.035, 1.0375, 1.04, 1.035, 1.04, 1.045, 1.05, 1.06, 1.07, 1.09, 1.1]
        
        
elif(SGgas == 0.7):
    if(t == 10):
        ZfactorList = [1, 0.91, 0.81, 0.71, 0.61, 0.51, 0.47, 0.465, 0.5, 0.53, 0.57, 0.6, 0.64, 0.67, 0.71, 0.74, 0.77, 0.81, 0.85, 0.88, 0.92]
    elif(t == 25):
        ZfactorList = [1, 0.93, 0.84, 0.77, 0.69, 0.62, 0.56, 0.55, 0.565, 0.58, 0.6, 0.63, 0.66, 0.69, 0.72, 0.75, 0.79, 0.82, 0.86, 0.89, 0.93]
    elif(t == 50):
        ZfactorList = [0.94, 0.87, 0.815, 0.75, 0.7, 0.64, 0.62, 0.615, 0.623, 0.635, 0.65, 0.67, 0.7, 0.73, 0.76, 0.79, 0.82, 0.87, 0.9, 0.93]
    elif(t == 75):
        ZfactorList = [1, 0.95, 0.89, 0.85, 0.79, 0.75, 0.7, 0.68, 0.66, 0.665, 0.675, 0.69, 0.71, 0.73, 0.75, 0.78, 0.81, 0.83, 0.87, 0.89, 0.93]
    elif(t == 100):
        ZfactorList = [1, 0.96, 0.91, 0.87, 0.83, 0.79, 0.76, 0.73, 0.718, 0.71, 0.72, 0.73, 0.74, 0.76, 0.78, 0.8, 0.83, 0.85, 0.88, 0.9, 0.93]
    elif(t == 150):
        ZfactorList = [1, 0.97, 0.93, 0.9, 0.87, 0.85, 0.825, 0.81, 0.795, 0.79, 0.793, 0.8, 0.81, 0.82, 0.83, 0.85, 0.87, 0.88, 0.91, 0.92, 0.95]
    elif(t == 200):
        ZfactorList = [1, 0.97, 0.95, 0.93, 0.91, 0.89, 0.87, 0.86, 0.85, 0.84, 0.85, 0.86, 0.87, 0.885, 0.905, 0.92, 0.94, 0.95, 0.97]
    elif(t == 300):
        ZfactorList = [1, 0.98, 0.97, 0.96, 0.945, 0.94, 0.93, 0.921, 0.919, 0.92, 0.921, 0.922, 0.925, 0.93, 0.94, 0.95, 0.96, 0.98, 0.99, 1.01, 1.02]
    if(t == 400):
        ZfactorList = [1.0, 0.99, 0.98, 0.978, 0.972, 0.97, 0.965, 0.96, 0.959, 0.9595, 0.961, 0.965, 0.971, 0.979, 0.985, 0.99, 1.005, 1.012, 1.022, 1.032, 1.05]
    if(t == 500):
        ZfactorList = [1.0, 1.0, 0.95, 0.9, 0.89, 0.81, 0.8, 0.8, 0.81, 0.82, 0.88, 0.9, 0.95, 1.002, 1.011, 1.019, 1.029, 1.031, 1.045, 1.051, 1.06]
    if(t == 600):
        ZfactorList = [1.0, 1.0, 1.0, 1.0, 0.99, 0.95, 0.91, 0.9, 0.9, 0.99, 1.009, 1.015, 1.02, 1.028, 1.03, 1.04, 1.048, 1.051, 1.061, 1.07, 1.08]
    if(t == 700):
        ZfactorList = [1.0, 1.0, 1.0, 1.0, 1.0, 1.003, 1.005, 1.009, 1.012, 1.018, 1.02, 1.03, 1.038, 1.04, 1.049, 1.05, 1.06, 1.065, 1.07, 1.08, 1.09]


elif(SGgas == 0.8):
    if(t == 10):
        ZfactorList = [1, 0.96, 0.7, 0.56, 0.41, 'not defined', 0.4, 0.51, 0.53, 0.52, 0.56, 0.6, 0.65, 0.68, 0.72]
    elif(t == 25):
        ZfactorList = [1, 0.87, 0.76, 0.64, 0.54, 0.46, 0.44, 0.45, 0.48, 0.52, 0.55, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.87, 0.92, 0.96]
    elif(t == 50):
        ZfactorList = [1, 0.89, 0.8, 0.68, 0.6, 0.53, 0.49, 0.49, 0.51, 0.55, 0.58, 0.61, 0.65, 0.69, 0.72, 0.76, 0.8, 0.84, 0.87, 0.91, 0.95]
    elif(t == 75):
        ZfactorList = [1, 0.91, 0.84, 0.75, 0.66, 0.6, 0.55, 0.55, 0.56, 0.59, 0.62, 0.64, 0.67, 0.7, 0.73, 0.76, 0.8, 0.84, 0.87, 0.91, 0.95]
    elif(t == 100):
        ZfactorList = [1, 0.94, 0.87, 0.83, 0.75, 0.7, 0.65, 0.62, 0.63, 0.64, 0.66, 0.67, 0.7, 0.73, 0.76, 0.78, 0.83, 0.86, 0.89, 0.93, 0.96]
    elif(t == 150):
        ZfactorList = [1, 0.95, 0.93, 0.84, 0.8, 0.77, 0.74, 0.73, 0.73, 0.75, 0.76, 0.78, 0.81, 0.82, 0.84, 0.86, 0.88, 0.9, 0.93, 0.94, 0.96]
    elif(t == 200):
        ZfactorList = [1, 0.96, 0.94, 0.91, 0.87, 0.85, 0.83, 0.81, 0.79, 0.79, 0.81, 0.82, 0.84, 0.85, 0.86, 0.88, 0.9, 0.93, 0.94, 0.95, 0.97]
    elif(t == 250):
        ZfactorList = [1, 0.98, 0.96, 0.93, 0.91, 0.89, 0.87, 0.86, 0.85, 0.85, 0.86, 0.87, 0.89, 0.91, 0.92, 0.93, 0.95, 0.97, 0.99, 1.0]
    elif(t == 300):
        ZfactorList = [1, 0.99, 0.95, 0.93, 0.91, 0.89, 0.86, 0.84, 0.83, 0.83, 0.84, 0.85, 0.86, 0.87, 0.89, 0.91, 0.93, 0.94, 0.96, 0.97, 0.98]
    elif(t == 350):
        ZfactorList = [1, 0.99, 0.96, 0.94, 0.93, 0.91, 0.89, 0.88, 0.87, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.94, 0.95, 0.96, 0.97, 0.99, 1.01]
    elif(t == 400):
        ZfactorList = [1, 0.99, 0.98, 0.97, 0.96, 0.95, 0.94, 0.93, 0.94, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0, 1.01, 1.02, 1.03, 1.04, 1.05]
    elif(t == 500):
        ZfactorList = [1, 1.0, 0.99, 0.98, 0.98, 0.98, 0.97, 0.96, 0.96, 0.97, 0.98, 0.98, 0.99, 1.0, 1.01, 1.01, 1.03, 1.04, 1.06, 1.07, 1.08]
    elif(t == 700):
        ZfactorList = [1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.02, 1.03, 1.03, 1.04, 1.04, 1.05, 1.05, 1.06, 1.06, 1.06, 1.07, 1.08, 1.09, 1.09]
    elif(t == 1000):
        ZfactorList = [1, 1.01, 1.01, 1.02, 1.03, 1.03, 1.04, 1.04, 1.05, 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined', 'not defined']


elif(SGgas == 0.9):
    if(t == 25):
        ZfactorList = [1, 0.82, 0.65, 0.47,'not defined', 'not defined', 'not defined', 'not defined', 0.41, 0.46, 0.5, 0.54, 0.59, 0.63, 0.67, 0.72, 0.77, 0.82, 0.87, 0.91, 0.95]
    elif(t == 50):
        ZfactorList = [1, 0.84, 0.71, 0.55, 0.4, 'not defined', 'not defined', 'not defined', 0.44, 0.49, 0.53, 0.56, 0.61, 0.66, 0.69, 0.74, 0.78, 0.82, 0.87, 0.91, 0.95]
    elif(t == 75):
        ZfactorList = [1, 0.89, 0.77, 0.64, 0.55, 0.5, 0.47, 0.47, 0.49, 0.51, 0.55, 0.59, 0.64, 0.69, 0.71, 0.76, 0.8, 0.84, 0.88, 0.91, 0.95]
    elif(t == 100):
        ZfactorList = [1, 0.9, 0.81, 0.7, 0.62, 0.56, 0.54, 0.54, 0.55, 0.58, 0.61, 0.64, 0.68, 0.71, 0.74, 0.79, 0.81, 0.85, 0.88, 0.91, 0.95]
    elif(t == 150):
        ZfactorList = [1, 0.94, 0.87, 0.79, 0.71, 0.68, 0.64, 0.63, 0.63, 0.64, 0.66, 0.68, 0.71, 0.73, 0.77, 0.8, 0.84, 0.86, 0.89, 0.92, 0.95]
    elif(t == 200):
        ZfactorList = [1, 0.95, 0.91, 0.86, 0.82, 0.78, 0.75, 0.72, 0.71, 0.71, 0.73, 0.75, 0.78, 0.8, 0.82, 0.85, 0.88, 0.91, 0.93, 0.95]
    elif(t == 250):
        ZfactorList = [1, 0.97, 0.94, 0.91, 0.88, 0.85, 0.82, 0.8, 0.78, 0.78, 0.79, 0.8, 0.82, 0.84, 0.85, 0.87, 0.89, 0.91, 0.93, 0.95, 0.97]
    elif(t == 300):
        ZfactorList = [1, 0.99, 0.95, 0.93, 0.91, 0.89, 0.86, 0.84, 0.83, 0.83, 0.84, 0.85, 0.86, 0.87, 0.89, 0.91, 0.93, 0.94, 0.96, 0.97, 0.98]
    elif(t == 350):
        ZfactorList = [1, 0.99, 0.96, 0.94, 0.93, 0.91, 0.89, 0.88, 0.87, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.94, 0.95, 0.96, 0.97, 0.99, 1.01]
    elif(t == 400):
        ZfactorList = [1, 0.99, 0.98, 0.96, 0.95, 0.94, 0.92, 0.91, 0.91, 0.91, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.01, 1.03]
    elif(t == 450):
        ZfactorList = [1, 0.99, 0.98, 0.97, 0.96, 0.95, 0.94, 0.93, 0.93, 0.93, 0.94, 0.95, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.03, 1.04]
    elif(t == 500):
        ZfactorList = [1, 1, 0.99, 0.97, 0.97, 0.96, 0.96, 0.95, 0.95, 0.95, 0.96, 0.96, 0.97, 0.98, 0.99, 0.99, 1.01, 1.02, 1.03, 1.04, 1.05]
    elif(t == 600):
        ZfactorList = [1,  1, 0.99, 0.98, 0.98, 0.98, 0.98, 0.97, 0.97, 0.97, 0.98, 0.98, 0.99, 0.99, 1, 1.01, 1.02, 1.03, 1.05, 1.06, 1.07]
    elif(t == 700):
        ZfactorList = [1, 1, 1, 1, 1, 0.99, 0.99, 0.99, 0.98, 1, 1.01, 1.02, 1.02, 1.04, 1.04, 1.05, 1.05, 1.06, 1.07, 1.08, 1.09]
    elif(t == 800):
        ZfactorList = [1, 1.001, 1.002, 1.003, 1.007, 1.010, 1.012, 1.018, 1.020, 1.024, 1.030, 1.035, 1.040, 1.045, 1.050, 1.055, 1.060, 1.070, 1.080, 1.085, 1.090]
    elif(t == 900):
        ZfactorList = [1, 1.005, 1.010, 1.015, 1.020, 1.025, 1.030, 1.035, 1.040, 1.045, 1.050, 1.055, 1.060, 1.065, 1.070, 1.075, 1.080, 1.085, 1.090, 1.095, 1.100]

k = 0
for i in range(21):
    if PList[i]==p:
        k=i

Zfactor = ZfactorList[k]
print("Zfactor = ", Zfactor)


rl = oil_density
rg = 2.7 * SGgas * p / (t*Zfactor)

print("gas density = ", rg, "lb/ft^3")


Cd = 0.34

Vt = 0.0119 *((((rl - rg) * dm_liquid)/(rg*Cd)) ** 0.5)

print("Vt = ", Vt, "ft/s")

schet = 0
delta = 100
bolean = 0
ReList = []
CdList = []

while(schet < 100):
    Re = 0.0049 * (rg * dm_liquid * Vt)/miu
    ReList.append(Re)
    #print ("Re = ", Re)
    Cdold = Cd
    CdList.append(Cd)
    Cd = (24 / Re) + (3 / (Re ** 0.5)) + 0.34
    #print("Cd= ", Cd)
    Vtold = Vt
    Vt = 0.0119 * ((rl - rg) * dm_liquid/(rg * Cd)) ** 0.5
    #print("Vt = ", Vt)
    schet = schet + 1
    delta = Cd - Cdold
    if delta < 0.1 and bolean == 0:
        Cdlast = Cd
        bolean = 1
print("Cd = ", Cdlast)

Cd = Cdlast

import matplotlib.pyplot as plt
# Создаем график
plt.plot(ReList, CdList, marker='o', linestyle='-', color='b', label='Данные')

# Настраиваем график
plt.title('Dependence of Cd from Re')  # Заголовок
plt.xlabel('Re')  # Название оси X
plt.ylabel('Cd')  # Название оси Y
plt.legend()  # Добавляем легенду
plt.grid(True)  # Включаем сетку

# Отображаем график
plt.show()

#print("Gas Flowrate(MMscfd): ")
#Qg = float(input())
Qg = 6.6

d_squared_gas_phase = 5040 * ((t * Zfactor * Qg) / p) *( ( rg * Cd / ((rl - rg) * dm_liquid)) ** 0.5)
d = d_squared_gas_phase ** 0.5

print("d_squared_gas_phase = ", d_squared_gas_phase, "inch^2")
print("d = ", d_squared_gas_phase**0.5, "inch")

print("retention time(minutes):")
tr = float(input())

#print("SG oil: ")
#SG_o = float(input())
SG_o = 0.867

#print("SG water: ")
#SG_w = float(input())
SG_w = 1.07

delta_SG = SG_w - SG_o

#print("Oil flowrate(BOPD):")
#Qoil = int(input())
Qoil = 5000

#print("Water flowrate(BWPD):")
#Qwater = float(input())
Qwater = 6000

d_squaredh = tr * (Qoil + Qwater)/0.12
print("d_squaredh = ", d_squaredh)
print("h first = ", d_squaredh/d_squared_gas_phase)

hList = [d_squaredh/d**2]
dList = [d]
LssList = []
SRList = []
for i in range(1, 50):
    if d < 36:
        Lss = ((d_squaredh/d**2) + 76) / 12
    else:
        Lss = ((d_squaredh/d**2) + d + 40)/12
    LssList.append(Lss)
    SRList.append(12*Lss/d)
    #print("SR = ", 12*Lss/d, end = " ")
    d = d + 1
    dList.append(d)
    hList.append(d_squaredh/(d**2))

for i in range(50):
    if 3 < SRList[i] < 3.1:
        f = i
        break
        
print("Lss = ", LssList[f], "ft")
print("h = ", hList[f], "inches")
print("d = ", dList[f], "inches")


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from stl import mesh

# Исходные размеры цилиндра
length_ft = LssList[f]  # Длина цилиндра в футах
diameter_inch = dList[f] # Диаметр цилиндра в дюймах

# Переводим диаметр в футы
diameter_ft = diameter_inch / 12  # 1 фут = 12 дюймов
radius_ft = diameter_ft / 2  # Радиус цилиндра в футах

# Параметры сетки
num_sides = 100  # Количество сторон цилиндра (гладкость)
num_height_points = 50  # Точек вдоль высоты

# Сетка углов и высот
theta = np.linspace(0, 2 * np.pi, num_sides)
z = np.linspace(0, length_ft, num_height_points)
theta_grid, z_grid = np.meshgrid(theta, z)

# Координаты поверхности цилиндра
x_grid = radius_ft * np.cos(theta_grid)
y_grid = radius_ft * np.sin(theta_grid)

# Рисуем цилиндр
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Рисуем поверхность цилиндра
ax.plot_surface(x_grid, y_grid, z_grid, cmap='plasma', alpha=0.8)

# Настройка пропорций
ax.set_box_aspect([2 * radius_ft, 2 * radius_ft, length_ft])  # Пропорции цилиндра

# Настройки осей
ax.set_xlabel('X (ft)')
ax.set_ylabel('Y (ft)')
ax.set_zlabel('Z (ft)')
plt.show()

# Создание STL-файла
# 1. Создаём вершины цилиндра
vertices = []
for z_val in z:  # Проходим по высоте
    for angle in theta:  # Проходим по окружности
        x = radius_ft * np.cos(angle)
        y = radius_ft * np.sin(angle)
        vertices.append([x, y, z_val])

# 2. Создаём треугольники для поверхности цилиндра
faces = []

# Верхняя и нижняя границы
for i in range(num_sides - 1):
    # Верхняя часть
    faces.append([i, (i + 1) % num_sides, i + num_sides])
    # Нижняя часть
    faces.append([(i + 1) % num_sides, (i + 1) % num_sides + num_sides, i + num_sides])

# Формируем данные для STL
vertices = np.array(vertices)
faces = np.array(faces)

cylinder_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, face in enumerate(faces):
    for j in range(3):
        cylinder_mesh.vectors[i][j] = vertices[face[j]]

# Сохраняем STL-файл
cylinder_mesh.save('cylinder_fixed.stl')
print("STL файл 'cylinder_fixed.stl' успешно создан!")


