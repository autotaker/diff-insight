---
date: '2024-11-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e12bec9...MicrosoftDocs:6042051
summary: 最近の変更により、Azureの関連ドキュメントに新しい「ソリューションアクセラレーター」が追加され、非構造的データの処理や知識のマイニングに役立つ機能が紹介されました。これにより、Azure
  AIやOpenAIサービスを活用した効率的な情報抽出と管理が可能になります。主な新機能として、「ドキュメント知識マイニングソリューションアクセラレーター」と「会話型知識マイニングソリューションアクセラレーター」が追加されました。特に、コンタクトセンターの会話データから洞察を得る仕組みが提供されています。全体として、ブレイキングチェンジはないものの、新しいリソースの追加が行われており、ユーザーにとって非常に価値のある更新といえます。これにより、複雑なデータセットから必要な情報を効率的に抽出・分析し、迅速な意思決定が可能になることが期待されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e12bec9...MicrosoftDocs:6042051){target="_blank"}

# ハイライト
最近の変更では、Azureの関連ドキュメントに新しい「ソリューションアクセラレーター」が追加され、非構造的データの処理や知識のマイニングにさらに役立つ機能が紹介されています。これにより、Azure AIとOpenAIサービスを利活用したより効率的な情報抽出と管理が可能になります。

## 新機能
- 「ドキュメント知識マイニングソリューションアクセラレーター」が追加され、非構造的な文書から要約やエンティティを抽出し、それに基づく検索やチャットをサポートするコードとドキュメントを提供します。
- 「会話型知識マイニングソリューションアクセラレーター」も紹介され、特にコンタクトセンターの会話から洞察を得るためのツールを用意しています。

## ブレイキングチェンジ
- ブレイキングチェンジは特にありません。全体的に新しいリソースの追加による拡張です。

## その他の更新
- 関連ドキュメントに、これらのアクセラレーターへのリンクが追加されました。特に、「Retrieval-augmented generation (RAG)」の概要やAzure Searchの解説内にこれらが含まれています。

# インサイト
このドキュメントの更新は、Azureを利用するユーザーにとって非常に価値のあるものです。新しいアクセラレーターは、複雑なデータセットから必要な情報を効率的に抽出し分析するための能力を提供します。

特に「ドキュメント知識マイニングアクセラレーター」は、Azure OpenAIサービスとAzure AIドキュメントインテリジェンス技術を活用し、非構造的なマルチモーダルドキュメントの解析を容易にしています。このため、企業や開発者はより迅速にドキュメント内の重要情報を取得し、さらにその情報に基づく検索や対話型エクスペリエンスを提供できるようになります。

また、「会話型知識マイニングアクセラレーター」はコンタクトセンターの対話データなどを分析し、実用的な洞察を抽出することを目的としています。これにより、顧客対応やサービス改善にリアルタイムで役立てることができるでしょう。

