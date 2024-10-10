---
date: '2024-10-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:eb045a9...MicrosoftDocs:7341d04
summary: 今回の変更は、いくつかのドキュメントの修正と更新を含み、具体的にはモデルの最大リクエストトークン数の修正、埋め込みモデルの最大トークン数に関する明確化、Azure
  AI Searchのデータ取り込みプロセスの更新、そしてモデルのプロビジョン状況の確認が行われています。新機能は追加されていませんが、既存の情報がより正確に更新されました。破壊的な変更はありませんが、更新によって異なる理解が生じる可能性があります。また、数値表記の修正や利用可能地域に関する情報の更新が行われ、ユーザーの理解が向上しました。これらの修正は、サービス利用者が正確な情報に基づいた行動を取れるようにするための重要な施策です。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:eb045a9...MicrosoftDocs:7341d04){target="_blank"}

# ハイライト

今回の変更は、いくつかのドキュメントにおける修正と更新を含んでおり、具体的には、モデルの最大リクエストトークン数の修正、埋め込みモデルの最大トークン数に関する明確化、Azure AI Searchのデータ取り込みプロセスの更新、そしてモデルのプロビジョン状況の確認です。

## 新機能
特に新機能というわけではなく、既存の機能や説明が修正され、より正確な情報が提供されるようになっています。

## 破壊的変更
今回の変更には、直接的に破壊的な変更は含まれていません。しかし、情報が更新され、正確性が向上したことで、ユーザーが異なる理解をする可能性はあります。

## その他の更新
- 数値表記の修正や、新しい説明の追加によるユーザー理解の改善。
- データ取り込みやモデルプロビジョンに関する利用可能地域やプロセスの更新。

# インサイト

修正・更新された変更は、多くのユーザーが利用するドキュメントの内容をより正確で最新の状態に保つために行われたものです。以下に各変更の詳細な説明を示します。

まず、`models.md` と `embeddings.md` における最大リクエストトークン数の修正です。これは、特定のモデルが許容するトークン数が更新され、特に多くのトークンを扱うことが想定されるAPIリクエストにおいて、ユーザーが制限を正しく理解できるようにしています。また、数値の表示が読みやすく調整され、数値による誤解を防ぐためにドキュメントが見直されています。

次に、`ai-search-ingestion.md` の更新では、Azure AI Searchのデータ取り込み方法が慎重に改訂されています。統合ベクトル化プロセスの導入により、取り込みが簡素化されていますが、この変更が既存のAPI契約に影響をもたらさないことが強調されております。これには、ユーザーのデータがよりスムーズかつ効率的に処理されることを意味しています。

最後に、`provisioned-models.md` における修正によって、モデルの地域ごとの利用可能性が明確にされました。地域ごとのプロビジョン状況を明示することは、ユーザーが自分の環境におけるモデルの利用可否を判断しやすくします。これにより、地域に基づくモデルの戦略的配置が可能になるため、ビジネスニーズに迅速に対応できます。

