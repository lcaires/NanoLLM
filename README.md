# NanoLLM
An fun elementary introduction to language models, using a very small Python program


Here you may find a lightweight tutorial with examples on how language models Large Language Models such as ChatGPT work in a very very simplified setting, accessible to K12 kids taking the first steps in programming and computational thinking.

It is based on a tiny 80 lines Python program that, after training with some text content, uses the context of just the last two words to predict the next word to generate text on the fly.

Large Language Models such as ChatGPT and Gemini are all the rage these days ! Although LLMs are based on sophisticated machine learning techniques behind generative artificial intelligence tools like ChatGPT, at the very bottom they rely on statistical prediction of what is the most likely word (or token) to follow a prompt. NanoLM uses instead a very elementary statistical model called a Markov Chain. It is something really simple, as I explain the my slides (see below).
The slides and code are based on a lecture at my Programming Fundamentals course for freshers at Instituto Superior Técnico Informática no Técnico and inspired on a exercise in “The Practice of Programming” old textbook by Kernighan & Pike.
The generated text is of course fairly messy in general, but very often it also makes sense, and may even be fun 🙂 ! You may try to further develop NanoLM, it is just an embryo, that can be improved it in many ways.

The generated text only by chance appears in the original training set, as it is produced at random based on a coarse probability distribution “learned” from the training data.
The Python code also types the text out like NanoLM if is “thinking” at the keyboard 🙂

