# PPN : Propagandist Pseudo-News dataset

In parallel with the recent Ukraine special operation, an additional information warfare has developped on the Internet. To this end, several websites were created with the main intent to polarize and destabilize occidental countries.

These websites are however monitored and identified by governemental organizations such as VIGINUM in France. Even when they are quickly identified by authorities, they have the time to damage the information landscape. The identification of these websites is very important as they hide their intentions, while relying on a pro-Russia narrative through several news topics.

Such content is interesting to analyze, taking several forms (from opinion essays to strict propaganda), and permitting to study and identify anti-Occident narratives linked to current conflicts in the world.

With this dataset, we propose to compile articles from 5 different sources identified as Russian-controlled with democracy-threatening or polarizing content by the VIGINUM organisation. They are all part of the same misinformation campaign, but target different users and have different purposes. The websites are the following and were collected at different dates:

 - Reliable Recent News (rrn[.]media - collected the 13/09/2023) : is a Russian propaganda website publishing articles in 9 different languages (Arabic, Chinese, English, French, German, Italian, Russian, Spanish and Ukrainian). The coverage of all languages varies over time and the topics evolve with the geopolitical context. It contains 12 427 articles, all with a pro-Russia or anti-Occident component.
  - Tribunal Ukraine (tribunalukraine[.]info - collected the 09/11/2023) : was created to accuse Ukraine of commiting war crimes and benefiting financially from the open conflict. The articles are all in 5 languages (English, French, German, Russian and Spanish). It is composed of 995 articles for each language.
  - War on Fakes (waronfakes[.]com - collected the 09/11/2023) : is a fake multilingual fact-checking platform used to deny allegations of Russian war crimes. It is the _defense_ counterpart of Tribunal Ukraine, which aims at damaging the Ukrainian army reputation. It doesn't contain real newspaper articles, but a quick summary of an allegation, and why it should be considered a _Fake News_. There are 344 facts in 6 languages (Arabic, Chinese, English, French, German and Spanish).
  - Notre Pays (notrepays[.]today - collected the 09/11/2023) : is a French-writing website created one year after the Ukraine invasion publishing polarizing news with the aim of damaging trust in Occidental institutions, with a total of 503 French articles
  - La Virgule (lavirgule[.]news - collected the 09/11/2023) : is a website created at the same time as notrepays and has the same objective. It contains 480 polarizing articles.

Articles are collected using News-please [@Hambourg2017] and are given with the initially collected metadata in the `file.html.json` files, after the removal of the `localpath` field, for privacy reasons. The kept fields are the following:

- `authors` : The authors of the article, often the publishing website
- `date_download` : The initial download date of the article, to track possible changes between versions of the articles
- `date_modify` : If we have scrapped several times the same article, it would be the time of last download
- `date_publish` : The data for which the article first appeared on the internet. This field may be inacurrate in some cases
- `description` : A summary of the article to be seen on preview for RSS feeds
- `filename` : The name of the corresponding html file, provided in the same subfolder as the metadata file
- `image_url` : The URL of the first related picture in the article. This could be used to make the dataset multimodal, with the illustration choices done to make readers react
- `language` : The estimated language of the article estimated by the scrapper. It corresponds well to the reality for multilingual websites, but is mostly wrong from the articles from the French-reading websites, which are mostly labeled `en`
- `title` : The title of the article
- `title_page` : The title to be displayed in the tab name of the web browser
- `title_rss` : The title to be used by RSS scrappers
- `source_domain` : The origin website domain
- `maintext` : The main content of the web page. Works well for most languages, but the module has encountered difficulties for articles written in Chinese, for which this field may be empty
- `url` : The url of the article


# Statistics

| Language | Number of documents
|---|--:
| Arabic |   1 079
| Chinese |   794
|English |   3 219
| French |   4 141
| German |   3 341
|Italian |   1 796
|Russian |   1 435
| Spanish |   2 485
| Ukrainian |   439
| **Total** |   18 729

# Cite us

```

@inproceedings{faye-etal-2024-exposing,
    title = "Exposing propaganda: an analysis of stylistic cues comparing human annotations and machine classification",
    author = "Faye, G{\'e}raud  and
      Icard, Benjamin  and
      Casanova, Morgane  and
      Chanson, Julien  and
      Maine, Fran{\c{c}}ois  and
      Bancilhon, Fran{\c{c}}ois  and
      Gadek, Guillaume  and
      Gravier, Guillaume  and
      {\'E}gr{\'e}, Paul",
    editor = "Pyatkin, Valentina  and
      Fried, Daniel  and
      Stengel-Eskin, Elias  and
      Stengel-Eskin, Elias  and
      Liu, Alisa  and
      Pezzelle, Sandro",
    booktitle = "Proceedings of the Third Workshop on Understanding Implicit and Underspecified Language",
    month = mar,
    year = "2024",
    address = "Malta",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.unimplicit-1.6",
    pages = "62--72",
}

```


# License

This dataset and associated code in the repository are distributed under the CC BY-NC 4.0 license.

# Used tools

[@Hamborg2017] Hamborg, Felix and Meuschke, Norman and Breitinger, Corinna and Gipp, Bela. \news-please: A Generic News Crawler and Extractor\, 2017, Proceedings of the 15th International Symposium of Information Science
