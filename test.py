import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize_sentence(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1


    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq

    sumValues = sum(sentenceValue.values())

    if len(sentenceValue) > 0:
        average = int(sumValues / len(sentenceValue))
    else:
        average = 0

    summary = ''

    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (0.2 * average)):
            summary += " " + sentence
    return summary

input_sentence = """Sixteen years after the Na'vi repelled the RDA invasion of Pandora,[a] Jake Sully lives as chief of the Omatikaya clan and raises a family with Neytiri, which includes sons Neteyam and Lo'ak, daughter Tuk, and adopted children Kiri (born from Grace Augustine's inert avatar) and Spider, the Pandora-born human son of the late Colonel Miles Quaritch. To the Na'vi's dismay, the RDA, led by their new leader Frances Ardmore, returns to colonize Pandora, as Earth is dying. Among the new arrivals are Recombinants—Na'vi avatars implanted with the memories of deceased human soldiers—with Quaritch's recombinant serving as the leader.

A year later, Jake leads a guerilla campaign against the RDA. During a counterinsurgency mission, Quaritch and his subordinates capture Jake's children. Jake and Neytiri arrive and free them, killing several of Quaritch's soldiers, but Spider remains captured by Quaritch, who recognizes him as his son. After the RDA fails to get information from Spider, Quaritch decides to spend time with his son to draw him on his side. In turn, Spider teaches Quaritch about Na'vi culture and language. Aware of the danger posed by Spider's knowledge of his whereabouts, Jake and his family exile themselves from the Omatikaya and retreat to Pandora's eastern seaboard, where the Metkayina clan gives them refuge. There, the family learns the ways of the reef people, Kiri develops a spiritual bond with the sea, and Lo'ak befriends Tsireya, the daughter of chief Tonowari and his wife, Ronal.

After defending Kiri against Aonung, Tonowari's son, Lo'ak apologizes at Jake's insistence. Aonung and his friends then entice Lo'ak to a trip into a sea predator's territory and leave him stranded. Lo'ak is saved from the predator and befriended by Payakan, a Tulkun—an intelligent and pacifistic whale-like species whom the Metkayina consider their spiritual brethren. Upon his return, Lo'ak wins Aonung's friendship by taking the blame for the trip, but is told that Payakan is an outcast among the Tulkun. Later, Kiri links to the Metkayina's underwater Spirit Tree and spiritually "meets" her biological mother, Grace, whose consciousness lives within Pandora. During the link-induced trance, Kiri suffers a seizure and falls unconscious, nearly drowning.

Jake summons Norm Spellman and Max Patel for help using their medical equipment, where they diagnose Kiri with epilepsy and warn that she cannot connect to the Spirit Tree again, as doing so may kill her. Although Ronal saves Kiri, Quaritch tracks Norm and Max's aircraft to the archipelago where the Metkayina live. Bringing Spider with him, Quaritch joins forces with the RDA's marine operations, led by Captain Mick Scoresby, and commandeers a whaling vessel that hunts Tulkuns to extract an anti-aging serum called amrita.[b] Quaritch's squad raids the archipelago, interrogating the tribes about Jake's location to no avail. Quaritch then orders the whalers to kill Tulkuns near the villages to draw Jake out. Lo'ak mentally links with Payakan and learns that he was cast out because he went against the pacifist ways of his species and attacked the whalers who killed his mother, causing many deaths.

When the Metkayina learns of the Tulkun killings, Lo'ak rushes off to warn Payakan, followed by his siblings and friends. They find Payakan being hunted, and Quaritch captures Lo'ak, Tsireya, and Tuk. Jake, Neytiri, and the Metkayina set out to confront the humans and rescue the kids. Quaritch forces Jake to surrender, but Payakan attacks the whalers, triggering a fight between the Metkayina and the humans. Spider cripples the vessel, and Neteyam rescues Lo'ak, Tsireya, and Spider but is fatally shot by one of Quaritch's men. Devastated, Jake and Neytiri go back to save their remaining children that were recaptured. Jake faces Quaritch, who uses Kiri as a hostage. When Neytiri does the same with Spider, Quaritch at first denies their relationship, but desists once Neytiri cuts Spider across the chest.

Jake, Quaritch, Neytiri, and Tuk end up trapped inside the sinking vessel. After a tense skirmish, Jake strangles Quaritch unconscious and is rescued by Lo'ak and Payakan, while Kiri recovers Neytiri and Tuk. Spider rescues Quaritch, but refuses to go with him and rejoins Jake's family, who welcomes him as a true son. After Neteyam's funeral, Jake informs Tonowari of his decision to leave the Metkayina. Still, the chief respectfully identifies Jake as part of the clan and welcomes him and his family to stay. Before vowing to resume their campaign against the RDA, Jake and his family accept and live their new life at sea."""
summary = summarize_sentence(input_sentence)
print(summary)
