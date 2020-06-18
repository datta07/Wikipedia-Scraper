# Wikipedia Scraper
Python Program for Wikipedia Scraping.

## Features
      1) Short Description of the page
      2) Dictionary content of Page Bio or vcard info
      3) Scraps all the table content to json

## How To Use
      1) Install required packages using
            >> pip install -r requirements.txt
      2) Change the wikipedia page link in scraper.py
      3) Run scraper.py

## Example
   Response for https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam
      
      {
        "short-description":"Avul Pakir Jainulabdeen Abdul Kalam (/ˈæbdəl kəˈlɑːm/ (listen); 15 October 1931 – 27 July 2015) was an Indian aerospace scientist and politician who served as the 11th President of India from 2002 to 2007. He was born and raised in Rameswaram, Tamil Nadu and studied physics and aerospace engineering. He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of India for his work on the development of ballistic missile and launch vehicle technology.[2][3][4] He also played a pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.[5]\nKalam was elected as the 11th President of India in 2002 with the support of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the \"People's President\",[6] he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, India's highest civilian honour.\nWhile delivering a lecture at the Indian Institute of Management Shillong, Kalam collapsed and died from an apparent cardiac arrest on 27 July 2015, aged 83.[7] Thousands, including national-level dignitaries, attended the funeral ceremony held in his hometown of Rameshwaram, where he was buried with full state honours.[8]\n",

          "Info-data":{"Prime Minister":"Atal Bihari Vajpayee Manmohan Singh","Vice President":"Krishan Kant Bhairon Singh Shekhawat","Preceded by":"K. R. Narayanan","Succeeded by":"Pratibha Patil","Born":"Avul Pakir Jainulabdeen Abdul Kalam (1931-10-15)15 October 1931 Rameswaram, Madras Presidency, British India (present-day Tamil Nadu, India)","Died":"27 July 2015(2015-07-27) (aged 83) Shillong, Meghalaya, India","Resting place":"Pei Karumbu Ground, Rameswaram, Tamil Nadu, India","Alma mater":"St. Joseph's College, Tiruchirappalli (B.Eng.)Madras Institute of Technology (M.Eng.)","Profession":"Aerospace scientistAuthor","Awards":"Padma Bhushan (1981)   Padma Vibhushan (1990)   Bharat Ratna (1997) Hoover Medal (2009) NSS Von Braun Award (2013)","Notable work(s)":"Wings of Fire, India 2020, Ignited Minds, Indomitable Spirit, Transcendence: My Spiritual Experiences with Pramukh Swamiji","Signature":"","Website":"abdulkalam.com","Fields":"Aerospace Engineering","Institutions":"Defence Research and Development Organisation Indian Space Research Organisation"},

          "Tabuler data":{"table1":[{},{"2014":null,"Honorary professor":null,"Beijing University, China[171][172]":"/wiki/Beijing_University"},{"2014":null,"Doctor of Science":"/wiki/Doctor_of_Science","Edinburgh University, UK[173]":"/wiki/Edinburgh_University"},{"2013":null,"Von Braun Award":"/wiki/National_Space_Society#Awards","National Space Society":"/wiki/National_Space_Society"},{"2012":null,"Doctor of Laws (Honoris Causa)":"/wiki/Honoris_Causa","Simon Fraser University[174]":"/wiki/Simon_Fraser_University"},{"2011":null,"IEEE Honorary Membership":"/wiki/IEEE_Honorary_Membership","IEEE[175]":"/wiki/IEEE"},{"2010":null,"Doctor of Engineering":"/wiki/Doctor_of_Engineering","University of Waterloo[176]":"/wiki/University_of_Waterloo"},{"2009":null,"Honorary Doctorate":"/wiki/Honorary_Doctorate","Oakland University[177]":"/wiki/Oakland_University"},{"2009":null,"Hoover Medal":"/wiki/Hoover_Medal","ASME Foundation, USA[178]":"#cite_note-178"},{"2009":null,"International von Kármán Wings Award":null,"California Institute of Technology, USA[179]":"/wiki/California_Institute_of_Technology"},{"2008":null,"Doctor of Engineering (Honoris Causa)":"/wiki/Honoris_Causa","Nanyang Technological University, Singapore[180]":"/wiki/Nanyang_Technological_University"},{"2008":null,"Doctor of Science (Honoris Causa)":"/wiki/Honoris_Causa","Aligarh Muslim University, Aligarh[181][182]":"/wiki/Aligarh_Muslim_University"},{"2007":null,"Honorary Doctorate of Science and Technology":null,"Carnegie Mellon University[183]":"/wiki/Carnegie_Mellon_University"},{"2007":null,"King Charles II Medal":null,"Royal Society, UK[184][185][186]":"/wiki/Royal_Society"},{"2007":null,"Honorary Doctorate of Science":null,"University of Wolverhampton, UK[187]":"/wiki/University_of_Wolverhampton"},{"2000":null,"Ramanujan Award":null,"Alwars Research Centre, Chennai[188]":"#cite_note-iitm-188"},{"1998":null,"Veer Savarkar Award":null,"Government of India[13]":"/wiki/Government_of_India"},{"1997":null,"Indira Gandhi Award for National Integration":"/wiki/Indira_Gandhi_Award_for_National_Integration","Indian National Congress[13][188]":"#cite_note-PIB01march12-13"},{"1997":null,"Bharat Ratna":"/wiki/Bharat_Ratna","Government of India[188][189]":"#cite_note-iitm-188"},{"1995":null,"Honorary Fellow":null,"National Academy of Medical Sciences,[190]":"/wiki/National_Academy_of_Medical_Sciences"},{"1994":null,"Distinguished Fellow":null,"Institute of Directors (India)[191]":"/wiki/Institute_of_Directors_(India)"},{"1990":null,"Padma Vibhushan":"/wiki/Padma_Vibhushan","Government of India[188][192]":"#cite_note-iitm-188"},{"1981":null,"Padma Bhushan":"/wiki/Padma_Bhushan","Government of India[188][192]":"#cite_note-iitm-188"}],"table2":[{"":null,"Wikimedia Commons has media related to Avul Pakir Jainulabdeen Abdul Kalam.":"https://commons.wikimedia.org/wiki/Category:Avul_Pakir_Jainulabdeen_Abdul_Kalam"}],"table3":[{"":null,"Wikiquote has quotations related to: A. P. J. Abdul Kalam":"https://en.wikiquote.org/wiki/Special:Search/A._P._J._Abdul_Kalam"}],"table4":[{},{"ListList by longevity":"/wiki/List_of_presidents_of_India"},{"Rajendra PrasadSarvepalli RadhakrishnanZakir HussainV. V. GiriFakhruddin Ali AhmedNeelam Sanjiva ReddyZail SinghR. VenkataramanShankar Dayal SharmaK. R. NarayananA. P. J. Abdul KalamPratibha PatilPranab MukherjeeRam Nath Kovind (incumbent)":"/wiki/Rajendra_Prasad","":"/wiki/File:Flag_of_India.svg"},{"V. V. GiriMohammad HidayatullahB. D. Jatti":"/wiki/V._V._Giri"},{"EducationOfficial aircraftOfficial residencePresident's BodyguardPrevious experienceSpouses":"/wiki/List_of_Indian_Presidents_by_university_education"}],"table5":[{},{"C. Rajagopalachari, Sarvepalli Radhakrishnan, and C. V. Raman (1954)Bhagwan Das, Mokshagundam Visvesvarayya, and Jawaharlal Nehru (1955)Govind Ballabh Pant (1957)Dhondo Keshav Karve (1958)":"/wiki/C._Rajagopalachari","":"/wiki/File:Bharat_Ratna.jpg"},{"Bidhan Chandra Roy and Purushottam Das Tandon (1961)Rajendra Prasad (1962)Zakir Husain and Pandurang Vaman Kane (1963)Lal Bahadur Shastri (1966)Indira Gandhi (1971)V. V. Giri (1975)K. Kamaraj (1976)Mother Teresa (1980)":"/wiki/Bidhan_Chandra_Roy"},{"Vinoba Bhave (1983)Khan Abdul Ghaffar Khan (1987)M. G. Ramachandran (1988)B. R. Ambedkar and Nelson Mandela (1990)Rajiv Gandhi, Vallabhbhai Patel, and Morarji Desai (1991)Abul Kalam Azad, J. R. D. Tata, and Satyajit Ray (1992)Gulzarilal Nanda, Aruna Asaf Ali, and A. P. J. Abdul Kalam (1997)M. S. Subbulakshmi  and Chidambaram Subramaniam (1998)Jayaprakash Narayan, Amartya Sen, Gopinath Bordoloi, and Ravi Shankar (1999)":"/wiki/Vinoba_Bhave"},{"Lata Mangeshkar and Bismillah Khan (2001)Bhimsen Joshi (2008)C. N. R. Rao and Sachin Tendulkar (2014)Madan Mohan Malaviya and Atal Bihari Vajpayee (2015)Nanaji Deshmukh, Bhupen Hazarika, and Pranab Mukherjee (2019)":"/wiki/Lata_Mangeshkar"}],"table6":[{},{"Ebrahim AlkaziKishori AmonkarAmitabh BachchanTeejan BaiM. BalamuralikrishnaT. BalasaraswatiAsha BhosleNandalal BoseHariprasad ChaurasiaGirija DeviKumar GandharvaAdoor GopalakrishnanSatish GujralGangubai HangalBhupen HazarikaM. F. HusainIlaiyaraajaSemmangudi Srinivasa IyerBhimsen JoshiAli Akbar KhanAmjad Ali KhanAllauddin KhanBismillah KhanGhulam Mustafa KhanYamini KrishnamurthyDilip KumarR. K. LaxmanBirju MaharajKishan MaharajLata MangeshkarSonal MansinghMallikarjun MansurZubin MehtaMario MirandaChhannulal MishraKelucharan MohapatraRaghunath MohapatraJasraj MotiramBenode Behari MukherjeeHrishikesh MukherjeeRajinikanthRam NarayanD. K. PattammalK. Shankar PillaiBalwant Moreshwar PurandareAkkineni Nageswara RaoKaloji Narayana RaoSatyajit RayS. H. RazaZohra SehgalUday ShankarRavi ShankarV. ShantaramShivkumar SharmaUmayalpuram K. SivaramanM. S. SubbulakshmiK. G. SubramanyanKapila VatsyayanHomai VyarawallaK. J. Yesudas":"/wiki/Ebrahim_Alkazi"},{"Bimala Prasad ChalihaNaresh ChandraT. N. ChaturvediJayanto Nath ChaudhuriSuranjan DasRajeshwar DayalBasanti DeviP. N. DharJyotindra Nath DixitM. S. GillHafiz Mohamad IbrahimH. V. R. IyengarBhola Nath JhaDattatraya Shridhar JoshiAjudhiya Nath KhoslaRai KrishnadasaV. KrishnamurthyP. Prabhakar KumaramangalamPratap Chandra LalK. B. LallSam ManekshawOm Prakash MehraMohan Sinha MehtaM. G. K. MenonBrajesh MishraSumati MorarjeeA. Ramasamy MudaliarSardarilal Mathradas NandaChakravarthi V. NarasimhanBraj Kumar NehruBhairab Dutt PandeGhananand PandeVijaya Lakshmi PanditT. V. RajeswarC. R. Krishnaswamy RaoPattadakal Venkanna R. RaoV. K. R. V. RaoKhusro Faramurz RustamjiHarish Chandra SarinBinay Ranjan SenHomi SethnaArjan SinghHarbaksh SinghKirpal SinghManmohan SinghTarlok SinghLallan Prasad SinghBalaram SivaramanChandrika Prasad SrivastavaT. SwaminathanArun Shridhar VaidyaDharma ViraNarinder Nath Vohra":"/wiki/Bimala_Prasad_Chaliha"},{"V. S. R. ArunachalamJagdish BhagwatiSatyendra Nath BoseTara ChandSuniti Kumar ChatterjiD. P. ChattopadhyayaBhabatosh DattaAvinash DixitMahasweta DeviJohn Kenneth GalbraithSarvepalli GopalLakshman Shastri JoshiKaka KalelkarDhondo Keshav KarveGopinath KavirajKuvempuO. N. V. KurupPrasanta Chandra MahalanobisSitakant MahapatraJohn MathaiKotha Satchidananda MurthyGiani Gurmukh Singh MusafirBasanti Dulal NagchaudhuriBal Ram NandaR. K. NarayanP. ParameswaranAmrita PritamK. N. RajC. RangarajanRaja RaoRamoji RaoHormasji Maneckji SeervaiRajaram ShastriKalu Lal ShrimaliGovindbhai ShroffKhushwant SinghChandeshwar Prasad Narayan SinghPremlila Vithaldas ThackerseyMahadevi VarmaBashir Hussain Zaidi":"/wiki/V._S._R._Arunachalam"},{"Jasbir Singh BajajB. K. GoyalPurshotam LalA. Lakshmanaswami MudaliarS. I. PadmavatiAutar Singh PaintalKantilal Hastimal SanchetiBalu SankaranV. ShantaVithal Nagesh ShirodkarPrakash Narain TandonBrihaspati Dev TrigunaM. S. Valiathan":"/wiki/Jasbir_Singh_Bajaj"},{"Sunderlal BahugunaB. K. S. IyengarRambhadracharyaRavi ShankarVishwesha TeerthaJaggi Vasudev":"/wiki/Sunderlal_Bahuguna"},{"L. K. AdvaniMontek Singh AhluwaliaAruna Asaf AliFazal AliAdarsh Sein AnandMadhav Shrihari AneyParkash Singh BadalSikander BakhtMilon K. BanerjiMirza Hameedullah BegP. N. BhagwatiRaja ChelliahChandra Kisan DaphtaryNiren DeC. D. DeshmukhAnthony Lancelot DiasUma Shankar DikshitKazi Lhendup DorjeeGeorge FernandesP. B. GajendragadkarBenjamin GilmanIsmaïl Omar GuellehZakir HusainV. R. Krishna IyerJagmohanLakshmi Chand JainArun JaitleyAditya Nath JhaMurli Manohar JoshiAnerood JugnauthMehdi Nawaz JungAli Yavar JungVijay KelkarHans Raj KhannaV. N. KhareBalasaheb Gangadhar KherAkhlaqur Rahman KidwaiJivraj Narayan MehtaV. K. Krishna MenonHirendranath MukherjeeAjoy MukherjeePranab MukherjeePadmaja NaiduGulzarilal NandaGovind NarainFali Sam NarimanHosei NorotaNanabhoy PalkhivalaK. ParasaranHari Vinayak PataskarSunder Lal PatwaSharad PawarNaryana Raghvan PillaiSri PrakasaN. G. RangaRavi Narayana ReddyY. Venugopal ReddyGhulam Mohammed SadiqLakshmi SahgalP. A. SangmaM. C. SetalvadKaran SinghNagendra SinghSwaran SinghWalter SisuluSoli SorabjeeKalyan SundaramSushma SwarajChandulal Madhavlal TrivediAtal Bihari VajpayeeM. N. VenkatachaliahKottayan Katankot VenugopalJigme Dorji Wangchuck":"/wiki/L._K._Advani"},{"V. K. AatreSalim AliNorman BorlaugSubrahmanyan ChandrasekharRajagopala ChidambaramCharles CorreaSatish DhawanAnil KakodkarA. P. J. Abdul KalamKrishnaswamy KasturiranganHar Gobind KhoranaDaulat Singh KothariVerghese KurienRaghunath Anant MashelkarG. Madhavan NairRoddam NarasimhaJayant NarlikarRajendra K. PachauriBenjamin Peary PalYash PalI. G. PatelVenkatraman RamakrishnanK. R. RamanathanRaja RamannaC. R. RaoC. N. R. RaoPalle Rama RaoUdupi Ramachandra RaoVikram SarabhaiMan Mohan SharmaObaid SiddiqiE. SreedharanM. R. SrinivasanGeorge SudarshanM. S. Swaminathan":"/wiki/V._K._Aatre"},{"Baba AmtePandurang Shastri AthavaleJanaki Devi BajajMirabehnKamaladevi ChattopadhyayDurgabai DeshmukhNanaji DeshmukhNirmala DeshpandeMohan DhariaU. N. DhebarValerian GraciasVeerendra HeggadeMary Clubwala JadhavGaganvihari Lallubhai MehtaUsha MehtaSister NirmalaNellie Sengupta":"/wiki/Baba_Amte"},{"Viswanathan AnandEdmund HillaryMary KomSachin Tendulkar":"/wiki/Viswanathan_Anand"},{"Dhirubhai AmbaniGhanshyam Das BirlaAshok Sekhar GangulyKarim Al Hussaini Aga KhanLakshmi MittalAnil Manibhai NaikN. R. Narayana MurthyM. NarasimhamPrithvi Raj Singh OberoiAzim PremjiPrathap C. ReddyJ. R. D. TataRatan Tata":"/wiki/Dhirubhai_Ambani"},{" Portal Category WikiProject":"/wiki/Portal:India"}],"table7":[{},{"Sunil Gavaskar":"/wiki/Sunil_Gavaskar"},{"Vainu BappuPrafulla DesaiA. P. J. Abdul KalamGopinath MohantyPrabhat Kumar MukhopadhyayaAmritlal NagarMrinal SenAvabai Bomanji Wadia":"/wiki/Vainu_Bappu"},{"Jasbir Singh BajajS. BalachanderGottipati BrahmaiahRani GaidinliuKhadim Hussain KhanStella KramrischJal Minocher MehtaGrace MorleySyed Zahoor QasimKamal RanadiveP. N. Pattabhirama SastriJhabarmal SharmaAjit Ram Verma":"/wiki/Jasbir_Singh_Bajaj"},{"Richard AttenboroughDoraiswamy IyengarV. G. JogK. Sankaran NairPrem NazirSwraj Paul, Baron Paul RajkumarK. G. RamanathanKershasp Tehmurasp SatarawalaSubodh Chandra SenguptaAdi M. SethnaArun Kumar SharmaBenudhar SharmaBhalindra SinghUmrao Singh":"/wiki/Richard_Attenborough"},{"Horace AlexanderMichael FerreiraSivaji GanesanJnan Prakash GhoshKotha Satchidananda MurthyHosur NarasimhaiahSripada PinakapaniIshwari PrasadB. C. SanyalMarie SetonArchana SharmaObaid SiddiqiNatwar SinghGanda SinghVijay TendulkarBaldev Upadhyaya":"/wiki/Horace_Alexander"},{"Durga Das BasuShiba P. ChatterjeeEknath Vasant ChitnisVirender Lal ChopraGurbaksh Singh DhillonSantidev GhoshBhimsen JoshiTribhuvandas LuharSadat Abul MasudKalanidhi NarayananBernard PetersThakazhi Sivasankara PillaiGopala RamanujamS. RamaseshanVuppuluri Ganapathi SastryAmarjit SinghGurbachan Singh TalibBhalchandra UdgaonkarSrinivasan Varadarajan":"/wiki/Durga_Das_Basu"},{"Pushpa Mittra BhargavaEla BhattManohar Lal ChibberAminuddin DagarV. KrishnamurthyJean RiboudSidney Dillon RipleyRajeev SethiMartand SinghC. Venkataraman SundaramBadri Nath TandonGulshan Lal TandonR. K. Trivedi":"/wiki/Pushpa_Mittra_Bhargava"},{"Balamani AmmaKishori AmonkarNikhil BanerjeeRoddam NarasimhaR. D. PradhanAnnada Shankar RayJulio RibeiroMan Mohan SharmaLaxmi Prasad SihareFarokh UdwadiaMohammad Yunus":"/wiki/Balamani_Amma"},{"19th Kushok Bakula RinpocheRam Prakash BambahKartar Singh DuggalAshok Sekhar GangulyAbid HussainShreyans Prasad JainKelucharan MohapatraBal Ram NandaAkkineni Nageswara RaoPratury Trirumala RaoRenuka RayB. V. SreekantanSatya Pal Wahi":"/wiki/19th_Kushok_Bakula_Rinpoche"},{"Fenner Brockway, Baron BrockwayBanoo Jehangir CoyajiGirija DeviKattingeri Krishna HebbarGirilal JainAnna Rajam MalhotraM. V. MathurAshesh Prosad MitraRussi ModySuresh Shankar NadkarniNarinder Singh RandhawaYoshio SakurauchiLakshman SinghPrakash Narain Tandon":"/wiki/Fenner_Brockway,_Baron_Brockway"},{"# Posthumous conferral1954–19591960–19691970–19791980–19891990–19992000–20092010–20192020–2029":"/wiki/List_of_Padma_Bhushan_award_recipients_(1954%E2%80%931959)"}],"table8":[{},{"AvionicsTejasAdvanced Medium Combat AircraftOther HAL programmesHJT-36HTT-40DhruvRudraLight Combat HelicopterLight Utility HelicopterUnmanned aerial vehiclesNishantRustomLakshyaKapothakaUlkaFluffyAURA UAVImperial EagleNetra":"/wiki/HAL_Tejas","TejasAdvanced Medium Combat Aircraft":"/wiki/HAL_Tejas","HJT-36HTT-40DhruvRudraLight Combat HelicopterLight Utility Helicopter":"/wiki/HAL_HJT-36","NishantRustomLakshyaKapothakaUlkaFluffyAURA UAVImperial EagleNetra":"/wiki/DRDO_Nishant"},{"TejasAdvanced Medium Combat Aircraft":"/wiki/HAL_Tejas"},{"HJT-36HTT-40DhruvRudraLight Combat HelicopterLight Utility Helicopter":"/wiki/HAL_HJT-36"},{"NishantRustomLakshyaKapothakaUlkaFluffyAURA UAVImperial EagleNetra":"/wiki/DRDO_Nishant"},{"Small armsINSASVidhwansakMSMCMCIWSArtillery systems and ammunitionPinaka Multi Barrel Rocket LauncherM-46 CatapultBhim-T6Dhanush Howitzer":"/wiki/INSAS_rifle","INSASVidhwansakMSMCMCIWS":"/wiki/INSAS_rifle","Pinaka Multi Barrel Rocket LauncherM-46 CatapultBhim-T6Dhanush Howitzer":"/wiki/Pinaka_Multi_Barrel_Rocket_Launcher"},{"INSASVidhwansakMSMCMCIWS":"/wiki/INSAS_rifle"},{"Pinaka Multi Barrel Rocket LauncherM-46 CatapultBhim-T6Dhanush Howitzer":"/wiki/Pinaka_Multi_Barrel_Rocket_Launcher"},{"TanksArjunArjun Mk-IITank EXDRDO light tankInfantry fighting vehicleAbhay IFVOther vehiclesCarrier Mortar TrackedArmoured Engineer Reconnaissance VehicleLight Armoured VehicleKartik BLTDaksh":"/wiki/Arjun_(tank)","ArjunArjun Mk-IITank EXDRDO light tank":"/wiki/Arjun_(tank)","Abhay IFV":"/wiki/Abhay_IFV","Carrier Mortar TrackedArmoured Engineer Reconnaissance VehicleLight Armoured VehicleKartik BLTDaksh":"/wiki/Carrier_Mortar_Tracked"},{"ArjunArjun Mk-IITank EXDRDO light tank":"/wiki/Arjun_(tank)"},{"Abhay IFV":"/wiki/Abhay_IFV"},{"Carrier Mortar TrackedArmoured Engineer Reconnaissance VehicleLight Armoured VehicleKartik BLTDaksh":"/wiki/Carrier_Mortar_Tracked"},{"Electronic warfareSamyuktaTarang RadarsINDRARajendra RadarSwordfish Long Range Tracking RadarMulti-mode radar3D Airborne Warning and ControlSuper Vision-2000BFSR-SR3D-CARSwathi Weapon Locating RadarSoftwareNETRA":"/wiki/Samyukta_Electronic_Warfare_System","SamyuktaTarang ":"/wiki/Samyukta_Electronic_Warfare_System","INDRARajendra RadarSwordfish Long Range Tracking RadarMulti-mode radar3D Airborne Warning and ControlSuper Vision-2000BFSR-SR3D-CARSwathi Weapon Locating Radar":"/wiki/Indian_Doppler_Radar","NETRA":"/wiki/DRDO_NETRA"},{"SamyuktaTarang ":"/wiki/Samyukta_Electronic_Warfare_System"},{"INDRARajendra RadarSwordfish Long Range Tracking RadarMulti-mode radar3D Airborne Warning and ControlSuper Vision-2000BFSR-SR3D-CARSwathi Weapon Locating Radar":"/wiki/Indian_Doppler_Radar"},{"NETRA":"/wiki/DRDO_NETRA"},{"Ballistic missilesAgniAgni-IAgni-IIAgni-IIIAgni-IVAgni-VAgni-VIPrithviIIIIIIDhanushSRBMShauryaPrahaarSLBMK-15K-4K-5Cruise missilesNirbhayBrahMosIIHSTDVAir-to-air missilesAstra BVRAAMDRDO Anti-Radiation MissileAnti-tank missilesNagDRDO Anti Tank MissileSurface-to-airAkashTrishulMaitri missileBarak 8QRSAMAir-to-surfaceHelinaBrahMos Air launched VariantAnti-ballisticPrithvi Air Defence (PAD)Advanced Air Defence (AAD)TorpedoesAdvanced Light Torpedo ShyenaVarunastra Heavy Weight Torpedo":"/wiki/Ballistic_missile","AgniAgni-IAgni-IIAgni-IIIAgni-IVAgni-VAgni-VIPrithviIIIIIIDhanushSRBMShauryaPrahaarSLBMK-15K-4K-5":"/wiki/Agni_(missile)","Agni-IAgni-IIAgni-IIIAgni-IVAgni-VAgni-VI":"/wiki/Agni-I","IIIIIIDhanush":"/wiki/Prithvi_missile#Prithvi_I","ShauryaPrahaar":"/wiki/Shaurya_(missile)","K-15K-4K-5":"/wiki/Sagarika_(missile)","NirbhayBrahMosIIHSTDV":"/wiki/Nirbhay_missile","Astra BVRAAMDRDO Anti-Radiation Missile":"/wiki/Astra_missile","NagDRDO Anti Tank Missile":"/wiki/Nag_missile","AkashTrishulMaitri missileBarak 8QRSAM":"/wiki/Akash_missile","HelinaBrahMos Air launched Variant":"/wiki/Nag_missile#Advanced_variants","Prithvi Air Defence (PAD)Advanced Air Defence (AAD)":"/wiki/Indian_Ballistic_Missile_Defence_Programme#Prithvi_Air_Defence_(PAD)","Advanced Light Torpedo ShyenaVarunastra Heavy Weight Torpedo":"/wiki/Advanced_Light_Torpedo_Shyena"},{"AgniAgni-IAgni-IIAgni-IIIAgni-IVAgni-VAgni-VIPrithviIIIIIIDhanushSRBMShauryaPrahaarSLBMK-15K-4K-5":"/wiki/Agni_(missile)","Agni-IAgni-IIAgni-IIIAgni-IVAgni-VAgni-VI":"/wiki/Agni-I","IIIIIIDhanush":"/wiki/Prithvi_missile#Prithvi_I","ShauryaPrahaar":"/wiki/Shaurya_(missile)","K-15K-4K-5":"/wiki/Sagarika_(missile)"},{"Agni-IAgni-IIAgni-IIIAgni-IVAgni-VAgni-VI":"/wiki/Agni-I"},{"IIIIIIDhanush":"/wiki/Prithvi_missile#Prithvi_I"},{"ShauryaPrahaar":"/wiki/Shaurya_(missile)"},{"K-15K-4K-5":"/wiki/Sagarika_(missile)"},{"NirbhayBrahMosIIHSTDV":"/wiki/Nirbhay_missile"},{"Astra BVRAAMDRDO Anti-Radiation Missile":"/wiki/Astra_missile"},{"NagDRDO Anti Tank Missile":"/wiki/Nag_missile"},{"AkashTrishulMaitri missileBarak 8QRSAM":"/wiki/Akash_missile"},{"HelinaBrahMos Air launched Variant":"/wiki/Nag_missile#Advanced_variants"},{"Prithvi Air Defence (PAD)Advanced Air Defence (AAD)":"/wiki/Indian_Ballistic_Missile_Defence_Programme#Prithvi_Air_Defence_(PAD)"},{"Advanced Light Torpedo ShyenaVarunastra Heavy Weight Torpedo":"/wiki/Advanced_Light_Torpedo_Shyena"},{"Laser-guidedSudarshan Smart Anti-Airfield Weapon":"/wiki/Sudarshan_laser-guided_bomb","Sudarshan Smart Anti-Airfield Weapon":"/wiki/Sudarshan_laser-guided_bomb"},{"Sudarshan Smart Anti-Airfield Weapon":"/wiki/Sudarshan_laser-guided_bomb"},{"ScientistsMaj General Ranjit Lal JetleyRam Narain AgarwalA. P. J. Abdul KalamA. Sivathanu PillaiW SelvamurthyV. K. SaraswatV. K. AatreRaja RamannaV. S. MahalingamKeshav Dattatreya NayakTessy ThomasShashikala SinhaIpsita Biswas":"/wiki/Ranjit_Lal_Jetley","Maj General Ranjit Lal JetleyRam Narain AgarwalA. P. J. Abdul KalamA. Sivathanu PillaiW SelvamurthyV. K. SaraswatV. K. AatreRaja RamannaV. S. MahalingamKeshav Dattatreya NayakTessy ThomasShashikala SinhaIpsita Biswas":"/wiki/Ranjit_Lal_Jetley"},{"Maj General Ranjit Lal JetleyRam Narain AgarwalA. P. J. Abdul KalamA. Sivathanu PillaiW SelvamurthyV. K. SaraswatV. K. AatreRaja RamannaV. S. MahalingamKeshav Dattatreya NayakTessy ThomasShashikala SinhaIpsita Biswas":"/wiki/Ranjit_Lal_Jetley"},{"GTX 37-14UGTX-35VS KaveriKaveri Marine Gas TurbineGATET engine":"/wiki/Gas_Turbine_Research_Establishment#Products"},{"Project IndigoProject ValiantProject DevilIGMDPIndian Ballistic Missile Defence ProgrammeDYSLs":"/wiki/Project_Indigo"},{"Indian Missile ProgrammeIndian Armed Forces":"/wiki/Integrated_Guided_Missile_Development_Programme"}],"table9":[{"TejasAdvanced Medium Combat Aircraft":"/wiki/HAL_Tejas"},{"HJT-36HTT-40DhruvRudraLight Combat HelicopterLight Utility Helicopter":"/wiki/HAL_HJT-36"},{"NishantRustomLakshyaKapothakaUlkaFluffyAURA UAVImperial EagleNetra":"/wiki/DRDO_Nishant"}],"table10":[{"INSASVidhwansakMSMCMCIWS":"/wiki/INSAS_rifle"},{"Pinaka Multi Barrel Rocket LauncherM-46 CatapultBhim-T6Dhanush Howitzer":"/wiki/Pinaka_Multi_Barrel_Rocket_Launcher"}],"table11":[{"ArjunArjun Mk-IITank EXDRDO light tank":"/wiki/Arjun_(tank)"},{"Abhay IFV":"/wiki/Abhay_IFV"},{"Carrier Mortar TrackedArmoured Engineer Reconnaissance VehicleLight Armoured VehicleKartik BLTDaksh":"/wiki/Carrier_Mortar_Tracked"}],"table12":[{"SamyuktaTarang ":"/wiki/Samyukta_Electronic_Warfare_System"},{"INDRARajendra RadarSwordfish Long Range Tracking RadarMulti-mode radar3D Airborne Warning and ControlSuper Vision-2000BFSR-SR3D-CARSwathi Weapon Locating Radar":"/wiki/Indian_Doppler_Radar"},{"NETRA":"/wiki/DRDO_NETRA"}],"table13":[{"AgniAgni-IAgni-IIAgni-IIIAgni-IVAgni-VAgni-VIPrithviIIIIIIDhanushSRBMShauryaPrahaarSLBMK-15K-4K-5":"/wiki/Agni_(missile)","Agni-IAgni-IIAgni-IIIAgni-IVAgni-VAgni-VI":"/wiki/Agni-I","IIIIIIDhanush":"/wiki/Prithvi_missile#Prithvi_I","ShauryaPrahaar":"/wiki/Shaurya_(missile)","K-15K-4K-5":"/wiki/Sagarika_(missile)"},{"Agni-IAgni-IIAgni-IIIAgni-IVAgni-VAgni-VI":"/wiki/Agni-I"},{"IIIIIIDhanush":"/wiki/Prithvi_missile#Prithvi_I"},{"ShauryaPrahaar":"/wiki/Shaurya_(missile)"},{"K-15K-4K-5":"/wiki/Sagarika_(missile)"},{"NirbhayBrahMosIIHSTDV":"/wiki/Nirbhay_missile"},{"Astra BVRAAMDRDO Anti-Radiation Missile":"/wiki/Astra_missile"},{"NagDRDO Anti Tank Missile":"/wiki/Nag_missile"},{"AkashTrishulMaitri missileBarak 8QRSAM":"/wiki/Akash_missile"},{"HelinaBrahMos Air launched Variant":"/wiki/Nag_missile#Advanced_variants"},{"Prithvi Air Defence (PAD)Advanced Air Defence (AAD)":"/wiki/Indian_Ballistic_Missile_Defence_Programme#Prithvi_Air_Defence_(PAD)"},{"Advanced Light Torpedo ShyenaVarunastra Heavy Weight Torpedo":"/wiki/Advanced_Light_Torpedo_Shyena"}],"table14":[{"Agni-IAgni-IIAgni-IIIAgni-IVAgni-VAgni-VI":"/wiki/Agni-I"},{"IIIIIIDhanush":"/wiki/Prithvi_missile#Prithvi_I"},{"ShauryaPrahaar":"/wiki/Shaurya_(missile)"},{"K-15K-4K-5":"/wiki/Sagarika_(missile)"}],"table15":[{"Sudarshan Smart Anti-Airfield Weapon":"/wiki/Sudarshan_laser-guided_bomb"}],"table16":[{"Maj General Ranjit Lal JetleyRam Narain AgarwalA. P. J. Abdul KalamA. Sivathanu PillaiW SelvamurthyV. K. SaraswatV. K. AatreRaja RamannaV. S. MahalingamKeshav Dattatreya NayakTessy ThomasShashikala SinhaIpsita Biswas":"/wiki/Ranjit_Lal_Jetley"}],"table17":[{},{"Department of Space (DoS)":"/wiki/Department_of_Space"},{"Indian Space Research Organisation (ISRO)Antrix CorporationIndian Institute of Space Science and Technology (IIST)Indian Institute of Remote Sensing (IIRS)Laboratory for Electro-Optics Systems (LEOS)National Atmospheric Research Laboratory (NARL)New Space India Limited (NSIL)Physical Research Laboratory (PRL)Development and Educational Communication Unit (DECU)Integrated Space CellDefence Space Agency":"/wiki/Indian_Space_Research_Organisation","":"/wiki/File:Indian_Space_Research_Organisation_Logo.svg"},{"BhaskaraGAGANGSATINSATIRNSSIRSCartosatRISATRohiniSROSSChandrayaanHuman Spaceflight Programme":"/wiki/Bhaskara_(satellite)"},{"APPLEAryabhataHAMSATIMS-1Megha-TropiquesNISARSARALSouth Asia SatelliteSRESRE IIKalpana-1CARE":"/wiki/Ariane_Passenger_Payload_Experiment"},{"AstrosatAditya-L1 (planned)XPoSat (planned)AstroSat-2 (proposed)":"/wiki/Astrosat"},{"Chandrayaan-1Chandrayaan-2Chandrayaan-3 (planned, 2021)Lunar Polar Exploration Mission (proposed)Mars Orbiter MissionMars Orbiter Mission 2 (proposed)Shukrayaan-1 (proposed)":"/wiki/Chandrayaan-1"},{"Gaganyaan (Under development)":"/wiki/Gaganyaan"},{"EnginesCE-7.5CE-20VikasOrbitalSLVASLVPSLVGSLVMk IMk IIMk IIISuborbitalRohiniATVConceptsULVUnder developmentRLV Technology Demonstration ProgrammeRLV-TDHEXSSLVSCE-200":"/wiki/CE-7.5"},{"Indian Deep Space Network (IDSN)ISRO Satellite Centre (ISAC)ISRO Telemetry, Tracking and Command Network (ISTRAC)Master Control Facility (MCF)Satish Dhawan Space Centre (SDSC)Thumba Equatorial Rocket Launching Station (TERLS)ISRO Satellite Integration and Testing Establishment (ISITE)Vikram Sarabhai Space Center (VSSC)Liquid Propulsion Systems Centre (LPSC)ISRO Propulsion ComplexHuman Space Flight Centre (HSFC)":"/wiki/Indian_Deep_Space_Network"},{"SAGA-220 (supercomputer)RESPOND":"/wiki/SAGA-220"},{"List of Indian satellitesList of Satish Dhawan Space Centre launchesList of ISRO missionsList of ISRO chairpersons":"/wiki/List_of_Indian_satellites"}],"table18":[{},{"TrombayPokhranCIRUS reactorRajasthanThar Desert":"/wiki/Trombay"},{"Defence Research and Development OrganisationTerminal Ballistics Research LaboratoryHigh Energy Materials Research LaboratoryBhabha Atomic Research Centre":"/wiki/Defence_Research_and_Development_Organisation"},{"Indira GandhiJagjivan RamTapishwar Narain RainaSwaran Singh":"/wiki/Indira_Gandhi"},{"Raja RamannaHomi SethnaWaman Dattatreya PatwardhanP. K. IyengarRajagopala ChidambaramRavi GroverAnil KakodkarA. K. GangulyM. P. Parameswaran":"/wiki/Raja_Ramanna"},{"Indian nuclear programmeHistory of nuclear weaponsPokhran-II (May 13, 1998)Indo-American nuclear dealNuclear proliferation":"/wiki/India_and_weapons_of_mass_destruction"},{"See also: Nuclear power in India":"/wiki/Nuclear_power_in_India"}],"table19":[{"BNF: cb13756488m (data)CANTIC: a11179582GND: 124468047ISNI: 0000 0000 8128 1158LCCN: n98925888NDL: 01087382NLA: 41505655NLI: 004940823NLK: KAC200902737NTA: 326558217SUDOC: 061027200Trove: 1440106VIAF: 49404258 WorldCat Identities: lccn-n98925888":"/wiki/BNF_(identifier)"}]}
      }
