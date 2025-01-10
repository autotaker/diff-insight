---
date: '2025-01-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6c9883f...MicrosoftDocs:1227d31
summary: このコードの変更は主にドキュメント内の表記やリンクの修正に焦点を当てたマイナーな更新である。新しい国名や言語の表記の変更、JavaScript SDKのサンプルリンクの更新、地域可用性に関する表現の明確化が含まれており、特にトルコの国名を「Turkey」から「Türkiye」に、言語名を「Oriya」から「Odia」に修正している。また、地域に関する記述を「country」から「country/region」に変更した。これらの更新は、グローバルなユーザーに対してより正確な情報を提供し、Azure
  AIの機能を効果的に活用できるよう支援することを目的としている。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6c9883f...MicrosoftDocs:1227d31){target="_blank"}

# Highlights
このコードの変更は全体としてマイナーな更新が多く、主にドキュメント内の表記やリンクの修正に焦点を当てている。特に、新しい国名や言語の表記に関する修正、JavaScript SDKのサンプルリンクの更新、および地域可用性に関する表現の明確化が含まれている。

## New features
- なし

## Breaking changes
- なし

## Other updates
- トルコの国名表記を「Turkey」から「Türkiye」に変更。
- 「Oriya」を「Odia」に修正。
- 「Azure AI Inference package for JavaScript」に関連するサンプルリンクを最新のURLに更新。
- 地域に関する記述を「country」から「country/region」に変更。

# Insights
このドキュメントの更新は、現代の標準に沿った表記を用いることで、グローバルなユーザーに対してより正確な情報を提供することを目的としている。例えば、トルコの新しい国名「Türkiye」への修正は国際的な調和を反映したものであり、「Odia」という言語名の修正は地域特有の文化を尊重するものだ。

また、JavaScript SDKのサンプルリンクの更新は、新しい情報にアクセスしやすくすることを目的としており、開発者がAzure AIの機能を効果的に利用できるよう支援する。これには、古くなったリンクを最新のGitHubリポジトリに更新することで、ユーザーエクスペリエンスを向上させるという意図がある。

さらに、地域に関する記述の明確化や表現の統一は、ユーザーが利用する地域に関する情報を正確に把握できるようにするための重要なステップである。これにより、ユーザーは必要なサービスを利用可能な地域で確実に利用できるようになり、配置に関する計画を立てやすくなる。

