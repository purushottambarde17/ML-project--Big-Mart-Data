from flask import Flask , request ,render_template
import pickle



app = Flask(__name__)


@app.route("/")
def function():
    return render_template ("index.html")

@app.route ('/function_to_pull_data', methods=["post"])

def my_model_prediction():
    
    model = pickle.load(open(r'C:\Users\vishn\OneDrive\Desktop\flask_frt_end\myLRmodel.pkl', "rb"))
    
    
    data = request.form
    print(data)
    
    
    user_input = [[int(data['Item_Weight']),
                   float(data['Item_Visibility']),
                   int(data['Item_MRP']),
                   int(data['Outlet_Establishment_Year']),
                   int(data['Item_Outlet_Sales'])]]
    
    print(user_input)
    
    
    result = model.predict(user_input)
    print(result)
    
    a = str(result[0])
    
    return render_template("result.html", predictions_result = a )




if __name__ == "__main__":
    app.run(debug=True)
    
    #  Bigmart Store Location is in ==  {{predictions_result}}