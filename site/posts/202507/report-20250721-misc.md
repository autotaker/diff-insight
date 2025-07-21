---
date: '2025-07-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1217e71...MicrosoftDocs:043ab30
summary: このコードの変更は、主にマイナーな更新を含み、各記事の表現の明確化やリンクの修正が行われました。これにより、ユーザーの学習体験が向上し、情報が一貫性を保つことができるようになっています。特に、言語サービスに関する内部リンクの修正、カスタム質問応答に関するベストプラクティスの明確化、新機能に関する情報の追加が行われています。重大な互換性の問題はなく、全体的に文書の品質を高め、読みやすさと情報の正確性を向上させることを目的としています。これにより、ユーザーはより効果的な言語処理やボット開発が可能になり、ビジネスでの成果を最大化できるようになっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1217e71...MicrosoftDocs:043ab30){target="_blank"}

# Highlights
このコードの変更は主にマイナーな更新を含み、各記事に対して表現の明確化やリンクの修正が行われました。これにより、ユーザーの学習体験が向上し、情報が一貫性を保つことができるようになっています。

## New features
- 言語サービスの概要に関する内部リンクの修正が行われ、正確な相対パスが指定されました。
- 「カスタム質問応答」に関するベストプラクティスの明確化が行われ、質問と回答のペアに関する表現が改善されました。
- Azure AI Languageの新機能に新しいバージョンのトレーニング設定やエージェントテンプレート、PII検出の強化に関する情報が追加されました。

## Breaking changes
- 特に重大な変更や互換性の問題は示されていません。

## Other updates
- 各記事内で、表現をより明確にし、情報をより効果的に伝えることを目的とした修正が施されています。
- 「Power Virtual Agents」に関連したチュートリアルのテキスト構成が改善され、リンクの表現が明確化されました。

# Insights
これらの更新は、Azureの言語サービスに関するドキュメント全体の品質を向上させ、読みやすさと情報の正確性を高めることを目的としています。具体的には、リンクの修正により、読者は正しいリソースに迅速にアクセスできるようになります。さらに、「カスタム質問応答」に関するベストプラクティスの記事では、質問と回答のペアやタグの付け方について具体的なアプローチが示され、実際の導入時に役立つ情報が強化されています。

また、「Text Analytics for Health」のコンテナ使用方法に関連して、特にDockerのコマンドを実行する際の細かい注意事項やRAIに関する情報が追記されています。これにより、ユーザーがシステムを構築する際の潜在的な問題を回避しやすくなりました。

さらに、「Azure AI Language」の新機能に関するドキュメントの更新は、最新の機能を活用するための知識を提供し、技術の進展に伴う新機能を効果的に取り入れることをサポートします。最新のトレーニング設定やエージェントテンプレート、新しいルーティング戦略に関する情報は、Azureクラウドインフラストラクチャを利用する企業にとって重要なアップデートであり、業界の最前線に立つための鍵となります。