全体として、これらの更新は情報の正確性と可用性を高め、ユーザーがAzure AIのサービスを活用する際の利便性を向上させるために設計されている。特に技術者や開発者にとって、多言語および地域における整合性のある情報提供は、実装や展開の最適化に大いに役立つだろう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [prebuilt.md](#item-ac5486) | minor update | トルコの国名表記の修正 | modified | 1 | 1 | 2 | 
| [language-support.md](#item-2c8ef2) | minor update | オディアの表記変更 | modified | 1 | 1 | 2 | 
| [deploy-models-cohere-command.md](#item-3e97f4) | minor update | JavaScript SDKのサンプルリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-cohere-embed.md](#item-eab662) | minor update | JavaScript SDKのサンプルリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-jais.md](#item-0bd11f) | minor update | JavaScript SDKのサンプルリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | JavaScript SDKのサンプルリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-mistral-open.md](#item-84e005) | minor update | JavaScript SDKのサンプルリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | JavaScript SDKのサンプルリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-phi-3-5-vision.md](#item-8d6d7d) | minor update | JavaScript SDKのサンプルリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-phi-3-vision.md](#item-bd5aae) | minor update | JavaScript SDKのサンプルリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | JavaScript SDKのサンプルリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-phi-4.md](#item-c40212) | minor update | JavaScript SDKのサンプルリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-serverless-availability.md](#item-143252) | minor update | 地域に関する記述の明確化 | modified | 1 | 1 | 2 | 
| [model-catalog-overview.md](#item-278001) | minor update | 地域に関する記述の明確化 | modified | 1 | 1 | 2 | 
| [region-availability-maas.md](#item-35d79c) | minor update | 地域に関する表現の統一 | modified | 19 | 19 | 38 | 


# Modified Contents
## articles/ai-services/document-intelligence/language-support/prebuilt.md{#item-ac5486}

<details>
<summary>Diff</summary>
````diff
@@ -207,7 +207,7 @@ Azure AI Document Intelligence models provide multilingual document processing s
 | &bullet; Spanish (`es`) |Spain (`es`)|
 | &bullet; Swedish (`sv`) | Sweden (`se`)|
 | &bullet; Thai (`th`) | Thailand (`th`)|
-| &bullet; Turkish (`tr`) | Turkey (`tr`)|
+| &bullet; Turkish (`tr`) | Türkiye (`tr`)|
 | &bullet; Ukrainian (`uk`) | Ukraine (`uk`)|
 | &bullet; Vietnamese (`vi`) | Vietnam (`vi`)|
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トルコの国名表記の修正"
}
```

### Explanation
この変更は、ドキュメント内のトルコの国名表記を修正する小さな更新です。具体的には、「Turkey（トルコ）」という表記が「Türkiye（トルコ）」に変更されました。この修正は、国の名前の正確な表記を反映させるために行われました。これは、ユーザーが国名を正確に理解するための重要な更新といえます。関連する行も軽微な変更が行われ、ドキュメントは引き続き多言語の文書処理を提供することができます。

## articles/ai-services/language-service/language-detection/language-support.md{#item-2c8ef2}

<details>
<summary>Diff</summary>
````diff
@@ -187,7 +187,7 @@ If you have content expressed in a less frequently used language, you can try La
 | Kannada                               | `kn`        | `Latn`, `Knda` |
 | Malayalam                             | `ml`        | `Latn`, `Mlym` |
 | Marathi	                            | `mr`        | `Latn`, `Deva` |
-| Oriya                                 | `or`        | `Latn`, `Orya` |
+| Odia                                  | `or`        | `Latn`, `Orya` |
 | Punjabi                               | `pa`        | `Latn`, `Guru` |
 | Tamil                                 | `ta`        | `Latn`, `Taml` |
 | Telugu                                | `te`        | `Latn`, `Telu` |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オディアの表記変更"
}
```

### Explanation
この変更は、ドキュメント内の「Oriya」という表記を「Odia」に修正する小規模な更新です。これは、言語の正確な呼称を反映させるためのもので、オディアは、インドのオディシャ州で話される言語です。この修正により、言語の名称が現代の標準に沿った形で表示され、ユーザーに正しい情報が提供されるようになります。また、関連する情報も適切に更新され、言語検出サービスにおけるサポートが強化されています。

## articles/ai-studio/how-to/deploy-models-cohere-command.md{#item-3e97f4}

<details>
<summary>Diff</summary>
````diff
@@ -2129,7 +2129,7 @@ For more examples of how to use Cohere models, see the following examples and tu
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | Web requests                              | Bash              | [Command-R](https://aka.ms/samples/cohere-command-r/webrequests) - [Command-R+](https://aka.ms/samples/cohere-command-r-plus/webrequests) |
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)      |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/samples/cohere-command/openaisdk)             |
 | LangChain                                 | Python            | [Link](https://aka.ms/samples/cohere/langchain)                     |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンク更新"
}
```

### Explanation
この変更は、「Azure AI Inference package for JavaScript」に関するリンクを更新する小規模な修正です。具体的には、サンプルリンクが新しいGitHubリポジトリのURLに変更されました。この修正により、ユーザーが最新のサンプルコードにアクセスしやすくなり、JavaScriptでのAzure AIインファレンスパッケージの使用をより効果的に学ぶことが可能になります。変更後のリンクは、Azure SDKの最新のリポジトリに向けられ、最新の情報を反映した提供が行われていることを示しています。

## articles/ai-studio/how-to/deploy-models-cohere-embed.md{#item-eab662}

<details>
<summary>Diff</summary>
````diff
@@ -631,7 +631,7 @@ Cohere Embed V3 models can optimize the embeddings based on its use case.
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | Web requests                              | Bash              | [cohere-embed.ipynb](https://aka.ms/samples/embed-v3/webrequests) |
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)      |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/samples/cohere-embed/openaisdk)             |
 | LangChain                                 | Python            | [Link](https://aka.ms/samples/cohere-embed/langchain)                     |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンク更新"
}
```

### Explanation
この変更は、「Azure AI Inference package for JavaScript」に関連するサンプルリンクを更新する小規模な修正です。具体的には、JavaScript SDKに関するサンプルリンクが新しいGitHubリポジトリのURLに変更されました。この修正によって、ユーザーは最新のリソースにアクセスしやすくなり、Cohere Embed V3モデルを使用したアプリケーションの開発をよりスムーズに行えるようになります。更新されたリンクは、以前のリンクから移行され、最新のサンプルコードを含むリポジトリに指向されることで、情報の正確性と最新性が向上しています。

## articles/ai-studio/how-to/deploy-models-jais.md{#item-0bd11f}

<details>
<summary>Diff</summary>
````diff
@@ -1169,7 +1169,7 @@ For more examples of how to use Jais models, see the following examples and tuto
 
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 
 ## Cost and quota considerations for Jais models deployed as serverless API endpoints
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンク更新"
}
```

### Explanation
この変更は、「Azure AI Inference package for JavaScript」に関連するサンプルリンクを更新する小規模な修正です。変更前は古いリンクが使用されていましたが、最新のGitHubリポジトリのURLへと更新されました。この修正により、ユーザーはアプリケーション開発に必要な最新のサンプルコードに直接アクセスできるようになり、Jaisモデルの有効な使用方法をより簡単に学習できるようになります。更新されたリンクは、特にJavaScriptを使用したAIモデルの活用を支援するために重要です。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -2016,7 +2016,7 @@ For more examples of how to use Mistral models, see the following examples and t
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/mistral-large/openaisdk)                  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンク更新"
}
```

### Explanation
この変更は、「Azure AI Inference package for JavaScript」に関連するサンプルリンクを最新の情報に更新するマイナーな修正です。変更前は古いURLが使用されていましたが、最新のGitHubリポジトリへのリンクに差し替えられました。この更新により、ユーザーはMistralモデルを使用する際に必要な最新のサンプルコードに簡単にアクセスできるようになります。これにより、Azure AIにおけるJavaScriptの利用が一層スムーズになり、ユーザーが具体的な実装例を参照しやすくなります。全体的に、情報の正確性が向上し、ユーザーエクスペリエンスを改善することを目的とした変更です。

## articles/ai-studio/how-to/deploy-models-mistral-open.md{#item-84e005}

<details>
<summary>Diff</summary>
````diff
@@ -1285,7 +1285,7 @@ For more examples of how to use Mistral models, see the following examples and t
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/mistral-large/openaisdk)                  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンク更新"
}
```

### Explanation
この変更は、「Azure AI Inference package for JavaScript」に関連するサンプルリンクを最新のGitHubリポジトリのURLに修正するマイナーな更新です。変更前は以前のリンクが含まれていましたが、最新のサンプルにアクセスできるように最新のリンクに更新されました。この修正により、ユーザーはMistralモデルを操作する際に必要な最新のサンプルコードに直接アクセスできるようになり、特にJavaScriptを使用した開発が容易になります。全体として、より正確で有用な情報が提供され、AIモデルの利用に関する理解が深まることが期待されます。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -2216,7 +2216,7 @@ For more examples of how to use Mistral models, see the following examples and t
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/mistral-large/openaisdk)                  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンク更新"
}
```

