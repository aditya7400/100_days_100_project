import pandas
data = pandas.read_csv("state_data.csv")

def give_cor(state_name):

    if state_name in data["state"].values:

        my_data = data[data["state"] ==state_name]
        x_cor = my_data["x"].values[0]
        y_cor = my_data["y"].values[0]
        return (int(x_cor),int(y_cor))
    else:
        print("not found")



