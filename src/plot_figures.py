from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


all_features_misclassification = [4,5,4,8,5,3,4,4,3,1,4,4,2,3,5,5,5,2,4,5,]
all_features_total_sample_size = [2836,2794,2879,2894,2889,2926,2878,2922,2915,2922,2832,2875,2884,2920,2850,2931,2869,2885,2885,2942]

all_features_fpositives = [0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,3,0,0,0,6]
all_features_fnegatives = []
all_features_accuracies = []
x = []
i = 0
while i < len(all_features_misclassification) :
	all_features_fnegatives.append(all_features_misclassification[i] - all_features_fpositives[i])
	all_features_accuracies.append((all_features_total_sample_size[i]-all_features_misclassification[i])*100/float(all_features_total_sample_size[i]))
	i = i + 1
	x.append(i)

worst_case_fpositive_NH = 3
total_number_of_packets = 0.7*2685

worst_case_fpositive_rate_NH = (worst_case_fpositive_NH/float(total_number_of_packets))*100
mean_accuracy = (sum(all_features_accuracies)/float(len(all_features_accuracies)))
worst_case_fp_rate = (max(all_features_fpositives)/float(0.7*2685))*100
worst_case_fn_rate = (max(all_features_fnegatives)/float(2884 - 0.7*2685))*100

f2 = interp1d(x,all_features_accuracies, kind='cubic')
plt.plot(x,all_features_accuracies,'o',x,f2(x),'-')
plt.xlabel("Iteration number")
plt.ylabel("Accuracy (%)")
plt.legend(['data', 'linear'], loc='best')
plt.show()

print "Worst case fpositive rate all features = ", worst_case_fp_rate
print "Worst case fnegative rate all features = ", worst_case_fn_rate
print "Mean accuracy = ", mean_accuracy
print "Max accuracy = ", max(all_features_accuracies)
print "Min accuracy = ", min(all_features_accuracies)
print "Worst case fpositive rate with no CF hits = ", worst_case_fpositive_rate_NH