### Explanation
この更新は、「Azure AI Inference package for JavaScript」に関連するサンプルリンクを最新のURLに修正するマイナーな変更です。以前のリンクは古くなっており、GitHubリポジトリの最新のサンプルコードへのリンクにアップデートされました。これにより、ユーザーはMistralモデルを利用する際に、最新のサンプルコードにより簡単にアクセスできるようになります。この修正は、特にJavaScriptを使用する開発者にとって、リソースへのアクセスを向上させ、使用方法を理解するのに役立つ情報が提供されることを目指しています。全体的に、ユーザーエクスペリエンスの改善が期待される内容です。

## articles/ai-studio/how-to/deploy-models-phi-3-5-vision.md{#item-8d6d7d}

<details>
<summary>Diff</summary>
````diff
@@ -1614,7 +1614,7 @@ For more examples of how to use Phi-3 family models, see the following examples
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/phi-3/openaisdk)                  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンク更新"
}
```

### Explanation
この変更は、「Azure AI Inference package for JavaScript」に関連するサンプルリンクを最新のGitHubリポジトリのURLに修正するマイナーな更新です。これにより、ユーザーはPhi-3ファミリーのモデルの利用方法に関する最新のサンプルコードにアクセスしやすくなります。元々のリンクは古くなっていたため、修正によって、最新の情報へアクセスできるようにされています。この更新は、特にJavaScriptを使用してモデルを実装する開発者にとって、利用可能なリソースを改善し、より良いエクスペリエンスを提供することを目的としています。全体として、この更新により、Phi-3モデルの運用に関する理解が深まることが期待されます。

## articles/ai-studio/how-to/deploy-models-phi-3-vision.md{#item-bd5aae}

<details>
<summary>Diff</summary>
````diff
@@ -1405,7 +1405,7 @@ For more examples of how to use Phi-3 family models, see the following examples
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/phi-3/openaisdk)                  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンク更新"
}
```