これらの更新によって、Azure Searchが持つ強力な情報検索・マイニング機能がさらに強化され、ユーザーはこのプラットフォームを用いてより洗練されたAI技術の活用ができるようになります。従来のデータ処理に比べ、Azureのこれらアクセラレーターを使用することで、効率性と成果の向上が期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [resource-tools.md](#item-0c6ac1) | minor update | ドキュメント知識マイニングソリューションアクセラレーターの追加 | modified | 1 | 0 | 1 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | 新しいソリューションアクセラレーターの追加 | modified | 2 | 0 | 2 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | 新しいソリューションアクセラレーターの情報追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/search/resource-tools.md{#item-0c6ac1}

<details>
<summary>Diff</summary>
````diff
@@ -30,4 +30,5 @@ Productivity tools are built by engineers at Microsoft, but aren't part of the A
 |-----------|------------ |-------------|
 | [Build your own copilot Solution Accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator) | Code and docs to build a copilot for specific use cases.| [Client advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ClientAdvisor/README.md) <br>[Generic document generator](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator) <br>[Research assistant](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ResearchAssistant/README.md) |
 | [Chat with your data solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator/blob/main/README.md) |  Code and docs to create interactive search solution in production environments.  | [https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) |
+| [Document knowledge mining solution accelerator](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator/blob/main/README.md) |  Code and docs built on Azure OpenAI Service and Azure AI Document Intelligence to process and extract summaries, entities, and metadata from unstructured, multimodal documents and enable searching and chatting over this data.  | [https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator) |
 | [Knowledge Mining accelerator](https://github.com/Azure-Samples/azure-search-knowledge-mining/blob/main/README.md) | Code and docs to jump start a knowledge store using your data. | [https://github.com/Azure-Samples/azure-search-knowledge-mining](https://github.com/Azure-Samples/azure-search-knowledge-mining) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント知識マイニングソリューションアクセラレーターの追加"
}
```

### Explanation
この変更は、`articles/search/resource-tools.md` ドキュメント内に新しい行を追加し、「ドキュメント知識マイニングソリューションアクセラレーター」についての情報を提供しています。このアクセラレーターは、Azure OpenAIサービスとAzure AIドキュメントインテリジェンスを利用して、非構造的なマルチモーダルドキュメントから要約、エンティティ、およびメタデータを処理・抽出し、さらにそのデータに対して検索やチャットを可能にするコードとドキュメントを提供します。この追加により、ユーザーは新しいリソースを活用して、より効率的に知識を活用できるようになります。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -230,6 +230,8 @@ A RAG solution that includes Azure AI Search can leverage [built-in data chunkin
   
   + [Conversational Knowledge Mining solution accelerator](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services)
 
+  + [Document Knowledge Mining accelerator](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator)
+
   + [Build your own copilot solution accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator)
 
     + [Client Advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ClientAdvisor/README.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいソリューションアクセラレーターの追加"
}
```

### Explanation
この変更では、`articles/search/retrieval-augmented-generation-overview.md` ドキュメントに新たに2つのリンクが追加されました。これにより、ユーザーは「会話型知識マイニングソリューションアクセラレーター」と「ドキュメント知識マイニングアクセラレーター」の情報にアクセスできるようになります。これらのアクセラレーターは、Azureの機能を活用して知識の管理や利用を支援するために設計されており、ユーザーがより効率的にAI技術を活用する手助けを提供します。この更新により、RAG（情報取得強化生成）ソリューションの理解が深まることが期待されます。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -111,6 +111,8 @@ Or, try solution accelerators:
 
 + [**Conversational Knowledge Mining** solution accelerator](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services) helps you create an interactive solution to extract actionable insights from post-contact center transcripts.
 
++ [**Document Knowledge Mining accelerator**](https://github.com/microsoft/Document-Knowledge-Mining-Solution-Accelerator) helps you process and extract summaries, entities, and metadata from unstructured, multimodal documents.
+
 + [**Build your own copilot** solution accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator), leverages Azure OpenAI Service, Azure AI Search and Microsoft Fabric, to create custom copilot solutions.
 
   + [Generic copilot](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator) helps you build your own copilot to identify relevant documents, summarize unstructured information, and generate Word document templates using your own data.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新しいソリューションアクセラレーターの情報追加"
}
```

### Explanation
この変更では、`articles/search/search-what-is-azure-search.md` ドキュメントに2つの新しいソリューションアクセラレーターに関する情報が追加されました。具体的には、「会話型知識マイニングソリューションアクセラレーター」と「ドキュメント知識マイニングアクセラレーター」が紹介されています。前者は、コンタクトセンターの会話Transcriptから実用的な洞察を抽出するためのインタラクティブなソリューションの構築を支援します。後者は、非構造的でマルチモーダルなドキュメントから要約、エンティティ、およびメタデータを処理・抽出する手助けをします。この更新により、Azure Searchの多様な適用方法がより一層明確になり、ユーザーにとっての利便性が向上します。


