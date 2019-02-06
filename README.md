# Google Search Results in Python

This Python package allows you to scrape and parse Google Search Results using [SerpWow](https://serpwow.com). In addition to [Search](https://serpwow.com/docs/search/overview) you can also use this package to access the SerpWow [Locations API](https://serpwow.com/docs/locations/overview) and [Account API](https://serpwow.com/docs/account/overview).

## Installation
You can install google-search-results-serpwow with:

```shell
$ pip install google-search-results-serpwow
```

and upgrade with:

```shell
$ pip install google-search-results-serpwow --upgrade
```

## Documentation
We have included examples here but full SerpWow API documentation is available at the [API Docs](https://serpwow.com/docs):
- [Search API Docs](https://serpwow.com/docs/search/overview) 
- [Locations API Docs](https://serpwow.com/docs/locations/overview) 
- [Account API Docs](https://serpwow.com/docs/account/overview)

You can also use the [API Playground](https://app.serpwow.com/playground) to visually build Google search requests using SerpWow.

## Simple Example
Simplest example for a standard query "pizza", returning the Google SERP (Search Engine Results Page) data as JSON:
```python
from serpwow.google_search_results import GoogleSearchResults
import json

# create the serpwow object, passing in our API key
serpwow = GoogleSearchResults("demo")

# set up a dict for the search parameters
params = {
  "q" : "pizza"
}

# retrieve the search results as JSON
result = serpwow.get_json(params)

# pretty-print the result
print json.dumps(result, indent=2, sort_keys=True)
```

## Response
```json
{
request_info: {
success: true
},
search_metadata: {
id: "20c8e44e9cacedabbdff2d9b7e854436056d4f33",
created_at: "2019-02-06T13:32:55.978Z",
processed_at: "2019-02-06T13:32:56.113Z",
google_url: "https://www.google.com/search?q=pizza&oq=pizza&sourceid=chrome&ie=UTF-8",
cached: true,
total_time_taken: 0.14
},
search_parameters: {
q: "pizza"
},
search_information: {
total_results: 1480000000,
time_taken_displayed: 0.45,
query_displayed: "pizza",
detected_location: "Ireland"
},
local_map: {
link: "https://www.google.com/search?q=pizza&npsic=0&rflfq=1&rldoc=1&rlha=0&rllag=53350059,-6249133,1754&tbm=lcl&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4QtgN6BAgBEAQ",
gps_coordinates: {
latitude: 53.350059,
longitude: -6.249133,
altitude: 1754
},
local_results: [
{
position: 1,
title: "Apache Pizza Temple Bar",
extensions: [
"American-style pizza-delivery chain"
],
rating: 3.6,
reviews: 382,
type: "Pizza",
block_position: 1
},
{
position: 2,
title: "Ciao Woodfire Pizza",
extensions: [
"Casual",
"Vegetarian options",
"Delivery"
],
rating: 4.3,
reviews: 80,
price: "€",
type: "Pizza",
block_position: 1
},
{
position: 3,
title: "Independent Pizza Company",
extensions: [
"American-style pizza restaurant"
],
rating: 4.4,
reviews: 458,
type: "Pizza",
block_position: 1
}
],
knowledge_graph: {
title: "Pizza",
type: "Dish",
description: "Pizza is a savory dish of Italian origin, consisting of a usually round, flattened base of leavened wheat-based dough topped with tomatoes, cheese, and various other ingredients baked at a high temperature, traditionally in a wood-fired oven.",
source: {
name: "Wikipedia",
link: "https://en.wikipedia.org/wiki/Pizza"
},
nutrition_facts: {
total_fat: [
"10 g",
"15%"
],
saturated_fat: [
"4.5 g",
"22%"
],
polyunsaturated_fat: [
"1.7 g"
],
monounsaturated_fat: [
"2.6 g"
],
trans_fat: [
"0.2 g"
],
cholesterol: [
"17 mg",
"5%"
],
sodium: [
"598 mg",
"24%"
],
potassium: [
"172 mg",
"4%"
],
total_carbohydrate: [
"33 g",
"11%"
],
dietary_fiber: [
"2.3 g",
"9%"
],
sugar: [
"3.6 g"
],
protein: [
"11 g",
"22%"
]
}
},
related_searches: [
{
query: "apache pizza",
link: "https://www.google.com/search?q=apache+pizza&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q1QIoAHoECAUQAQ"
},
{
query: "domino's pizza",
link: "https://www.google.com/search?q=domino%27s+pizza&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q1QIoAXoECAUQAg"
},
{
query: "dominos pizza",
link: "https://www.google.com/search?q=dominos+pizza&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q1QIoAnoECAUQAw"
},
{
query: "pizza delivery dublin",
link: "https://www.google.com/search?q=pizza+delivery+dublin&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q1QIoA3oECAUQBA"
},
{
query: "pizza near me",
link: "https://www.google.com/search?q=pizza+near+me&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q1QIoBHoECAUQBQ"
},
{
query: "four star pizza",
link: "https://www.google.com/search?q=four+star+pizza&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q1QIoBXoECAUQBg"
},
{
query: "pizza hut",
link: "https://www.google.com/search?q=pizza+hut&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q1QIoBnoECAUQBw"
},
{
query: "apache pizza menu",
link: "https://www.google.com/search?q=apache+pizza+menu&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q1QIoB3oECAUQCA"
}
],
related_places: [
{
link: "https://www.google.com/search?tbm=lcl&q=pizza&rflfq=1&num=20&stick=H4sIAAAAAAAAAB1QS0pDQRAki4hrn7h4qxyhu_q_9SZCAgZBxASEHMcTeC5PYT1nMTNdUNVVdX-3LuhAD6bVBpIR0usSWhs0aWLpKtG6PqoHzMJtvNOlrBvrg0HGiuxogZWUrsu0eKVqiyREuoLgtqCRQECjPapATdOSGDWM6ZBVgXWx7HaqasLUPEVqXXSg6QUTunNRWlsXzj4akUihv6LnTRTigxiZbO9IDfKtaHyykBV0xK1O0OiSwhyEt2_2yecbMtqaUdxZuakGSqs90TXFuJlGFJ1TMkwz5mAFyv6y1EE2I4g43P-9Bn9iwhSTklXKVhTmw01myRODCoLOPtiGIVTLmFF-drvf3dPz6XI9HM_v76fPy-HrfH09vJ2Pl-_9_uN8u738AZh-lQfPAQAA&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q_KoBMA16BAgCEAM",
theme: "Best dinners with kids",
places: "Pinocchio Italian Restaurant - Temple Bar, Cafe Topolisand more",
images: [
"https://lh5.googleusercontent.com/p/AF1QipNhGt40OpSS408waVJUHeItGrrGqImmEKzuVbBv=w152-h152-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipMzhfQ6u9DOuLAY-rPhHaYouDQyyFy6085y7xtu=w102-h57-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipPNqK84NbZBzDUV1Vn5sueyYSZMwpvGrxush_T5=w102-h57-n-k-no"
]
},
{
link: "https://www.google.com/search?tbm=lcl&q=pizza&rflfq=1&num=20&stick=H4sIAAAAAAAAAB1QvU1DYRBTiiBaCNWrWADp7PvfgSUigcJrIgqqjMMEzMUU3MdVJ8vns31_tz0hTaCSZMLMhKjcTiWgspWmBq-uqO0UsIwWoYqqGtuG6VJVbmmhFiRMa0QVKd5YEmixTOd26potgBIJilQ6hhrmI9QCjzTaHPWokuJYxlqKpNb8z_B2GCuycmwUa3tUSmsW1GuMpeTSJK3mv3Z7U2hWPuh8YQfEPTsiR6cXKqFhDLd2ddB1rFqHT5ZcQTF7BIeKZsTUIQOkjk7IKrAjM9sHaQ8d6YXSnMNcjhIwsFetNqnZ0h2G1Db8U4MN0UkbXXMUje0ETMU20aaHGafh53D4PTy8nr_eX6775ePr-W2_7tfL9_H4ud9u5z8CuZO3zgEAAA&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q_KoBMA56BAgCEAU",
theme: "Late-night dining",
places: "Boco, Namaste Indiaand more",
images: [
"https://lh5.googleusercontent.com/p/AF1QipPplDG-CdG87ReWIHEUy7M-Nzn3N119mf78TT4_=w152-h152-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipNpPfdjCOSjQ1pshTzJ6gwtjfwxtPey3rHKHMjW=w102-h57-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipOeAIOYK5sw8nCFUUK03_62o0poG2qjqA-SNQy8=w102-h57-n-k-no"
]
},
{
link: "https://www.google.com/search?tbm=lcl&q=pizza&rflfq=1&num=20&stick=H4sIAAAAAAAAACVRu01EQRDTBYfIkO4RvYgS5uf5dEELLyBAJEggIa4cKri6qAKviFbr9dge7_3d_qiuJRh1G9eRqILtW3WahQjEcrqlIKSGpguiIzMd4m2yb5DuRlSkB4c0vPeL1uQUePEG4F0ctyYmU0WrMDHXXqhFM4DPYAhGNIg29UPhqkXlyTDsW0ZXOLOUM2xPyxJoRSkoIe1epjOzb014AmZl_h87SUWaG6ntAbXg0ksAjmxrK6FbNgd9v8C4UK8OMtFGElvxiZAc0KZqoGrLXxhFfJBsRIrdNP05LCrcjuckqleBlW7qHmSXziptoeJsyYAOMGg6nxbXYwXnh9DbDGV2O51-Tw_Pr9fr8fR5vL0cX8f3x8_5_L6QPyk2E4XNAQAA&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q_KoBMA96BAgCEAc",
theme: "Pizza takeaways",
places: "Dublin Pizza Company, Honest To Goodness Cafe And Pizzaand more",
images: [
"https://lh5.googleusercontent.com/p/AF1QipM2mVPCTr9GPY3PVPN15SOjqzyf1cO2USxJtkrK=w152-h152-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipNlVdW8axoHQX5d2Q9lhti2P4f2zIeBtAAh5-KG=w102-h57-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipOIoaeHqOQbmtYzLf0lxO4KjLa-PBG_06-Ek3EU=w102-h57-n-k-no"
]
},
{
link: "https://www.google.com/search?tbm=lcl&q=pizza&rflfq=1&num=20&stick=H4sIAAAAAAAAABVQuY1bUQyEgjUcS45-pBKG55CpOxEMBQYMeIFVtOW4AtflKjz_RQ_kcK6vX47bDpJtNkA7MCw7buaRuzYRrVfrrOObORs91ezRz4fTmoYRtRa-YSsulh83rdwTKHjvDFgQNGtLtKWbrAQNPK7h2OBY1MCDmgrJhAXoTstMuA1lNcy3jN0emEx5Oa6LUQQ3rrEkjj1uPuWzviJdR1dhxFnhVfK3HdvGiXSdm1A4pSvXLRinT-tA5aTCRyHGcdyUGLA-IwhsRp6kOqJzXG6wVYonKG06T13VIq0o1XcVjws03MgmvVPAk87SpzmEKvVRTKbsI131IINJ_L1c_l2u358fr_v7r8eP58f99fv-fLz-vL29__z8fPwHQ-QPickBAAA&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q_KoBMBB6BAgCEAk",
theme: "Best places to eat",
places: "Ciao Bella Roma, CheckPoint Pizzaand more",
images: [
"https://lh5.googleusercontent.com/p/AF1QipONhxEqcPsl27RwWiNRoo3gzC2PU0MGgxkFexog=w152-h152-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipNsWNtqugo3fvb1Qm3h1jYNkBoNxnPisUyOQclG=w102-h57-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipOwQTN2a5003KndO0tsCY9zHDOcL1JkbkuqW66c=w102-h57-n-k-no"
]
},
{
link: "https://www.google.com/search?tbm=lcl&q=pizza&rflfq=1&num=20&stick=H4sIAAAAAAAAAB2QuU2EURCDtQGIEPETvYgS5vIcXdACEhusRIBAIqAcKqAuqsBvs3d4xp99d7sOy0y1HkF2epqi1qOaRQvGZzAmFtFYh5dLTbRpJEZcBJQK2nVG0eE5bTmxHrQmp6Dh3gC8i07CORWP0QC6zHodyQFPaUplzADb9tRYTAxKIty8zNcxDVEMSOhhrbDZUsmypAzumlWdug5-Rve46kTBx9soRZobNm9ALdSvAMzOq8goyTfsDmWMbkllwq4O3tvL2IsxKKFbJ3nmAlTzvVSqtYyxch1V7tPOViWkWQNmPcAiSRIiydVs2rcTacpNSd_JykM4rtPCsiW0keWMlr-n09_p_vny_f3y9Hp-u3ydPy7nz5-bm_f99A9iWNweygEAAA&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q_KoBMBF6BAgCEAs",
theme: "Pizza deliveries",
places: "Apache Pizza O'Connell Street, Quick Pizza and Peri Peri Chickenand more",
images: [
"https://lh5.googleusercontent.com/p/AF1QipOkjGA3wCtMAC14dTbbc0Jir5VrsGCumTougi2l=w152-h152-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipNEBa3VDP3HjiEkEFQ1hsYKCzoiheXwYV1VqjWM=w102-h57-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipMiByet5OwZJPSn7wYxIQnyNEMIWlqGlwDjxPi3=w102-h57-n-k-no"
]
},
{
link: "https://www.google.com/search?tbm=lcl&q=pizza&rflfq=1&num=20&stick=H4sIAAAAAAAAAB2QO0qFUQyEuYVi_V-rU7kBIa_JYyP2gg8EUfHa6HJcgetyFc7vgdNMkpkvuThfm6d2B0ojU7X513FMShEq6UUFFliX6p3esauWmQ1OrSPrZiECsZxuKcjeqiUYdRvXkaiCUVWPkrBp0zFNGfd1bFHb-yw8FD2dvbbRaRW0GIKtXmyMshgFmC5K4OlZR3p6xDjjlI-kypWM1tXquwFLxZUixxPhZZCuMUcRftCFIk9Fqc5M0nJ2yq4SIQsS-b9RUOYJRvgqpJXzUwFrrqTCEaeJrE1rcgoa7g3Aew-CADJDzGZImiQ9eUUqPkFKyyBxrI3JAhOnnAZX05_D4few3dw_Xj-8P92_3D1_Xp3eXj9O32dnb09fX7d_4R_SL8YBAAA&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q_KoBMBJ6BAgCEA0",
theme: "Veg-friendly spots",
places: "Siri Indian Cuisine, Bagots Huttonand more",
images: [
"https://lh5.googleusercontent.com/p/AF1QipOJQrmxUne3F1V48SvuIVJw7HE8WHpdLcHpU-7X=w152-h152-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipPY194nnIFsu8szJ5yG4MdE1nQH3KqUbvG4ROew=w102-h57-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipP8d48uGHjmxpUTf0_VjjI3yI2c1cp7dcVsxcip=w102-h57-n-k-no"
]
},
{
link: "https://www.google.com/search?tbm=lcl&q=pizza&rflfq=1&num=20&stick=H4sIAAAAAAAAABVQOVIDQRArB6bIlyLYyE_oVt8xL3HAFXnLhsTP4QW8i1egTaZm1JJamseHdWm1aSQQ0GiPKqzLIAaiOgAkOqR1Z7q68JoKK8sUMlO9ckRgYmaO8VoXzn1G20jKpFXF-kR1moS3E7MQawhNhWSMwc25fzqbVJsplI5GuktMJnYDGqEa7ikTETNCFJ1TMsw93M8g2utiFob9adUOnWaChVuJl42YyLi2skDzzdjFGUfZbWSqIgKRakxZjnZGVWfQEZ6hWlbYQX7IcNoId1CN3qtasS09MmuarUb4KwxKK4orvMKy0neQ0uaEQt6GQgYlsncEWcicNP89HP4Ozy8fr-ftdNsuX7fT2-V6er9evrfbz_G4fd7v539Dd-ayzwEAAA&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q_KoBMBN6BAgCEA8",
theme: "Cheap spots for groups",
places: "Umi Falafel, Papa John's Pizzaand more",
images: [
"https://lh5.googleusercontent.com/p/AF1QipOcRwmUSTcFBk2_wjt93PLdlgqqqMv_xR9XfaV-=w152-h152-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipNMg1o-2EGsWhwMdSYfwLTp_OAkLsQZ_PNoz3HQ=w102-h57-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipOSB9M-uaOv9VwhP6u89Jf24QKda0rGQDQh2E7V=w102-h57-n-k-no"
]
},
{
link: "https://www.google.com/search?tbm=lcl&q=pizza&rflfq=1&num=20&stick=H4sIAAAAAAAAAB2Qu02EMRCEdcEhRHg_kSNK2PfuxFRywUmQnQQR5VABdVEFYyzZwT5mvvHjwzrcVQemiRC-Ia3rUHWPgLek8qSFrmctMU_smslYQizXURpdELbEuWSIXseImhvcwkNzMDXrSJmZjI7yKDMNZ5FzAei4F0_CmpqjjjHOJIkmsttoH2xaj0WUIDMBWYe552ikEDwKHfM_quWSMUFNT_ExWRdtcCDp68N1n96ZgsEbolkdFqDzOsBwJqowM8kh-I7vUz4RKmWUnQ3GqlmMJBzYO4QbBgDLFOskVGYZHdbFS2eHUVLxz3k3acNQKpmkq7Yp-k_ItEGACm0HPX9Op9_T0-vb7Xp_uV0_P77P5_v719f1D2Hcy-7DAQAA&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q_KoBMBR6BAgCEBE",
theme: "Cheap eats",
places: "aperitivo, Madina Desi Curry Coand more",
images: [
"https://lh5.googleusercontent.com/p/AF1QipOYiiTn-UudBLRkePxeB89k69xUDE5ilmDTM2pK=w152-h152-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipO5vUl1IjmZIHOU61ypc3JAxTP2o0zo5eUC7QVO=w102-h57-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipNAieDC_N9fPxeGuM9YXx7OB0OtLp4-VO71MsdX=w102-h57-n-k-no"
]
},
{
link: "https://www.google.com/search?tbm=lcl&q=pizza&rflfq=1&num=20&stick=H4sIAAAAAAAAABWPvWkDYRBEuUDGsc5g-CI3YNj_nW3AruOCCwxGmNMpUTmqwHWpCq2yZVjem3l9GTOXcFiKknMasZJ26BkmhAJ7sZAZxlGFShOsDhJNSh6zEwC3tFALETbFmBN9GpGTRAGUTv1ZHs2PSK5GVBaPN3aP1iaBQhLa_Ke9Up0UXcLBqPaNo1HTRSVU0I2CvEVa1shyTcksZ5ZmMhV7cGR3NGjr85mGeFiZqoGTeis6DeOu0wUzisQRaL-79pBIVE8VkRT7n6b79P79e9nX0-fXtq4f23rel8u2nPbz7XD4-7lelwdhjBC6TwEAAA&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q_KoBMBV6BAgCEBM",
theme: "Gluten-Free restaurants",
places: "Independent Pizza Company, Paulies Pizzaand more",
images: [
"https://lh5.googleusercontent.com/p/AF1QipOuL1PX6ZCTNOs6ZmH5f0oAtkbJl9cNs_TMrEow=w152-h152-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipP_Lfuu_a60iDwa-Ogx9pz113_28-1oRMleNk0M=w102-h57-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipMXin-v-A3E6JruEIOE742qiDUFLAjdlAoMEuHk=w102-h57-n-k-no"
]
},
{
link: "https://www.google.com/search?tbm=lcl&q=pizza&rflfq=1&num=20&stick=H4sIAAAAAAAAABWRS0oFUQxEeQPFsS0IPXIDQuWfbMS54AdB9PHEgS7HFbguV2HdHjWhUnVS9-J83xIKSMbEQEOkqvcrcWhqpIWVpE9Z1b5NeWjDVVBwKy9QWg4xlGqJO_ekl1RREi5Iq04J9dg3_qk6EDSfblRgvzTFUCMWDbXi2n45Mi1Yg_BRsbJ98xzLYKoGukYtGFMpnqDlkrarpZHIfLzEesCPeC2UapN9lMZGuAy67JuImTvzwctlYQqV8HCMSCKI2YWk0oZBbVkKQrUvpmEZRJAGki12hTA-TCO8apI7Um2ua8p-qj2V8MVjM9dRpT4SkZoQj5qeVf56DI7FZJEU6_49HP4O13ePz7dPp5fHt4fXr5un99PN8-n98_jxc3Z2fPn-vv8Hujir5M8BAAA&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q_KoBMBZ6BAgCEBU",
theme: "Veg-friendly for groups",
places: "Bach 16, Koh Restaurant & Cocktail Loungeand more",
images: [
"https://lh5.googleusercontent.com/p/AF1QipOsbpx9mTfH5mWSmEoNCp2zrHj3NwnebpCcDZre=w152-h152-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipNP4xqbTwRYlDvPYaET4YvIqiLrkFfA5z-G6O5x=w102-h57-n-k-no",
"https://lh5.googleusercontent.com/p/AF1QipPVhyEZWdBderrrwKqWBHHDhRn0KRGbaLoM3iGp=w102-h57-n-k-no"
]
}
],
pagination: {
current: "1",
next: "https://www.google.com/search?q=pizza&ei=fRZQXMKqL8en1fAPitiT8AI&start=10&sa=N&ved=0ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q8NMDCOkB",
other_pages: {
2: "https://www.google.com/search?q=pizza&ei=fRZQXMKqL8en1fAPitiT8AI&start=10&sa=N&ved=0ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q8tMDCNcB",
3: "https://www.google.com/search?q=pizza&ei=fRZQXMKqL8en1fAPitiT8AI&start=20&sa=N&ved=0ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q8tMDCNkB",
4: "https://www.google.com/search?q=pizza&ei=fRZQXMKqL8en1fAPitiT8AI&start=30&sa=N&ved=0ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q8tMDCNsB",
5: "https://www.google.com/search?q=pizza&ei=fRZQXMKqL8en1fAPitiT8AI&start=40&sa=N&ved=0ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q8tMDCN0B",
6: "https://www.google.com/search?q=pizza&ei=fRZQXMKqL8en1fAPitiT8AI&start=50&sa=N&ved=0ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q8tMDCN8B",
7: "https://www.google.com/search?q=pizza&ei=fRZQXMKqL8en1fAPitiT8AI&start=60&sa=N&ved=0ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q8tMDCOEB",
8: "https://www.google.com/search?q=pizza&ei=fRZQXMKqL8en1fAPitiT8AI&start=70&sa=N&ved=0ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q8tMDCOMB",
9: "https://www.google.com/search?q=pizza&ei=fRZQXMKqL8en1fAPitiT8AI&start=80&sa=N&ved=0ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q8tMDCOUB",
10: "https://www.google.com/search?q=pizza&ei=fRZQXMKqL8en1fAPitiT8AI&start=90&sa=N&ved=0ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4Q8tMDCOcB"
},
api_pagination: {
next: "https://api.serpwow.com/live/search?api_key=4BCC1B8B&q=pizza&start=10",
other_pages: {
2: "https://api.serpwow.com/live/search?api_key=4BCC1B8B&q=pizza&start=10",
3: "https://api.serpwow.com/live/search?api_key=4BCC1B8B&q=pizza&start=20",
4: "https://api.serpwow.com/live/search?api_key=4BCC1B8B&q=pizza&start=30",
5: "https://api.serpwow.com/live/search?api_key=4BCC1B8B&q=pizza&start=40",
6: "https://api.serpwow.com/live/search?api_key=4BCC1B8B&q=pizza&start=50",
7: "https://api.serpwow.com/live/search?api_key=4BCC1B8B&q=pizza&start=60",
8: "https://api.serpwow.com/live/search?api_key=4BCC1B8B&q=pizza&start=70",
9: "https://api.serpwow.com/live/search?api_key=4BCC1B8B&q=pizza&start=80",
10: "https://api.serpwow.com/live/search?api_key=4BCC1B8B&q=pizza&start=90"
}
}
},
organic_results: [
{
position: 1,
title: "10 Best Pizzas in Dublin - A slice of the city for every price point ...",
link: "https://www.independent.ie/life/travel/ireland/10-best-pizzas-in-dublin-a-slice-of-the-city-for-every-price-point-37248689.html",
domain: "www.independent.ie",
displayed_link: "https://www.independent.ie/.../10-best-pizzas-in-dublin-a-slice-of-the-city-for-every-p...",
snippet: "Oct 20, 2018 - Looking for the best pizza in Dublin? Pól Ó Conghaile scours the city for top-notch pie... whatever your budget.",
cached_page_link: "https://webcache.googleusercontent.com/search?q=cache:wezzRov42dkJ:https://www.independent.ie/life/travel/ireland/10-best-pizzas-in-dublin-a-slice-of-the-city-for-every-price-point-37248689.html+&cd=4&hl=en&ct=clnk&gl=ie",
block_position: 2
},
{
position: 2,
title: "Domino's Pizza: Pizza for Delivery or Takeaway Near You",
link: "https://www.dominos.ie/",
domain: "www.dominos.ie",
displayed_link: "https://www.dominos.ie/",
snippet: "Visit Domino's Pizza for a tasty pizza delivery or takeaway near you. Order online today for a piping hot pizza delivered directly to your door.",
cached_page_link: "https://webcache.googleusercontent.com/search?q=cache:djFeLNPbR3wJ:https://www.dominos.ie/+&cd=5&hl=en&ct=clnk&gl=ie",
related_page_link: "https://www.google.com/search?q=related:https://www.dominos.ie/+pizza&tbo=1&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4QHzAEegQICRAF",
block_position: 2
},
{
position: 3,
title: "Pizza Takeaway and Restaurant Delivery | Order Online at Just Eat",
link: "https://www.just-eat.ie/takeaways/pizza/",
domain: "www.just-eat.ie",
displayed_link: "https://www.just-eat.ie › Home › All cuisine types › Pizza",
snippet: "Who doesn't love pizza, right? Order online with Just Eat for collection or delivery from the best pizza takeaways and restaurants in your local area.",
cached_page_link: "https://webcache.googleusercontent.com/search?q=cache:G8MduioP3LoJ:https://www.just-eat.ie/takeaways/pizza/+&cd=6&hl=en&ct=clnk&gl=ie",
related_page_link: "https://www.google.com/search?q=related:https://www.just-eat.ie/takeaways/pizza/+pizza&tbo=1&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4QHzAFegQICxAG",
block_position: 2
},
{
position: 4,
title: "Pizza Delivery, Deals & Takeaway | Order Online with Pizza Hut Delivery",
link: "https://www.pizzahutdelivery.ie/",
domain: "www.pizzahutdelivery.ie",
displayed_link: "https://www.pizzahutdelivery.ie/",
snippet: "Pizza Hut - Order pizza online for free delivery, get the best deals, and find your nearest branch for dine-in or collection.",
cached_page_link: "https://webcache.googleusercontent.com/search?q=cache:2jlup2QZFpgJ:https://www.pizzahutdelivery.ie/+&cd=7&hl=en&ct=clnk&gl=ie",
block_position: 2
},
{
position: 5,
title: "The 10 Best Pizza Places in Dublin - TripAdvisor",
link: "https://www.tripadvisor.ie/Restaurants-g186605-c31-Dublin_County_Dublin.html",
domain: "www.tripadvisor.ie",
displayed_link: "https://www.tripadvisor.ie › ... › Province of Leinster › County Dublin › Dublin",
snippet: "Best Pizza in Dublin, County Dublin: Find TripAdvisor traveller reviews of Dublin Pizza places and search by price, location, and more.",
cached_page_link: "https://webcache.googleusercontent.com/search?q=cache:OS-Ar9hB_ngJ:https://www.tripadvisor.ie/Restaurants-g186605-c31-Dublin_County_Dublin.html+&cd=8&hl=en&ct=clnk&gl=ie",
related_page_link: "https://www.google.com/search?q=related:https://www.tripadvisor.ie/Restaurants-g186605-c31-Dublin_County_Dublin.html+pizza&tbo=1&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4QHzAHegQIDxAG",
block_position: 2
},
{
position: 6,
title: "Four Star Pizza Ireland, Pizza Delivery at its finest!",
link: "https://fourstarpizza.ie/",
domain: "fourstarpizza.ie",
displayed_link: "https://fourstarpizza.ie/",
snippet: "To bring you a truly authentic pizza experience our dough is still freshly made every day in each of our stores and we ensure that only the best ingredients are ...",
cached_page_link: "https://webcache.googleusercontent.com/search?q=cache:JqnTEa0okeoJ:https://fourstarpizza.ie/+&cd=9&hl=en&ct=clnk&gl=ie",
block_position: 2
},
{
position: 7,
title: "Pizza Delivery & Takeaway Artane, Clontarf, Marino, Fairview, Beaumont",
link: "https://www.apache.ie/pizza-apache-pizza-artane",
domain: "www.apache.ie",
displayed_link: "https://www.apache.ie/pizza-apache-pizza-artane",
snippet: "Any Large Pizza only €9.99 in Value Deals section! Pizza takeaway & delivery service in Artane. We also deliver to surrounding areas near Artane such as ...",
cached_page_link: "https://webcache.googleusercontent.com/search?q=cache:mwhDOeVShqoJ:https://www.apache.ie/pizza-apache-pizza-artane+&cd=10&hl=en&ct=clnk&gl=ie",
block_position: 2
},
{
position: 8,
title: "Pizza Delivery & Takeaway Temple Bar | Order Pizza Online - Dublin",
link: "https://www.apache.ie/pizza-apache-temple-bar",
domain: "www.apache.ie",
displayed_link: "https://www.apache.ie/pizza-apache-temple-bar",
snippet: "Pizza takeaway & delivery service in Temple Bar and areas near Temple Bar. Large Pizza only €9.99 in Value Deals section! Best quality and value around, ...",
cached_page_link: "https://webcache.googleusercontent.com/search?q=cache:G3eZzlW5-rMJ:https://www.apache.ie/pizza-apache-temple-bar+&cd=11&hl=en&ct=clnk&gl=ie",
block_position: 2
},
{
position: 9,
title: "Sano Pizza | Fresh Affordable & Delicious Pizza - Dublin",
link: "https://sano.pizza/",
domain: "sano.pizza",
displayed_link: "https://sano.pizza/",
snippet: "ABOUT. At Sano Pizza our Neapolitan Pizza is a softer style pizza, its chewy crusts and delicious flavours make is stand out from the crowd. Our dough is made ...",
cached_page_link: "https://webcache.googleusercontent.com/search?q=cache:tQPutmnVfH4J:https://sano.pizza/+&cd=12&hl=en&ct=clnk&gl=ie",
block_position: 2
},
{
position: 10,
title: "Pizza Republic: Pizza Dublin | Freshest Take Away & Delivery in Town",
link: "http://www.pizzarepublic.ie/",
domain: "www.pizzarepublic.ie",
displayed_link: "www.pizzarepublic.ie/",
snippet: "Order Pizza online in Dublin from Pizza Republic & have fresh Pizza delivered to your door. View Our Pizza Menu.",
cached_page_link: "http://webcache.googleusercontent.com/search?q=cache:B87n9p9hwMoJ:www.pizzarepublic.ie/+&cd=13&hl=en&ct=clnk&gl=ie",
related_page_link: "https://www.google.com/search?q=related:www.pizzarepublic.ie/+pizza&tbo=1&sa=X&ved=2ahUKEwiC3cLZ0JLgAhXHUxUIHQrsBC4QHzAMegQIDRAF",
block_position: 2
}
]
}
```

## Getting an API Key
To get a free API Key head over to [app.serpwow.com/signup](https://app.serpwow.com/signup).


## Searching with a location
Example of a Google query geo-locating the query as if the user were located in New York. 
```python
from serpwow.google_search_results import GoogleSearchResults
import json

# create the serpwow object, passing in our API key
serpwow = GoogleSearchResults("demo")

# set up a dict for the query (q) and location parameters
# note that the "location" parameter should be a value
# returned from the Locations API
params = {
  "q" : "pizza",
  "location" : "New York,New York,United States"
}

# retrieve the search results as JSON
result = serpwow.get_json(params)

# pretty-print the result
print json.dumps(result, indent=2, sort_keys=True)
```

## Searching Google Places, Google Videos, Google Images, Google Shopping and Google News
Use the ``search_type`` param to search Google Places, Videos, Images and News. See the [Search API Parameters Docs](https://serpwow.com/docs/search/parameters) for full details of the additional params available for each search type.
```python
from serpwow.google_search_results import GoogleSearchResults
import json

# create the serpwow object, passing in our API key
serpwow = GoogleSearchResults("demo")

# perform a search on Google News, just looking at blogs, filtering out duplicates
params = {
  "q" : "football news",
  "search_type" : "news",
  "news_type" : "blogs",
  "show_duplicates" : "false"
}
result = serpwow.get_json(params)
print json.dumps(result, indent=2, sort_keys=True)

# perform a search on Google Places for "plumber" in London
params = {
  "search_type" : "places",
  "q" : "plumber",
  "location" : "London,England,United Kingdom"
}
result = serpwow.get_json(params)
print json.dumps(result, indent=2, sort_keys=True)

# perform an image search on Google Images for "red flowers"
params = {
  "q" : "red flowers",
  "search_type" : "images"
}
result = serpwow.get_json(params)
print json.dumps(result, indent=2, sort_keys=True)
```

## Returning results as JSON, HTML and CSV
``google-search-results-serpwow`` can return data in JSON, HTML and CSV formats using the ``get_json``, ``get_html`` and ``get_csv`` methods. For CSV results use the ``csv_fields`` param ([docs](https://serpwow.com/docs/search/csvfields)) to request specific result fields.
```python
from serpwow.google_search_results import GoogleSearchResults
import json

# create the serpwow object, passing in our API key
serpwow = GoogleSearchResults("demo")

# set up a dict for the query (q) and location parameters
# note that the "location" parameter should be a value
# returned from the Locations API
params = {
  "q" : "pizza",
  "location" : "New York,New York,United States"
}

# retrieve the search results as JSON
result_json = serpwow.get_json(params)

# retrieve the search results as HTML
result_html = serpwow.get_html(params)

# retrieve the search results as CSV
result_csv = serpwow.get_csv(params)
```

## Requesting mobile and tablet results
To request that SerpWow renders the Google search results via a mobile or tablet browser use the ``device`` param:
```python
from serpwow.google_search_results import GoogleSearchResults
import json

serpwow = GoogleSearchResults("demo")

# set up the mobile params
params_mobile = {
  "q" : "pizza",
  "device" : "mobile"
}

# set up the tablet params
params_tablet = {
  "q" : "pizza",
  "device" : "tablet"
}

# set up the desktop params (note we omit the "device" param)
params_desktop = {
  "q" : "pizza"
}

# retrieve the mobile search results
result_mobile_json = serpwow.get_json(params_mobile)

# retrieve the tablet search results
result_tablet_json = serpwow.get_json(params_tablet)

# retrieve the desktop search results
result_desktop_json = serpwow.get_json(params_desktop)
```

## Parsing results
When making a request via the ``get_json`` method a standard Python ``dict`` is returned. You can inspect this dict to iterate, parse and store the results in your app.
```python
from serpwow.google_search_results import GoogleSearchResults
import json

# make a simple query, returning JSON
serpwow = GoogleSearchResults("demo")
result = serpwow.get_json({ "q" : "pizza" })

# determine if the request was successful
success = result["request_info"]

if success:
  
  # extract the time taken and number of organic results
  time_taken = result["search_metadata"]["total_time_taken"]
  organic_result_count = len(result["organic_results"])

  # print
  print str(organic_result_count) + " organic results returned in " + str(time_taken) + "s"
```

## Paginating results, returning up to 100 results per page
Use the ``start`` and ``num`` parameters to paginate through Google search results. ``start`` is 0-based. The maximum number of results returned per page (controlled by the ``num`` param) is 100 (a Google-imposed limitation) for all ``search_type``'s apart from Google Places, where the maximum is 20. Here's an example.
```python
from serpwow.google_search_results import GoogleSearchResults
import json

# request the first 100 results
serpwow = GoogleSearchResults("demo")
params = {
  "q" : "pizza",
  "start" : 0,
  "num": 100
}
result_page_1 = serpwow.get_json(params)

# request the next 100 results
params["start"] = 100
result_page_2 = serpwow.get_json(params)

# pretty-print the result
print "Page 1"
print json.dumps(result_page_1, indent=2, sort_keys=True)
print "Page 2"
print json.dumps(result_page_2, indent=2, sort_keys=True)
```

## Search example with all parameters
```python
from serpwow.google_search_results import GoogleSearchResults

# create the serpwow object, passing in our API key
serpwow = GoogleSearchResults("demo")

# set up a dict for the search parameters
params = {
  "q" : "pizza",
  "search_type" : "images",
  "gl" : "us",
  "hl" : "en",
  "location" : "New York,New York,United States",
  "google_domain" : "google.com",
  "time_period" : "custom",
  "sort_by" : "date",
  "time_period_min" : "02/01/2018",
  "time_period_max" : "02/08/2019",
  "device" : "mobile",
  "csv_fields" : "search.q,organic_results.position,organic_results.domain",
  "start" : "0",
  "num" : "100"
}

# retrieve the search results as CSV
result = serpwow.get_csv(params)

print result
```


## Locations API Example
The [Locations API](https://serpwow.com/docs/locations/overview) allows you to search for SerpWow supported Google search locations. You can supply the ``full_name`` returned by the Locations API as the ``location`` parameter in a Search API query (see [Searching with a location](https://github.com/serpwow/google-search-results-python#searching-with-a-location) example above) to retrieve search results geo-located to that location.
```python
from serpwow.google_search_results import GoogleSearchResults
import json

# create the serpwow object, passing in our API key
serpwow = GoogleSearchResults("demo")

# set up a dict for the location query parameters
params = {
  "q" : "mumbai"
}

# retrieve locations matching the query parameters as JSON
result = serpwow.get_locations(params)

# pretty-print the result
print json.dumps(result, indent=2, sort_keys=True)
```

## Account API Example
The [Account API](https://serpwow.com/docs/account/overview) allows you to check your current SerpWow usage and billing information. 
```python
from serpwow.google_search_results import GoogleSearchResults
import json

# create the serpwow object, passing in our API key
serpwow = GoogleSearchResults("demo")

# get our account info
result = serpwow.get_account()

# pretty-print the result
print json.dumps(result, indent=2, sort_keys=True)
```