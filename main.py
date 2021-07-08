from sklearn.datasets import load_iris, load_wine, load_breast_cancer
import selectors_lib as slct

if __name__ == '__main__':
    iris = load_iris()
    wine = load_wine()
    breast_cancer = load_breast_cancer()
    data = ["Iris", "Wine", "Breast cancer"]
    X = [iris.data, wine.data, breast_cancer.data]
    y = [iris.target, wine.target, breast_cancer.target]
    
    for i in range(len(data)):
        print("\n" + data[i] + ", " + str(len(X[i][0])) + " features:")
        X[i], y[i] = slct.randomize_data(X[i], y[i]) 
        forward_search = slct.forward_search(X[i], y[i])
        variance_threshold = slct.variance_threshold(X[i])
        no_selectors = slct.knn_score(X[i], y[i]) 
        forward_selector = slct.knn_score(forward_search, y[i]) 
        variance_selector = slct.knn_score(variance_threshold, y[i])
        
        print("No selectors: " + str(slct.knn_score(X[i], y[i])) + "%")
        print("Forward search selector: " + str(forward_selector) + "%")
        print("Variance threshold selector: " + str(variance_selector) + "%")