### Explanation
この変更は、Phi-3ファミリーのモデルに関連するドキュメント内で、「Azure AI Inference package for JavaScript」についてのサンプルリンクを更新するマイナーな修正です。以前のリンクは、Azure SDKのJavaScriptバージョンへの古いリンクでしたが、これを最新のGitHubリポジトリのリンクに修正しました。この更新により、開発者は新しいサンプルコードに簡単にアクセスでき、より効果的にモデルを活用することが可能になります。全体的に、このリンクの更新は、ユーザーにとっての実用性を向上させ、最新のリソースに基づく情報提供を図っています。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -1458,7 +1458,7 @@ For more examples of how to use Phi-3 family models, see the following examples
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/phi-3/openaisdk)                  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンク更新"
}
```

### Explanation
この変更は、「Azure AI Inference package for JavaScript」のサンプルリンクを最新のGitHubリポジトリのURLに修正するマイナーな更新です。変更前のリンクは古く、正確な情報を提供していませんでしたが、修正後は最新のサンプルコードにアクセスできるようになります。これにより、開発者はPHP-3モデルを利用するためのリソースにより簡単にアクセスでき、実践的な例を見つけやすくなります。全体的に、このリンクの更新は、ユーザーへの情報提供を改善し、最新のリソースに基づく有用な情報を提供することを目的としています。

## articles/ai-studio/how-to/deploy-models-phi-4.md{#item-c40212}

<details>
<summary>Diff</summary>
````diff
@@ -1117,7 +1117,7 @@ For more examples of how to use Phi-4 family models, see the following examples
 | Description                               | Language          | Sample                                                          |
 |-------------------------------------------|-------------------|-----------------------------------------------------------------|
 | CURL request                              | Bash              | [Link](https://aka.ms/phi-3/webrequests-sample)         |
-| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://aka.ms/azsdk/azure-ai-inference/javascript/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
 | Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
 | Python web requests                       | Python            | [Link](https://aka.ms/phi-3/webrequests-sample)         |
 | OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/phi-3/openaisdk)                  |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKのサンプルリンク更新"
}
```

### Explanation
この変更は、「Azure AI Inference package for JavaScript」についてのサンプルリンクを更新するマイナーな修正です。具体的には、リンクが古くなっていたため、更新後は最新のGitHubリポジトリへのリンクに変更されました。この修正により、開発者は最新のサンプルコードに直接アクセスでき、Phi-4ファミリーのモデルを使用する際の参考資料として役立てることができます。全体として、このリンクの更新は、情報の正確性と利用可能性を向上させることを目的とし、ユーザーにとっての利便性を高めることに寄与しています。

## articles/ai-studio/how-to/deploy-models-serverless-availability.md{#item-143252}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ Certain models in the model catalog can be deployed as a serverless API with pay
 
 ## Region availability
 
