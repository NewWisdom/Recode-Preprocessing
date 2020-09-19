def audio_preprocessing():
    import librosa
    import librosa.display
    # import IPython.display
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import matplotlib.font_manager as fm
    import glob
    from IPython import get_ipython


    # get_ipython().run_line_magic('matplotlib', 'inline')

    #FIG_SIZE = (15,10)
    

    folder_list = glob.glob("add_data/*") # 오디오 데이터 파일 위치 
    print(folder_list)
    print(len(folder_list))
    file_list=[] 
    index=0
    for i in range(len(folder_list)):
        file=glob.glob(folder_list[i]+"/*")
        file_list.append(file)

        
        file_cnt=0
        for j in file_list[i]:
            frame_length = 0.025
            frame_stride = 0.010
            y, sr = librosa.load(j,sr=16000)
            win_length = int(np.ceil(frame_length*sr))
            window = 'hamming'
            nfft = int(round(sr*frame_length))
            hop_length = int(round(sr*frame_stride))
            plt.figure(figsize=(4,10))
            Si = librosa.feature.melspectrogram(y=y,sr=sr,n_mels=40, n_fft=nfft, hop_length=hop_length,win_length=win_length, window=window,center=True, pad_mode='reflect', fmin=0.0)
            DB = librosa.amplitude_to_db(Si, ref=np.max)
            
            librosa.display.specshow(DB.T, sr=sr, x_axis='linear', y_axis='time',hop_length=hop_length)
            plt.axis('off')


            # plt.xlabel("Time")
            # plt.ylabel("MFCC coefficients")
            # plt.colorbar()
            # plt.title("MFCCs")
            
            #save image
            fig = plt.gcf() 
            
            fig.savefig("./add_img/"+str(index)+'-'+str(file_cnt)+'.png',bbox_inches='tight',pad_inches=0)
            plt.close()
            file_cnt+=1
            
        index+=1
    print("complete!")       
audio_preprocessing()