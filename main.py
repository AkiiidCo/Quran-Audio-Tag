import os
import eyed3

folder = "./Audio/Quran-Mishary Alafasy"
artist = "Mishary Alafasy"
album = "Quran Mishary Alafasy"

titles = {
    "001": "001 Al-Fatiha",
    "002": "002 Al-Baqara",
    "003": "003 Al-Imran",
    "004": "004 An-Nisa",
    "005": "005 Al-Maida",
    "006": "006 Al-Anam",
    "007": "007 Al-Araf",
    "008": "008 Al-Anfal",
    "009": "009 At-Tawba",
    "010": "010 Yunus",
    "011": "011 Hud",
    "012": "012 Yusuf",
    "013": "013 Ar-Rad",
    "014": "014 Ibrahim",
    "015": "015 Al-Hijr",
    "016": "016 An-Nahl",
    "017": "017 Al-Isra",
    "018": "018 Al-Kahf",
    "019": "019 Maryam",
    "020": "020 Ta-Ha",
    "021": "021 Al-Anbiya",
    "022": "022 Al-Hajj",
    "023": "023 Al-Muminun",
    "024": "024 An-Nur",
    "025": "025 Al-Furqan",
    "026": "026 Ash-Shuara",
    "027": "027 An-Naml",
    "028": "028 Al-Qasas",
    "029": "029 Al-Ankabut",
    "030": "030 Ar-Rum",
    "031": "031 Luqman",
    "032": "032 As-Sajda",
    "033": "033 Al-Ahzab",
    "034": "034 Saba",
    "035": "035 Fatir",
    "036": "036 Ya-Sin",
    "037": "037 As-Saffat",
    "038": "038 Sad",
    "039": "039 Az-Zumar",
    "040": "040 Ghafir",
    "041": "041 Fussilat",
    "042": "042 Ash-Shura",
    "043": "043 Az-Zukhruf",
    "044": "044 Ad-Dukhan",
    "045": "045 Al-Jathiyah",
    "046": "046 Al-Ahqaf",
    "047": "047 Muhammad",
    "048": "048 Al-Fath",
    "049": "049 Al-Hujurat",
    "050": "050 Qaf",
    "051": "051 Adh-Dhariyat",
    "052": "052 At-Tur",
    "053": "053 An-Najm",
    "054": "054 Al-Qamar",
    "055": "055 Ar-Rahman",
    "056": "056 Al-Waqia",
    "057": "057 Al-Hadid",
    "058": "058 Al-Mujadila",
    "059": "059 Al-Hashr",
    "060": "060 Al-Mumtahina",
    "061": "061 As-Saff",
    "062": "062 Al-Jumua",
    "063": "063 Al-Munafiqun",
    "064": "064 At-Taghabun",
    "065": "065 At-Talaq",
    "066": "066 At-Tahrim",
    "067": "067 Al-Mulk",
    "068": "068 Al-Qalam",
    "069": "069 Al-Haaqqa",
    "070": "070 Al-Maarij",
    "071": "071 Nuh",
    "072": "072 Al-Jinn",
    "073": "073 Al-Muzzammil",
    "074": "074 Al-Muddathir",
    "075": "075 Al-Qiyama",
    "076": "076 Al-Insan",
    "077": "077 Al-Mursalat",
    "078": "078 An Naba",
    "079": "079 An-Naziat",
    "080": "080 Abasa",
    "081": "081 At-Takwir",
    "082": "082 Al-Infitar",
    "083": "083 Al-Mutaffifin",
    "084": "084 Al-Inshiqaq",
    "085": "085 Al-Burooj",
    "086": "086 At-Tariq",
    "087": "087 Al-Ala",
    "088": "088 Al-Ghashiya",
    "089": "089 Al-Fajr",
    "090": "090 Al-Balad",
    "091": "091 Ash-Shams",
    "092": "092 Al-Lail",
    "093": "093 Ad-Duha",
    "094": "094 Ash-Sharh",
    "095": "095 At-Tin",
    "096": "096 Al-Alaq",
    "097": "097 Al-Qadr",
    "098": "098 Al-Bayyina",
    "099": "099 Az-Zalzalah",
    "100": "100 Al-Adiyat",
    "101": "101 Al-Qaria",
    "102": "102 At-Takathur",
    "103": "103 Al-Asr",
    "104": "104 Al-Humaza",
    "105": "105 Al-Fil",
    "106": "106 Quraish",
    "107": "107 Al-Maun",
    "108": "108 Al-Kawthar",
    "109": "109 Al-Kafirun",
    "110": "110 An-Nasr",
    "111": "111 Al-Masad",
    "112": "112 Al-Ikhlas",
    "113": "113 Al-Falaq",
    "114": "114 An-Nas",
}

audio_files = os.listdir(folder)
audio_files.sort()

if ".DS_Store" in audio_files:
    audio_files.remove(".DS_Store")

print("audio_files: ", audio_files)

for i in range(len(audio_files)):
    audio_file = audio_files[i]

    audiofile = eyed3.load(folder + "/" + audio_file)
    audiofile.tag.artist = artist
    audiofile.tag.album_artist = artist
    audiofile.tag.album = album
    audiofile.tag.genre = "Quran"
    audiofile.tag.title = titles[audio_file.split(".")[0]]
    audiofile.tag.track_num = i + 1

    audiofile.tag.save()
