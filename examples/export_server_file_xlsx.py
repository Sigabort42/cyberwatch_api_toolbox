"""Export vulnerability in file xlsx"""

from cbw_api_toolbox.cbw_api import CBWApi

import xlsxwriter

API_KEY = ''
SECRET_KEY = ''
API_URL = ''

leafs = [
    ("Ordinateurs", 9, ["Nom",
                        "Systeme d'exploitation",
                        "Groupes de l'ordinateur",
                        "Criticité",
                        "Statut",
                        "Nombre de vulnérabilités détectées",
                        "Statut correctif",
                        "Nombre de correctifs disponibles",
                        "Cyberwatch Mode"]),
    ("Vulnerabilité", 7, ["Vulnerabilité",
                          "Ordinateur affecté",
                          "Groupes de l'ordinateur affecté",
                          "Score CVSS",
                          "Technologies affectées",
                          "Date de détéction",
                          "Ignorée"]),
    ("Correctifs", 4, ["Ordinateur affecté",
                       "Technologies",
                       "Action corrective",
                       "Vulnérabilités"])
]

client = CBWApi(API_URL, API_KEY, SECRET_KEY)
servers = client.servers()
SERVERS = []

def export_server_xlsx():
    """Function to export server to an xlsx file"""
    print("Creating file server xlsx")
    workbook = xlsxwriter.Workbook(leafs[0][0] + ".xlsx")
    worksheet = workbook.add_worksheet(leafs[0][0])

    i = 0
    while i < leafs[0][1]:
        worksheet.write(0, i, leafs[0][2][i])
        i += 1

    i = 1
    for server in servers:
        print("1-Server::server id => {0} name => {1}".format(server.id, server.hostname))
        server = client.server(server.id)
        SERVERS.append(server)
        group_server = ""
        if server.groups:
            group_server = ', '.join([group.name for group in server.groups])
        worksheet.write(i, 0, server.hostname)
        worksheet.write(i, 1, server.os['name'] if server.os else "")
        worksheet.write(i, 2, group_server)
        worksheet.write(i, 3, server.criticality)
        worksheet.write(i, 4, server.status['comment'])
        worksheet.write(i, 5, str(server.cve_announcements_count))
        worksheet.write(i, 6, server.status['comment'])
        worksheet.write(i, 7, str(server.updates_count))
        worksheet.write(i, 8, str(server.agent_version))
        i += 1

    workbook.close()
    print("Done")
    return True

def export_correctifs_server_xlsx():
    """Function to export correctifs to an xlsx file"""
    print("Creating file correctifs xlsx")

    workbook = xlsxwriter.Workbook(leafs[2][0] + ".xlsx")
    worksheet = workbook.add_worksheet(leafs[2][0])

    i = 0
    while i < leafs[2][1]:
        worksheet.write(0, i, leafs[2][2][i])
        i += 1


    i = 1
    for server in SERVERS:
        if server.updates:
            print("3-Correctifs::server id => {0} name => {1}".format(server.id, server.hostname))
            for update in server.updates:
                worksheet.write(i, 0, server.hostname)
                if update['current']:
                    up = update["current"]["version"]
                else:
                    up = ""
                worksheet.write(i, 1, update["target"]["product"])
                worksheet.write(i, 2, up + " -> " + update["target"]["version"])

                cve_list = []
                for cve in update["cve_announcements"]:
                    cve_list.append(cve["cve_code"])
                worksheet.write(i, 3, ", ".join(cve_list))

                i += 1

    workbook.close()
    print("Done")
    return True

def export_vulnerability_xlsx():
    """Function to export vulnerability to an xlsx file"""
    print("Creating file vulnerabilité xlsx")

    workbook = xlsxwriter.Workbook(leafs[1][0] + ".xlsx")
    worksheet = workbook.add_worksheet(leafs[1][0])

    i = 0
    while i < leafs[1][1]:
        worksheet.write(0, i, leafs[1][2][i])
        i += 1

    i = 1
    for server in SERVERS:
        if server.cve_announcements:
            print("2-Vulnerability::server id => {0} name => {1}".format(server.id, server.hostname))
            for cve in server.cve_announcements:
                worksheet.write(i, 0, cve.cve_code)
                worksheet.write(i, 1, server.hostname)
                worksheet.write(i, 2, cve.cve_code)

                group_server = ""
                if server.groups:
                    group_server = ', '.join([group.name for group in server.groups])
                worksheet.write(i, 3, group_server)

                worksheet.write(i, 4, cve.cve_score)

                update = [update for update in server.updates]
                worksheet.write(i, 5, ', '.join([u['target']['product'] for u in update]))
                worksheet.write(i, 6, cve.created_at)
                i += 1

    workbook.close()
    print("Done")
    return True

def export_voc_file_xlsx():
    """Method to export vulnerability, server, correctifs to an xlsx files"""
    export_server_xlsx()
    export_vulnerability_xlsx()
    export_correctifs_server_xlsx()
    print("Done All")
    return True

print(export_voc_file_xlsx())