これにより、読者はAzure AIサービスを活用して、より効果的な言語処理やボット開発が可能となり、ビジネスでの成果を最大化できるようになります。全体として、過去の情報を刷新しつつ、最新技術に関する豊富な情報を提供することで、ユーザーの理解を深め、製品の利用価値を高めています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-f138b4) | minor update | 言語サービスの概要におけるリンクの修正 | modified | 3 | 3 | 6 | 
| [best-practices.md](#item-f97daf) | minor update | カスタム質問応答のベストプラクティスの更新 | modified | 35 | 36 | 71 | 
| [overview.md](#item-631b23) | minor update | カスタム質問応答の概要の更新 | modified | 9 | 9 | 18 | 
| [power-virtual-agents.md](#item-aec51d) | minor update | Power Virtual Agentsに関するチュートリアルの更新 | modified | 1 | 1 | 2 | 
| [use-containers.md](#item-9dddb4) | minor update | コンテナ使用方法に関するドキュメントの更新 | modified | 2 | 1 | 3 | 
| [whats-new.md](#item-69b272) | minor update | Azure AI Languageの新機能に関するドキュメントの更新 | modified | 9 | 11 | 20 | 


# Modified Contents
## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -248,6 +248,6 @@ Use Language service containers to deploy API features on-premises. These Docker
 
 An AI system includes not only the technology, but also the people who use it, the people affected by it, and the deployment environment. Read the following articles to learn about responsible AI use and deployment in your systems:
 
-* [Transparency note for the Language service](/azure/ai-foundry/responsible-ai/language-service/transparency-note)
-* [Integration and responsible use](/azure/ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use)
-* [Data, privacy, and security](/azure/ai-foundry/responsible-ai/language-service/data-privacy)
+* [Transparency note for the Language service](../../ai-foundry/responsible-ai/language-service/transparency-note.md)
+* [Integration and responsible use](../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md)
+* [Data, privacy, and security](../../ai-foundry/responsible-ai/language-service/data-privacy.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サービスの概要におけるリンクの修正"
}
```

### Explanation
今回の変更は、言語サービスに関する概要記事において、内部リンクのパスを修正するものであり、マイナーな更新として位置付けられます。具体的には、リンクの形式が変更され、相対パスが正確に指定されました。これにより、マークダウン内のリンクが正しく機能し、読者が適切なリソースにアクセスできるようになります。該当するリンクは、「透明性に関する注意事項」、「統合と責任ある使用」、「データ、プライバシー、セキュリティ」に関する情報を提供しています。安定した情報提供を保つための重要な修正です。

## articles/ai-services/language-service/question-answering/concepts/best-practices.md{#item-f97daf}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ ms.service: azure-ai-language
 author: laujan
 ms.author: lajanuar
 ms.topic: conceptual
-ms.date: 06/21/2025
+ms.date: 07/17/2025
 ms.custom: language-service-question-answering
 ---
 
@@ -19,15 +19,15 @@ Custom question answering is continually improving the algorithms that extract q
 
 ## Creating good questions and answers
 
-We’ve used the following list of question and answer pairs as representation of a project to highlight best practices when authoring projects for custom question answering.
+We use the following list of question and answer pairs to represent a project. This approach helps highlight best practices when creating projects for custom question answering.
 
 | Question | Answer |
 |----------|----------|
 | I want to buy a car |There are three options to buy a car.|
 | I want to purchase software license |Software license can be purchased online at no cost.|
 | What is the price of Microsoft stock? | $200. |
 | How to buy Microsoft Services | Microsoft services can be bought online.|
-| Want to sell car | Please send car pics and document.|
+| Want to sell car | Send car pics and document.|
 | How to get access to identification card? | Apply via company portal to get identification card.|
 
 ### When should you add alternate questions to question and answer pairs?
@@ -39,61 +39,61 @@ Custom question answering employs a transformer-based ranker that takes care of
 
 The service can return the expected response for semantically similar queries such as:
 
-“How much is Microsoft stock worth?
-“How much is Microsoft share value?”
-“How much does a Microsoft share cost?”
-“What is the market value of a Microsoft stock?”
-“What is the market value of a Microsoft share?”
+"How much is Microsoft stock worth?
+"How much is Microsoft share value?"
+"How much does a Microsoft share cost?"
+"What is the market value of a Microsoft stock?"
+"What is the market value of a Microsoft share?"
 
-However, it’s important to understand that the confidence score with which the system returns the correct response will vary based on the input query and how different it is from the original question answer pair.  
+The confidence score that the system assigns to its response can vary. This variation depends on the input query and how much it differs from the original question-answer pair. 
 
-There are certain scenarios that require the customer to add an alternate question. When it’s already verified that for a particular query the correct answer isn’t returned despite being present in the project, we advise adding that query as an alternate question to the intended question answer pair.
+There are certain scenarios that require the customer to add an alternate question. If you already verified that a specific query doesn't return the correct answer, even though the answer exists in the project, we recommend taking further action. Add that query as an alternate question to the intended question and answer pair. This step can help ensure users receive the correct response in the future.
 
 ### How many alternate questions per question answer pair is optimal?
 
-Users can add as many alternate questions as they want, but only first 5 will be considered for core ranking. However, the rest will be useful for exact match scenarios. It is also recommended to keep the different intent/distinct alternate questions at the top for better relevance and score.
+Users can add as many alternate questions as they want, but only first 5 are considered for core ranking. However, the rest is useful for exact match scenarios. We also recommended keeping the different intent/distinct alternate questions at the top for better relevance and score.
 
 Semantic understanding in custom question answering should be able to take care of similar alternate questions.
 
-The return on investment will start diminishing once you exceed 10 questions. Even if you’re adding more than 10 alternate questions, try to make the initial 10 questions as semantically dissimilar as possible so that all kinds of intents for the answer are captured by these 10 questions.  For the project at the beginning of this section, in question answer pair #1, adding alternate questions such as “How can I buy a car”, “I wanna buy a car” aren’t required. Whereas adding alternate questions such as “How to purchase a car”, “What are the options of buying a vehicle” can be useful.
+The return on investment decreases after you exceed 10 questions. Even if you include more than 10 alternate questions, focus on making the first 10 questions as semantically different as possible. By doing so, you ensure that these 10 questions capture all possible intents for the answer. For the project at the beginning of this section, in question answer pair #1, adding alternate questions such as *How can I buy a car* or *I want to buy a car* aren't required. Whereas adding alternate questions such as *How to purchase a car*, *What are the options of buying a vehicle* can be useful.
 
 ### When to add synonyms to a project?
 
 Custom question answering provides the flexibility to use synonyms at the project level, unlike QnA Maker where synonyms are shared across projects for the entire service.
 
-For better relevance, you need to provide a list of acronyms that the end user intends to use interchangeably. The following is a list of acceptable acronyms:
+For better relevance, you need to provide a list of acronyms that the end user intends to use interchangeably. The following list details acceptable acronyms:
 
 * `MSFT` – Microsoft
 * `ID` – Identification
 * `ETA` – Estimated time of Arrival
 
-Other than acronyms, if you think your words are similar in context of a particular domain and generic language models won’t consider them similar, it’s better to add them as synonyms. For instance, if an auto company producing a car model X receives queries such as “my car’s audio isn’t working” and the project has questions on “fixing audio for car X”, then we need to add ‘X’ and ‘car’ as synonyms.
+Other than acronyms, if you think your words are similar in context of a particular domain and generic language models doesn't consider them similar, it's better to add them as synonyms. For instance, an auto company producing a car model X receives queries such as *my car's audio isn't working* and the project has questions on *fixing audio for car X*. Then, we need to add 'X' and 'car' as synonyms.
 
-The transformer-based model already takes care of most of the common synonym cases, for example: `Purchase – Buy`, `Sell - Auction`, `Price – Value`. For another example, consider the following question answer pair: Q: “What is the price of Microsoft Stock?” A: “$200”.  
+The transformer-based model already takes care of most of the common synonym cases, for example: `Purchase – Buy`, `Sell - Auction`, `Price – Value`. For another example, consider the following question answer pair: Q: *What is the price of Microsoft Stock?* A: *$200*. 
 
-If we receive user queries like “Microsoft stock value”,” Microsoft share value”, “Microsoft stock worth”, “Microsoft share worth”, “stock value”, etc., you should be able to get the correct answer even though these queries have words like "share", "value", and "worth", which aren’t originally present in the project.
+If users ask questions like *Microsoft stock value*, *Microsoft share value*, *Microsoft stock worth*, *Microsoft share worth*, or just *stock value*, you should still be able to provide the correct answer. It's important to maintain this clarity, even though terms such as *share*, *value*, and *worth* aren't originally included in the project.
 
-Special characters are not allowed in synonyms.
+Special characters aren't allowed in synonyms.
 
 ### How are lowercase/uppercase characters treated?
 
-Question answering takes casing into account but it's intelligent enough to understand when it’s to be ignored. You shouldn’t be seeing any perceivable difference due to wrong casing.
+Question answering takes casing into account but it's intelligent enough to understand when it's to be ignored. You shouldn't be seeing any perceivable difference due to wrong casing.
 
 ### How are question answer pairs prioritized for multi-turn questions?
 
-When a project has hierarchical relationships (either added manually or via extraction) and the previous response was an answer related to other question answer pairs, for the next query we give slight preference to all the children question answer pairs, sibling question answer pairs, and grandchildren question answer pairs in that order. Along with any query, the [custom question answering REST API](/rest/api/questionanswering/question-answering/get-answers) expects a `context` object with the property `previousQnAId`, which denotes the last top answer. Based on this previous `QnAID`, all the related `QnAs` are boosted.
+When a project includes hierarchical relationships—whether they're added manually or through extraction—special handling is applied. If the previous response addressed a question that belongs to a related set of question-answer pairs, it affects how we handle subsequent queries. For the next query, we give slight preference to all child question-answer pairs first. Preference is then given to sibling question-answer pairs, followed by grandchild question-answer pairs, in that order. Along with any query, the [custom question answering REST API](/rest/api/questionanswering/question-answering/get-answers) expects a `context` object with the property `previousQnAId`, which denotes the last top answer. Based on this previous `QnAID`, all the related `QnAs` are boosted.
 
 ### How are accents treated?
 
-Accents are supported for all major European languages. If the query has an incorrect accent, the confidence score might be slightly different, but the service still returns the relevant answer and takes care of minor errors by leveraging fuzzy search.
+Accents are supported for all major European languages. If the query has an incorrect accent, the confidence score might be slightly different, but the service still returns the relevant answer and takes care of minor errors by using fuzzy search.
 
 ### How is punctuation in a user query treated?
 
-Punctuation is ignored in a user query before sending it to the ranking stack. Ideally it shouldn’t impact the relevance scores. Punctuation that is ignored is as follows:  `,?:;\"'(){}[]-+。./!*؟`
+Punctuation is ignored in a user query before sending it to the ranking stack. Ideally it shouldn't impact the relevance scores. Punctuation that is ignored is as follows:  `,?:;\"'(){}[]-+。./!*؟`
 
 ## Chit-Chat
 
-Add chit-chat to your bot, to make your bot more conversational and engaging, with low effort. You can easily add chit-chat data sources from pre-defined personalities when creating your project, and change them at any time. Learn how to [add chit-chat to your KB](../How-To/chit-chat.md).
+Add chit-chat to your bot, to make your bot more conversational and engaging, with low effort. You can easily add chit-chat data sources from predefined personalities when creating your project, and change them at any time. Learn how to [add chit-chat to your KB](../How-To/chit-chat.md).
 
 Chit-chat is supported in [many languages](../how-to/chit-chat.md#language-support).
 
@@ -109,19 +109,18 @@ Chit-chat is supported for several predefined personalities:
 |Caring |[qna_chitchat_caring.tsv](https://qnamakerstore.blob.core.windows.net/qnamakerdata/editorial/qna_chitchat_caring.tsv) |
 |Enthusiastic |[qna_chitchat_enthusiastic.tsv](https://qnamakerstore.blob.core.windows.net/qnamakerdata/editorial/qna_chitchat_enthusiastic.tsv) |
 
-The responses range from formal to informal and irreverent. You should select the personality that is closest aligned with the tone you want for your bot. You can view the [datasets](https://github.com/Microsoft/BotBuilder-PersonalityChat/tree/master/CSharp/Datasets), and choose one that serves as a base for your bot, and then customize the responses.
+The responses range from formal to informal and irreverent. You should select the personality that is closest aligned with the tone you want for your bot. You can view the datasets, and choose one that serves as a base for your bot, and then customize the responses.
 
 ### Edit bot-specific questions
 
-There are some bot-specific questions that are part of the chit-chat data set, and have been filled in with generic answers. Change these answers to best reflect your bot details.
+There are some bot-specific questions that are part of the chit-chat data set, and are completed with generic answers. Change these answers to best reflect your bot details.
 
 We recommend making the following chit-chat question answer pairs more specific:
 
 * Who are you?
 * What can you do?
-* How old are you?
+* What is your age?
 * Who created you?
-* Hello
 
 ### Adding custom chit-chat with a metadata tag
 
@@ -131,15 +130,15 @@ If you add your own chit-chat question answer pairs, make sure to add metadata s
 
 The custom question answering REST API uses both questions and the answer to search for best answers to a user's query.
 
-### Searching questions only when answer isn’t relevant
+### Searching questions only when answer isn't relevant
 
 Use the [`RankerType=QuestionOnly`](#choosing-ranker-type) if you don't want to search answers.
 
-An example of this is when the project is a catalog of acronyms as questions with their full form as the answer. The value of the answer won’t help to search for the appropriate answer.
+An example is when the project is a catalog of acronyms as questions with their full form as the answer. The value of the answer doesn't help to search for the appropriate answer.
 
 ## Ranking/Scoring
 
-Make sure you’re making the best use of the supported ranking features. Doing so will improve the likelihood that a given user query is answered with an appropriate response.
+Make sure you're making the best use of the supported ranking features. Doing so improves the likelihood that a given user query is answered with an appropriate response.
 
 ### Choosing a threshold
 
@@ -151,7 +150,7 @@ By default, custom question answering searches through questions and answers. If
 
 ### Add alternate questions
 
-Alternate questions to improve the likelihood of a match with a user query. Alternate questions are useful when there are multiple ways in which the same question may be asked. This can include changes in the sentence structure and word-style.
+Alternate questions to improve the likelihood of a match with a user query. Alternate questions are useful when there are multiple ways in which the same question may be asked. The alternate questions can include changes in the sentence structure and word-style.
 
 |Original query|Alternate queries|Change|
 |--|--|--|
@@ -160,15 +159,15 @@ Alternate questions to improve the likelihood of a match with a user query. Alte
 
 ### Use metadata tags to filter questions and answers
 
-Metadata adds the ability for a client application to know it shouldn’t take all answers but instead to narrow down the results of a user query based on metadata tags. The project answer can differ based on the metadata tag, even if the query is the same. For example, *"where is parking located"* can have a different answer if the location of the restaurant branch is different - that is, the metadata is *Location: Seattle* versus *Location: Redmond*.
+Metadata adds the ability for a client application to know it shouldn't take all answers but instead to narrow down the results of a user query based on metadata tags. The project answer can differ based on the metadata tag, even if the query is the same. For example, the answer to *where is parking located* can vary depending on the branch location. If the metadata is *Location: Seattle*, the answer is different than if the metadata is *Location: Redmond*.
 
 ### Use synonyms
 
-While there’s some support for synonyms in the English language, use case-insensitive [word alterations](../tutorials/adding-synonyms.md) to add synonyms to keywords that take different forms.
+While there's some support for synonyms in the English language, use case-insensitive [word alterations](../tutorials/adding-synonyms.md) to add synonyms to keywords that take different forms.
 
 |Original word|Synonyms|
 |--|--|
-|buy|purchase<br>net-banking<br>net banking|
+|buy|purchase<br>Net-banking<br>Net banking|
 
 ---
 
@@ -183,15 +182,15 @@ For example, you might have two separate question answer pairs with the followin
 |where is the parking *location*|
 |where is the ATM *location*|
 
-Since these two questions are phrased with very similar words, this similarity could cause very similar scores for many user queries that are phrased like  *"where is the `<x>` location"*. Instead, try to clearly differentiate with queries like  *"where is the parking lot"* and *"where is the ATM"*, by avoiding words like "location" that could be in many questions in your project.
+Since these two questions are phrased with similar words, this similarity could cause similar scores for many user queries that are phrased like  *where is the `<x>` location*. Instead, try to clearly differentiate your queries. For example, use specific questions like *where is the parking lot* and *where is the ATM*. Avoid using general words like *location*, since they could appear in many different questions throughout your project.
 
 ## Collaborate
 
-Custom question answering allows users to collaborate on a project. Users need access to the associated Azure resource group in order to access the projects. Some organizations may want to outsource the project editing and maintenance, and still be able to protect access to their Azure resources. This editor-approver model is done by setting up two identical language resources with identical custom question answering projects in different subscriptions and selecting one for the edit-testing cycle. Once testing is finished, the project contents are exported and transferred with an [import-export](../how-to/migrate-knowledge-base.md) process to the language resource of the approver that will finally deploy the project and update the endpoint.
+Custom question answering allows users to collaborate on a project. Users need access to the associated Azure resource group in order to access the projects. Some organizations may want to outsource the project editing and maintenance, and still be able to protect access to their Azure resources. This editor-approver model is done by setting up two identical language resources with identical custom question answering projects in different subscriptions and selecting one for the edit-testing cycle. Once testing is finished, the project contents are exported. They're then transferred using an [import-export](../how-to/migrate-knowledge-base.md) process. This process moves the contents to the language resource of the approver, who deploys the project and updates the endpoint.
 
 ## Active learning
 
-[Active learning](../tutorials/active-learning.md) does the best job of suggesting alternative questions when it has a wide range of quality and quantity of user-based queries. It’s important to allow client-applications' user queries to participate in the active learning feedback loop without censorship. Once questions are suggested in Language Studio, you can review and accept or reject those suggestions.
+[Active learning](../tutorials/active-learning.md) does the best job of suggesting alternative questions when it has a wide range of quality and quantity of user-based queries. It's important to allow client-applications' user queries to participate in the active learning feedback loop without censorship. Once questions are suggested in Language Studio, you can review and accept or reject those suggestions.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答のベストプラクティスの更新"
}
```

### Explanation
今回の変更は、「カスタム質問応答」に関するベストプラクティスを記載した記事の改訂であり、マイナーな更新と見なされます。具体的には、文中の表現をより明確にするための修正が行われ、いくつかの文が改善されました。例えば、質問と回答のペアの説明や、代替質問の付け加え方、メタデータタグの使用方法、シソーラスに関する情報が洗練されています。

さらに、日付が更新され、構文や表現がより具体的かつ簡潔なものに置き換えられました。特にリーダビリティが向上し、情報の正確さが保証されている点が特徴です。全体として、これにより読者がカスタム質問応答システムを効果的に活用できるようになることを目的としています。

## articles/ai-services/language-service/question-answering/overview.md{#item-631b23}

<details>
<summary>Diff</summary>
````diff
@@ -6,20 +6,20 @@ author: laujan
 ms.author: lajanuar
 recommendations: false
 ms.topic: overview
-ms.date: 03/24/2025
+ms.date: 07/16/2025
 keywords: "qna maker, low code chat bots, multi-turn conversations"
 ms.custom: language-service-question-answering
 ---
 
 # What is custom question answering?
 
-Custom question answering provides cloud-based Natural Language Processing (NLP) that allows you to create a natural conversational layer over your data. It is used to find appropriate answers from customer input or from a project.
+Custom question answering provides cloud-based Natural Language Processing (NLP) that allows you to create a natural conversational layer over your data. It's used to find appropriate answers from customer input or from a project.
 
 Custom question answering is commonly used to build conversational client applications, which include social media applications, chat bots, and speech-enabled desktop applications. This offering includes features like enhanced relevance using a deep learning ranker, precise answers, and end-to-end region support.
 
 Custom question answering comprises two capabilities:
 
-* Custom question answering: Using this capability users can customize different aspects like edit question and answer pairs extracted from the content source, define synonyms and metadata, accept question suggestions etc.
+* Custom question answering: Using this capability, users can customize different aspects like edit question and answer pairs extracted from the content source, define synonyms, and metadata, accept question suggestions etc.
 * [QnA Maker](./../../qnamaker/Overview/overview.md): This capability allows users to get a response by querying a text passage without having the need to manage knowledge bases.
 
 This documentation contains the following article types:
@@ -31,11 +31,11 @@ This documentation contains the following article types:
 
 ## When to use custom question answering
 
-* **When you have static information** - Use custom question answering when you have static information in your project. This project is custom to your needs, which you've built with documents such as PDFs and URLs.
+* **When you have static information** - Use custom question answering when you have static information in your project. This project is custom to your needs, which you built with documents such as PDFs and URLs.
 * **When you want to provide the same answer to a request, question, or command** - when different users submit the same question, the same answer is returned.
-* **When you want to filter static information based on meta-information** - add [metadata](./tutorials/multiple-domains.md) tags to provide additional filtering options relevant to your client application's users and the information. Common metadata information includes [chit-chat](./how-to/chit-chat.md), content type or format, content purpose, and content freshness. <!--TODO: Fix Link-->
-* **When you want to manage a bot conversation that includes static information** - your project takes a user's conversational text or command and answers it. If the answer is part of a pre-determined conversation flow, represented in your project with [multi-turn context](./tutorials/guided-conversations.md), the bot can easily provide this flow.
-* **When you want to use an agent to get an exact answer** - Use the [exact question answering](https://aka.ms/exact-answer-agent-template) agent template answers high-value predefined questions deterministically to ensure consistent and accurate responses or the [intent routing](https://aka.ms/intent-triage-agent-template) agent template, which detects user intent and provides exact answering. Perfect for deterministically intent routing and exact question answering with human control.
+* **When you want to filter static information based on meta-information** - add [metadata](./tutorials/multiple-domains.md) tags to provide added filtering options relevant to your client application's users and the information. Common metadata information includes [chit-chat](./how-to/chit-chat.md), content type or format, content purpose, and content freshness. <!--TODO: Fix Link-->
+* **When you want to manage a bot conversation that includes static information** - your project takes a user's conversational text or command and answers it. If the answer is part of a predetermined conversation flow, represented in your project with [multi-turn context](./tutorials/guided-conversations.md), the bot can easily provide this flow.
+* **When you want to use an agent to get an exact answer** - Use the [exact question answering](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog/msft-agent-samples/foundry-agent-service-sdk/customer-service-agent) agent template answers high-value predefined questions deterministically to ensure consistent and accurate responses or the [intent routing](https://github.com/azure-ai-foundry/foundry-samples/tree/main/samples/agent-catalog/msft-agent-samples/foundry-agent-service-sdk/intent-routing-agent) agent template, which detects user intent and provides exact answering. Perfect for deterministically intent routing and exact question answering with human control.
 
 ## What is a project?
 
@@ -56,7 +56,7 @@ Once a custom question answering project is published, a client application send
 
 |Step|Action|
 |:--|:--|
-|1|The client application sends the user's _question_ (text in their own words), "How do I programmatically update my project?" to your project endpoint.|
+|1|The client application sends the user's _question_ (text in their own words) to your project endpoint, *How do I programmatically update my project?*|
 |2|Custom question answering uses the trained project to provide the correct answer and any follow-up prompts that can be used to refine the search for the best answer. Custom question answering returns a JSON-formatted response.|
 |3|The client application uses the JSON response to make decisions about how to continue the conversation. These decisions can include showing the top answer and presenting more choices to refine the search for the best answer. |
 |||
@@ -69,7 +69,7 @@ Once your project is edited, publish the project to a working [Azure Web App bot
 
 ## High quality responses with layered ranking
 
-The custom question answering system uses a layered ranking approach. The data is stored in Azure search, which also serves as the first ranking layer. The top results from Azure search are then passed through custom question answering's NLP re-ranking model to produce the final results and confidence score.
+The custom question answering system uses a layered ranking approach. The data is stored in Azure search, which also serves as the first ranking layer. The top results from Azure search are then passed through custom question answering's NLP reranking model to produce the final results and confidence score.
 
 ## Multi-turn conversations
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム質問応答の概要の更新"
}
```

### Explanation
今回の変更は、「カスタム質問応答」に関する概要記事の内容を更新したもので、主に表現の明確化と時系列の修正が行われました。具体的には、日付の更新があり、内容の一部が再構成されることで、文の流れや理解しやすさが向上しています。例えば、質問と回答のペアを編集する際の具体的なフレーズに対する表現が改善され、より読みやすく、直感的に理解しやすい内容に変更されました。

この更新により、カスタム質問応答システムを利用する際の注意点やベストプラクティスがより明確に示され、読者がシステムを効果的に活用できることを目的としています。また、リーダビリティを高めるために、不要な言い回しが削除され、分かりやすい言葉が選ばれるようになっています。全体として、より使いやすく親しみやすい内容に仕上がっています。

## articles/ai-services/language-service/question-answering/tutorials/power-virtual-agents.md{#item-aec51d}

<details>
<summary>Diff</summary>
````diff
@@ -53,7 +53,7 @@ Although the bot can connect to your project from any topic, this tutorial uses
 Create a fallback topic by following the steps in [Configure the system fallback topic in Power Virtual Agents](/power-virtual-agents/authoring-system-fallback-topic).
 
 ## Use the authoring canvas to add an action
-Use the Power Virtual Agents authoring canvas to connect the fallback topic to your project. The topic starts with the unrecognized user text. Add an action that passes that text to custom question answering, and then shows the answer as a message. The last step of displaying an answer is handled as a [separate step](../../../QnAMaker/Tutorials/integrate-with-power-virtual-assistant-fallback-topic.md#add-your-solutions-flow-to-power-virtual-agents), later in this tutorial.
+Use the Power Virtual Agents authoring canvas to connect the fallback topic to your project. The topic starts with the unrecognized user text. Add an action that passes that text to custom question answering, and then shows the answer as a message. The last step of displaying an answer is handled as a [separate step](../../../QnAMaker/Tutorials/integrate-with-power-virtual-assistant-fallback-topic.md), later in this tutorial.
 
 This section creates the fallback topic conversation flow.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Power Virtual Agentsに関するチュートリアルの更新"
}
```

### Explanation
この変更は、「Power Virtual Agents」に関するチュートリアルのコンテンツをわずかに更新したものであり、マイナーな更新とされています。具体的には、テキストの構成を改善するために、リンク先を調整しました。元の文では「最後のステップ」としてリンクが提及されていましたが、より明確な表現を用いることで、関連情報へのアクセスが容易になっています。

この更新により、読者はカスタム質問応答に関する情報をより効果的に利用でき、その結果、ボットの設定や会話フローをスムーズに実装できるようになることを目指しています。また、文の明確さを高めることによって、学習体験全体を向上させる効果も期待されています。全体として、利用者がチュートリアルに従いやすくなったことが特徴です。

## articles/ai-services/language-service/text-analytics-for-health/how-to/use-containers.md{#item-9dddb4}

<details>
<summary>Diff</summary>
````diff
@@ -62,9 +62,10 @@ docker pull mcr.microsoft.com/azure-cognitive-services/textanalytics/healthcare:
 Once the container is on the host computer, use the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command and run the containers. The container continues to run until you stop it.
 
 > [!IMPORTANT]
+
 > * The docker commands in the following sections use the back slash, `\`, as a line continuation character. Replace or remove the back slash based on your host operating system's requirements.
 > * The `Eula`, `Billing`, and `ApiKey` options must be specified to run the container; otherwise, the container doesn't start. For more information, see [Billing](#billing).
->   * The [responsible AI](/azure/ai-foundry/responsible-ai/language-service/transparency-note) (RAI) acknowledgment must also be present with a value of `accept`.
+> * The [responsible AI](/azure/ai-foundry/responsible-ai/language-service/transparency-note) (RAI) acknowledgment must also be present with a value of `accept`.
 > * The sentiment analysis and language detection containers use v3 of the API, and are generally available. The key phrase extraction container uses v2 of the API, and is in preview.
 
 There are multiple ways you can install and run the Text Analytics for health container.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテナ使用方法に関するドキュメントの更新"
}
```

### Explanation
この変更は、「Text Analytics for Health」のコンテナ使用方法に関するドキュメントにおける軽微な更新です。具体的には、重要な注意事項のセクションに内容を追加し、ユーザーがコンテナを実行する際の操作手順をより明確に示すことを目的としています。

変更点としては、以下の内容が含まれています。まず、Dockerのコマンドを使用する際の行継続文字を説明する文が追加され、ユーザーがホストオペレーティングシステムに応じてバックスラッシュの置き換えや削除を行う必要があることが明示されています。また、RAI（Responsible AI）に関する追加の注意事項が強調され、コンテナを正常に実行するために必要な項目について再確認されています。

これらの変更により、ユーザーはコンテナを使用する際の注意点をより理解しやすくなり、スムーズに作業を進めることができるようになります。また、文書全体の一貫性と明確さを保つことで、利用者の利便性を向上させる効果も期待されます。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 07/14/2025
+ms.date: 07/16/2025
 ms.author: lajanuar
 ---
 
@@ -16,17 +16,17 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
 ## June 2025
 
-* A new version of the Conversational Language Understanding (CLU) training configuration, aimed at minimizing overpredictions of the [None intent](conversational-language-understanding/concepts/none-intent.md)—particularly in multilingual contexts—is now available via the REST API using **trainingConfigVersion 2025-07-01-preview**. For more information, *see* [Train your model: request body data](conversational-language-understanding/how-to/train-model.md?tabs=rest-api#request-body).
+**New version of the Conversational Language Understanding (CLU) training configuration**. This new version is aimed at minimizing overpredictions of the [None intent](conversational-language-understanding/concepts/none-intent.md)—particularly in multilingual contexts—is now available via the REST API using **trainingConfigVersion 2025-07-01-preview**. For more information, *see* [Train your model: request body data](conversational-language-understanding/how-to/train-model.md?tabs=rest-api#request-body).
 
-* The [Build your conversational agent](https://github.com/Azure-Samples/Azure-Language-OpenAI-Conversational-Agent-Accelerator) accelerator project is updated to include a new routing strategy—**TRIAGE_AGENT**. This strategy uses an agent hosted on Azure AI Foundry Agent Service. It utilizes Conversational Language Understanding (CLU) and Custom Question Answering (CQA) as tools to triage user intent for downstream agent routing. Additionally, these tools help deliver precise answers to specific questions. For more information, *see* [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216)
+**Updated [Build your conversational agent](https://github.com/Azure-Samples/Azure-Language-OpenAI-Conversational-Agent-Accelerator) accelerator project**. The update includes a new routing strategy—**TRIAGE_AGENT**. This strategy uses an agent hosted on Azure AI Foundry Agent Service. It utilizes Conversational Language Understanding (CLU) and Custom Question Answering (CQA) as tools to triage user intent for downstream agent routing. Additionally, these tools help deliver precise answers to specific questions. For more information, *see* [TechCommunity Blog Post](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-language-new-features-to-accelerate-your-agent-development/4415216)
 
-* The following [.NET SDKs](/dotnet/api/overview/azure/ai.textanalytics-readme?view=azure-dotnet&preserve-view=true) are now available, and support the latest REST API version **2025-15-05-preview**:
+**[.NET SDKs](/dotnet/api/overview/azure/ai.textanalytics-readme?view=azure-dotnet&preserve-view=true) support**. The following `.NET SDK`s are now available, and support the latest REST API version **2025-15-05-preview**:
 
-  * [Azure.AI.Language.Text 1.0.0-beta.3](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/cognitivelanguage/Azure.AI.Language.Conversations/CHANGELOG.md) provides inference capabilities for a wide range of language processing tasks. These tasks include language detection, sentiment analysis, key phrase extraction, and named entity recognition (NER). The capabilities also cover personally identifiable information (PII) entity recognition, entity linking, text analytics for healthcare, custom NER, and custom text classification. In addition, both extractive and abstractive text summarization are supported.
+  * [Azure.AI.Language.Text 1.0.0-beta.3](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/cognitivelanguage/Azure.AI.Language.Conversations/CHANGELOG.md) provides inference capabilities for a wide range of language processing tasks. These tasks include language detection, sentiment analysis, key phrase extraction, and named entity recognition (NER). The capabilities also include recognizing and linking personally identifiable information (PII) entities. Additionally, they offer text analytics for healthcare, custom named entity recognition (NER), and custom text classification. Both extractive and abstractive text summarization are also supported.
 
   * [Azure.AI.Language.Conversation 2.0.0-beta.3](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/cognitivelanguage/Azure.AI.Language.Conversations/CHANGELOG.md) provides inference capabilities for conversational PII, conversational language understanding (CLU), and conversation summarization.
 
-* The Text PII GPU container is now available for integration. You can access it on the [Microsoft Artifact Registry](https://mcr.microsoft.com/artifact/mar/azure-cognitive-services/textanalytics/pii/) using the tag `gpu`.
+**Text PII GPU container is now available for integration**. You can access this container on the [Microsoft Artifact Registry](https://mcr.microsoft.com/artifact/mar/azure-cognitive-services/textanalytics/pii/) using the tag `gpu`.
 
 ## May 2025
 
@@ -35,7 +35,7 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 * Improved AI quality for `PhoneNumber` entity type.
 
 **New agent templates**. Azure AI Language now supports the following agent templates:
-*  [Intent routing](../agents/concepts/agent-catalog.md): Detects user intent and provides precise answers, ideal for deterministic intent routing, and exact question answering with human oversight.
+*  [Intent routing](../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md): Detects user intent and provides precise answers, ideal for deterministic intent routing, and exact question answering with human oversight.
 *   [Exact question answering](../agents/concepts/agent-catalog.md): Delivers consistent, accurate responses to high-value predefined questions through deterministic methods.
 
 **PII detection enhancements**. Azure AI Language introduces new customization and entity subtype features for PII detection:
@@ -55,7 +55,7 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
 * Updated and improved model GA release for NER
 * Expanded context window for [PII redaction](personally-identifiable-information/overview.md?tabs=text-pii) – This service update expands the window of detection the PII redaction service considers, enhancing quality and accuracy.
-* Added prediction capability for custom models, including conversational language Understanding (CLU), custom named entity recognition (NER), and custom text classification, are now available in three new regions: Jio India Central, UK West, and Canada East.
+/python/api/azure-cognitiveservices-language-luis/index* Added prediction capability for custom models, including conversational language Understanding (CLU), custom named entity recognition (NER), and custom text classification, are now available in three new regions: Jio India Central, UK West, and Canada East.
 * Scanned PDF PII - [Document input for PII redaction](personally-identifiable-information/how-to/redact-document-pii.md) now supports scanned PDFs, enabling PII detection and redaction in both digital and nondigital documents using `OCR`.
 
 ## March 2025
@@ -126,7 +126,7 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 * [Conversational PII redaction](https://techcommunity.microsoft.com/blog/ai-azure-ai-services-blog/announcing-conversational-pii-detection-service-s-general/4162881) service in English-language contexts is now Generally Available (GA).
 * Conversation Summarization now supports 12 added languages in preview as listed [here](summarization/language-support.md).
 * Summarization Meeting or Conversation Chapter titles features support reduced length to focus on the key topics.
-* Enable support for data augmentation for diacritics to generate variations of training data for diacritic variations used in some natural languages which are especially useful for Germanic and Slavic languages.
+* Enable support for data augmentation for diacritics to generate variations of training data for diacritic variations used in some natural languages, which are especially useful for Germanic and Slavic languages.
 
 ## February 2024
 
@@ -198,8 +198,6 @@ Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up
 
     [**ReadMe**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text)
 
-    [**Samples**](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text/samples/v1-beta)
-
     ### [Python](#tab/python)
 
     [**Package (PyPi)**](https://pypi.org/project/azure-ai-textanalytics/5.3.0b2/)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Languageの新機能に関するドキュメントの更新"
}
```

### Explanation
この変更は、「Azure AI Language」の新機能に関するドキュメントを更新したもので、いくつかの重要な情報が追加され、既存の情報が改訂されています。主に、新しいバージョンのトレーニング設定、エージェントテンプレート、PII検出の強化に関する情報が整理されており、読みやすさと情報の明確さが向上しています。

具体的な変更点としては、以下の内容があります：

1. **Conversational Language Understanding (CLU)**の新しいトレーニング設定に関する説明が強調されており、多言語環境での誤判定を最小限に抑えるために設計されています。
2. **Build your conversational agent**プロジェクトの更新内容が明確化され、新しいルーティング戦略が導入されたことが強調されています。
3. **.NET SDKs**のサポートに関する情報が更新され、最新のREST APIバージョンに対応していることが記載されています。
4. **Text PII GPUコンテナ**の統合が可能であることが強調されており、そのアクセス方法についても記載されています。

この文書の更新により、利用者は最新の機能や改善点についての理解を深めることができ、Azure AI Languageをより効果的に活用できるようになります。また、内容の一貫性と明確さを保つことで、学習体験の質を向上させることが期待されます。


