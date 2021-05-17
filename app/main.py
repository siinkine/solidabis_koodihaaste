from typing import Reversible
from flask import Flask, request, render_template 
import json
from util import compute_consumption, compare_results
from petrol_price import  get_scraped_avg_prices
from car_data import cars
import json


app=Flask(__name__)
@app.route('/', methods =["GET", "POST"])
def gfg():
  
    if request.method == "POST":
       
       con = float(request.form.get("mydropdown")) 
       d = float(request.form.get("dis"))
       vel1 = float(request.form.get("vel1"))
       vel2 = float(request.form.get("vel2")) 
       vel = [vel1, vel2] 

       time, consumption = compute_consumption(con, d, vel) #compute consumption
       res, diffs = compare_results(time, consumption, vel) #compute differences of two results
       petrol_prices = get_scraped_avg_prices() #get petrol prices
        
       return render_template("result.html", res = res, diffs = diffs, prices = petrol_prices)
    
    return render_template("form.html", cars = cars)
  

if __name__=='__main__':
    app.run(debug = False)