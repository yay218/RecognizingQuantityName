from sklearn import tree
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model
from sklearn.metrics import confusion_matrix


# dataset = pd.read_csv('feature_new.csv')
# print dataset.groupby('label').size()
none = pd.read_csv('features_none.csv').as_matrix()
none_feature = none[:, :-1]
none_label = none[:, -1]

length = pd.read_csv('features_length.csv').as_matrix()
length_feature = length[:, :-1]
length_label = length[:, -1]

time = pd.read_csv('features_time.csv').as_matrix()
time_feature = time[:, :-1]
time_label = time[:, -1]

percent = pd.read_csv('features_percent.csv').as_matrix()
percent_feature = percent[:, :-1]
percent_label = percent[:, -1]

currency = pd.read_csv('features_currency.csv').as_matrix()
currency_feature = currency[:, :-1]
currency_label = currency[:, -1]

weight = pd.read_csv('features_weight.csv').as_matrix()
weight_feature = weight[:, :-1]
weight_label = weight[:, -1]

forest_accuracy = 0
tree_accuracy = 0
lin_svc_accuracy = 0
rbf_svc_accuracy = 0
logreg_accuracy = 0


for i in range(10):
	train_feature_all = pd.DataFrame()
	train_label_all = pd.DataFrame()
	test_feature_all = pd.DataFrame()
	test_label_all = pd.DataFrame()
	
	for feature, label in zip([none_feature, length_feature, time_feature, percent_feature, currency_feature, weight_feature], [none_label, length_label, time_label, percent_label, currency_label, weight_label]):
		test_index = range(feature.shape[0]/10*i+1, feature.shape[0]/10*(i+1)+1)
		train_index = np.setdiff1d(range(feature.shape[0]), test_index)
		train_index = np.random.choice(train_index, 928)

		train_feature, test_feature = pd.DataFrame(feature[train_index]), pd.DataFrame(feature[test_index])
		train_label, test_label = pd.DataFrame(label[train_index]), pd.DataFrame(label[test_index])

		train_feature_frames = [train_feature_all, train_feature]
		train_feature_all = pd.concat(train_feature_frames)
		train_label_frames = [train_label_all, train_label]
		train_label_all = pd.concat(train_label_frames)
		test_feature_frames = [test_feature_all, test_feature]
		test_feature_all = pd.concat(test_feature_frames)
		test_label_frames = [test_label_all, test_label]
		test_label_all = pd.concat(test_label_frames)
		# print train_feature_all.shape

	forest_model = RandomForestClassifier(n_estimators = 200, max_depth=12, random_state=0)
	forest_model.fit(train_feature_all, np.ravel(train_label_all))
	forest_importances = forest_model.feature_importances_
	forest_predict_test = forest_model.predict(test_feature_all)
	print forest_predict_test
	forest_accuracy = forest_accuracy + accuracy_score(test_label_all, forest_predict_test)




	# tree_model = tree.DecisionTreeClassifier().fit(train_feature_all, np.ravel(train_label_all))
	# tree_predict_test = tree_model.predict(test_feature_all)
	# tree_accuracy = tree_accuracy + accuracy_score(test_label_all, tree_predict_test)
	
	# lin_svc = svm.LinearSVC(C=1.0).fit(train_feature_all, np.ravel(train_label_all))
	# lin_svc_predict_test = lin_svc.predict(test_feature_all)
	# lin_svc_accuracy = lin_svc_accuracy + accuracy_score(test_label_all, lin_svc_predict_test)
	
	# rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=1.0).fit(train_feature_all, np.ravel(train_label_all))
	# rbf_svc_predict_test = rbf_svc.predict(test_feature_all)
	# rbf_svc_accuracy = rbf_svc_accuracy + accuracy_score(test_label_all, rbf_svc_predict_test)
	
	# logreg = linear_model.LogisticRegression(C=1e5).fit(train_feature_all, np.ravel(train_label_all))
	# logreg_predict_test = logreg.predict(test_feature_all)
	# logreg_accuracy = logreg_accuracy + accuracy_score(test_label_all, logreg_predict_test)

print forest_importances
print forest_accuracy/10
cm = confusion_matrix(test_label_all, forest_predict_test, labels=[1.0, 2.0, 3.0, 4.0, 5.0, 0.0])
print cm
# print tree_accuracy/10
# print lin_svc_accuracy/10
# print rbf_svc_accuracy/10
# print logreg_accuracy/10
		


