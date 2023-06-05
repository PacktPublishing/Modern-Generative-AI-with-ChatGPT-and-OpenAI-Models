
# Modern Generative AI with ChatGPT and OpenAI Models	

<a href="https://www.packtpub.com/product/modern-generative-ai-with-chatgpt-and-openai-models/9781805123330"><img src="https://m.media-amazon.com/images/I/41Mf1KzmKOL._SX404_BO1,204,203,200_.jpg" alt="Modern Generative AI with ChatGPT and OpenAI Models" height="256px" align="right"></a>

This is the code repository for [Modern Generative AI with ChatGPT and OpenAI Models](https://www.packtpub.com/product/modern-generative-ai-with-chatgpt-and-openai-models/9781805123330), published by Packt.

**Leverage the capabilities of OpenAI's LLM for productivity and innovation with GPT3 and GPT4**

## What is this book about?

Generative AI models and AI language models are becoming increasingly popular due to their unparalleled capabilities. This book will provide you with insights into the inner workings of the LLMs and guide you through creating your own language models. You’ll start with an introduction to the field of generative AI, helping you understand how these models are trained to generate new data.

Next, you’ll explore use cases where ChatGPT can boost productivity and enhance creativity. You’ll learn how to get the best from your ChatGPT interactions by improving your prompt design and leveraging zero, one, and few-shots learning capabilities. The use cases are divided into clusters of marketers, researchers, and developers, which will help you apply what you learn in this book to your own challenges faster.

You’ll also discover enterprise-level scenarios that leverage OpenAI models’ APIs available on Azure infrastructure; both generative models like GPT-3 and embedding models like Ada. For each scenario, you’ll find an end-to-end implementation with Python, using Streamlit as the frontend and the LangChain SDK to facilitate models' integration into your applications.

By the end of this book, you’ll be well equipped to use the generative AI field and start using ChatGPT and OpenAI models’ APIs in your own projects.

This book covers the following exciting features: 
* Understand generative AI concepts from basic to intermediate level
* Focus on the GPT architecture for generative AI models
* Maximize ChatGPT’s value with an effective prompt design
* Explore applications and use cases of ChatGPT
* Use OpenAI models and features via API calls
* Build and deploy generative AI systems with Python
* Leverage Azure infrastructure for enterprise-level use cases
* Ensure responsible AI and ethics in generative AI systems 

If you feel this book is for you, get your [copy](https://www.amazon.com/Modern-Generative-ChatGPT-OpenAI-Models/dp/1805123335/ref=sr_1_1?keywords=Modern+Generative+AI+with+ChatGPT+and+OpenAI+Models&s=books&sr=1-1) today!


## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
query = st.text_area("Ask a question about the document")
if query:
      docs = faiss_index.similarity_search(query, k=1)
      button = st.button("Submit")
      if button:
          st.write(get_answer(faiss_index, query))
```

**Following is what you need for this book:**
This book is for individuals interested in boosting their daily productivity; businesspersons looking to dive deeper into real-world applications to empower their organizations; data scientists and developers trying to identify ways to boost ML models and code; marketers and researchers seeking to leverage use cases in their domain – all by using Chat GPT and OpenAI Models.

A basic understanding of Python is required; however, the book provides theoretical descriptions alongside sections with code so that the reader can learn the concrete use case application without running the scripts.

With the following software and hardware list you can run all code files present in the book (Chapter 1-11).

### Software and Hardware List

| Chapter  | Software required                                                                    | OS required                        |
| -------- | -------------------------------------------------------------------------------------| -----------------------------------|
|  	1-11	   |  Python 3.7.1 or higher   | Any OS | 		
|  	1-11	   |  Streamlit  | Any OS | 		
|  	1-11	   | LangChain | Any OS | 		
|  	1-11	   | OpenAI model APIs | OpenAI account | 		
|  	1-11	   | Azure OpenAI Service | Azure Account Subscription enabled for Azure OpenAI | 		



### Related products <Other books you may enjoy>
* Exploring GPT-3  [[Packt]](https://www.packtpub.com/product/exploring-gpt-3/9781800563193) [[Amazon]](https://www.amazon.com/Exploring-GPT-3-unofficial-general-purpose-processing/dp/1800563191/ref=sr_1_1?keywords=Exploring+GPT-3&s=books&sr=1-1)
  
* GPT-3  [[Packt]](https://www.packtpub.com/product/gpt-3/9781805125228) [[Amazon]](https://www.amazon.com/GPT-3-Ultimate-Building-Products-OpenAI/dp/1805125222/ref=sr_1_1?keywords=GPT-3&s=books&sr=1-1)
  
## Get to Know the Author
**Valentina Alto** graduated in 2021 in Data Science. Since 2020 she has been working in Microsoft as Azure Solution Specialist and, since 2022, she focused on Data&AI workloads within the Manufacturing and Pharmaceutical industry. She has been working on customers’ projects closely with system integrators to deploy cloud architecture with a focus on datalake house and DWH, data integration and engineering, IoT and real-time analytics, Azure Machine Learning, Azure cognitive services (including Azure OpenAI Service), and PowerBI for dashboarding. She holds a BSc in Finance and an MSc degree in Data Science from Bocconi University, Milan, Italy. Since her academic journey she has been writing Tech articles about Statistics, Machine Learning, Deep Learning and AI on various publications. She has also written a book about the fundamentals of Machine Learning with Python.
