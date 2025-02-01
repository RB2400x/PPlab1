from classes import *
def commands(objects: list, access: list):# функция, принимающая команды пользователя
    print("Введите команду. Список команд:\n"
            "Класс пациент:\n"
            " создать объект - pw\n"
            " изменить номер телефона - pcn\n"
            " вывести данные объекта - pr\n"
            "Класс врач:\n"
            " создать объект - dw\n"
            " вывести данные объекта - dr\n"
            "Класс запись на приём:\n"
            " создать объект - aw\n"
            " отменить запись - acn\n"
            " перенести запись - ars\n"
            " вывести данные объекта - ar\n"
            "Класс запись о приёме:\n"
            " создать объект - mw\n"
            " вывести данные объекта - mr\n"
            "Класс тест:\n"
            " создать объект - tw\n"
            " вывести данные объекта - tr\n"
            "Класс лаборатория:\n"
            " создать объект - lw\n"
            " вывести данные объекта - lr\n"
            "Завершение программы - e\n")
    c = input()
    match c:
        case 'pw':
            print("Введите данные пациента:")
            exc=objects[0].setPatient()
            if exc==None:
                access[0] = True
                objects[0].writePatientJSON()
                objects[0].writePatientXML()
                print("Создание объекта завершено")
            else:
                print("Создание объекта прервано")
        case 'pr':
            if access[0]:
                objects[0].getInfo()
                objects[0].readPatientJSON()
                objects[0].readPatientXML()
            else:
                print("Сначала нужно создать объект")
        case 'pcn':
            if access[0]:
                npn = input("Введите новый номер телефона ") #newPhoneNumber
                objects[0].updateContactInfo(npn)
                objects[0].writePatientJSON()
                objects[0].writePatientXML()
            else:
                print("Сначала нужно создать объект")
        case 'dw':
            print("Введите данные врача:")
            exc = objects[1].setDoctor()
            if exc == None:
                access[1] = True
                objects[1].writeDoctorJSON()
                objects[1].writeDoctorXML()
                print("Создание объекта завершено")
            else:
                print("Создание объекта прервано")
        case 'dr':
            if access[1]:
                objects[1].getInfo()
                objects[1].readDoctorJSON()
                objects[1].readDoctorXML()
            else:
                print("Сначала нужно создать объект")
        case 'aw':
            print("Введите данные о записи на приём:")
            exc = objects[2].setAppointment()
            if exc == None:
                access[2] = True
                objects[2].writeAppointmentJSON()
                objects[2].writeAppointmentXML()
                print("Создание объекта завершено")
            else:
                print("Создание объекта прервано")
        case 'ar':
            if access[2]:
                objects[2].getAppointmentInfo()
                objects[2].readAppointmentJSON()
                objects[2].readAppointmentXML()
            else:
                print("Сначала нужно создать объект")
        case 'ars':
            if access[2]:
                print("Введите новую дату:")
                apd = Date()  # appointment date
                exc = apd.setdate()
                if exc == None:
                    objects[2].rescheduleAppointment(apd)
                    objects[2].writeAppointmentJSON()
                    objects[2].writeAppointmentXML()
                else:
                    print("Перенос записи отменён")
            else:
                print("Сначала нужно создать объект")
        case 'acn':
            if access[2]:
                objects[2]=Appointment()
                objects[2].cancelAppointment()
                access[2] = False
            else:
                print("Сначала нужно создать объект")
        case 'mw':
            print("Введите данные записи о приёме:")
            exc = objects[3].setMedicalRecord()
            if exc == None:
                objects[3].writeMedicalRecordJSON()
                objects[3].writeMedicalRecordXML()
                access[3] = True
                print("Создание объекта завершено")
            else:
                print("Создание объекта прервано")
        case 'mr':
            if access[3]:
                objects[3].getRecordDetails()
                objects[3].readMedicalRecordJSON()
                objects[3].readMedicalRecordXML()
            else:
                print("Сначала нужно создать объект")
        case 'tw':
            print("Введите данные о тесте:")
            exc = objects[4].setTest()
            if exc == None:
                access[4] = True
                objects[4].writeTestJSON()
                objects[4].writeTestXML()
                print("Создание объекта завершено")
            else:
                print("Создание объекта прервано")
        case 'tr':
            if access[4]:
                objects[4].getTestDetails()
                objects[4].readTestJSON()
                objects[4].readTestXML()
            else:
                print("Сначала нужно создать объект")
        case 'lw':
            print("Введите данные о лаборатории:")
            exc = objects[5].setLaboratory()
            if exc == None:
                access[5] = True
                objects[5].writeLaboratoryJSON()
                objects[5].writeLaboratoryXML()
                print("Создание объекта завершено")
            else:
                print("Создание объекта прервано")
        case 'lr':
            if access[5]:
                objects[5].getLabInfo()
                objects[5].readLaboratoryJSON()
                objects[5].readLaboratoryXML()
            else:
                print("Сначала нужно создать объект")
        case 'e':
            print("Программа завершена")
        case _:
            print("Неверная команда")
    return c