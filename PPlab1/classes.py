import json
import xml.etree.ElementTree as ET
class ValueNumberException(Exception): #исключение - число не в нужном диапазоне
    def __init__(self, minvalue: int, maxvalue: int):
        self.minvalue = minvalue
        self.maxvalue = maxvalue
    def __str__(self):
        return f"Значение должно быть в диапазоне от {self.minvalue} до {self.maxvalue}"
class Date: # класс для представления даты
    def __init__(self):# создание объекта по умолчанию
        self.day: int
        self.month: int
        self.year: int
    def setdate(self):# ввод даты
        try:
            day = int(input("Введите день "))
            if 1 <= day <= 31:
                self.day = day
            else:
                raise ValueNumberException(1,31)
            month = int(input("Введите месяц "))
            if 1 <= month <= 12:
                self.month = month
            else:
                raise ValueNumberException(1, 12)
            year = int(input("Введите год "))
            if 1900 <= year:
                self.year = year
            else:
                raise Exception("Число должно быть не менее 1900")
        except ValueError:
            print("Нужно ввести число")
            return ValueError
        except ValueNumberException as vne:
            print(vne)
            return vne
        except Exception as e:
            print(e)
            return e
    def getDate(self):# вывод даты
        print(self.day, '.', self.month, '.', self.year, sep='')
    def data_to_dict(self):# преобразование даты в словарь для записи  в json
        dictionary = {
            "day": self.day,
            "month": self.month,
            "year": self.year,
        }
        return dictionary
class Patient:# пациент
    def __init__(self):
        self.id: int
        self.name: str
        self.birthDate: Date
        self.gender: str
        self.phoneNumber: str
    def setPatient(self):
        try:
            id = int(input("Введите ID "))
        except ValueError:
            print("id должно быть числом.")
            return ValueError
        print("Введите дату рождения:")
        pbd = Date()  # patient birthdate
        exc = pbd.setdate()
        if exc!=None:
            return exc
        self.id=id
        self.name = input("Введите имя ")
        self.birthDate = pbd
        self.gender = input("Введите пол ")
        self.phoneNumber = input("Введите номер телефона ")
    def updateContactInfo (self, phoneNumber: str):# изменить номер телефона
        self.phoneNumber=phoneNumber
    def getInfo(self):# вывод информации
        print('Информация о пациенте:')
        print(' ID:', self.id)
        print(' Имя:', self.name)
        print(' Дата рождения: ',end='')
        self.birthDate.getDate()
        print(' Пол:', self.gender)
        print(' Номер телефона:', self.phoneNumber)
    def writePatientJSON(self):
        patient = {
            "id": self.id,
            "name": self.name,
            "birthDate": self.birthDate.data_to_dict(),
            "gender": self.gender,
            "phoneNumber": self.phoneNumber,
        }
        with open('patients.json', 'w') as json_file:
            json.dump(patient, json_file)
    def writePatientXML(self):
        root = ET.Element('patients')
        item = ET.SubElement(root, "patient")
        item.attrib["id"] = str(self.id)
        item.attrib["name"] = self.name
        date = ET.SubElement(item, "date")
        date.attrib["day"] = str(self.birthDate.day)
        date.attrib["month"] = str(self.birthDate.month)
        date.attrib["year"] = str(self.birthDate.year)
        item.attrib["gender"] = self.gender
        item.attrib["phoneNumber"] = self.phoneNumber
        tree = ET.ElementTree(root)
        ET.indent(tree, '  ')
        tree.write('patients.xml')
    def readPatientJSON(self):
        with open('patients.json', 'r') as json_file:
            data = json.load(json_file)
            print("Запись в файле JSON:")
            print(data)
    def readPatientXML(self):
        print("Запись в файле XML:")
        tree = ET.parse('patients.xml')
        root = tree.getroot()
        for elem in root.iter():
            if elem.tag!='patients':
                print(elem.tag, elem.attrib)
class Doctor:# врач
    def __init__(self):
        self.id: int
        self.name: str
        self.specialization: str
        self.phoneNumber: str
    def setDoctor(self):
        try:
            id = int(input("Введите ID "))
        except ValueError:
            print("id должно быть числом.")
            return ValueError
        self.id = id
        self.name = input("Введите имя ")
        self.specialization = input("Введите специализацию ")
        self.phoneNumber = input("Введите номер телефона ")
    def getInfo(self):# вывод информации
        print('Информация о враче:')
        print(' ID:', self.id)
        print(' Имя:', self.name)
        print(' Специализация:', self.specialization)
        print(' Номер телефона:', self.phoneNumber)
    def writeDoctorJSON(self):
        doctor = {
            "id": self.id,
            "name": self.name,
            "specialization": self.specialization,
            "phoneNumber": self.phoneNumber,
        }
        with open('doctors.json', 'w') as json_file:
            json.dump(doctor, json_file)
    def writeDoctorXML(self):
        root = ET.Element('doctors')
        item = ET.SubElement(root, "doctor")
        item.attrib["id"] = str(self.id)
        item.attrib["name"] = self.name
        item.attrib["specialization"] = self.specialization
        item.attrib["phoneNumber"] = self.phoneNumber
        tree = ET.ElementTree(root)
        ET.indent(tree, '  ')
        tree.write('doctors.xml')
    def readDoctorJSON(self):
        with open('doctors.json', 'r') as json_file:
            data = json.load(json_file)
            print("Запись в файле JSON:")
            print(data)
    def readDoctorXML(self):
        print("Запись в файле XML:")
        tree = ET.parse('doctors.xml')
        root = tree.getroot()
        for elem in root.iter():
            if elem.tag!='doctors':
                print(elem.tag, elem.attrib)
