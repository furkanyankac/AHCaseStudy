
#### a.URL of the Report
https://docs.google.com/spreadsheets/d/1jJT7Y1riKsSOvUidsLyMyuBgl6JZtWSd39lqtF_Q0jU/edit#gid=0

#### b.Used tech-stack ( library/framework etc.)

BeautifulSoap: Htmlden verileri ayıklayarak tagler de bulunan ürün detayları elde edilmiştir.
Pandas: Projede input olarak verilen excel dosyasına erişmek/verileri elde etmek ve data frame veri yapısı için pandas kütüphanesi kullanıldı.
Google xxx API: Google spreadsheets aracılığıyla rapor dosyasına erişim ve yazma işlemlerinde kullanıldı.
Request: Verileri çekmek için hedef URL'e HTTP GET sorgusu göndermek ve response handle etmek için kullanıldı.

#### c.A brief description of the challenges you face.

1- Google Spreadsheet erişimi sırasında okuma yapılabiliyordu, fakat yazma yetkisi olmadığından BAD_REQUEST response'u alınıyordu. Çözüm olarak Google Spreadsheet API için en yetkili scope seçildi.

2- Belirli bir katalogdaki ürünlerin verileri çekilirken ilgili her ürüne GET isteği atılarak verilere erişmeye çalıştım. Sonrasında hız problemi ve performans düşüklüğü nedeniyle katalogdaki tüm ürünlerin verilerini bir sorguda elde ettim.

#### d.What did you learn from this project?

Web sitesindeki verilere yazılım yoluyla erişmek, bu verilerden anlamlı bilgiler elde etmek ve bu bilgileri kullanarak başka bir ortama rapor sunmak gibi kazanımlar elde ettim.
Karşılaşmış olduğum hatalar sonucunda çözüm yolu ararken yeni bakış açıları kazandım.
Yeni library ve framework'ler keşfettim.

#### e.Answers of the additional questions

##### 1. If I’d have 10.000 urls that I should visit, then it takes hours to finish. What
can we make to fasten this process?

Multithreading kullanarak bu 10.000 URL'i threadlerin paralel olarak işlemesini sağlardım.

##### 2. What can we make or use to automate this process to run once a day?
Write your recommendations.

Kodu her gün belirtilen zamanda çalıştıracak bir script yazılabilir.

##### 3. Please briefly explain what an API is and how it works.

API, bir node'a veri göndermek veya veri almak için kullanılan bir arayüzdür. Bu arayüzün endpointlerinin node tarafından sağlanması gerekir. Bu endpointlere kendi
kuralları dahilinde atılan istekler aracılığıyla istenilen cevaplar node tarafından alınabilir.