これらのドキュメント修正は、サービス利用者が不正確な情報に基づいて行動するリスクを減らし、より良いユーザーエクスペリエンスを提供するための重要な施策と言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [models.md](#item-db2c37) | minor update | モデルのリクエスト制限の修正 | modified | 3 | 3 | 6 | 
| [embeddings.md](#item-e38d07) | minor update | 埋め込みモデルの最大トークン数に関する明確化 | modified | 2 | 1 | 3 | 
| [ai-search-ingestion.md](#item-60c204) | minor update | データ取り込みプロセスの変更 | modified | 6 | 7 | 13 | 
| [provisioned-models.md](#item-8ee639) | minor update | モデルのプロビジョン状況の更新 | modified | 5 | 5 | 10 | 


# Modified Contents
## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -430,10 +430,10 @@ These models can only be used with Embedding API requests.
 
 |  Model ID | Max Request (tokens) | Output Dimensions |Training Data (up-to)
 |---|---| :---:|:---:|:---:|
-| `text-embedding-ada-002` (version 2) |8,191 | 1,536 | Sep 2021 |
+| `text-embedding-ada-002` (version 2) |8,192 | 1,536 | Sep 2021 |
 | `text-embedding-ada-002` (version 1) |2,046 | 1,536 | Sep 2021 |
-| `text-embedding-3-large` | 8,191 | 3,072 |Sep 2021 |
-| `text-embedding-3-small` | 8,191|  1,536 | Sep 2021 |
+| `text-embedding-3-large` | 8,192 | 3,072 |Sep 2021 |
+| `text-embedding-3-small` | 8,192|  1,536 | Sep 2021 |
 
 > [!NOTE]
 > When sending an array of inputs for embedding, the max number of input items in the array per call to the embedding endpoint is 2048.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのリクエスト制限の修正"
}
```

### Explanation
この変更は、`models.md` ドキュメントにおける特定のモデルの最大リクエストトークン数の値を更新しています。具体的には、以下の2つのモデルに対する最大リクエストトークン数が8,191から8,192に変更されました:

- `text-embedding-ada-002`（バージョン2）
- `text-embedding-3-large`
- `text-embedding-3-small`

これにより、ドキュメント内での正確性が向上し、ユーザーにより正しい情報が提供されます。元のメモリ制限と数値が誤ってプロパティ化されていたことにより、修正が必要でした。この更新を通じて、Embedding APIの利用者は適切なリクエスト制限を理解し、正しい数のトークンを送信できるようになります。

## articles/ai-services/openai/how-to/embeddings.md{#item-e38d07}

<details>
<summary>Diff</summary>
````diff
@@ -126,8 +126,9 @@ return $response.data.embedding
 
 ### Verify inputs don't exceed the maximum length
 
-- The maximum length of input text for our latest embedding models is 8192 tokens. You should verify that your inputs don't exceed this limit before making a request.
+- The maximum length of input text for our latest embedding models is 8,192 tokens. You should verify that your inputs don't exceed this limit before making a request.
 - If sending an array of inputs in a single embedding request the max array size is 2048.
+- The sum of the token count of the entire array of inputs sent in a single API call is subject to the max token limit of 8192. For example, you cannot send an array of 2,048 inputs with each input having five tokens or more. The total token count of this API request would be 10,240 total tokens, 2,048 tokens over the 8192 per API call token limit.
 
 
 ## Limitations & risks
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "埋め込みモデルの最大トークン数に関する明確化"
}
```

### Explanation
この変更は、`embeddings.md` ドキュメントにおける埋め込みモデルの最大入力トークン数に関する情報を更新しています。具体的には、以下の2点が修正されています。

1. **最大長の数値形式の修正**: 最大入力トークン数が「8192」から「8,192」に表記され、数値がより読みやすい形式に変更されました。
   
2. **追加の説明**: 新たに、APIコールで送信される入力の配列のトークン数の合計が最大トークン制限に従う必要があることが強調されています。たとえば、各入力が5トークン以上であれば、2048個の入力を送った場合、合計トークン数が10,240になり、制限を超えるため、そのようなリクエストは許可されないという説明が加えられています。

これにより、ユーザーは埋め込みモデルを使用する際の制限についてより明確に理解できるようになります。

## articles/ai-services/openai/includes/ai-search-ingestion.md{#item-60c204}

<details>
<summary>Diff</summary>
````diff
@@ -3,17 +3,16 @@ manager: nitinme
 ms.service: azure-ai-studio
 ms.custom:
 ms.topic: include
-ms.date: 03/25/2024
+ms.date: 10/08/2024
 ms.author: aahi
 author: aahill
 ---
 
 ### How data is ingested into Azure AI search
 
-Data is ingested into Azure AI search using the following process:
+As of September 2024, the ingestion APIs switched to [integrated vectorization](/azure/search/vector-search-integrated-vectorization). This update does **not** alter the existing API contracts. Integrated vectorization, a new offering of Azure AI Search, utilizes prebuilt skills for chunking and embedding the input data. The Azure OpenAI On Your Data ingestion service no longer employs custom skills. Following the migration to integrated vectorization, the ingestion process has undergone some modifications and as a result only the following assets are created:
+   * `{job-id}-index`
+   * `{job-id}-indexer`, if an hourly or daily schedule is specified, otherwise, the indexer is cleaned-up at the end of the ingestion process.
+   * `{job-id}-datasource`
 
-1. Ingestion assets are created in Azure AI Search resource and Azure storage account. Currently these assets are: indexers, indexes, data sources, a [custom skill](/azure/search/cognitive-search-custom-skill-interface) in the search resource, and a container (later called the chunks container) in the Azure storage account. You can specify the input Azure storage container using the [Azure OpenAI studio](https://oai.azure.com/), or the [ingestion API (preview)](/rest/api/azureopenai/ingestion-jobs). By default, text is assumed to use the UTF-8 encoding. To specify a different encoding, use the encoding configuration property. See the [.NET documentation](/dotnet/fundamentals/runtime-libraries/system-text-encoding#list-of-encodings) for a list of supported encodings.
-
-2. Data is read from the input container, contents are opened and chunked into small chunks with a maximum of 1,024 tokens each. If vector search is enabled, the service calculates the vector representing the embeddings on each chunk. The output of this step (called the "preprocessed" or "chunked" data) is stored in the chunks container created in the previous step. 
-
-3. The preprocessed data is loaded from the chunks container, and indexed in the Azure AI Search index.
\ No newline at end of file
+The chunks container is no longer available, as this functionality is now inherently managed by Azure AI Search.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ取り込みプロセスの変更"
}
```

### Explanation
この変更は、`ai-search-ingestion.md` ドキュメントにおけるAzure AI Searchへのデータ取り込みプロセスに関する説明を更新しています。以下の主要なポイントが修正されています。

1. **日付の更新**: ドキュメントの最終更新日が「2024年3月25日」から「2024年10月8日」に変更されました。

2. **取り込みプロセスの新しい説明**: 2024年9月以降、取り込みAPIが「統合ベクトル化」へ移行したことが明記され、これは既存のAPI契約に影響を与えないことが強調されています。この統合ベクトル化は、事前に作成されたスキルを利用して入力データのチャンク化や埋め込みを行います。

3. **新しい取り込み資産のリスト**: 移行後に作成される資産のリストが提供されており、これには `{job-id}-index`、`{job-id}-indexer`（スケジュールが指定された場合）、および `{job-id}-datasource` が含まれます。

4. **チャンクコンテナの管理変更**: 従来の「チャンクコンテナ」は利用できなくなり、この機能はAzure AI Searchによって内在的に管理されるようになったことが記述されています。

この更新により、ユーザーはAzure AI Searchのデータ取り込みに関する最新の手順を理解しやすくなっています。

## articles/ai-services/openai/includes/model-matrix/provisioned-models.md{#item-8ee639}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.date: 10/03/2024
 
 | **Region**     | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   |
 |:-------------------|:-------------------:|:---------------------------:|:---------------------------:|:-------------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|
-| australiaeast      | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | ✅                            | ✅                    | ✅                       | ✅                       |
+| australiaeast      | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | ✅                       | ✅                       |
 | brazilsouth        | ✅                | ✅                        | ✅                        | -                           | ✅                       | -                      | ✅                            | ✅                    | ✅                       | -                      |
 | canadacentral      | ✅                | -                       | -                       | -                           | -                      | -                      | -                           | ✅                    | -                      | ✅                       |
 | canadaeast         | ✅                | ✅                        | -                       | ✅                            | ✅                       | -                      | ✅                            | -                   | ✅                       | -                      |
@@ -22,14 +22,14 @@ ms.date: 10/03/2024
 | japaneast          | -               | ✅                        | ✅                        | ✅                            | ✅                       | -                      | ✅                            | -                   | -                      | ✅                       |
 | koreacentral       | ✅                | -                       | -                       | ✅                            | ✅                       | -                      | ✅                            | ✅                    | ✅                       | -                      |
 | northcentralus     | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | ✅                       | ✅                       |
-| norwayeast         | ✅                | -                       | ✅                        | -                           | -                      | -                      | -                           | ✅                    | -                      | -                      |
+| norwayeast         | ✅                | -                       | ✅                        | -                           | -                      | -                      | ✅                            | ✅                    | -                      | -                      |
 | polandcentral      | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | -                           | ✅                    | ✅                       | ✅                       |
-| southafricanorth   | ✅                | ✅                        | -                       | ✅                            | -                      | -                      | -                           | ✅                    | ✅                       | -                      |
+| southafricanorth   | ✅                | ✅                        | -                       | ✅                            | ✅                       | -                      | -                           | ✅                    | ✅                       | -                      |
 | southcentralus     | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | -                           | ✅                    | ✅                       | ✅                       |
 | southindia         | ✅                | ✅                        | ✅                        | -                           | ✅                       | -                      | ✅                            | ✅                    | ✅                       | ✅                       |
 | swedencentral      | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | ✅                       | ✅                       |
 | switzerlandnorth   | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | ✅                            | ✅                    | ✅                       | ✅                       |
 | switzerlandwest    | -               | -                       | -                       | -                           | -                      | -                      | -                           | -                   | -                      | ✅                       |
 | uksouth            | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | -                           | ✅                    | ✅                       | ✅                       |
-| westus             | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | ✅                            | ✅                    | ✅                       | ✅                       |
-| westus3            | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | -                      | -                           | ✅                    | ✅                       | ✅                       |
\ No newline at end of file
+| westus             | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | ✅                            | ✅                    | ✅                       | ✅                       |
+| westus3            | ✅                | ✅                        | ✅                        | ✅                            | ✅                       | ✅                       | -                           | ✅                    | ✅                       | ✅                       |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのプロビジョン状況の更新"
}
```

### Explanation
この変更は、`provisioned-models.md` ドキュメントにおけるモデルのプロビジョン状況の表を更新しています。以下の主要なポイントが修正されています。

1. **地域の機能確認の更新**: 「australiaeast」、「northcentralus」、「southafricanorth」、「westus」、「westus3」などの地域におけるモデルのプロビジョン状況が更新され、特にいくつかの地域でのモデル利用可能性が追加されました。

2. **特定のモデルの対応状況の変更**: 各地域における各モデルの対応状況が調整され、一部のモデルが新たに「✅」でマークされるとともに、いくつかのモデルの応答が「-」から「✅」に、またその逆が発生しています。たとえば、「southafricanorth」での「gpt-4o」、および「westus3」での「gpt-4o-mini」などが新たに追加されたり、修正されたりしています。

この更新により、ユーザーは各地域における利用可能なモデルの最新情報を把握しやすくなっています。


