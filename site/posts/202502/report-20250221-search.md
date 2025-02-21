---
date: '2025-02-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:11dfa93...MicrosoftDocs:6d12544
summary: 今回の変更では、C#、Java、およびJavaScriptを使用したフルテキスト検索のクイックスタートガイドが更新されました。主な内容として、Microsoft
  Entra IDを利用したキーなし認証の推奨や、環境セットアップ手順の詳述が含まれています。JavaScriptおよびTypeScriptガイドに対しては大幅な構成変更が行われ、一部の不要な画像ファイルが削除されて文書がクリーンアップされました。また、最新の情報を提供するために文書の日付も更新され、全体的に情報の明確化が図られています。この一連の更新により、ユーザーにとってより利用しやすいガイドとなっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:11dfa93...MicrosoftDocs:6d12544){target="_blank"}

<format>
# Highlights
これらの変更は、C#、Java、およびJavaScriptを用いたフルテキスト検索のクイックスタートガイドの更新に焦点を当てています。新機能としては、Microsoft Entra IDを使用したキーなし認証の推奨や環境セットアップ手順の明確化があり、JavaScriptとTypeScriptのガイドに対する大幅な構成変更も実施されています。一部の不要な画像ファイルが削除され、文書の明確化と更新が図られています。

## New features
- クイックスタートガイドにおけるMicrosoft Entra IDを使用したキーなし認証の推奨。
- JavaScriptとTypeScriptガイドにおける環境設定手順の詳細化。
- サンプルコードの改善とエラーハンドリングの強化。

## Breaking changes
- JavaScriptとTypeScriptのクイックスタートガイドに対する大幅な内容更新。
- 画像ファイルの削除による文書のクリーンアップ。

## Other updates
- ドキュメントの日付更新により、最新情報を読者に提供。
- 文書の冗長性を低減し、情報の明確化。

# Insights
今回の変更では、フルテキスト検索ガイドがよりユーザーフレンドリーになるよう大幅に改善されています。具体的には、Microsoft Entra IDの使用が推奨されるキーなし認証として強調され、よりセキュアで管理が簡単な認証手法へと読者を導いています。これにより、APIキーの繰り返し生成や保護の手間を軽減し、開発者がセキュリティリスクを低減できるようになっています。

JavaScriptおよびTypeScriptガイドでは、ドキュメント全体の再構成が行われ、環境設定手順やサンプルコードが最新の標準に基づいたものとなっています。これにより、開発者はAzure AI Searchの機能をより効果的に活用でき、実践的なアプリケーション開発へと繋げることが可能です。特に、エラーハンドリングや非同期処理の強化は、実運用をスムーズにし、トラブルシューティングを容易にします。

画像の削除については、視覚情報が追加の価値を提供しない、または他の方法で効率的に置き換えられると判断されたためでしょう。これにより、ユーザーがテキスト情報に集中でき、ガイド全体の可読性が向上します。

