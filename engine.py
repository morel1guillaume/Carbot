
##dict of response for each type of intent
intent_response_dict = {
    "utter_bonjour":["Bonjour et bienvenue, Vous avez besoin d'un conseil ou d'un complément d'informaion sur votre véhicule, je me tiens à votre entière disposition pour vous apporter mon aide. Quelle est votre question"],
    "utter_vs":["A quel métier appartenez-vous ? (VS)"],
    "utter_vf":["A quel métier appartenez-vous ? (VF)"],
    "action_custom": ["Non Aphabet se charge de cette demande."],
    "action_pneu": ["pneu"],
    "action_pneu": ["pneu"],
    "utter_commande_vehicule": ["S'agit-il d'un VF ou VS ?"]

}

gstinfo_response_dict = {
    "GST": " Goods and Service Tax (GST) is a destination based tax on consumption of goods and services.",
    "benefits":"GST consumes more than a dozen taxes, thus making it hassle free and efficient.",
    "faq_link":'You can check all the answers here <a href="http://www.cbec.gov.in/resources//htdocs-cbec/deptt_offcr/faq-on-gst.pdf</a>'
}

gst_query_value_dict = {
    "12%":"Non-AC hotels, business class air ticket, frozen meat products, butter, cheese, ghee, dry fruits in packaged form, animal fat, sausage, fruit juices, namkeen and ketchup",
    "5%":"railways, air travel, branded paneer, frozen vegetables, coffee, tea, spices, kerosene, coal, medicines",
    "18%":"AC hotels that serve liquor, telecom services, IT services, flavored refined sugar, pasta, cornflakes, pastries and cakes",
    "28%":"5-star hotels, race club betting,wafers coated with chocolate, pan masala and aerated water",
    "exempt":"education, milk, butter milk, curd, natural honey, fresh fruits and vegetables, flour, besan"
}

def gst_info(entities):
    if entities == None:
        return "Could not find out specific information about this ..." +  gstinfo_response_dict["faq_link"]
    if len(entities) == 1:
        return gstinfo_response_dict[entities[0]]
    return "Sorry.." + gstinfo_response_dict["faq_link"]

def gst_query(entities):
    if entities == None:
        return "Could not query this ..." + gstinfo_response_dict["faq_link"]
    for ent in entities:
        qtype = ent["type"]
        qval = ent["entity"]
        if qtype == "gst-query-value":
            return gst_query_value_dict[qval]

        return gstinfo_response_dict[entities[0]]
    return "Sorry.." + gstinfo_response_dict["faq_link"]