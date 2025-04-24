# Audio Transcript Analysis with Power BI

This repository provides a complete workflow for analyzing audio transcript data using Power BI and external APIs for sentiment and key phrase extraction. The objective is to process `.wav` audio files located in the `audio/` folder, convert them into text, combine the transcripts, and load the final dataset into Power BI for advanced text analytics.

To begin, place your `.wav` audio files in the `audio/` directory. Use the `wav_to_txt.py` script to extract transcripts from each audio file. This will generate individual `.txt` files for each audio file, saved within the `audio/` folder. Once all transcripts are generated, execute the `concat_txt_files.py` script to combine them into a single file called `master.txt`. This master file will serve as the input for Power BI.

In Power BI Desktop, load the `master.txt` file using the “Get Data” > “Text/CSV” option. The file will appear as a single-column table, similar to survey data. From the Power Query Editor, you can then begin enriching the data using external API services. For sentiment analysis, refer to the implementation guide in `sentiment_label.md`, which outlines how to create a new column that invokes a sentiment analysis API using Azure Congitive Services. Similarly, to extract key phrases, follow the instructions in `key_phrases_function.md`. This involves setting up another column that sends the text content to a key phrase extraction API for further analysis.

By the end of this process, Power BI will display a dataset containing original transcript text, sentiment labels, and key phrases. These can be visualized using charts, tables, and word cloud to uncover meaningful patterns, such as sentiment trends over time or recurring phrases across sessions. 

This setup is ideal for analyzing customer calls, interviews, or any audio-based feedback at scale. Make sure to monitor API usage limits and authentication requirements, and optimize for performance when processing large volumes of data.