全体として、この一連の更新は技術的整合性とユーザビリティを高め、ドキュメントの質を向上させるものとなっています。開発者はこれらの変更を活用することで、より安心して最新のテクノロジーを駆使した開発を行えるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [full-text-csharp.md](#item-2e943a) | minor update | コンソールアプリケーションの作成手順についての更新 | modified | 3 | 3 | 6 | 
| [full-text-intro.md](#item-f655a1) | minor update | 文書の日付更新 | modified | 1 | 1 | 2 | 
| [full-text-java.md](#item-d659f9) | minor update | Javaによるフルテキスト検索のクイックスタートガイドの更新 | modified | 3 | 3 | 6 | 
| [full-text-javascript.md](#item-568e3a) | breaking change | JavaScriptによるフルテキスト検索クイックスタートの大幅更新 | modified | 505 | 341 | 846 | 
| [full-text-typescript.md](#item-6630e8) | breaking change | TypeScriptによるフルテキスト検索クイックスタートの大幅更新 | modified | 428 | 329 | 757 | 
| [create-index-no-data.png](#item-72216f) | minor update | 不要な画像ファイルの削除 | removed | 0 | 0 | 0 | 
| [service-name-and-keys.png](#item-1a7e47) | minor update | サービス名とキーに関する画像の削除 | removed | 0 | 0 | 0 | 
| [search-get-started-text.md](#item-935941) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [search-howto-index-encrypted-blobs.md](#item-a7097a) | minor update | 画像と不必要な文字列の削除 | modified | 0 | 2 | 2 | 
| [tutorial-multiple-data-sources.md](#item-71558f) | minor update | 画像の削除 | modified | 0 | 2 | 2 | 


# Modified Contents
## articles/search/includes/quickstarts/full-text-csharp.md{#item-2e943a}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 1. Create a new folder `full-text-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
     ```shell
-    mkdir full-text-quickstart && cd full-text-quickstart
+    mkdir full-text-quickstart && code full-text-quickstart
     ```
 
 1. Create a new console application with the following command:
@@ -65,7 +65,7 @@ In the prior [set up](#set-up) section, you created a new console application an
 
 In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
 
-The sample code in this quickstart uses Microsoft Entra ID for authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
 #### [Microsoft Entra ID](#tab/keyless)
 
@@ -623,7 +623,7 @@ In *Program.cs*, you created two clients:
 
 Both clients need the search service endpoint and credentials described previously in the [resource information](#retrieve-resource-information) section.
 
-The sample code in this quickstart uses Microsoft Entra ID for authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
 #### [Microsoft Entra ID](#tab/keyless)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンソールアプリケーションの作成手順についての更新"
}
```

### Explanation
この変更は、C#によるフルテキスト検索のクイックスタートガイドにおけるコンソールアプリケーションの作成手順に関する内容です。具体的には、Microsoft Entra IDを用いたキーなしの認証を推奨する記述が明確化されました。以下の2か所で変更が加えられています。

1. コマンド実行に関する説明で、ディレクトリを作成した後に「Visual Studio Codeでそのフォルダを開く」といった指示が、具体的に「code full-text-quickstart」と更新されました。これにより、ユーザーはより直感的にコマンドを実行できるようになりました。

2. 認証に関する部分では、Microsoft Entra IDの使用が「推奨されるキーなし認証」として明確に説明され、情報がより一貫性を持って伝えられるようになりました。これにより、APIキーを使用した場合の手続きについても、変更が適切に示されています。

全体として、今回の小規模な更新はユーザーにとっての理解を助け、コンソールアプリケーション作成時の手順をより明瞭にしています。

## articles/search/includes/quickstarts/full-text-intro.md{#item-f655a1}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/12/2025
+ms.date: 2/19/2025
 ---
 
 Learn how to use the *Azure.Search.Documents* client library to create, load, and query a search index using sample data for [full text search](../../search-lucene-query-architecture.md). Full text search uses Apache Lucene for indexing and queries, and a BM25 ranking algorithm for scoring results.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書の日付更新"
}
```

### Explanation
この変更は、フルテキスト検索に関する導入ガイド文書の日付情報を更新したものです。具体的には、`ms.date`の項目が「2025年2月12日」から「2025年2月19日」に変更されています。この日付は文書の最終更新日を示しており、内容が最近更新されたことを読者に知らせる役割を果たします。

それによって、読者は最新の情報に基づいてコンテンツを確認することができ、特に新しい機能や修正があった場合に正確な参照を持つことができます。全体として、この変更はユーザーの理解を促進し、文書の信頼性を向上させるものです。

## articles/search/includes/quickstarts/full-text-java.md{#item-d659f9}

<details>
<summary>Diff</summary>
````diff
@@ -93,11 +93,11 @@ The sample in this quickstart works with the Java Runtime. Install a Java Develo
 
 ## Create, load, and query a search index
 
-In the prior [set up](#set-up) section, you created a new console application and installed the Azure AI Search client library. 
+In the prior [set up](#set-up) section, you installed the Azure AI Search client library and other dependencies. 
 
 In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
 
-The sample code in this quickstart uses Microsoft Entra ID for authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
 #### [Microsoft Entra ID](#tab/keyless)
 
@@ -540,7 +540,7 @@ In *App.java* you created two clients:
 
 Both clients need the search service endpoint and credentials described previously in the resource information section.
 
-The sample code in this quickstart uses Microsoft Entra ID for authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
 #### [Microsoft Entra ID](#tab/keyless)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaによるフルテキスト検索のクイックスタートガイドの更新"
}
```

### Explanation
この変更は、Javaによるフルテキスト検索のクイックスタートガイドに関するもので、文書内の一部の記述を明確にするための内容が更新されました。主な変更点は以下の通りです：

1. **依存関係の明示**: 一つ目の変更として、以前の「新しいコンソールアプリケーションを作成した」との記述が、「Azure AI Searchクライアントライブラリやその他の依存関係をインストールした」と修正され、手順がより正確に示されています。これにより、ユーザーは必要なすべてのセットアップ手順を理解しやすくなります。

2. **認証方法の明確化**: さらに、Microsoft Entra IDを使用した認証方法について、従来の表現から「推奨されるキーなし認証」というフレーズに変更されました。これにより、読者に対してより一貫した理解を促すことが期待されます。

この変更は全体として、ユーザーがフルテキスト検索を実装する際のプロセスを簡潔に理解できるように配慮されています。

## articles/search/includes/quickstarts/full-text-javascript.md{#item-568e3a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/12/2025
+ms.date: 2/19/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -27,258 +27,524 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
-## Set up your environment
+## Set up
 
-We used the following tools to create this quickstart.
+1. Create a new folder `full-text-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-+ [Visual Studio Code](https://code.visualstudio.com), which has built-in support for creating JavaScript apps
-
-+ [Node.js](https://nodejs.org) and [npm](https://www.npmjs.com)
-
-## Create the project
-
-1. Start Visual Studio Code.
-
-1. Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) by using **Ctrl+Shift+P** and open the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal).
-
-1. Create a development directory, giving it the name *quickstart*:
-
-    ```cmd
-    mkdir quickstart
-    cd quickstart
+    ```shell
+    mkdir full-text-quickstart && code full-text-quickstart
     ```
 
-1. Initialize an empty project with npm by running the following command. To fully initialize the project, press Enter multiple times to accept the default values, except for the License, which you should set to *MIT*. 
+1. Create the `package.json` with the following command:
 
-    ```cmd
-    npm init
+    ```shell
+    npm init -y
     ```
 
-1. Install `@azure/search-documents`, the [JavaScript/TypeScript SDK for Azure AI Search](/javascript/api/overview/azure/search-documents-readme). 
+1. Install the Azure AI Search client library ([Azure.Search.Documents](/javascript/api/overview/azure/search-documents-readme)) for JavaScript with:
 
-    ```cmd
+    ```console
     npm install @azure/search-documents
     ```
 
-1. Install `dotenv`, which is used to import the environment variables such as your search service name and API key.
+1. For the **recommended** passwordless authentication, install the Azure Identity client library with:
 
-    ```cmd
-    npm install dotenv
+    ```console
+    npm install @azure/identity
     ```
 
-1. Navigate to the *quickstart* directory, then confirm that you've configured the project and its dependencies by checking that your *package.json* file looks similar to the following json:
 
-    ```json
-    {
-      "name": "quickstart",
-      "version": "1.0.0",
-      "description": "Azure AI Search Quickstart",
-      "main": "index.js",
-      "scripts": {
-        "test": "echo \"Error: no test specified\" && exit 1"
-      },
-      "keywords": [
-        "Azure",
-        "Search"
-      ],
-      "author": "Your Name",
-      "license": "MIT",
-      "dependencies": {
-        "@azure/search-documents": "^11.3.0",
-        "dotenv": "^16.0.2"
-      }
-    }
-    ```
-
-1. Create a file *.env* to hold your search service parameters:
 
-    ```
-    SEARCH_API_KEY=<YOUR-SEARCH-ADMIN-API-KEY>
-    SEARCH_API_ENDPOINT=<YOUR-SEARCH-SERVICE-URL>
-    ```
+## Create, load, and query a search index
 
-Replace the `YOUR-SEARCH-SERVICE-URL` value with the name of your search service endpoint URL. Replace `<YOUR-SEARCH-ADMIN-API-KEY>` with the admin key you recorded earlier. 
+In the prior [set up](#set-up) section, you installed the Azure AI Search client library and other dependencies. 
 
-## Create index.js file
+In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
 
-Next we create an *index.js* file, which is the main file that hosts our code.
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
-At the top of this file, we import the `@azure/search-documents` library:
+#### [Microsoft Entra ID](#tab/keyless)
 
-```javascript
-const { SearchIndexClient, SearchClient, AzureKeyCredential, odata } = require("@azure/search-documents");
+```java
+String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();
 ```
 
-Next, we need to require the `dotenv` package to read in the parameters from the *.env* file as follows:
-
-```javascript
-// Load the .env file if it exists
-require("dotenv").config();
+#### [API key](#tab/api-key)
 
-// Getting endpoint and apiKey from .env file
-const endpoint = process.env.SEARCH_API_ENDPOINT || "";
-const apiKey = process.env.SEARCH_API_KEY || "";
+```java
+String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
 ```
+---
 
-With our imports and environment variables in place, we're ready to define the main function.
+1. Create a new file named *index.js* and paste the following code into *index.js*:
+
+    ```javascript
+    // Import from the @azure/search-documents library
+    import { SearchIndexClient, odata } from "@azure/search-documents";
+    // Import from the Azure Identity library
+    import { DefaultAzureCredential } from "@azure/identity";
+    // Importing the hotels sample data
+    import hotelData from './hotels.json' assert { type: "json" };
+    // Load the .env file if it exists
+    import * as dotenv from "dotenv";
+    dotenv.config();
+    // Defining the index definition
+    const indexDefinition = {
+        "name": "hotels-quickstart",
+        "fields": [
+            {
+                "name": "HotelId",
+                "type": "Edm.String",
+                "key": true,
+                "filterable": true
+            },
+            {
+                "name": "HotelName",
+                "type": "Edm.String",
+                "searchable": true,
+                "filterable": false,
+                "sortable": true,
+                "facetable": false
+            },
+            {
+                "name": "Description",
+                "type": "Edm.String",
+                "searchable": true,
+                "filterable": false,
+                "sortable": false,
+                "facetable": false,
+                "analyzerName": "en.lucene"
+            },
+            {
+                "name": "Description_fr",
+                "type": "Edm.String",
+                "searchable": true,
+                "filterable": false,
+                "sortable": false,
+                "facetable": false,
+                "analyzerName": "fr.lucene"
+            },
+            {
+                "name": "Category",
+                "type": "Edm.String",
+                "searchable": true,
+                "filterable": true,
+                "sortable": true,
+                "facetable": true
+            },
+            {
+                "name": "Tags",
+                "type": "Collection(Edm.String)",
+                "searchable": true,
+                "filterable": true,
+                "sortable": false,
+                "facetable": true
+            },
+            {
+                "name": "ParkingIncluded",
+                "type": "Edm.Boolean",
+                "filterable": true,
+                "sortable": true,
+                "facetable": true
+            },
+            {
+                "name": "LastRenovationDate",
+                "type": "Edm.DateTimeOffset",
+                "filterable": true,
+                "sortable": true,
+                "facetable": true
+            },
+            {
+                "name": "Rating",
+                "type": "Edm.Double",
+                "filterable": true,
+                "sortable": true,
+                "facetable": true
+            },
+            {
+                "name": "Address",
+                "type": "Edm.ComplexType",
+                "fields": [
+                    {
+                        "name": "StreetAddress",
+                        "type": "Edm.String",
+                        "filterable": false,
+                        "sortable": false,
+                        "facetable": false,
+                        "searchable": true
+                    },
+                    {
+                        "name": "City",
+                        "type": "Edm.String",
+                        "searchable": true,
+                        "filterable": true,
+                        "sortable": true,
+                        "facetable": true
+                    },
+                    {
+                        "name": "StateProvince",
+                        "type": "Edm.String",
+                        "searchable": true,
+                        "filterable": true,
+                        "sortable": true,
+                        "facetable": true
+                    },
+                    {
+                        "name": "PostalCode",
+                        "type": "Edm.String",
+                        "searchable": true,
+                        "filterable": true,
+                        "sortable": true,
+                        "facetable": true
+                    },
+                    {
+                        "name": "Country",
+                        "type": "Edm.String",
+                        "searchable": true,
+                        "filterable": true,
+                        "sortable": true,
+                        "facetable": true
+                    }
+                ]
+            }
+        ],
+        "suggesters": [
+            {
+                "name": "sg",
+                "searchMode": "analyzingInfixMatching",
+                "sourceFields": [
+                    "HotelName"
+                ]
+            }
+        ]
+    };
+    async function main() {
+        // Your search service endpoint
+        const searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+        // Use the recommended keyless credential instead of the AzureKeyCredential credential.
+        const credential = new DefaultAzureCredential();
+        //const credential = new AzureKeyCredential(Your search service admin key);
+        // Create a SearchIndexClient to send create/delete index commands
+        const searchIndexClient = new SearchIndexClient(searchServiceEndpoint, credential);
+        // Creating a search client to upload documents and issue queries
+        const indexName = "hotels-quickstart";
+        const searchClient = searchIndexClient.getSearchClient(indexName);
+        console.log('Checking if index exists...');
+        await deleteIndexIfExists(searchIndexClient, indexName);
+        console.log('Creating index...');
+        let index = await searchIndexClient.createIndex(indexDefinition);
+        console.log(`Index named ${index.name} has been created.`);
+        console.log('Uploading documents...');
+        let indexDocumentsResult = await searchClient.mergeOrUploadDocuments(hotelData['value']);
+        console.log(`Index operations succeeded: ${JSON.stringify(indexDocumentsResult.results[0].succeeded)} `);
+        // waiting one second for indexing to complete (for demo purposes only)
+        sleep(1000);
+        console.log('Querying the index...');
+        console.log();
+        await sendQueries(searchClient);
+    }
+    async function deleteIndexIfExists(searchIndexClient, indexName) {
+        try {
+            await searchIndexClient.deleteIndex(indexName);
+            console.log('Deleting index...');
+        }
+        catch {
+            console.log('Index does not exist yet.');
+        }
+    }
+    async function sendQueries(searchClient) {
+        // Query 1
+        console.log('Query #1 - search everything:');
+        let searchOptions = {
+            includeTotalCount: true,
+            select: ["HotelId", "HotelName", "Rating"]
+        };
+        let searchResults = await searchClient.search("*", searchOptions);
+        for await (const result of searchResults.results) {
+            console.log(`${JSON.stringify(result.document)}`);
+        }
+        console.log(`Result count: ${searchResults.count}`);
+        console.log();
+        // Query 2
+        console.log('Query #2 - search with filter, orderBy, and select:');
+        let state = 'FL';
+        searchOptions = {
+            filter: odata `Address/StateProvince eq ${state}`,
+            orderBy: ["Rating desc"],
+            select: ["HotelId", "HotelName", "Rating"]
+        };
+        searchResults = await searchClient.search("wifi", searchOptions);
+        for await (const result of searchResults.results) {
+            console.log(`${JSON.stringify(result.document)}`);
+        }
+        console.log();
+        // Query 3
+        console.log('Query #3 - limit searchFields:');
+        searchOptions = {
+            select: ["HotelId", "HotelName", "Rating"],
+            searchFields: ["HotelName"]
+        };
+        searchResults = await searchClient.search("sublime cliff", searchOptions);
+        for await (const result of searchResults.results) {
+            console.log(`${JSON.stringify(result.document)}`);
+        }
+        console.log();
+        // Query 4
+        console.log('Query #4 - limit searchFields and use facets:');
+        searchOptions = {
+            facets: ["Category"],
+            select: ["HotelId", "HotelName", "Rating"],
+            searchFields: ["HotelName"]
+        };
+        searchResults = await searchClient.search("*", searchOptions);
+        for await (const result of searchResults.results) {
+            console.log(`${JSON.stringify(result.document)}`);
+        }
+        console.log();
+        // Query 5
+        console.log('Query #5 - Lookup document:');
+        let documentResult = await searchClient.getDocument('3');
+        console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.HotelName}`);
+        console.log();
+    }
+    function sleep(ms) {
+        return new Promise(resolve => setTimeout(resolve, ms));
+    }
+    main().catch((err) => {
+        console.error("The sample encountered an error:", err);
+    });
+    ```
 
-Most of the functionality in the SDK is asynchronous so we make our main function `async`. We also include a `main().catch()` below the main function to catch and log any errors encountered:
+1. Create a file named *hotels.json* and paste the following code into *hotels.json*:
 
-```javascript
-async function main() {
-    console.log(`Running Azure AI Search JavaScript quickstart...`);
-    if (!endpoint || !apiKey) {
-        console.log("Make sure to set valid values for endpoint and apiKey with proper authorization.");
-        return;
+    ```json
+    {
+        "value": [
+            {
+                "HotelId": "1",
+                "HotelName": "Secret Point Motel",
+                "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
+                "Description_fr": "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.",
+                "Category": "Boutique",
+                "Tags": ["pool", "air conditioning", "concierge"],
+                "ParkingIncluded": false,
+                "LastRenovationDate": "1970-01-18T00:00:00Z",
+                "Rating": 3.6,
+                "Address": {
+                    "StreetAddress": "677 5th Ave",
+                    "City": "New York",
+                    "StateProvince": "NY",
+                    "PostalCode": "10022"
+                }
+            },
+            {
+                "HotelId": "2",
+                "HotelName": "Twin Dome Motel",
+                "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
+                "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
+                "Category": "Boutique",
+                "Tags": ["pool", "free wifi", "concierge"],
+                "ParkingIncluded": "false",
+                "LastRenovationDate": "1979-02-18T00:00:00Z",
+                "Rating": 3.6,
+                "Address": {
+                    "StreetAddress": "140 University Town Center Dr",
+                    "City": "Sarasota",
+                    "StateProvince": "FL",
+                    "PostalCode": "34243"
+                }
+            },
+            {
+                "HotelId": "3",
+                "HotelName": "Triple Landscape Hotel",
+                "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+                "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
+                "Category": "Resort and Spa",
+                "Tags": ["air conditioning", "bar", "continental breakfast"],
+                "ParkingIncluded": "true",
+                "LastRenovationDate": "2015-09-20T00:00:00Z",
+                "Rating": 4.8,
+                "Address": {
+                    "StreetAddress": "3393 Peachtree Rd",
+                    "City": "Atlanta",
+                    "StateProvince": "GA",
+                    "PostalCode": "30326"
+                }
+            },
+            {
+                "HotelId": "4",
+                "HotelName": "Sublime Cliff Hotel",
+                "Description": "Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 1800 palace.",
+                "Description_fr": "Le sublime Cliff Hotel est situé au coeur du centre historique de sublime dans un quartier extrêmement animé et vivant, à courte distance de marche des sites et monuments de la ville et est entouré par l'extraordinaire beauté des églises, des bâtiments, des commerces et Monuments. Sublime Cliff fait partie d'un Palace 1800 restauré avec amour.",
+                "Category": "Boutique",
+                "Tags": ["concierge", "view", "24-hour front desk service"],
+                "ParkingIncluded": true,
+                "LastRenovationDate": "1960-02-06T00:00:00Z",
+                "Rating": 4.6,
+                "Address": {
+                    "StreetAddress": "7400 San Pedro Ave",
+                    "City": "San Antonio",
+                    "StateProvince": "TX",
+                    "PostalCode": "78216"
+                }
+            }
+        ]
     }
+    ```
 
-    // remaining quickstart code will go here
-}
+1. Create a file named *hotels_quickstart_index.json* and paste the following code into *hotels_quickstart_index.json*:
 
-main().catch((err) => {
-    console.error("The sample encountered an error:", err);
-});
-```
+    ```json
+    {
+    	"name": "hotels-quickstart",
+    	"fields": [
+    		{
+    			"name": "HotelId",
+    			"type": "Edm.String",
+    			"key": true,
+    			"filterable": true
+    		},
+    		{
+    			"name": "HotelName",
+    			"type": "Edm.String",
+    			"searchable": true,
+    			"filterable": false,
+    			"sortable": true,
+    			"facetable": false
+    		},
+    		{
+    			"name": "Description",
+    			"type": "Edm.String",
+    			"searchable": true,
+    			"filterable": false,
+    			"sortable": false,
+    			"facetable": false,
+    			"analyzerName": "en.lucene"
+    		},
+    		{
+    			"name": "Description_fr",
+    			"type": "Edm.String",
+    			"searchable": true,
+    			"filterable": false,
+    			"sortable": false,
+    			"facetable": false,
+    			"analyzerName": "fr.lucene"
+    		},
+    		{
+    			"name": "Category",
+    			"type": "Edm.String",
+    			"searchable": true,
+    			"filterable": true,
+    			"sortable": true,
+    			"facetable": true
+    		},
+    		{
+    			"name": "Tags",
+    			"type": "Collection(Edm.String)",
+    			"searchable": true,
+    			"filterable": true,
+    			"sortable": false,
+    			"facetable": true
+    		},
+    		{
+    			"name": "ParkingIncluded",
+    			"type": "Edm.Boolean",
+    			"filterable": true,
+    			"sortable": true,
+    			"facetable": true
+    		},
+    		{
+    			"name": "LastRenovationDate",
+    			"type": "Edm.DateTimeOffset",
+    			"filterable": true,
+    			"sortable": true,
+    			"facetable": true
+    		},
+    		{
+    			"name": "Rating",
+    			"type": "Edm.Double",
+    			"filterable": true,
+    			"sortable": true,
+    			"facetable": true
+    		},
+    		{
+    			"name": "Address",
+    			"type": "Edm.ComplexType",
+    			"fields": [
+    				{
+    					"name": "StreetAddress",
+    					"type": "Edm.String",
+    					"filterable": false,
+    					"sortable": false,
+    					"facetable": false,
+    					"searchable": true
+    				},
+    				{
+    					"name": "City",
+    					"type": "Edm.String",
+    					"searchable": true,
+    					"filterable": true,
+    					"sortable": true,
+    					"facetable": true
+    				},
+    				{
+    					"name": "StateProvince",
+    					"type": "Edm.String",
+    					"searchable": true,
+    					"filterable": true,
+    					"sortable": true,
+    					"facetable": true
+    				},
+    				{
+    					"name": "PostalCode",
+    					"type": "Edm.String",
+    					"searchable": true,
+    					"filterable": true,
+    					"sortable": true,
+    					"facetable": true
+    				},
+    				{
+    					"name": "Country",
+    					"type": "Edm.String",
+    					"searchable": true,
+    					"filterable": true,
+    					"sortable": true,
+    					"facetable": true
+    				}
+    			]
+    		}
+    	],
+    	"suggesters": [
+    		{
+    			"name": "sg",
+    			"searchMode": "analyzingInfixMatching",
+    			"sourceFields": [
+    				"HotelName"
+    			]
+    		}
+    	]
+    }
+    ```
 
-With that in place, we're ready to create an index.
-
-## Create index 
-
-Create a file *hotels_quickstart_index.json*. This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
-
-Add the following content to *hotels_quickstart_index.json* or [download the file](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels_quickstart_index.json). 
-
-```json
-{
-    "name": "hotels-quickstart",
-    "fields": [
-        {
-            "name": "HotelId",
-            "type": "Edm.String",
-            "key": true,
-            "filterable": true
-        },
-        {
-            "name": "HotelName",
-            "type": "Edm.String",
-            "searchable": true,
-            "filterable": false,
-            "sortable": true,
-            "facetable": false
-        },
-        {
-            "name": "Description",
-            "type": "Edm.String",
-            "searchable": true,
-            "filterable": false,
-            "sortable": false,
-            "facetable": false,
-            "analyzerName": "en.lucene"
-        },
-        {
-            "name": "Description_fr",
-            "type": "Edm.String",
-            "searchable": true,
-            "filterable": false,
-            "sortable": false,
-            "facetable": false,
-            "analyzerName": "fr.lucene"
-        },
-        {
-            "name": "Category",
-            "type": "Edm.String",
-            "searchable": true,
-            "filterable": true,
-            "sortable": true,
-            "facetable": true
-        },
-        {
-            "name": "Tags",
-            "type": "Collection(Edm.String)",
-            "searchable": true,
-            "filterable": true,
-            "sortable": false,
-            "facetable": true
-        },
-        {
-            "name": "ParkingIncluded",
-            "type": "Edm.Boolean",
-            "filterable": true,
-            "sortable": true,
-            "facetable": true
-        },
-        {
-            "name": "LastRenovationDate",
-            "type": "Edm.DateTimeOffset",
-            "filterable": true,
-            "sortable": true,
-            "facetable": true
-        },
-        {
-            "name": "Rating",
-            "type": "Edm.Double",
-            "filterable": true,
-            "sortable": true,
-            "facetable": true
-        },
-        {
-            "name": "Address",
-            "type": "Edm.ComplexType",
-            "fields": [
-                {
-                    "name": "StreetAddress",
-                    "type": "Edm.String",
-                    "filterable": false,
-                    "sortable": false,
-                    "facetable": false,
-                    "searchable": true
-                },
-                {
-                    "name": "City",
-                    "type": "Edm.String",
-                    "searchable": true,
-                    "filterable": true,
-                    "sortable": true,
-                    "facetable": true
-                },
-                {
-                    "name": "StateProvince",
-                    "type": "Edm.String",
-                    "searchable": true,
-                    "filterable": true,
-                    "sortable": true,
-                    "facetable": true
-                },
-                {
-                    "name": "PostalCode",
-                    "type": "Edm.String",
-                    "searchable": true,
-                    "filterable": true,
-                    "sortable": true,
-                    "facetable": true
-                },
-                {
-                    "name": "Country",
-                    "type": "Edm.String",
-                    "searchable": true,
-                    "filterable": true,
-                    "sortable": true,
-                    "facetable": true
-                }
-            ]
-        }
-    ],
-    "suggesters": [
-        {
-            "name": "sg",
-            "searchMode": "analyzingInfixMatching",
-            "sourceFields": [
-                "HotelName"
-            ]
-        }
-    ]
-}
-```
+1. Sign in to Azure with the following command:
+
+    ```shell
+    az login
+    ```
+
+1. Run the JavaScript code with the following command:
+
+    ```shell
+    node index.js
+    ```
+
+## Explaining the code
+
+### Create index
+
+The *hotels_quickstart_index.json* file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
 
 With our index definition in place, we want to import *hotels_quickstart_index.json* at the top of *index.js* so the main function can access the index definition.
 
@@ -325,106 +591,11 @@ let index = await indexClient.createIndex(indexDefinition);
 console.log(`Index named ${index.name} has been created.`);
 ```
 
-## Run the sample
-
-At this point, you're ready to run the sample. Use a terminal window to run the following command:
-
-```cmd
-node index.js
-```
-
-If you [downloaded the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) and haven't installed the required packages yet, run `npm install` first.
-
-You should see a series of messages describing the actions being taken by the program. 
-
-Open the **Overview** of your search service in the Azure portal. Select the **Indexes** tab. You should see something like the following example:
-
-:::image type="content" source="../../media/search-get-started-javascript/create-index-no-data.png" alt-text="Screenshot of Azure portal, search service Overview, Indexes tab." border="false":::
-
-In the next step, you'll add data to index. 
-
-## Load documents 
+### Load documents 
 
 In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programatically push the documents to the index.
 
-Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. You can either download [hotels.json](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels.json) or create your own *hotels.json* file with the following content:
-
-```json
-{
-    "value": [
-        {
-            "HotelId": "1",
-            "HotelName": "Stay-Kay City Hotel",
-            "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-            "Description_fr": "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.",
-            "Category": "Boutique",
-            "Tags": ["pool", "air conditioning", "concierge"],
-            "ParkingIncluded": false,
-            "LastRenovationDate": "1970-01-18T00:00:00Z",
-            "Rating": 3.6,
-            "Address": {
-                "StreetAddress": "677 5th Ave",
-                "City": "New York",
-                "StateProvince": "NY",
-                "PostalCode": "10022"
-            }
-        },
-        {
-            "HotelId": "2",
-            "HotelName": "Old Century Hotel",
-            "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
-            "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
-            "Category": "Boutique",
-            "Tags": ["pool", "free wifi", "concierge"],
-            "ParkingIncluded": "false",
-            "LastRenovationDate": "1979-02-18T00:00:00Z",
-            "Rating": 3.6,
-            "Address": {
-                "StreetAddress": "140 University Town Center Dr",
-                "City": "Sarasota",
-                "StateProvince": "FL",
-                "PostalCode": "34243"
-            }
-        },
-        {
-            "HotelId": "3",
-            "HotelName": "Gastronomic Landscape Hotel",
-            "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-            "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
-            "Category": "Resort and Spa",
-            "Tags": ["air conditioning", "bar", "continental breakfast"],
-            "ParkingIncluded": "true",
-            "LastRenovationDate": "2015-09-20T00:00:00Z",
-            "Rating": 4.8,
-            "Address": {
-                "StreetAddress": "3393 Peachtree Rd",
-                "City": "Atlanta",
-                "StateProvince": "GA",
-                "PostalCode": "30326"
-            }
-        },
-        {
-            "HotelId": "4",
-            "HotelName": "Sublime Palace Hotel",
-            "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
-            "Description_fr": "Le Sublime Palace Hotel est situé au coeur du centre historique de sublime dans un quartier extrêmement animé et vivant, à courte distance de marche des sites et monuments de la ville et est entouré par l'extraordinaire beauté des églises, des bâtiments, des commerces et Monuments. Sublime Palace fait partie d'un Palace 1800 restauré avec amour.",
-            "Category": "Boutique",
-            "Tags": ["concierge", "view", "24-hour front desk service"],
-            "ParkingIncluded": true,
-            "LastRenovationDate": "1960-02-06T00:00:00Z",
-            "Rating": 4.6,
-            "Address": {
-                "StreetAddress": "7400 San Pedro Ave",
-                "City": "San Antonio",
-                "StateProvince": "TX",
-                "PostalCode": "78216"
-            }
-        }
-    ]
-}
-```
-
-Similar to what we did with the `indexDefinition`, we also need to import `hotels.json` at the top of *index.js* so that the data can be accessed in our main function.
+Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. Similar to what we did with the `indexDefinition`, we also need to import `hotels.json` at the top of *index.js* so that the data can be accessed in our main function.
 
 ```javascript
 const hotelData = require('./hotels.json');
@@ -453,27 +624,7 @@ let indexDocumentsResult = await searchClient.mergeOrUploadDocuments(hotelData['
 console.log(`Index operations succeeded: ${JSON.stringify(indexDocumentsResult.results[0].succeeded)}`);
 ```
 
-Run the program again with `node index.js`. You should see a slightly different set of messages from those you saw in Step 1. This time, the index *does* exist, and you should see a message about deleting it before the app creates the new index and posts data to it. 
-
-Before we run the queries in the next step, define a function to have the program wait for one second. This is done just for test/demo purposes to ensure the indexing finishes and that the documents are available in the index for our queries.
-
-```javascript
-function sleep(ms) {
-    var d = new Date();
-    var d2 = null;
-    do {
-        d2 = new Date();
-    } while (d2 - d < ms);
-}
-```
-
-To have the program wait for one second, call the `sleep` function like below:
-
-```javascript
-sleep(1000);
-```
-
-## Search an index
+### Search an index
 
 With an index created and documents uploaded, you're ready to send queries to the index. In this section, we send five different queries to the search index to demonstrate different pieces of query functionality available to you.
 
@@ -485,6 +636,8 @@ await sendQueries(searchClient);
 
 Queries are sent using the `search()` method of `searchClient`. The first parameter is the search text and the second parameter specifies search options.
 
+#### Query example 1
+
 The first query searches `*`, which is equivalent to searching everything and selects three of the fields in the index. It's a best practice to only `select` the fields you need because pulling back unnecessary data can add latency to your queries.
 
 The `searchOptions` for this query also has `includeTotalCount` set to `true`, which returns the number of matching results found.
@@ -509,6 +662,8 @@ async function sendQueries(searchClient) {
 
 The remaining queries outlined below should also be added to the `sendQueries()` function. They're separated here for readability.
 
+#### Query example 2
+
 In the next query, we specify the search term `"wifi"` and also include a filter to only return results where the state is equal to `'FL'`. Results are also ordered by the Hotel's `Rating`.
 
 ```javascript
@@ -526,6 +681,8 @@ for await (const result of searchResults.results) {
 }
 ```
 
+#### Query example 3
+
 Next, the search is limited to a single searchable field using the `searchFields` parameter. This approach is a great option to make your query more efficient if you know you're only interested in matches in certain fields. 
 
 ```javascript
@@ -542,6 +699,9 @@ for await (const result of searchResults.results) {
 console.log();
 ```
 
+
+#### Query example 4
+
 Another common option to include in a query is `facets`. Facets allow you to build out filters on your UI to make it easy for users to know what values they can filter down to.
 
 ```javascript
@@ -558,6 +718,8 @@ for await (const result of searchResults.results) {
 }
 ```
 
+#### Query example 5
+
 The final query uses the `getDocument()` method of the `searchClient`. This allows you to efficiently retrieve a document by its key. 
 
 ```javascript
@@ -566,6 +728,8 @@ let documentResult = await searchClient.getDocument(key='3')
 console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.HotelName}`)
 ```
 
-## Run the sample again
+#### Summary of queries
+
+The previous queries show multiple ways of matching terms in a query: full-text search, filters, and autocomplete.
 
-Run the program by using `node index.js`. Now, in addition to the previous steps, the queries are sent and the results written to the console.
+Full text search and filters are performed using the `searchClient.search` method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the `filter` property of the `SearchOptions` class. To filter without searching, just pass "*" for the `searchText` parameter of the `search` method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "JavaScriptによるフルテキスト検索クイックスタートの大幅更新"
}
```

### Explanation
この変更は、JavaScriptによるフルテキスト検索のクイックスタートガイドに対する大規模な更新を含んでいます。主な変更点は以下の通りです：

1. **文書の日時の更新**: 更新日時が「2025年2月12日」から「2025年2月19日」に変更されています。

2. **内容の大幅な追加と削除**: 追加された行が505行、削除された行が341行、合計846行の内容が変更されました。このため、文書の構造や流れが大きく見直されています。

3. **リアルタイムな手順とコードの変更**: 環境のセットアップ手順が新しくなり、URLリンクやコマンドが最新の情報に更新されています。また、推奨される認証方法についての情報が明確にされ、Microsoft Entra IDを使用したキーレス認証に重点が置かれています。

4. **サンプルコードの改善**: サンプルコードが改訂され、ユーザーが特定の手順と結果を追いやすくするための詳細で包括的な説明も強調されています。特に、コードの自動化、エラーハンドリング、データのインデックス作成およびクエリ実行の方法が改善されています。

これによって、利用者はAzure AI Searchをより効果的に使用できるようになり、ドキュメントが与える指導と手順が最新の標準と一致することが保証されます。

## articles/search/includes/quickstarts/full-text-typescript.md{#item-6630e8}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ author: eric-urban
 ms.author: eur
 ms.service: azure-ai-search
 ms.topic: include
-ms.date: 2/12/2025
+ms.date: 2/19/2025
 ---
 
 [!INCLUDE [Full text introduction](full-text-intro.md)]
@@ -27,276 +27,456 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
-## Set up your environment
+## Set up
 
-We used the following tools to create this quickstart.
+1. Create a new folder `full-text-quickstart` to contain the application and open Visual Studio Code in that folder with the following command:
 
-+ [Visual Studio Code](https://code.visualstudio.com), which has built-in support for creating JavaScript apps
-
-+ [Node.js LTS](https://nodejs.org) and [npm](https://www.npmjs.com)
-
-* [TypeScript](https://www.typescriptlang.org/download/)
-
-## Create the project
-
-1. Start Visual Studio Code.
-
-1. Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) by using **Ctrl+Shift+P** and open the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal).
+    ```shell
+    mkdir full-text-quickstart && code full-text-quickstart
+    ```
 
-1. Create a development directory, giving it the name *quickstart*:
+1. Create the `package.json` with the following command:
 
-    ```cmd
-    mkdir quickstart
-    cd quickstart
+    ```shell
+    npm init -y
     ```
 
-1. Initialize an empty project with npm by running the following command. To fully initialize the project, press Enter multiple times to accept the default values, except for the License, which you should set to *MIT*. 
+1. Update the `package.json` to ECMAScript with the following command: 
 
-    ```cmd
-    npm init
+    ```shell
+    npm pkg set type=module
     ```
 
-1. Install `@azure/search-documents`, the [JavaScript/TypeScript SDK for Azure AI Search](/javascript/api/overview/azure/search-documents-readme). 
+1. Install the Azure AI Search client library ([Azure.Search.Documents](/javascript/api/overview/azure/search-documents-readme)) for JavaScript with:
 
-    ```cmd
+    ```console
     npm install @azure/search-documents
     ```
 
-1. Install `dotenv`, which is used to import the environment variables such as your search service name and API key.
+1. For the **recommended** passwordless authentication, install the Azure Identity client library with:
 
-    ```cmd
-    npm install dotenv
+    ```console
+    npm install @azure/identity
     ```
 
-1. Navigate to the *quickstart* directory, then confirm that you've configured the project and its dependencies by checking that your *package.json* file looks similar to the following json:
 
-    ```json
-    {
-      "name": "quickstart",
-      "version": "1.0.0",
-      "description": "Azure AI Search Quickstart",
-      "main": "index.js",
-      "scripts": {
-        "test": "echo \"Error: no test specified\" && exit 1"
-      },
-      "keywords": [
-        "Azure",
-        "Search"
-      ],
-      "author": "Your Name",
-      "license": "MIT",
-      "dependencies": {
-        "@azure/search-documents": "^12.1.0",
-        "dotenv": "^16.4.5"
-      }
-    }
-    ```
+## Create, load, and query a search index
 
-1. Create a file *.env* to hold your search service parameters:
+In the prior [set up](#set-up) section, you installed the Azure AI Search client library and other dependencies. 
 
-    ```
-    SEARCH_API_KEY=<YOUR-SEARCH-ADMIN-API-KEY>
-    SEARCH_API_ENDPOINT=<YOUR-SEARCH-SERVICE-URL>
-    ```
+In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
 
-Replace the `YOUR-SEARCH-SERVICE-URL` value with the name of your search service endpoint URL. Replace `<YOUR-SEARCH-ADMIN-API-KEY>` with the admin key you recorded earlier. 
+The sample code in this quickstart uses Microsoft Entra ID for the recommended keyless authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
-## Create index.ts file
+#### [Microsoft Entra ID](#tab/keyless)
 
-Next we create an *index.ts* file, which is the main file that hosts our code.
+```javascript
+const searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+const credential = new DefaultAzureCredential();
+```
 
-At the top of this file, we import the `@azure/search-documents` library:
+#### [API key](#tab/api-key)
 
-```typescript
-import {
-    AzureKeyCredential,
-    ComplexField,
-    odata,
-    SearchClient,
-    SearchFieldArray,
-    SearchIndex,
-    SearchIndexClient,
-    SearchSuggester,
-    SimpleField
-} from "@azure/search-documents";
+```javascript
+const searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+const credential = new AzureKeyCredential(apiKey);
 ```
+---
 
-Next, we need to require the `dotenv` package to read in the parameters from the *.env* file as follows:
-
-```typescript
-// Load the .env file if it exists
-import dotenv from 'dotenv';
-dotenv.config();
+1. Create a new file named *index.ts* and paste the following code into *index.ts*:
+
+    ```typescript
+    // Import from the @azure/search-documents library
+    import {
+        SearchIndexClient,
+        SearchClient,
+        SearchFieldDataType,
+        AzureKeyCredential,
+        odata,
+        SearchIndex
+    } from "@azure/search-documents";
+    
+    // Import from the Azure Identity library
+    import { DefaultAzureCredential } from "@azure/identity";
+    
+    // Importing the hotels sample data
+    import hotelData from './hotels.json' assert { type: "json" };
+    
+    // Load the .env file if it exists
+    import * as dotenv from "dotenv";
+    dotenv.config();
+    
+    // Defining the index definition
+    const indexDefinition: SearchIndex = {
+    	"name": "hotels-quickstart",
+    	"fields": [
+    		{
+    			"name": "HotelId",
+    			"type": "Edm.String" as SearchFieldDataType,
+    			"key": true,
+    			"filterable": true
+    		},
+    		{
+    			"name": "HotelName",
+    			"type": "Edm.String" as SearchFieldDataType,
+    			"searchable": true,
+    			"filterable": false,
+    			"sortable": true,
+    			"facetable": false
+    		},
+    		{
+    			"name": "Description",
+    			"type": "Edm.String" as SearchFieldDataType,
+    			"searchable": true,
+    			"filterable": false,
+    			"sortable": false,
+    			"facetable": false,
+    			"analyzerName": "en.lucene"
+    		},
+    		{
+    			"name": "Description_fr",
+    			"type": "Edm.String" as SearchFieldDataType,
+    			"searchable": true,
+    			"filterable": false,
+    			"sortable": false,
+    			"facetable": false,
+    			"analyzerName": "fr.lucene"
+    		},
+    		{
+    			"name": "Category",
+    			"type": "Edm.String" as SearchFieldDataType,
+    			"searchable": true,
+    			"filterable": true,
+    			"sortable": true,
+    			"facetable": true
+    		},
+    		{
+    			"name": "Tags",
+    			"type": "Collection(Edm.String)",
+    			"searchable": true,
+    			"filterable": true,
+    			"sortable": false,
+    			"facetable": true
+    		},
+    		{
+    			"name": "ParkingIncluded",
+    			"type": "Edm.Boolean",
+    			"filterable": true,
+    			"sortable": true,
+    			"facetable": true
+    		},
+    		{
+    			"name": "LastRenovationDate",
+    			"type": "Edm.DateTimeOffset",
+    			"filterable": true,
+    			"sortable": true,
+    			"facetable": true
+    		},
+    		{
+    			"name": "Rating",
+    			"type": "Edm.Double",
+    			"filterable": true,
+    			"sortable": true,
+    			"facetable": true
+    		},
+    		{
+    			"name": "Address",
+    			"type": "Edm.ComplexType",
+    			"fields": [
+    				{
+    					"name": "StreetAddress",
+    					"type": "Edm.String" as SearchFieldDataType,
+    					"filterable": false,
+    					"sortable": false,
+    					"facetable": false,
+    					"searchable": true
+    				},
+    				{
+    					"name": "City",
+    					"type": "Edm.String" as SearchFieldDataType,
+    					"searchable": true,
+    					"filterable": true,
+    					"sortable": true,
+    					"facetable": true
+    				},
+    				{
+    					"name": "StateProvince",
+    					"type": "Edm.String" as SearchFieldDataType,
+    					"searchable": true,
+    					"filterable": true,
+    					"sortable": true,
+    					"facetable": true
+    				},
+    				{
+    					"name": "PostalCode",
+    					"type": "Edm.String" as SearchFieldDataType,
+    					"searchable": true,
+    					"filterable": true,
+    					"sortable": true,
+    					"facetable": true
+    				},
+    				{
+    					"name": "Country",
+    					"type": "Edm.String" as SearchFieldDataType,
+    					"searchable": true,
+    					"filterable": true,
+    					"sortable": true,
+    					"facetable": true
+    				}
+    			]
+    		}
+    	],
+    	"suggesters": [
+    		{
+    			"name": "sg",
+    			"searchMode": "analyzingInfixMatching",
+    			"sourceFields": [
+    				"HotelName"
+    			]
+    		}
+    	]
+    };
+    
+    async function main() {
+        
+    	// Your search service endpoint
+    	const searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+    	
+    	// Use the recommended keyless credential instead of the AzureKeyCredential credential.
+    	const credential = new DefaultAzureCredential();
+    	//const credential = new AzureKeyCredential(Your search service admin key);
+    	
+    	// Create a SearchIndexClient to send create/delete index commands
+    	const searchIndexClient: SearchIndexClient = new SearchIndexClient(
+    		searchServiceEndpoint,
+    		credential
+    	);
+    
+    	// Creating a search client to upload documents and issue queries
+    	const indexName: string  = "hotels-quickstart";
+        const searchClient: SearchClient<any> = searchIndexClient.getSearchClient(indexName);
+    
+        console.log('Checking if index exists...');
+        await deleteIndexIfExists(searchIndexClient, indexName);
+    
+        console.log('Creating index...');
+        let index: SearchIndex = await searchIndexClient.createIndex(indexDefinition);
+        console.log(`Index named ${index.name} has been created.`);
+    
+        console.log('Uploading documents...');
+        let indexDocumentsResult = await searchClient.mergeOrUploadDocuments(hotelData['value']);
+        console.log(`Index operations succeeded: ${JSON.stringify(indexDocumentsResult.results[0].succeeded)} `);
+    
+        // waiting one second for indexing to complete (for demo purposes only)
+        sleep(1000);
+    
+        console.log('Querying the index...');
+        console.log();
+        await sendQueries(searchClient);
+    }
+    
+    async function deleteIndexIfExists(searchIndexClient: SearchIndexClient, indexName: string) {
+        try {
+            await searchIndexClient.deleteIndex(indexName);
+            console.log('Deleting index...');
+        } catch {
+            console.log('Index does not exist yet.');
+        }
+    }
+    
+    async function sendQueries(searchClient: SearchClient<any>) {
+        // Query 1
+        console.log('Query #1 - search everything:');
+        let searchOptions: any = {
+            includeTotalCount: true,
+            select: ["HotelId", "HotelName", "Rating"]
+        };
+    
+        let searchResults = await searchClient.search("*", searchOptions);
+        for await (const result of searchResults.results) {
+            console.log(`${JSON.stringify(result.document)}`);
+        }
+        console.log(`Result count: ${searchResults.count}`);
+        console.log();
+    
+    
+        // Query 2
+        console.log('Query #2 - search with filter, orderBy, and select:');
+        let state = 'FL';
+        searchOptions = {
+            filter: odata`Address/StateProvince eq ${state}`,
+            orderBy: ["Rating desc"],
+            select: ["HotelId", "HotelName", "Rating"]
+        };
+    
+        searchResults = await searchClient.search("wifi", searchOptions);
+        for await (const result of searchResults.results) {
+            console.log(`${JSON.stringify(result.document)}`);
+        }
+        console.log();
+    
+        // Query 3
+        console.log('Query #3 - limit searchFields:');
+        searchOptions = {
+            select: ["HotelId", "HotelName", "Rating"],
+            searchFields: ["HotelName"]
+        };
+    
+        searchResults = await searchClient.search("sublime cliff", searchOptions);
+        for await (const result of searchResults.results) {
+            console.log(`${JSON.stringify(result.document)}`);
+        }
+        console.log();
+    
+        // Query 4
+        console.log('Query #4 - limit searchFields and use facets:');
+        searchOptions = {
+            facets: ["Category"],
+            select: ["HotelId", "HotelName", "Rating"],
+            searchFields: ["HotelName"]
+        };
+    
+        searchResults = await searchClient.search("*", searchOptions);
+        for await (const result of searchResults.results) {
+            console.log(`${JSON.stringify(result.document)}`);
+        }
+        console.log();
+    
+        // Query 5
+        console.log('Query #5 - Lookup document:');
+        let documentResult = await searchClient.getDocument('3');
+        console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.HotelName}`);
+        console.log();
+    }
+    
+    function sleep(ms: number) {
+        return new Promise(resolve => setTimeout(resolve, ms));
+    }
+    
+    main().catch((err) => {
+        console.error("The sample encountered an error:", err);
+    });
+    ```
 
-// Getting endpoint and apiKey from .env file
-const endpoint = process.env.SEARCH_API_ENDPOINT || "";
-const apiKey = process.env.SEARCH_API_KEY || "";
-```
+1. Create a file named *hotels.json* and paste the following code into *hotels.json*:
 
-With our imports and environment variables in place, we're ready to define the main function.
+    ```json
+    {
+        "value": [
+            {
+                "HotelId": "1",
+                "HotelName": "Secret Point Motel",
+                "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
+                "Description_fr": "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.",
+                "Category": "Boutique",
+                "Tags": ["pool", "air conditioning", "concierge"],
+                "ParkingIncluded": false,
+                "LastRenovationDate": "1970-01-18T00:00:00Z",
+                "Rating": 3.6,
+                "Address": {
+                    "StreetAddress": "677 5th Ave",
+                    "City": "New York",
+                    "StateProvince": "NY",
+                    "PostalCode": "10022"
+                }
+            },
+            {
+                "HotelId": "2",
+                "HotelName": "Twin Dome Motel",
+                "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
+                "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
+                "Category": "Boutique",
+                "Tags": ["pool", "free wifi", "concierge"],
+                "ParkingIncluded": "false",
+                "LastRenovationDate": "1979-02-18T00:00:00Z",
+                "Rating": 3.6,
+                "Address": {
+                    "StreetAddress": "140 University Town Center Dr",
+                    "City": "Sarasota",
+                    "StateProvince": "FL",
+                    "PostalCode": "34243"
+                }
+            },
+            {
+                "HotelId": "3",
+                "HotelName": "Triple Landscape Hotel",
+                "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
+                "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
+                "Category": "Resort and Spa",
+                "Tags": ["air conditioning", "bar", "continental breakfast"],
+                "ParkingIncluded": "true",
+                "LastRenovationDate": "2015-09-20T00:00:00Z",
+                "Rating": 4.8,
+                "Address": {
+                    "StreetAddress": "3393 Peachtree Rd",
+                    "City": "Atlanta",
+                    "StateProvince": "GA",
+                    "PostalCode": "30326"
+                }
+            },
+            {
+                "HotelId": "4",
+                "HotelName": "Sublime Cliff Hotel",
+                "Description": "Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 1800 palace.",
+                "Description_fr": "Le sublime Cliff Hotel est situé au coeur du centre historique de sublime dans un quartier extrêmement animé et vivant, à courte distance de marche des sites et monuments de la ville et est entouré par l'extraordinaire beauté des églises, des bâtiments, des commerces et Monuments. Sublime Cliff fait partie d'un Palace 1800 restauré avec amour.",
+                "Category": "Boutique",
+                "Tags": ["concierge", "view", "24-hour front desk service"],
+                "ParkingIncluded": true,
+                "LastRenovationDate": "1960-02-06T00:00:00Z",
+                "Rating": 4.6,
+                "Address": {
+                    "StreetAddress": "7400 San Pedro Ave",
+                    "City": "San Antonio",
+                    "StateProvince": "TX",
+                    "PostalCode": "78216"
+                }
+            }
+        ]
+    }
+    ```
 
-Most of the functionality in the SDK is asynchronous so we make our main function `async`. We also include a `main().catch()` below the main function to catch and log any errors encountered:
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
 
-```typescript
-async function main() {
-    console.log(`Running Azure AI Search JavaScript quickstart...`);
-    if (!endpoint || !apiKey) {
-        console.log("Make sure to set valid values for endpoint and apiKey with proper authorization.");
-        return;
+    ```json
+    {
+        "compilerOptions": {
+          "module": "NodeNext",
+          "target": "ES2022", // Supports top-level await
+          "moduleResolution": "NodeNext",
+          "skipLibCheck": true, // Avoid type errors from node_modules
+          "strict": true // Enable strict type-checking options
+        },
+        "include": ["*.ts"]
     }
+    ```
 
-    // remaining quickstart code will go here
-}
+1. Transpile from TypeScript to JavaScript.
 
-main().catch((err) => {
-    console.error("The sample encountered an error:", err);
-});
-```
+    ```shell
+    tsc
+    ```
+    
+1. Sign in to Azure with the following command:
 
-With that in place, we're ready to create an index.
+    ```shell
+    az login
+    ```
 
-## Create index
+1. Run the JavaScript code with the following command:
 
-Create a file *hotels_quickstart_index.json*. This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
+    ```shell
+    node index.js
+    ```
 
-Add the following content to *hotels_quickstart_index.json* or [download the file](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels_quickstart_index.json).
-
-```json
-{
-    "name": "hotels-quickstart",
-    "fields": [
-        {
-            "name": "HotelId",
-            "type": "Edm.String",
-            "key": true,
-            "filterable": true
-        },
-        {
-            "name": "HotelName",
-            "type": "Edm.String",
-            "searchable": true,
-            "filterable": false,
-            "sortable": true,
-            "facetable": false
-        },
-        {
-            "name": "Description",
-            "type": "Edm.String",
-            "searchable": true,
-            "filterable": false,
-            "sortable": false,
-            "facetable": false,
-            "analyzerName": "en.lucene"
-        },
-        {
-            "name": "Description_fr",
-            "type": "Edm.String",
-            "searchable": true,
-            "filterable": false,
-            "sortable": false,
-            "facetable": false,
-            "analyzerName": "fr.lucene"
-        },
-        {
-            "name": "Category",
-            "type": "Edm.String",
-            "searchable": true,
-            "filterable": true,
-            "sortable": true,
-            "facetable": true
-        },
-        {
-            "name": "Tags",
-            "type": "Collection(Edm.String)",
-            "searchable": true,
-            "filterable": true,
-            "sortable": false,
-            "facetable": true
-        },
-        {
-            "name": "ParkingIncluded",
-            "type": "Edm.Boolean",
-            "filterable": true,
-            "sortable": true,
-            "facetable": true
-        },
-        {
-            "name": "LastRenovationDate",
-            "type": "Edm.DateTimeOffset",
-            "filterable": true,
-            "sortable": true,
-            "facetable": true
-        },
-        {
-            "name": "Rating",
-            "type": "Edm.Double",
-            "filterable": true,
-            "sortable": true,
-            "facetable": true
-        },
-        {
-            "name": "Address",
-            "type": "Edm.ComplexType",
-            "fields": [
-                {
-                    "name": "StreetAddress",
-                    "type": "Edm.String",
-                    "filterable": false,
-                    "sortable": false,
-                    "facetable": false,
-                    "searchable": true
-                },
-                {
-                    "name": "City",
-                    "type": "Edm.String",
-                    "searchable": true,
-                    "filterable": true,
-                    "sortable": true,
-                    "facetable": true
-                },
-                {
-                    "name": "StateProvince",
-                    "type": "Edm.String",
-                    "searchable": true,
-                    "filterable": true,
-                    "sortable": true,
-                    "facetable": true
-                },
-                {
-                    "name": "PostalCode",
-                    "type": "Edm.String",
-                    "searchable": true,
-                    "filterable": true,
-                    "sortable": true,
-                    "facetable": true
-                },
-                {
-                    "name": "Country",
-                    "type": "Edm.String",
-                    "searchable": true,
-                    "filterable": true,
-                    "sortable": true,
-                    "facetable": true
-                }
-            ]
-        }
-    ],
-    "suggesters": [
-        {
-            "name": "sg",
-            "searchMode": "analyzingInfixMatching",
-            "sourceFields": [
-                "HotelName"
-            ]
-        }
-    ]
-}
-```
+## Explaining the code
 
-With our index definition in place, we want to import *hotels_quickstart_index.json* at the top of *index.ts* so the main function can access the index definition.
+### Create index
+
+Create a file *hotels_quickstart_index.json*. This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
+
+We want to import *hotels_quickstart_index.json* so the main function can access the index definition.
 
 ```typescript
-// Importing the index definition and sample data
 import indexDefinition from './hotels_quickstart_index.json';
 
 interface HotelIndexDefinition {
@@ -345,107 +525,14 @@ console.log('Creating index...');
 let index = await indexClient.createIndex(hotelIndexDefinition);
 
 console.log(`Index named ${index.name} has been created.`);
-```
-
-## Run the sample
+``` 
 
-At this point, you're ready to build and run the sample. Use a terminal window to run the following commands to build your source with `tsc` then run your source with `node`:
-
-```cmd
-tsc
-node index.ts
-```
-
-If you [downloaded the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) and haven't installed the required packages yet, run `npm install` first.
-
-You should see a series of messages describing the actions being taken by the program. 
-
-Open the **Overview** of your search service in the Azure portal. Select the **Indexes** tab. You should see something like the following example:
-
-:::image type="content" source="../../media/search-get-started-javascript/create-index-no-data.png" alt-text="Screenshot of Azure portal, search service Overview, Indexes tab." border="false":::
-
-In the next step, you'll add data to index. 
-
-## Load documents 
+### Load documents 
 
 In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programatically push the documents to the index.
 
 Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. You can either download [hotels.json](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels.json) or create your own *hotels.json* file with the following content:
 
-```json
-{
-    "value": [
-        {
-            "HotelId": "1",
-            "HotelName": "Stay-Kay City Hotel",
-            "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
-            "Description_fr": "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.",
-            "Category": "Boutique",
-            "Tags": ["pool", "air conditioning", "concierge"],
-            "ParkingIncluded": false,
-            "LastRenovationDate": "1970-01-18T00:00:00Z",
-            "Rating": 3.6,
-            "Address": {
-                "StreetAddress": "677 5th Ave",
-                "City": "New York",
-                "StateProvince": "NY",
-                "PostalCode": "10022"
-            }
-        },
-        {
-            "HotelId": "2",
-            "HotelName": "Old Century Hotel",
-            "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
-            "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
-            "Category": "Boutique",
-            "Tags": ["pool", "free wifi", "concierge"],
-            "ParkingIncluded": "false",
-            "LastRenovationDate": "1979-02-18T00:00:00Z",
-            "Rating": 3.6,
-            "Address": {
-                "StreetAddress": "140 University Town Center Dr",
-                "City": "Sarasota",
-                "StateProvince": "FL",
-                "PostalCode": "34243"
-            }
-        },
-        {
-            "HotelId": "3",
-            "HotelName": "Gastronomic Landscape Hotel",
-            "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.",
-            "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
-            "Category": "Resort and Spa",
-            "Tags": ["air conditioning", "bar", "continental breakfast"],
-            "ParkingIncluded": "true",
-            "LastRenovationDate": "2015-09-20T00:00:00Z",
-            "Rating": 4.8,
-            "Address": {
-                "StreetAddress": "3393 Peachtree Rd",
-                "City": "Atlanta",
-                "StateProvince": "GA",
-                "PostalCode": "30326"
-            }
-        },
-        {
-            "HotelId": "4",
-            "HotelName": "Sublime Palace Hotel",
-            "Description": "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.",
-            "Description_fr": "Le Sublime Palace Hotel est situé au coeur du centre historique de sublime dans un quartier extrêmement animé et vivant, à courte distance de marche des sites et monuments de la ville et est entouré par l'extraordinaire beauté des églises, des bâtiments, des commerces et Monuments. Sublime Palace fait partie d'un Palace 1800 restauré avec amour.",
-            "Category": "Boutique",
-            "Tags": ["concierge", "view", "24-hour front desk service"],
-            "ParkingIncluded": true,
-            "LastRenovationDate": "1960-02-06T00:00:00Z",
-            "Rating": 4.6,
-            "Address": {
-                "StreetAddress": "7400 San Pedro Ave",
-                "City": "San Antonio",
-                "StateProvince": "TX",
-                "PostalCode": "78216"
-            }
-        }
-    ]
-}
-```
 
 Similar to what we did with the indexDefinition, we also need to import `hotels.json` at the top of *index.ts* so that the data can be accessed in our main function.
 
@@ -512,7 +599,7 @@ To have the program wait for one second, call the `sleep` function:
 sleep(1000);
 ```
 
-## Search an index
+### Search an index
 
 With an index created and documents uploaded, you're ready to send queries to the index. In this section, we send five different queries to the search index to demonstrate different pieces of query functionality available to you.
 
@@ -524,6 +611,8 @@ await sendQueries(searchClient);
 
 Queries are sent using the `search()` method of `searchClient`. The first parameter is the search text and the second parameter specifies search options.
 
+#### Query example 1
+
 The first query searches `*`, which is equivalent to searching everything and selects three of the fields in the index. It's a best practice to only `select` the fields you need because pulling back unnecessary data can add latency to your queries.
 
 The `searchOptions` for this query also has `includeTotalCount` set to `true`, which will return the number of matching results found.
@@ -557,6 +646,8 @@ async function sendQueries(
 
 The remaining queries outlined below should also be added to the `sendQueries()` function. They're separated here for readability.
 
+#### Query example 2
+
 In the next query, we specify the search term `"wifi"` and also include a filter to only return results where the state is equal to `'FL'`. Results are also ordered by the Hotel's `Rating`.
 
 ```typescript
@@ -573,6 +664,8 @@ for await (const result of searchResults.results) {
 }
 ```
 
+#### Query example 3
+
 Next, the search is limited to a single searchable field using the `searchFields` parameter. This approach is a great option to make your query more efficient if you know you're only interested in matches in certain fields. 
 
 ```typescript
@@ -588,6 +681,8 @@ for await (const result of searchResults.results) {
 }
 ```
 
+#### Query example 4
+
 Another common option to include in a query is `facets`. Facets allow you to provide self-directed drilldown from the results in your UI. The facets results can be turned into checkboxes in the result pane. 
 
 ```typescript
@@ -604,6 +699,8 @@ for await (const result of searchResults.results) {
 }
 ```
 
+#### Query example 5
+
 The final query uses the `getDocument()` method of the `searchClient`. This allows you to efficiently retrieve a document by its key. 
 
 ```typescript
@@ -612,6 +709,8 @@ let documentResult = await searchClient.getDocument('3')
 console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.HotelName}`)
 ```
 
-## Rerun the sample
+#### Summary of queries
+
+The previous queries show multiple ways of matching terms in a query: full-text search, filters, and autocomplete.
 
-Build and run the program with `tsc && node index.ts`. Now, in addition to the previous steps, the queries are sent and the results written to the console.
+Full text search and filters are performed using the `searchClient.search` method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the `filter` property of the `SearchOptions` class. To filter without searching, just pass "*" for the `searchText` parameter of the `search` method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "TypeScriptによるフルテキスト検索クイックスタートの大幅更新"
}
```

### Explanation
この変更は、TypeScriptによるフルテキスト検索のクイックスタートガイドに対する大規模な更新を含んでいます。主な変更点は以下の通りです：

1. **文書の日時の更新**: 更新日時が「2025年2月12日」から「2025年2月19日」に変更されています。

2. **環境設定手順の再構成**: 環境をセットアップする手順が見直され、より詳細なコマンドと説明が追加されました。新しくプロジェクトの作成や依存関係のインストール手順が具体的に記述されています。

3. **最新版のパッケージと推奨アプローチの導入**: 新たにAzure Identityクライアントライブラリのインストール手順が追加され、キーレス認証の使用が強調されています。

4. **主要コードの変更**: コード内のインポート構文やクライアントの設定方法が更新され、最新のベストプラクティスに従った修正が施されています。また、新たに`hotels.json`ファイルのデータ構造が詳述され、クエリの実行例も増えています。

5. **エラーハンドリングと非同期処理の改善**: 非同期関数の構造が洗練され、エラーハンドリングやデータ取得の効率が向上しています。クエリの実行に関する詳細な説明が追加され、ユーザーがいくつかの異なる方法でデータにアクセスできるようになっています。

これにより、読者はTypeScriptを使用したAzure AI Searchの実装について、より深い理解を得て、実際のアプリケーションで効果的に活用できるように設計されています。

## articles/search/media/search-get-started-javascript/create-index-no-data.png{#item-72216f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "不要な画像ファイルの削除"
}
```

### Explanation
この変更は、`create-index-no-data.png`という画像ファイルの削除を示しています。この画像ファイルは、JavaScriptによるAzure AI Searchのクイックスタートにおいて、インデックスがデータなしで作成される状況を示していた可能性があります。

削除されたことにより、ドキュメントやガイドの内容がより明確になり、他の関連するビジュアルコンテンツが強調されるか、あるいはその画像に代わる他の情報が提供されることが期待されます。この変更は、コンテンツの整理や更新の一環として、よりユーザー体験を向上させるためのものであると考えられます。

## articles/search/media/search-get-started-javascript/service-name-and-keys.png{#item-1a7e47}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス名とキーに関する画像の削除"
}
```

### Explanation
この変更では、`service-name-and-keys.png`という画像ファイルが削除されています。この画像は、JavaScriptにおけるAzure AI Searchの設定で使用されるサービス名やキーの情報を視覚的に示していたと推測されます。

この削除により、ドキュメント内での情報の整理や更新が進められていることが考えられます。具体的には、関連する情報が他の方法で提示されているか、もしくはその画像が不要と判断されたため、コンテンツのクオリティや一貫性を向上させる目的があると思われます。この変更は、ユーザーにとってより明確で簡潔な情報提供を促進するためのものでしょう。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.custom:
   - ignite-2023
 ms.topic: quickstart
 zone_pivot_groups: search-quickstart-full-text
-ms.date: 2/12/2025
+ms.date: 2/19/2025
 ---
 
 # Quickstart: Full text search using the Azure SDKs
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、`search-get-started-text.md`ファイルの内容に対する修正を示しています。具体的には、`ms.date`（最終更新日）の値が`2/12/2025`から`2/19/2025`に変更されています。

このような日付の更新は、ドキュメントの最新性を保持し、ユーザーに正確な情報を提供するために重要です。変更された日付は、コンテンツが最近更新されたことを示し、利用者にとって信頼性のあるリソースとなる助けになります。この修正は、全体的なコンテンツ管理や情報の鮮度を維持するために行われたものです。

## articles/search/search-howto-index-encrypted-blobs.md{#item-a7097a}

<details>
<summary>Diff</summary>
````diff
@@ -101,8 +101,6 @@ You should have an Azure Function app that contains the decryption logic and an
 
 2. In **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
 
-   ![Get the service name and admin and query keys](media/search-get-started-javascript/service-name-and-keys.png)
-
 All requests require an api-key in the header of every request sent to your service. A valid key establishes trust, on a per request basis, between the application sending the request and the service that handles it.
 
 ## Set up a REST client
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像と不必要な文字列の削除"
}
```

### Explanation
この変更は、`search-howto-index-encrypted-blobs.md`ファイルの修正を示しており、特に2行の削除が行われています。削除された部分には、サービス名や管理キーを取得するための手順を示す画像の参照文と、その直後に続く文章が含まれています。

具体的には、次のような内容が削除されました：
- 画像の挿入を提案するテキスト
- その画像の詳細説明的な文

この修正の意図は、文書の洗練や冗長性の削減にあると考えられます。不必要なコンテンツを排除することにより、読みやすさや情報の一貫性が向上したと推測されます。また、ドキュメントの内容がより明確になることで、ユーザーは必要な情報に迅速にアクセスできるようになります。

## articles/search/tutorial-multiple-data-sources.md{#item-71558f}

<details>
<summary>Diff</summary>
````diff
@@ -109,8 +109,6 @@ To authenticate to your search service, you'll need the service URL and an acces
 
 1. In **Settings** > **Keys**, get an admin key for full rights on the service. There are two interchangeable admin keys, provided for business continuity in case you need to roll one over. You can use either the primary or secondary key on requests for adding, modifying, and deleting objects.
 
-   :::image type="content" source="media/search-get-started-javascript/service-name-and-keys.png" alt-text="Get the service name and admin and query keys" border="false":::
-
 Having a valid key establishes trust, on a per request basis, between the application sending the request and the service that handles it.
 
 ## 2 - Set up your environment
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像の削除"
}
```

### Explanation
この変更は、`tutorial-multiple-data-sources.md`ファイルに対する修正を示しており、特に2行の削除が行われています。削除された部分には、サービス名や管理キーを取得するための手順を視覚的に示すための画像に関する記述が含まれています。

具体的には、画像の挿入を提案するテキストが削除されました。この修正は、ドキュメントの内容を簡潔にし、冗長性を低減することを目的としています。画像がなくても情報が理解できる場合には、テキストの明確さを保ちながら、視覚情報を省くことで読み手の集中を助けるための変更と言えます。結果として、ユーザーは必要な情報により焦点を当てられるようになります。


