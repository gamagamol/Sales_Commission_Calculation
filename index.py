import pandas as pd

product ={
    'Red':{
        "product_point":5000,
        "sales_point":1,
        
    },
    'Blue':{
        "product_point":10000,
        
        "sales_point":2,
    },
    'Yellow':{
        "product_point":25000,
        
        "sales_point":3,
        
    }
}



def commisionPoint(sales_point,managerial_level):
    result =0
    if managerial_level =="SP":
        
        if sales_point >0 and sales_point <=3 :
            result =75
        elif sales_point >= 4 and sales_point <=7 :
            result =100
        elif sales_point >= 8 and sales_point <=10 :
            result =125
        elif sales_point >= 10 and sales_point <=15 :
            result =150
        else : 
            result =200
    elif  managerial_level =="SM":
        if sales_point >0 and sales_point <=5 :
            result =75
        elif sales_point >= 6 and sales_point <=9 :
            result =100
        elif sales_point >= 10 and sales_point <=14 :
            result =125
        elif sales_point >= 15 and sales_point <=19 :
            result =150
        else: 
            result =200
    else:
        if sales_point >0 and sales_point <=20 :
            result =75
        elif sales_point >= 21 and sales_point <=49 :
            result =100
        elif sales_point >= 50 and sales_point <=74 :
            result =125
        elif sales_point >= 75 and sales_point <=99 :
            result =150
        else: 
            result =200
        
    return result
    
    
    
def performanceIntensive(sales_point,managerial_level,active_managerial):
    result=0
    if managerial_level=="SP":
        if sales_point >=5 and sales_point <=9:
            result =500000
        elif sales_point >= 10 and sales_point <=19:
            result =1500000
        elif sales_point >=20 and sales_point <=29:
            result =2000000
        elif sales_point >=30:
            result =3000000
    elif managerial_level=="SM":
        if sales_point >=2 and sales_point <5 :
                result =100000
        elif sales_point >=5  and sales_point <10:
            if active_managerial >=5 and active_managerial <10:
                result =100000
            elif active_managerial >10 :
                result =200000 
        elif sales_point >=10 and sales_point <15:
            if active_managerial >=5 and active_managerial <10:
                result =100000
            elif active_managerial >=10 and active_managerial <15:
                result =200000
            elif active_managerial >=15:
                result =500000
        elif sales_point >=15 and sales_point < 20 :
            if active_managerial >=5 and active_managerial <10:
                result =100000
            elif active_managerial >=10 and active_managerial <15:
                result =200000
            elif active_managerial >=15 and active_managerial <20:
                result =500000
            elif active_managerial >=20:
                result =1000000  
        elif sales_point >=20 :
            if active_managerial >=5 and active_managerial <10:
                result =100000
            elif active_managerial >=10 and active_managerial <15:
                result =200000
            elif active_managerial >=15 and active_managerial <20:
                result =500000
            elif active_managerial >=20 :
                result=1000000     
    else:
        if sales_point >=3 and sales_point <6 :
            if active_managerial >=20 and active_managerial <75:
                result =300000
            elif active_managerial >=75 and active_managerial <100:
                result =750000
            elif active_managerial >=100:
                result =1500000
                
        elif sales_point >=6  and sales_point <9:
            if active_managerial >=20 and active_managerial <50:
                result =500000
            elif active_managerial >=50 and active_managerial <75:
                result =750000
            elif active_managerial >=75 and active_managerial <100:
                result =1500000
            elif active_managerial >=100:
                result =2500000
            
        elif sales_point >=9 and sales_point <12:
            if active_managerial >=20 and active_managerial <50:
                result =1000000
            elif active_managerial >=50 and active_managerial <75:
                result =1500000
            elif active_managerial >=75 and active_managerial <100:
                result =1500000
            elif active_managerial >=100:
                result =3000000    
        elif sales_point >=12 and sales_point <15:
            if active_managerial >=20 and active_managerial <50:
                result =1500000
            elif active_managerial >=50 and active_managerial <75:
                result =1750000
            elif active_managerial >=75 and active_managerial <100:
                result =2000000
            elif active_managerial >=100:
                result =4000000
        elif sales_point >=15 :
            if active_managerial >=20 and active_managerial <50:
                result =200000
            elif active_managerial >=50 and active_managerial <75:
                result =3000000
            elif active_managerial >=75 and active_managerial < 100:
                result =400000
            elif active_managerial >=100 :
               result=10000000
        
    



