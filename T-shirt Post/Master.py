# -*- coding: utf8 -*-
from selenium import webdriver

print ('-------------------------------')
print ('T-shirt Post Teemolly')
print ('Power by Vip.phamquangthinh')
print ('Copyright@2017')
print ('-------------------------------')
url = str(input('Hãy nhập url Platform: \n'))

browser = webdriver.PhantomJS()
browser.get(url)
source = browser.page_source
browser.quit()

clrender = []
namecl=['title="White"','title="Sand"','title="Light Pink"','title="Ash Grey"','title="Light Blue"','title="Azalea"','title="Sport Grey"','title="Daisy"','title="Lime"','title="Carolina Blue"','title="Heliconia"','title="Gold"','title="Orange"','title="Tennessee Orange"','title="Red"','title="Sapphire"','title="Electric Green"','title="Purple"','title="Royal"','title="Irish Green"','title="Dark Heather"','title="Maroon"','title="Navy"','title="Forest Green"','title="Black"','title="Classic Pink"','title="Safety Green"','title="Cherry Red"','title="Cardinal Red"','title="Charcoal"','title="Military Green"','title="Dark Chocolate"']
hexcl =['#fcfcfc','#ffe9ba','#ffb2c4','#d6d7d9','#8cb4e8','#ff6dda','#999d9e','#f3fe2b','#79ff20','#5194bf','#8f1d59','#ffb502','#ff4902','#ff8400','#f30000','#0061c5','#00ac31','#490c95','#01298e','#008c35','#444545','#3b0018','#031037','#022d1b','#0b0b0b','#ffa8bf','#daff11','#b60000','#800000','#3b3b3b','#31432a','#140900']

for i in source.split():
    a = 0
    for j in namecl:
        if i == j :
            clrender.append(hexcl[a])
        a += 1

renderhex = ''
for i in clrender:
    css = '<div class="tn4" style="background-color: %s "></div>' % (i)
    renderhex = renderhex + css

cover =str(input('Nhập url cover cho post này : \n'))
tshirt = str(input('Hãy nhập tên của chiếc áo này ? \n'))
money = str(input('Bao nhiêu Dola Trump một cái ? \n'))
front = str(input('Mặt trước của áo trông ntn ? \n'))
back = str(input ('Còn mặt sau có cái gì không ? \n'))
detail = str(input ('Hãy nhập mô tả design ? \n'))
pixel = str(input ('Track with facebook pixel ? \n'))


html = """<div class="gia">""" + money + """</div>
<!--more-->
<div class="tm13">
<div class="container">
<div class="row">
<div class="col-12">
<div class="tn1">
<ul>
 	<li><a href="http://teemolly.com/?page_id=69">Fishing</a></li>
 	<li><a href="http://teemolly.com/?page_id=107">Jobs</a></li>
 	<li><a href="http://teemolly.com/?page_id=113">Gym </a></li>
 	<li><a href="http://teemolly.com/?page_id=115">Family</a></li>
 	<li><a href="http://teemolly.com/?page_id=119">Yoga</a></li>
 	<li><a href="http://teemolly.com/?page_id=123">Pets</a></li>
 	<li><a href="http://teemolly.com/?page_id=127">Sports</a></li>
 	<li><a href="http://teemolly.com/?page_id=129">MISC</a></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="tm35"> <img src=\"""" + cover + """\" alt="">
    </div>

    <div class="container">
        <div class="row">
            <div class="col-12">
                <div class="tm14">
                    <ul>
                        <li>Production</li>
                        <li>Maket</li>
                    </ul>
                </div>

            </div>
        </div>
        <div class="row">
            <div class="col-md-5 col-12">
                <div class="tm16">
                    <div class="tn1"><img src=\"""" + front + """\" alt=\"""" + detail + """\"></div>
                    <div class="tn2 tsde"><img src=\"""" + back + """\" alt=\"""" + detail + """\"></div>
                    <div class="tn3">
                        <div class="tn4"><a href="#."><img src=\"""" + front + """\" alt=\"""" + detail + """\"></a></div>
                        <div class="tn5"><a href="#."><img src=\"""" + back + """ alt=\"""" + detail + """\"></a></div>
                    </div>
                </div>
                <div class="tm36">
                    <ul>
                        <li class="tn1 tn3"><a href="#.">Front</a></li>
                        <li>|</li>
                        <li class="tn2"><a href="#.">Back</a></li>
                    </ul>
                </div>
            </div>
            <div class="col-md-1 col-0"></div>
            <div class="col-md-5 col-12">
                <div class="tm15">""" + tshirt + """</div>
                <div class="tm17">
                    <div class="tn1">
                        <p>Price :""" + money + """</p>
                    </div>
                    <div class="tn2">
                        <ul>
                            <li>Style available:</li>
                            <li>Unisex Cotton Tee, Gildan Hoodie, Men's Tank Top, Women's Tank Top , Unisex Long Sleeve ..</li>
                        </ul>
                        <ul>
                            <li>Color available:</li>
                            <li>
                                <div class="tn3">""" + renderhex + """</div>
                            </li>
                        </ul>
                        <ul>
                            <li>size available:</li>
                            <li>S, M, L, XL, 2XL, 3XL, 4XL, 5XL</li>
                        </ul>
                        <ul>
                            <li>100% cotton And ...</li>
                        </ul>
                    </div>
                </div>
                <div class="tm18">
                    <div class="tn2">
                        <a href=\"""" + url + """\" target="_blank">Learn more</a>
                    </div>
                </div>
                <div class="tm19">
                    <div class="tn1">Share this design!</div>
                    <div class="tn2">
                        <a href="javascript:fbshareCurrentPage()" target="_blank" alt="Share on Facebook">Facebook</a>
                    </div>
                    <div class="tn2 tn3">
                        <a href="" target="_blank">Twitter</a>
                    </div>
                </div>
            </div>

        </div>

    </div>
<script>
fbq('track', 'ViewContent', {
            content_type: 'Product',
            content_name: \'""" + pixel + """\'
        });
</script>
<div class="tm20"></div>"""

#post = open('output.html','w')
#post.write(html)

with open('output.html', 'w') as post:
    post.write(html)

print ('All Done !')
print ('-------------------------------')
pause = input()
