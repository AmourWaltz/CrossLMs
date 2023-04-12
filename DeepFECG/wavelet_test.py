import matplotlib.pyplot as pltimport pywtimport wfdbimport os# def wavelet_denoise(signal_lead, ):file_Path = '/Users/collcertaye/WorkSpace/Laboratory_FECG/FECG_2013DB/set-a'file_Name = 'a01'record = wfdb.rdrecord(os.path.join(file_Path, file_Name),                       sampfrom=0, sampto=10000, physical=True, channels=[0, 1, 2, 3])signal_lead = record.p_signalventricular_signal = record.p_signal[0:4000, 0]signal_annotation = wfdb.rdann(os.path.join(file_Path, file_Name), "atr", sampfrom=0, sampto=4000)ecg = ventricular_signal# ecg = pywt.data.ecg()  # 生成心电信号print(ecg)index = []data = []for i in range(len(ecg)-1):    X = float(i)    Y = float(ecg[i])    index.append(X)    data.append(Y)# data = list(ventricular_signal)# Create wavelet object and define parametersw = pywt.Wavelet('db8')maxlev = pywt.dwt_max_level(len(data), w.dec_len)print("maximum level is " + str(maxlev))threshold = 0.04  # Threshold for filtering# Decompose into wavelet components, to the level selected:coeffs = pywt.wavedec(data, 'db8', level=maxlev)# plt.figure()for i in range(1, len(coeffs)):    coeffs[i] = pywt.threshold(coeffs[i], threshold*max(coeffs[i]))  # 将噪声滤波datarec = pywt.waverec(coeffs, 'db8')  # 将信号进行小波重构mintime = 0maxtime = mintime + len(data) + 1plt.figure()plt.subplot(2, 1, 1)plt.plot(index[mintime:maxtime], data[mintime:maxtime])for loop_i in signal_annotation.sample:    print(loop_i)    plt.scatter(x=loop_i, y=data[loop_i], marker="*")plt.title("Raw signal")plt.subplot(2, 1, 2)plt.plot(index[mintime:maxtime], datarec[mintime:maxtime-1])for loop_i in signal_annotation.sample:    print(loop_i)    plt.scatter(x=loop_i, y=datarec[loop_i], marker="*")plt.title("Denoisy signal using db8")plt.tight_layout()plt.show()