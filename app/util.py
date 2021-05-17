#This file contains the computations for the car consumptions

def compute_consumption(con, d, vel, slope = 1.009):
    '''This function computes the consumption of a car with distance and two velocities  in vel. 
    INPUTS:
    con = scalar, consumption liters/100 km at velocity 1 km/h.
    d = scalar, travel distance in km.
    vel = list, velocities of the car in km/h. 
    Slope  = scalar, slope of the consumption in the linear model i.e. when increased by 
    1 km/h consumption rises times slope value. (default = 1.009)

    OUTPUTS:
    time = list, time passed for distance in hours when driving with velocities in list vel.
    consumption = list, total consumption in liters for distance d with velocities in list vel. 
    
    16.5.2021, Satu Inkinen
    '''


    time = []
    consumption = []
    for v in vel:

        #Travel time for distance:
        time.append(d/v) #[h]

        #Consumption:
        #Exponent model:
        #con_new = con.*slope.^(v-1)
    
        con_new = con*(slope**(v-1))
        consumption.append(con_new*d/100) #[l]

    return time, consumption



def compare_results(time, consumption, vel):
    '''This function compares the two scenarios and returns differences in dictionary '''

    res = []
    for i, t in enumerate(time):
           res.append({'c': i,'time': str(round(t, 5)),
            'consumption': str(round(consumption[i],5)),
            'velocity': str(round(vel[i]))})

       #Differences:
    diffs = {'time': str(round(abs(time[0]-time[1]), 3)), 'consumption': str(round(abs(consumption[0]-consumption[1]), 3))}   
    diffs['time_p'] = str(round(abs(100*((time[0]-time[1])/time[1]))))
    diffs['con_p'] = str(round(abs(100*((consumption[0]-consumption[1])/consumption[1]))))     

    if time[0]-time[1] > 0:
           diffs['X'] = 1
           diffs['Y'] = 0
           
    else:
            diffs['X'] = 0
            diffs['Y'] = 1
    
    return res, diffs     


if __name__ =="__main__":
    #Simple test for function:  
    con = 1 #l/100 km
    d =  100 #km
    vel = [1, 2, 10]

    time, consumption = compute_consumption(con, d, vel, slope = 1.009)

    time_true = [100, 50, 10] 
    consumption_true = [  1.0000, 1.0090, 1.0840]

    #simple sanity check:
    tol = 1e-4
    for i, t in enumerate(time):
    
        if abs(time_true[i]-t) < tol:
            print("time computation okay")
        else:
            print("Check travel time computation!")

    for i, c in enumerate(consumption):
        if abs(consumption_true[i]-c) < tol:
            print("consumption computation is okay")
        else:
            print("Check consumption computation!")

  