class Appointment:# запись на приём
    def __init__(self):
        self.id: int
        self.patientId: int
        self.doctorId: int
        self.status: str
        self.appointmentDate: Date
    def setAppointment(self):
        try:
            id = int(input("Введите ID записи "))
            patientId = int(input("Введите ID пациента "))
            doctorId = int(input("Введите ID врача "))
        except ValueError:
            print("id должно быть числом.")
            return ValueError
        print("Введите дату записи:")
        apd = Date()  # appointment date
        exc = apd.setdate()
        if exc != None:
            return exc
        self.id = id
        self.patientId = patientId
        self.doctorId = doctorId
        self.status = input("Введите статус записи ")
        self.appointmentDate = apd
    def cancelAppointment(self):# отмена записи
        # self=Appointment() не работает
        print("Запись отменена")
    def rescheduleAppointment (self, newDate: Date):# перенос записи
        if self.appointmentDate!=newDate:
            self.appointmentDate = newDate
            print("Запись успешно перенесена")
        else:
            print("Новая дата совпадает со старой")
    def getAppointmentInfo(self):# вывод информации
        print('Информация о записи на приём:')
        print(' ID записи:', self.id)
        print(' ID пациента:', self.patientId)
        print(' ID врача:', self.doctorId)
        print(' Статус записи:', self.status)
        print(' Дата записи: ',end='')
        self.appointmentDate.getDate()
    def writeAppointmentJSON(self):
        appointment = {
            "id": self.id,
            "patientId": self.patientId,
            "doctorId": self.doctorId,
            "status": self.status,
            "appointmentDate": self.appointmentDate.data_to_dict()
        }
        with open('appointments.json', 'w') as json_file:
            json.dump(appointment, json_file)
    def writeAppointmentXML(self):
        root = ET.Element('appointments')
        item = ET.SubElement(root, "appointment")
        item.attrib["id"] = str(self.id)
        item.attrib["patientId"] = str(self.patientId)
        item.attrib["doctorId"] = str(self.doctorId)
        item.attrib["status"] = self.status
        date = ET.SubElement(item, "date")
        date.attrib["day"] = str(self.appointmentDate.day)
        date.attrib["month"] = str(self.appointmentDate.month)
        date.attrib["year"] = str(self.appointmentDate.year)
        tree = ET.ElementTree(root)
        ET.indent(tree, '  ')
        tree.write('appointments.xml')
    def readAppointmentJSON(self):
        with open('appointments.json', 'r') as json_file:
            data = json.load(json_file)
            print("Запись в файле JSON:")
            print(data)
    def readAppointmentXML(self):
        print("Запись в файле XML:")
        tree = ET.parse('appointments.xml')
        root = tree.getroot()
        for elem in root.iter():
            if elem.tag!='appointments':
                print(elem.tag, elem.attrib)