def CalculateCommision (name,managerial_level,product_saled,active_managerial):
    result ={
        name :"name",
        "managerial_level":managerial_level,
        "product_point":0,
        "sales_point":0,
        "commision_point":0,
        "performance_incentive":0,
        "basic_commission":0,
        
    }
    
    if managerial_level == "SP":
        for ps in product_saled:
            result["product_point"] += product[ps["item"]]["product_point"] * ps["total"]
            result["sales_point"] += product[ps["item"]]["sales_point"] * ps["total"]
    else :
        result["product_point"] += product_saled["product_point"]
        result["sales_point"] += product_saled["sales_point"]
    
    # calculate commision point
    result["commision_point"]= commisionPoint(result["sales_point"],managerial_level)
        
    # calculate performance insentive
    result["performance_incentive"]= performanceIntensive(result["sales_point"],managerial_level,active_managerial)
        
    # calculate basic commision
    result["basic_commission"]=(result["product_point"] * result["commision_point"])/100
    
    return result
    



# Membaca file Excel
df = pd.read_excel('sales_commission_data.xlsx',header=1)

# RAW SP
df_sp = (
    df.sort_values(by=["SP", "Item"])
    .groupby(["SP", "Item"])
    .agg(
        count=("SO", "size"),
        SM=("SM", "first"),
        GM=("GM", "first")
    )
    .reset_index()
)
df_sp.rename(columns={"SP": "name", "Item": "item","SM": "sm","GM": "gm"}, inplace=True)
raw_sp=df_sp["managerial_level"] = "SP"
raw_sp = df_sp.to_dict(orient="records")

data_sp=[]
data_sm=[]
data_gm=[]


for rs in raw_sp:
    # prepare sp
    existing_entry_sp = next((entry for entry in data_sp if entry["name"] == rs["name"]), None)
    if existing_entry_sp:
        existing_entry_sp["product_saled"].append({
            "item": rs["item"],
            "total": rs["count"]
        })
    else:
        data_sp.append({
            "name": rs["name"],
            "managerial_level": rs["managerial_level"],
            "SM":rs["sm"],
            "GM":rs["gm"],
            "product_saled": [
                {
                    "item": rs["item"],
                    "total": rs["count"]
                }
            ]
        })   
        
      

        
   
           
    


    
for d in data_sp:
    result_sp=CalculateCommision(d["name"],d["managerial_level"],d["product_saled"],0)
    existing_entry_sm = next((entry for entry in data_sm if entry["name"] == d["SM"]), None)

    if existing_entry_sm:
        existing_entry_sm["product_saled"]["product_point"]+=result_sp["product_point"]
        existing_entry_sm["product_saled"]["sales_point"]+=result_sp["sales_point"]
        existing_entry_sm["active_managerial"]+=1
    else :       
        data_sm.append({
            "name":d["SM"],
            "GM":d["GM"],
            "managerial_level":"SM",
            "product_saled":{
                "product_point":result_sp["product_point"],
                "sales_point":result_sp["sales_point"],
            },
            "active_managerial":1
            })
        

for dm in data_sm:
    result_sm=CalculateCommision(dm["name"],dm["managerial_level"],dm["product_saled"],dm["active_managerial"])
    existing_entry_gm = next((entry_gm for entry_gm in data_gm if entry_gm["name"] == dm["GM"]), None)

    if existing_entry_gm:
        existing_entry_gm["product_saled"]["product_point"]+=result_sm["product_point"]
        existing_entry_gm["product_saled"]["sales_point"]+=result_sm["sales_point"]
        existing_entry_gm["active_managerial"]+=1
    else :       
        data_gm.append({
            "name":dm["GM"],
            "managerial_level":"GM",
            "product_saled":{
                "product_point":result_sm["product_point"],
                "sales_point":result_sm["sales_point"],
            },
            "active_managerial":1
            })



print(data_sp)
print(data_sm)
print(data_gm)