-Pay-as-you-go billing is available only to users whose Azure subscription belongs to a billing account in a country where the model provider has made the offer available (see "offer availability region" in the table in the next section). If the offer is available in the relevant region, the user then must have a Hub/Project in the Azure region where the model is available for deployment or fine-tuning, as applicable (see "Hub/Project Region" columns in the following tables).
+Pay-as-you-go billing is available only to users whose Azure subscription belongs to a billing account in a country/region where the model provider has made the offer available (see "offer availability region" in the table in the next section). If the offer is available in the relevant region, the user then must have a Hub/Project in the Azure region where the model is available for deployment or fine-tuning, as applicable (see "Hub/Project Region" columns in the following tables).
 
 [!INCLUDE [region-availability-maas](../includes/region-availability-maas.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域に関する記述の明確化"
}
```

### Explanation
この変更は、「地域の可用性」に関する記述を明確にするためのマイナーな更新です。具体的には、支払いプランの適用に関する条件について、"country"という表現を"country/region"に変更しました。この修正により、ユーザーはモデル提供者がオファーを利用可能とする地域に関する情報をより正確に理解できるようになり、必要な要件を把握することが容易になります。また、この変更は、関係するすべての地域のユーザーにサービスがどのように提供されるかを明示することを目的としています。全体的に、この文言の微調整は、ユーザーの認識を高めることに寄与しています。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -157,7 +157,7 @@ In Azure AI Foundry portal, you can use vector indexes and retrieval-augmented g
 
 ### Regional availability of offers and models
 
-Pay-per-token billing is available only to users whose Azure subscription belongs to a billing account in a country where the model provider has made the offer available. If the offer is available in the relevant region, the user then must have a project resource in the Azure region where the model is available for deployment or fine-tuning, as applicable. See [Region availability for models in serverless API endpoints | Azure AI Foundry](deploy-models-serverless-availability.md) for detailed information.
+Pay-per-token billing is available only to users whose Azure subscription belongs to a billing account in a country/region where the model provider has made the offer available. If the offer is available in the relevant region, the user then must have a project resource in the Azure region where the model is available for deployment or fine-tuning, as applicable. See [Region availability for models in serverless API endpoints | Azure AI Foundry](deploy-models-serverless-availability.md) for detailed information.
 
 ### Content safety for models deployed via serverless APIs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域に関する記述の明確化"
}
```

### Explanation
この変更は、「提供されるオファーやモデルの地域可用性」に関する記述を明確にするためのマイナーな更新です。具体的には、支払いプランに関する条件で、"country"という表現を"country/region"に変更しました。この修正によって、ユーザーはモデル提供者がオファーを利用可能としている地域について、より包括的な理解を得ることができます。この情報は、モデルがデプロイまたはファインチューニング可能なAzure地域において、必要なプロジェクトリソースを持つことに関連しています。全体として、この文言の修正は、ユーザーに対して正確な情報を提供し、利用可能性に関する理解を深めることを目的としています。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -15,31 +15,31 @@ ms.custom: include, references_regions
 
 |Model   |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-Cohere Command R+ 08-2024     |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
-Cohere Command R 08-2024     |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
-Cohere Command R+     |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
-Cohere Command R      | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3       | Not available        |
-Cohere Rerank v3 - English   |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
-Cohere Rerank v3 - Multilingual   |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
-Cohere Embed v3 - English    |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
-Cohere Embed v3 -  Multilingual    |  [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
+Cohere Command R+ 08-2024     |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
+Cohere Command R 08-2024     |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
+Cohere Command R+     |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3  | Not available        |
+Cohere Command R      | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3       | Not available        |
+Cohere Rerank v3 - English   |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
+Cohere Rerank v3 - Multilingual   |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
+Cohere Embed v3 - English    |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
+Cohere Embed v3 -  Multilingual    |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
 
 
 ### JAIS models
 
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-JAIS 30B Chat   |   [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Egypt    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
+JAIS 30B Chat   |   [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Egypt    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available       |
 
 ### Meta Llama models
 
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-Llama 2 7B <br> Llama 2 13B <br> Llama 2 70B     |   [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)     | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3    | West US 3       |
-Llama 2 7B Chat <br> Llama 2 70B Chat    | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3   | West US 3   |
-Llama 3 8B Instruct  <br> Llama 3 70B Instruct  | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available   |
-Llama 3.1 8B Instruct <br> Llama 3.1 70B Instruct | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3     | West US 3  |
-Llama 3.1 405B Instruct  | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3     | Not available  |
+Llama 2 7B <br> Llama 2 13B <br> Llama 2 70B     |   [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)     | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3    | West US 3       |
+Llama 2 7B Chat <br> Llama 2 70B Chat    | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3   | West US 3   |
+Llama 3 8B Instruct  <br> Llama 3 70B Instruct  | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3   | Not available   |
+Llama 3.1 8B Instruct <br> Llama 3.1 70B Instruct | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3     | West US 3  |
+Llama 3.1 405B Instruct  | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)    | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3     | Not available  |
 
 
 ### Microsoft Phi-3 family models
@@ -57,15 +57,15 @@ Phi-3-Medium-4K-Instruct  <br>  Phi-3-Medium-128K-Instruct  | Not applicable | E
 
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-Mistral Nemo     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
-Ministral-3B     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
-Mistral Small     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
-Mistral Large <br>  Mistral-Large (2407) <br> Mistral-Large (2411)    | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
+Mistral Nemo     | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong SAR<br> Israel     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
+Ministral-3B     | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong SAR <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
+Mistral Small     | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong SAR <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
+Mistral Large <br>  Mistral-Large (2407) <br> Mistral-Large (2411)    | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong SAR <br> Israel    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
 
 
 
 ### Nixtla models
 
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-TimeGEN-1     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Mexico <br> Israel  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3        |  Not available       |
+TimeGEN-1     | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Mexico <br> Israel  | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3        |  Not available       |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域に関する表現の統一"
}
```

### Explanation
この変更は、「地域可用性」に関するドキュメントの表現を統一するためのマイナーな更新です。具体的には、"Microsoft Managed Countries"という箇所での表現が、"Microsoft Managed countries/regions"に修正されました。この修正により、地域の定義がより一貫性を持ち、利用者にとって理解しやすくなります。また、表内のモデル情報に関しても、地域についての記述が一貫して整理されています。このように、ドキュメント全体としての明瞭性と整合性が向上しており、特にモデルの提供可能地域に関する情報が明確に伝わるようになっています。全体として、ユーザーが地域に関するオファーの可用性を正確に把握できることを目的とした改善です。


