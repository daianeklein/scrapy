import scrapy
from scrapy import Spider
from scrapy.http import Request


class ClasscentralSpider(scrapy.Spider):
    name = "classcentral"
    allowed_domains = ["classcentral.com"]
    start_urls = ["https://classcentral.com/subjects"]

    def __init__(self, subject = None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            #subject_url = response.xpath("//a[contains(span[@class='l-subjects-page__subject-label'], 'Arduino')]/@href").extract_first()
            subject_url = response.xpath("//a[contains(span[@class='l-subjects-page__subject-label'], '" + self.subject + "')]/@href").extract_first() 
            absolute_subject_url = response.urljoin(subject_url)

            yield Request(absolute_subject_url,
                        callback = self.parse_subject)
        else:
            self.log('Scraping all subjects')
            subjects = response.xpath('//a[@class="color-charcoal l-subjects-page__subject-link"]/@href').extract()
            for subject in subjects:
                absolute_subject_url = response.urljoin(subject)

                yield Request(absolute_subject_url,
                    callback = self.parse_subject)

    def parse_subject(self, response):
        subject_name = response.xpath('//h1/text()').extract_first()

        courses = response.xpath('//*[@class="catalog-grid__results"]')
        courses_name = courses.xpath('.//h2/text()').extract()
        courses_url = courses.xpath('//*[@class="color-charcoal course-name"]/@href').extract()
        absolute_course_url = [response.urljoin(url) for url in courses_url]

        for course_name, course_url in zip(courses_name, absolute_course_url):
            yield {'subject_name': subject_name,
                'course_name': course_name,
                'course_url': course_url}
                

        
