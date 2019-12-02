import csv
#deactivate
import psycopg2 as p
# from pg import DB
import MedicaldbDATA.Hospital as Hospital
import MedicaldbDATA.Connection as Connection
import  MedicaldbDATA.CreateTables as CreateTables
import MedicaldbDATA.Hospital_Specialization as Hospital_Specialization
import MedicaldbDATA.Location as Location
import MedicaldbDATA.hospital_location_rel as Hospital_Location_Rel



def master_fn():

    username = "anantpathak"
    passwrd = "Anant123!"
    dataB = "medicaldb"
    hostname = "localhost"

    DbObj = Connection.DBConnection(username=username, password=passwrd, dbName=dataB, hostadd=hostname)
    if DbObj.connectToDb() == False:
         print("Connection failed")
    #create all the tables:
    # CreateTables.create_tables(DbObj.connectionObj)
    #For table Hospital fetch data from CSV and put it in our medicalDb database in table hospital
    dataList = Hospital.hospital_data_fetch()
    Hospital.hospital_data_populate(DbObj.connectionObj, dataList)
    #For table: hospital_specialization
    dataList = ["Gastrointestinal","Eye","Nervous System", "Musculoskeletal", "Skin", "Genitourinary", "Cardiovascular", "Respiratory"]
    # Hospital_Specialization.Hospital_Specialization_data_populate(DbObj.connectionObj, dataList)
    #For table location.
    dataList.clear()
    dataList = Location.location_data_fetch()
    Location.location_data_populate(DbObj.connectionObj, dataList)
    #For table Hospital_Location_Rel
    dataList.clear()
    dataList = Hospital_Location_Rel.hospital_location_rel_data_fetch()
    Hospital_Location_Rel.hospital_location_rel_data_populate(DbObj.connectionObj, dataList)
    return DbObj

if __name__ == "__main__":
   DbObj = master_fn()
        
    


