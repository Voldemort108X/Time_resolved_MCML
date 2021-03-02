#%%
import mcml_scatter as mcml
N = 5000

def run_model(modelName,N):
    model = mcml.MCMLModel(modelName)
    #print(model.nt)
    model.do_one_run(N)
    model.sum_scale_result()
    return model

#%%
model_05 = run_model('HW30.5',N)
model_1 = run_model('HW31',N)
model_2 = run_model('HW32',N)
model_4 = run_model('HW34',N)

#%%
import matplotlib.pyplot as plt
import numpy as np
index_set = np.where(model_05.Time_array_Rd_rat!=0)
print(index_set[0].shape)
#plt.plot()


# %%
import numpy as np
modelList = [model_05,model_1,model_2,model_4]
import matplotlib.pyplot as plt
def plot_Quantity(modelList, QuantityName):
    plt.figure()
    for model in modelList:
        if QuantityName == 'Absorbance':
            index_set = np.where(model.Time_array_Arzt!=0)
            Absorbance, time = [],[]
            #print(model.Time_array_Arzt)
            for index in index_set[0]:
                Absorbance.append(model.A_t[index]), time.append(model.Time_array_Arzt[index]/1e-9)
            plt.plot(time,Absorbance)
            plt.xlabel('Time (ns)')
            plt.ylabel('Absorbance')
            

        elif QuantityName == 'Diffuse reflectance':
            index_set = np.where(model.Time_array_Rd_rat!=0)
            Reflectance, time = [],[]
            #print(model.Time_array_Arzt)
            for index in index_set[0]:
                Reflectance.append(model.Rd_t[index]), time.append(model.Time_array_Rd_rat[index]/1e-9)
            plt.plot(time,Reflectance)
            plt.xlabel('Time (ns)')
            plt.ylabel('Reflectance')

        elif QuantityName == 'Transmittance':
            index_set = np.where(model.Time_array_Tt_rat!=0)
            Transmittance, time = [],[]
            #print(model.Time_array_Arzt)
            for index in index_set[0]:
                Transmittance.append(model.Tt_t[index]), time.append(model.Time_array_Tt_rat[index]/1e-9)
            plt.plot(time,Transmittance)
            plt.xlabel('Time (ns)')
            plt.ylabel('Transmittance')
    plt.legend(('d=0.005 cm','d=0.01 cm','d=0.02 cm','d=0.04 cm'))
    #plt.show()
    plt.savefig(QuantityName+'.pdf',bbox_inches='tight')

plot_Quantity(modelList,'Absorbance')
plot_Quantity(modelList,'Diffuse reflectance')
plot_Quantity(modelList,'Transmittance')
# %%