class MedicalRecord:# запись о приёме
    def __init__(self):
        self.id: int
        self.patientId: int
        self.doctorId: int
        self.diagnosis: str
        self.treatmentPlan: str
        self.dateOfVisit: Date
    def setMedicalRecord(self):
        try:
            id = int(input("Введите ID записи "))
            patientId = int(input("Введите ID пациента "))
            doctorId = int(input("Введите ID врача "))
        except ValueError:
            print("id должно быть числом.")
            return ValueError
        print("Введите дату приёма: ")
        vd = Date()  # visit date
        exc = vd.setdate()
        if exc!=None:
            return exc
        self.id = id
        self.patientId = patientId
        self.doctorId = doctorId
        self.diagnosis = input("Введите диагноз ")
        self.treatmentPlan = input("Введите назначенный план лечения ")
        self.dateOfVisit = vd
    def getRecordDetails(self):# вывод информации
        print('Информация о записи на приём:')
        print(' ID записи:', self.id)
        print(' ID пациента:', self.patientId)
        print(' ID врача:', self.doctorId)
        print(' Диагноз:', self.diagnosis)
        print(' Назначенное лечение:', self.treatmentPlan)
        print(' Дата посещения: ', end='')
        self.dateOfVisit.getDate()
    def writeMedicalRecordJSON(self):
        record = {
            "id": self.id,
            "patientId": self.patientId,
            "doctorId": self.doctorId,
            "diagnosis": self.diagnosis,
            "treatmentPlan": self.treatmentPlan,
            "dateOfVisit": self.dateOfVisit.data_to_dict()
        }
        with open('records.json', 'w') as json_file:
            json.dump(record, json_file)
    def writeMedicalRecordXML(self):
        root = ET.Element('records')
        item = ET.SubElement(root, "record")
        item.attrib["id"] = str(self.id)
        item.attrib["patientId"] = str(self.patientId)
        item.attrib["doctorId"] = str(self.doctorId)
        item.attrib["diagnosis"] = self.diagnosis
        item.attrib["treatmentPlan"] = self.treatmentPlan
        date = ET.SubElement(item, "date")
        date.attrib["day"] = str(self.dateOfVisit.day)
        date.attrib["month"] = str(self.dateOfVisit.month)
        date.attrib["year"] = str(self.dateOfVisit.year)
        tree = ET.ElementTree(root)
        ET.indent(tree, '  ')
        tree.write('records.xml')
    def readMedicalRecordJSON(self):
        with open('records.json', 'r') as json_file:
            data = json.load(json_file)
            print("Запись в файле JSON:")
            print(data)
    def readMedicalRecordXML(self):
        print("Запись в файле XML:")
        tree = ET.parse('records.xml')
        root = tree.getroot()
        for elem in root.iter():
            if elem.tag != 'records':
                print(elem.tag, elem.attrib)
class Test:
    def __init__(self):
        self.id: int
        self.testName: str
        self.results: str
        self.laboratoryID: int
    def setTest(self):
        try:
            id = int(input("Введите ID "))
            laboratoryID = int(input("Введите ID лаборатории "))
        except ValueError:
            print("id должно быть числом.")
            return ValueError
        self.id=id
        self.testName = input("Введите название теста ")
        self.results = input("Введите результаты теста ")
        self.laboratoryID = laboratoryID
    def getTestDetails(self):# вывод информации
        print("Информация о тесте:")
        print(' ID теста:', self.id)
        print(' Название теста:', self.testName)
        print(' Результаты теста:', self.results)
        print(' ID лаборатории:', self.laboratoryID)
    def writeTestJSON(self):
        test = {
            "id": self.id,
            "testName": self.testName,
            "results": self.results,
            "laboratoryID": self.laboratoryID
        }
        with open('tests.json', 'w') as json_file:
            json.dump(test, json_file)
    def writeTestXML(self):
        root = ET.Element('tests')
        item = ET.SubElement(root, "test")
        item.attrib["id"] = str(self.id)
        item.attrib["testName"] = self.testName
        item.attrib["results"] = self.results
        item.attrib["laboratoryID"] = str(self.laboratoryID)
        tree = ET.ElementTree(root)
        ET.indent(tree, '  ')
        tree.write('tests.xml')
    def readTestJSON(self):
        with open('tests.json', 'r') as json_file:
            data = json.load(json_file)
            print("Запись в файле JSON:")
            print(data)
    def readTestXML(self):
        print("Запись в файле XML:")
        tree = ET.parse('tests.xml')
        root = tree.getroot()
        for elem in root.iter():
            if elem.tag != 'tests':
                print(elem.tag, elem.attrib)
class Laboratory:
    def __init__(self):
        self.id: int
        self.name: str
        self.location: str
    def setLaboratory(self):
        try:
            id = int(input("Введите ID "))
        except ValueError:
            print("id должно быть числом.")
            return ValueError
        self.id = id
        self.name = input("Введите название лаборатории ")
        self.location = input("Введите расположение лаборатории ")
    def getLabInfo(self):
        print("Информация о лаборатории:")
        print(' ID лаборатории:', self.id)
        print(' Название лаборатории:', self.name)
        print(' Расположение лаборатории:', self.location)
    def writeLaboratoryJSON(self):
        lab = {
            "id": self.id,
            "name": self.name,
            "location": self.location
        }
        with open('laboratories.json', 'w') as json_file:
            json.dump(lab, json_file)
    def writeLaboratoryXML(self):
        root = ET.Element('labs')
        item = ET.SubElement(root, "lab")
        item.attrib["id"] = str(self.id)
        item.attrib["name"] = self.name
        item.attrib["location"] = self.location
        tree = ET.ElementTree(root)
        ET.indent(tree, '  ')
        tree.write('laboratories.xml')
    def readLaboratoryJSON(self):
        with open('laboratories.json', 'r') as json_file:
            data = json.load(json_file)
            print("Запись в файле JSON:")
            print(data)
    def readLaboratoryXML(self):
        print("Запись в файле XML:")
        tree = ET.parse('laboratories.xml')
        root = tree.getroot()
        for elem in root.iter():
            if elem.tag != 'labs':
                print(elem.tag, elem.attrib)