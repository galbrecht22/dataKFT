from controller.Controller import Controller

INIT = True
EXTRACT = False
LOAD = True
TRANSFORM = True

if __name__ == '__main__':
    controller = Controller()

    if INIT:
        controller.init_environment(ingest=EXTRACT)

    if EXTRACT:
        controller.extract_tender_list(date_filter='2021-05-31')
        controller.extract_purchasers()
        controller.extract_ships()

    if LOAD:
        controller.load_tenders()
        controller.load_purchasers()
        controller.load_ships()

    if TRANSFORM:
        controller.transform()
