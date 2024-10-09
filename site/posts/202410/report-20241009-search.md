---
date: '2024-10-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e9690f5...MicrosoftDocs:eb045a9
summary: 今回の変更はAzure AI Searchに関するドキュメントのマイナーアップデートで、主な内容はスキルセット定義や各プログラミング言語でのクイックスタートガイドの改善、リソースツールの追加、RAGソリューションアクセラレーターの強化などです。新機能としては、キーボルトポータルの画像追加や顧客管理キー暗号化のサポートが含まれています。重要な互換性の問題はなく、既存ユーザーの利便性向上と新規ユーザーへの親しみやすさ向上が目的です。これにより、Azure
  AI Searchの利用がより効率的かつ信頼性のあるものとなります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e9690f5...MicrosoftDocs:eb045a9){target="_blank"}

# Highlights
今回の変更は、Azure AI Searchに関するドキュメントのマイナーアップデートとなっています。特に、スキルセット定義、C#、Java、JavaScript、Python、TypeScriptでのクイックスタートガイドの改善、リソースツールやRAGソリューションアクセラレーターの強化などが挙げられます。また、新機能として、キーボルトポータルの画像追加や顧客管理キー暗号化のサポートが含まれています。

## New features
- キーボルトポータルに関する新しい画像ファイルが追加され、暗号化キー管理の手順が視覚的にサポートされました。
- Azureポータルでの顧客管理キー暗号化のサポートが追加され、ユーザーはAzure Key Vaultから鍵を選択可能になりました。

## Breaking changes
- 特に重大な変更や互換性に影響を与える変更は含まれていません。

## Other updates
- スキルセット定義や各プログラミング言語におけるAzure AI Searchのクイックスタートガイドが内容の明確化や可読性向上を目指して更新されました。
- リソースツールに新しいツール（「Azure AI Search Lab」と「Back up and Restore (C#)」）が追加されました。
- RAGソリューションアクセラレーターの情報が強化され、ジェネリックコパイロットなど新しいアクセラレーターが追加されました。
- Pythonサンプルに音声ベースの生成AIアプリケーション用のアーキテクチャが追加されました。

# Insights
この一連のドキュメント更新は主に二つの目的を持っていると考えられます。一つは、既存ユーザーにとっての利便性の向上、もう一つは新規ユーザーに対する親しみやすさの向上です。まず、既存の開発者やユーザーにとって、手順やコードサンプルがより具体的かつ一貫性を持たせられていることで、Azure AI Searchを利用する上で効率が向上しています。特にクォータや暗号化キーの管理方法が明確になったことで、今後の開発や運用に関してユーザーの不安を和らげる効果があります。

次に、新しく追加された機能およびリソースは、Azure AI Searchを新たに導入しようとするユーザーにとって取っつきやすい材料となります。キーボルトポータルやRAGオーディオアーキテクチャのサンプルは、特定のニーズや興味を持つユーザーを強く引きつけ、Azureのツールやガイドに対する信頼性を高めるものとなっています。

最終的に、この更新はAzureエコシステムの中でのAzure AI Searchの役割と価値を再確認させるものであり、ユーザーがその能力をフルに活用できるよう、障壁を取り除くための努力の一環といえます。これにより、ユーザーがもつ異なるニーズに幅広く対応できる総合的なドキュメント体制が整備されていると言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-defining-skillset.md](#item-e2d71d) | minor update | スキルセットの定義に関する記事の更新 | modified | 30 | 30 | 60 | 
| [dotnet.md](#item-49258a) | minor update | C#でのAzure Searchクイックスタートに関するドキュメントの更新 | modified | 27 | 25 | 52 | 
| [java.md](#item-bd5406) | minor update | JavaでのAzure Searchクイックスタートに関するドキュメントの更新 | modified | 22 | 20 | 42 | 
| [javascript.md](#item-85ec57) | minor update | JavaScriptでのAzure Searchクイックスタートに関するドキュメントの更新 | modified | 24 | 24 | 48 | 
| [python.md](#item-162e74) | minor update | PythonでのAzure Searchクイックスタートに関するドキュメントの更新 | modified | 13 | 13 | 26 | 
| [typescript.md](#item-cded25) | minor update | TypeScriptでのAzure Searchクイックスタートに関するドキュメントの更新 | modified | 27 | 26 | 53 | 
| [assign-key-vault-portal.png](#item-783436) | new feature | キーボルトポータルの画像追加 | added | 0 | 0 | 0 | 
| [resource-demo-sites.md](#item-af1bd0) | minor update | デモサイトの情報更新 | modified | 1 | 3 | 4 | 
| [resource-tools.md](#item-0c6ac1) | minor update | リソースツールとアクセラレーターの情報更新 | modified | 15 | 5 | 20 | 
| [retrieval-augmented-generation-overview.md](#item-ec76e0) | minor update | RAGソリューションアクセラレーターの情報更新 | modified | 7 | 5 | 12 | 
| [samples-python.md](#item-d2bf09) | minor update | PythonサンプルにRAGオーディオアーキテクチャを追加 | modified | 2 | 1 | 3 | 
| [search-create-service-portal.md](#item-f90159) | minor update | サービスポータルでのクォータ要求手順の簡略化 | modified | 1 | 9 | 10 | 
| [search-get-started-text.md](#item-935941) | minor update | クイックスタートガイドのタイトルと内容を更新 | modified | 13 | 13 | 26 | 
| [search-security-manage-encryption-keys.md](#item-db3487) | minor update | 暗号化キーの管理に関する手順の更新 | modified | 20 | 4 | 24 | 
| [search-what-is-azure-search.md](#item-93853a) | minor update | Azure AI Searchに関する機能の追加 | modified | 9 | 1 | 10 | 
| [whats-new.md](#item-fa71b4) | minor update | Azureポータルでの顧客管理キー暗号化のサポート追加 | modified | 1 | 0 | 1 | 


# Modified Contents
## articles/search/cognitive-search-defining-skillset.md{#item-e2d71d}

<details>
<summary>Diff</summary>
````diff
@@ -1,29 +1,29 @@
 ---
 title: Create a skillset
 titleSuffix: Azure AI Search
-description: A skillset defines steps for content extraction, natural language processing, and image analysis. A skillset is attached to indexer. It's used to enrich and extract information from source data for indexing in Azure AI Search.
+description: Learn about skillsets and create a skillset in Azure AI Search using REST APIs.
 author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 01/10/2024
+ms.date: 10/04/2024
 ---
 
 # Create a skillset in Azure AI Search
 
-![indexer stages](media/cognitive-search-defining-skillset/indexer-stages-skillset.png "indexer stages")
+:::image type="content" source="media/cognitive-search-defining-skillset/indexer-stages-skillset.png" alt-text="Diagram showing the indexer stages, with Skillset Execution as the third stage of five.":::
 
-A skillset defines operations that generate textual content and structure from documents that contain images or unstructured text. Examples are OCR for images, entity recognition for undifferentiated text, and text translation. A skillset executes after text and images are extracted from an external data source, and after [field mappings](search-indexer-field-mappings.md) are processed.
+A skillset defines operations that generate textual content and structure from documents that contain images or unstructured text. Examples are optical character recognition (OCR) for images, entity recognition for undifferentiated text, and text translation. A skillset executes after text and images are extracted from an external data source, and after [field mappings](search-indexer-field-mappings.md) are processed.
 
 This article explains how to create a skillset using [REST APIs](/rest/api/searchservice/skillsets/create), but the same concepts and steps apply to other programming languages. 
 
 Rules for skillset definition include:
 
-+ A unique name within the skillset collection. A skillset is a top-level resource that can be used by any indexer.
-+ At least one skill. Three to five skills are typical. The maximum is 30.
-+ A skillset can repeat skills of the same type (for example, multiple Shaper skills).
++ Must have a unique name within the skillset collection. A skillset is a top-level resource that can be used by any indexer.
++ Must have at least one skill. Three to five skills are typical. The maximum is 30.
++ A skillset can repeat skills of the same type. For example, a skillset can have multiple Shaper skills.
 + A skillset supports chained operations, looping, and branching.
 
 Indexers drive skillset execution. You need an [indexer](search-howto-create-indexers.md), [data source](search-data-sources-gallery.md), and [index](search-what-is-an-index.md) before you can test your skillset.
@@ -65,7 +65,7 @@ After the name and description, a skillset has four main properties:
 
 + `skills` array, an unordered [collection of skills](cognitive-search-predefined-skills.md). Skills can be utilitarian (like splitting text), transformational (based on AI from Azure AI services), or custom skills that you provide. An example of a skills array is provided in the next section.
 
-+ `cognitiveServices` is used for [billable skills](cognitive-search-predefined-skills.md) that call Azure AI services APIs. Remove this section if you aren't using billable skills or Custom Entity Lookup. [Attach a resource](cognitive-search-attach-cognitive-services.md) if you are.
++ `cognitiveServices` is used for [billable skills](cognitive-search-predefined-skills.md) that call Azure AI services APIs. Remove this section if you aren't using billable skills or Custom Entity Lookup. If you are, attach [an Azure AI multi-service resource](cognitive-search-attach-cognitive-services.md).
 
 + `knowledgeStore` (optional) specifies an Azure Storage account and settings for projecting skillset output into tables, blobs, and files in Azure Storage. Remove this section if you don't need it, otherwise [specify a knowledge store](knowledge-store-create-rest.md).
 
@@ -75,7 +75,7 @@ After the name and description, a skillset has four main properties:
 
 Inside the skillset definition, the skills array specifies which skills to execute. Three to five skills are common, but you can add as many skills as necessary, subject to [service limits](search-limits-quotas-capacity.md#indexer-limits).
 
-The end result of an enrichment pipeline is textual content in either a search index or a knowledge store. For this reason, most skills either create text from images (OCR text, captions, tags), or analyze existing text to create new information (entities, key phrases, sentiment). Skills that operate independently are processed in parallel. Skills that depend on each other specify the output of one skill (such as key phrases) as the input of second skill (such as text translation). The search service determines the order of skill execution and the execution environment.
+The end result of an enrichment pipeline is textual content in either a search index or a knowledge store. For this reason, most skills either create text from images (OCR text, captions, tags), or analyze existing text to create new information (entities, key phrases, sentiment). Skills that operate independently are processed in parallel. Skills that depend on each other specify the output of one skill (such as key phrases) as the input of a second skill (such as text translation). The search service determines the order of skill execution and the execution environment.
 
 All skills have a type, context, inputs, and outputs. A skill might optionally have a name and description. The following example shows two unrelated [built-in skills](cognitive-search-predefined-skills.md) so that you can compare the basic structure.
 
@@ -128,11 +128,11 @@ All skills have a type, context, inputs, and outputs. A skill might optionally h
 Each skill is unique in terms of its input values and the parameters that it takes. [Skill reference documentation](cognitive-search-predefined-skills.md) describes all of the parameters and properties of a given skill. Although there are differences, most skills share a common set and are similarly patterned. 
 
 > [!NOTE]
-> You can build complex skillsets with looping and branching using the [Conditional skill](cognitive-search-skill-conditional.md) to create the expressions. The syntax is based on the [JSON Pointer](https://tools.ietf.org/html/rfc6901) path notation, with a few modifications to identify nodes in the enrichment tree. A `"/"` traverses a level lower in the tree and `"*"` acts as a for-each operator in the context. Numerous examples in this article illustrate the [the syntax](cognitive-search-skill-annotation-language.md). 
+> You can build complex skillsets with looping and branching using the [Conditional cognitive skill](cognitive-search-skill-conditional.md) to create the expressions. The syntax is based on the [JSON Pointer](https://tools.ietf.org/html/rfc6901) path notation, with a few modifications to identify nodes in the enrichment tree. A `"/"` traverses a level lower in the tree and `"*"` acts as a for-each operator in the context. Numerous examples in this article illustrate [the syntax](cognitive-search-skill-annotation-language.md). 
 
 ## Set skill context
 
-Each skill has a [context property](cognitive-search-working-with-skillsets.md#skill-context) that determines the level at which operations take place. If the "context" property isn't explicitly set, the default is `"/document"`, where the context is the whole document (the skill is called once per document).
+Each skill has a [context property](cognitive-search-working-with-skillsets.md#skill-context) that determines the level at which operations take place. If the `context` property isn't explicitly set, the default is `"/document"`, where the context is the whole document (the skill is called once per document).
 
 ```json
 "skills":[
@@ -152,21 +152,21 @@ Each skill has a [context property](cognitive-search-working-with-skillsets.md#s
 ]
 ```
 
-Context is usually set to one of the following examples:
+The `context` property is usually set to one of the following examples:
 
 | Context example | Description |
 |-----------------|-------------|
-| "context": "/document"  | (Default) Inputs and outputs are at the document level. |
-| "context": "/document/pages/*" | Some skills like sentiment analysis perform better over smaller chunks of text. If you're splitting a large content field into pages or sentences, the context should be over each component part. |
-| "context": "/document/normalized_images/*" | For image content, inputs and outputs are one per image in the parent document. |
+| `context`: `/document`  | (Default) Inputs and outputs are at the document level. |
+| `context`: `/document/pages/*` | Some skills like sentiment analysis perform better over smaller chunks of text. If you're splitting a large content field into pages or sentences, the context should be over each component part. |
+| `context`: `/document/normalized_images/*` | For image content, inputs and outputs are one per image in the parent document. |
 
-Context also determines where outputs are produced in the [enrichment tree](cognitive-search-working-with-skillsets.md#enrichment-tree). For example, the Entity Recognition skill returns a property called `"organizations"`, captured as `orgs`. If the context is `"/document"`, then an "organizations" node is added as a child of `"/document"`. If you then wanted to reference this node in downstream skills, the path would be `"/document/orgs"`.
+Context also determines where outputs are produced in the [enrichment tree](cognitive-search-working-with-skillsets.md#enrichment-tree). For example, the Entity Recognition skill returns a property called `organizations`, captured as `orgs`. If the context is `"/document"`, then an `organizations` node is added as a child of `"/document"`. If you then want to reference this node in downstream skills, the path is `"/document/orgs"`.
 
 ## Define inputs
 
 Skills read from and write to an enriched document. Skill inputs specify the origin of the incoming data. It's often the root node of the enriched document. For blobs, a typical skill input is the document's content property. 
 
-[Skill reference documentation](cognitive-search-predefined-skills.md) for each skill describes the inputs it can consume. Each input has a "name" that identifies a specific input, and a "source" that specifies the location of the data in the enriched document. The following example is from the Entity Recognition skill:
+[Skill reference documentation](cognitive-search-predefined-skills.md) for each skill describes the inputs it can consume. Each input has a `name` that identifies a specific input, and a `source` that specifies the location of the data in the enriched document. The following example is from the Entity Recognition skill:
 
 ```json
 "inputs": [
@@ -181,22 +181,22 @@ Skills read from and write to an enriched document. Skill inputs specify the ori
 ]
 ```
 
-+ Skills can have multiple inputs. The "name" is the specific input. For Entity Recognition, the specific inputs are "text" and "languageCode". 
++ Skills can have multiple inputs. The `name` is the specific input. For Entity Recognition, the specific inputs are *text* and *languageCode*.
 
-+ The "source" property specifies which field or row provides the content to be processed. For text-based skills, the source is a field in the document or row that provides text. For image-based skills, the node providing the input is normalized images.
++ The `source` property specifies which field or row provides the content to be processed. For text-based skills, the source is a field in the document or row that provides text. For image-based skills, the node providing the input is normalized images.
 
   | Source example | Description |
   |-----------------|-------------|
-  | "source": "/document"  | For a tabular data set, a document corresponds to a row.|
-  | "source": "/document/content"  | For blobs, the source is usually the blob's content property. |
-  | "source": "/document/some-named-field" | For text-based skills, such as entity recognition or key phrase extraction, the origin should be a field that contains sufficient text to be analyzed, such as a "description" or "summary". |
-  | "source": "/document/normalized_images/*" | For image content, the source is image that's been normalized during document cracking. |
+  | `source`: `/document`  | For a tabular data set, a document corresponds to a row.|
+  | `source`: `/document/content`  | For blobs, the source is usually the blob's content property. |
+  | `source`: `/document/some-named-field` | For text-based skills, such as entity recognition or key phrase extraction, the origin should be a field that contains sufficient text to be analyzed, such as a *description* or *summary*. |
+  | `source`: `/document/normalized_images/*` | For image content, the source is image that's been normalized during document cracking. |
 
 If the skill iterates over an array, both context and input source should include `/*` in the correct positions.
 
 ## Define outputs
 
-Each skill is designed to emit specific kinds of output, which are referenced by name in the skillset. A skill output has a "name" and an optional "targetName".
+Each skill is designed to emit specific kinds of output, which are referenced by name in the skillset. A skill output has a `name` and an optional `targetName`.
 
 [Skill reference documentation](cognitive-search-predefined-skills.md) for each skill describes the outputs it can produce. The following example is from the Entity Recognition skill:
 
@@ -217,19 +217,19 @@ Each skill is designed to emit specific kinds of output, which are referenced by
 ]
 ```
 
-+ Skills can have multiple outputs. The "name" identifies a specific output. For example, for Entity Recognition, output can be "persons", "locations", "organizations", among others. 
++ Skills can have multiple outputs. The `name` property identifies a specific output. For example, for Entity Recognition, output can be *persons*, *locations*, *organizations*, among others.
 
-+ "targetName" specifies the name you would like this node to have in the enriched document. This is useful if skill outputs have the same name. If you have multiple skills that return the same output, use the `"targetName"` for name disambiguation in enrichment node paths. If the target name is unspecified, the name property is used for both.
++ The `targetName` property specifies the name you would like this node to have in the enriched document. This is useful if skill outputs have the same name. If you have multiple skills that return the same output, use `targetName` for name disambiguation in enrichment node paths. If the target name is unspecified, the name property is used for both.
 
 Some situations call for referencing each element of an array separately. For example, suppose you want to pass *each element* of `"/document/orgs"` separately to another skill. To do so, add an asterisk to the path: `"/document/orgs/*"`.
 
 Skill output is written to the enriched document as a new node in the enrichment tree. It might be a simple value, such as a sentiment score or language code. It could also be a collection, such as a list of organizations, people, or locations. Skill output can also be a complex structure, as is the case with the Shaper skill. The inputs of the skill determine the composition of the shape, but the output is the named object, which can be referenced in a search index, a knowledge store projection, or another skill by its name.
 
 ## Add a custom skill
 
-This section includes an example of a [custom skill](cognitive-search-custom-skill-web-api.md). The URI points to an Azure Function, which in turn invokes the model or transformation that you provide. For more information, see [Define a custom interface](cognitive-search-custom-skill-interface.md).
+This section includes an example of a [custom skill](cognitive-search-custom-skill-web-api.md). The URI points to an Azure Function, which in turn invokes the model or transformation that you provide. For more information, see [Add a custom skill to an Azure AI Search enrichment pipeline](cognitive-search-custom-skill-interface.md).
 
-Although the custom skill is executing code that is external to the pipeline, in a skills array, it's just another skill. Like the built-in skills, it has a type, context, inputs, and outputs. It also reads and writes to an enrichment tree, just as the built-in skills do. Notice that the "context" field is set to `"/document/orgs/*"` with an asterisk, meaning the enrichment step is called *for each* organization under `"/document/orgs"`.
+Although the custom skill executes code that is external to the pipeline, in a skills array, it's just another skill. Like the built-in skills, it has a type, context, inputs, and outputs. It also reads and writes to an enrichment tree, just as the built-in skills do. Notice that the `context` field is set to `"/document/orgs/*"` with an asterisk, meaning the enrichment step is called *for each* organization under `"/document/orgs"`.
 
 Output, such as the company description in this example, is generated for each organization that's identified. When referring to the node in a downstream step (for example, in key phrase extraction), you would use the path `"/document/orgs/*/companyDescription"` to do so. 
 
@@ -269,15 +269,15 @@ Although skill output can be optionally cached for reuse purposes, it's usually
 
 ## Tips for a first skillset
 
-+ Try the [**Import data** wizard](search-import-data-portal.md). 
++ Try the [Import data wizard](search-import-data-portal.md). 
 
   The wizard automates several steps that can be challenging the first time around. It defines the skillset, index, and indexer, including field mappings and output field mappings. It also defines projections in a knowledge store if you're using one. For some skills, such as OCR or image analysis, the wizard adds utility skills that merge the image and text content that was separated during document cracking.
 
   After the wizard runs, you can open each object in the Azure portal to view its JSON definition.
 
 + Try [Debug Sessions](cognitive-search-debug-session.md) to invoke skillset execution over a target document and inspect the enriched document that the skillset creates. You can view and modify input and output settings and values. This tutorial is a good place to start: [Tutorial: Debug a skillset using Debug Sessions](cognitive-search-tutorial-debug-sessions.md).
 
-## Next steps
+## Next step
 
 Context and input source fields are paths to nodes in an enrichment tree. As a next step, learn more about the path syntax for nodes in an enrichment tree.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スキルセットの定義に関する記事の更新"
}
```

### Explanation
この変更は、Azure AI Searchにおけるスキルセットの定義に関する記事において、説明の明確化と情報の更新を行ったものです。具体的には、記事の説明文がより具体的になり、スキルセットの作成方法に関するコンテキストが強化されています。

変更点には、スキルやスキルセットの属性に関する記述が含まれており、スキルの定義や使用例が詳細に記載されています。また、スキルが出力するデータ構造や、スキルのコンテキストに関する情報が明確に説明されており、ユーザーがより簡単に理解できるようになっています。特に、REST APIを使用したスキルセットの作成に関する具体的な手順や、スキルの入力・出力に関する説明が改訂され、実践的なアドバイスも追加されています。

全体として、この記事はAzure AI Searchを利用する開発者やユーザーにとって、スキルセットを効果的に使用するための有益なリソースとなるように更新されています。

## articles/search/includes/quickstarts/dotnet.md{#item-49258a}

<details>
<summary>Diff</summary>
````diff
@@ -5,10 +5,12 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 06/09/2023
+ms.date: 10/07/2024
 ---
 
-Build a console application using the [**Azure.Search.Documents**](/dotnet/api/overview/azure/search.documents-readme) client library to create, load, and query a search index. Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11) to start with a finished project or follow these steps to create your own.
+Build a console application using the [Azure.Search.Documents](/dotnet/api/overview/azure/search.documents-readme) client library to create, load, and query a search index.
+
+Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11) to start with a finished project or follow these steps to create your own.
 
 #### Set up your environment
 
@@ -20,11 +22,11 @@ Build a console application using the [**Azure.Search.Documents**](/dotnet/api/o
 
 1. Search for [Azure.Search.Documents package](https://www.nuget.org/packages/Azure.Search.Documents/) and select version 11.0 or later.
 
-1. Select **Install** on the right to add the assembly to your project and solution.
+1. Select **Install** to add the assembly to your project and solution.
 
 #### Create a search client
 
-1. In **Program.cs**, change the namespace to `AzureSearch.SDK.Quickstart.v11` and then add the following `using` directives.
+1. In *Program.cs*, change the namespace to `AzureSearch.SDK.Quickstart.v11` and then add the following `using` directives.
 
    ```csharp
    using Azure;
@@ -34,9 +36,9 @@ Build a console application using the [**Azure.Search.Documents**](/dotnet/api/o
    using Azure.Search.Documents.Models;
    ```
 
-1. Create two clients: [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) creates the index, and [SearchClient](/dotnet/api/azure.search.documents.searchclient) loads and queries an existing index. Both need the service endpoint and an admin API key for authentication with create/delete rights.
+1. Copy the following code to create two clients. [SearchIndexClient](/dotnet/api/azure.search.documents.indexes.searchindexclient) creates the index, and [SearchClient](/dotnet/api/azure.search.documents.searchclient) loads and queries an existing index. Both need the service endpoint and an admin API key for authentication with create/delete rights.
 
-   Because the code builds out the URI for you, specify just the search service name in the "serviceName" property.
+   Because the code builds out the URI for you, specify just the search service name in the `serviceName` property.
 
    ```csharp
     static void Main(string[] args)
@@ -60,11 +62,11 @@ Build a console application using the [**Azure.Search.Documents**](/dotnet/api/o
 
 This quickstart builds a Hotels index that you'll load with hotel data and execute queries against. In this step, define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
 
-In this example, synchronous methods of the Azure.Search.Documents library are used for simplicity and readability. However, for production scenarios, you should use asynchronous methods to keep your app scalable and responsive. For example, you would use [CreateIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindexasync) instead of [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex).
+In this example, synchronous methods of the *Azure.Search.Documents* library are used for simplicity and readability. However, for production scenarios, you should use asynchronous methods to keep your app scalable and responsive. For example, you would use [CreateIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindexasync) instead of [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex).
 
-1. Add an empty class definition to your project: **Hotel.cs**
+1. Add an empty class definition to your project: *Hotel.cs*
 
-1. Copy the following code into **Hotel.cs** to define the structure of a hotel document. Attributes on the field determine how it's used in an application. For example, the `IsFilterable` attribute must be assigned to every field that supports a filter expression.
+1. Copy the following code into *Hotel.cs* to define the structure of a hotel document. Attributes on the field determine how it's used in an application. For example, the `IsFilterable` attribute must be assigned to every field that supports a filter expression.
 
     ```csharp
     using System;
@@ -110,15 +112,15 @@ In this example, synchronous methods of the Azure.Search.Documents library are u
     }
     ```
 
-   In the Azure.Search.Documents client library, you can use [SearchableField](/dotnet/api/azure.search.documents.indexes.models.searchablefield) and [SimpleField](/dotnet/api/azure.search.documents.indexes.models.simplefield) to streamline field definitions. Both are derivatives of a [SearchField](/dotnet/api/azure.search.documents.indexes.models.searchfield) and can potentially simplify your code:
+   In the *Azure.Search.Documents* client library, you can use [SearchableField](/dotnet/api/azure.search.documents.indexes.models.searchablefield) and [SimpleField](/dotnet/api/azure.search.documents.indexes.models.simplefield) to streamline field definitions. Both are derivatives of a [SearchField](/dotnet/api/azure.search.documents.indexes.models.searchfield) and can potentially simplify your code:
 
    + `SimpleField` can be any data type, is always non-searchable (it's ignored for full text search queries), and is retrievable (it's not hidden). Other attributes are off by default, but can be enabled. You might use a `SimpleField` for document IDs or fields used only in filters, facets, or scoring profiles. If so, be sure to apply any attributes that are necessary for the scenario, such as `IsKey = true` for a document ID. For more information, see [SimpleFieldAttribute.cs](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/src/Indexes/SimpleFieldAttribute.cs) in source code.
 
    + `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties. For more information, see the [SearchableFieldAttribute.cs](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/search/Azure.Search.Documents/src/Indexes/SearchableFieldAttribute.cs) in source code.
 
-   Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable), [IsSortable](/dotnet/api/azure.search.documents.indexes.models.searchfield.issortable), and [IsFacetable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfacetable) must be explicitly attributed, as shown in the sample above.
+   Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable), [IsSortable](/dotnet/api/azure.search.documents.indexes.models.searchfield.issortable), and [IsFacetable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfacetable) must be explicitly attributed, as shown in the previous sample.
 
-1. Add a second empty class definition to your project: **Address.cs**.  Copy the following code into the class.
+1. Add a second empty class definition to your project: *Address.cs*. Copy the following code into the class.
 
    ```csharp
    using Azure.Search.Documents.Indexes;
@@ -145,9 +147,9 @@ In this example, synchronous methods of the Azure.Search.Documents library are u
     }
    ```
 
-1. Create two more classes: **Hotel.Methods.cs** and **Address.Methods.cs** for ToString() overrides. These classes are used to render search results in the console output.  The contents of these classes aren't provided in this article, but you can copy the code from [files in GitHub](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11/AzureSearchQuickstart-v11).
+1. Create two more classes: *Hotel.Methods.cs* and *Address.Methods.cs* for `ToString()` overrides. These classes are used to render search results in the console output. The contents of these classes aren't provided in this article, but you can copy the code from [files in GitHub](https://github.com/Azure-Samples/azure-search-dotnet-samples/tree/main/quickstart/v11/AzureSearchQuickstart-v11).
 
-1. In **Program.cs**, create a [SearchIndex](/dotnet/api/azure.search.documents.indexes.models.searchindex) object, and then call the [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex) method to express the index in your search service. The index also includes a [SearchSuggester](/dotnet/api/azure.search.documents.indexes.models.searchsuggester) to enable autocomplete on the specified fields.
+1. In *Program.cs*, create a [SearchIndex](/dotnet/api/azure.search.documents.indexes.models.searchindex) object, and then call the [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex) method to express the index in your search service. The index also includes a [SearchSuggester](/dotnet/api/azure.search.documents.indexes.models.searchsuggester) to enable autocomplete on the specified fields.
 
    ```csharp
     // Create hotels-quickstart index
@@ -173,7 +175,7 @@ In Azure AI Search, search documents are data structures that are both inputs to
 
 When uploading documents, you must use an [IndexDocumentsBatch](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1) object. An `IndexDocumentsBatch` object contains a collection of [Actions](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1.actions), each of which contains a document and a property telling Azure AI Search what action to perform ([upload, merge, delete, and mergeOrUpload](/azure/search/search-what-is-data-import#indexing-actions)).
 
-1. In **Program.cs**, create an array of documents and index actions, and then pass the array to `IndexDocumentsBatch`. The documents below conform to the hotels-quickstart index, as defined by the hotel class.
+1. In *Program.cs*, create an array of documents and index actions, and then pass the array to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
 
     ```csharp
     // Upload documents in a single Upload request.
@@ -281,7 +283,7 @@ When uploading documents, you must use an [IndexDocumentsBatch](/dotnet/api/azur
 
     Once you initialize the [IndexDocumentsBatch](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1) object, you can send it to the index by calling [IndexDocuments](/dotnet/api/azure.search.documents.searchclient.indexdocuments) on your [SearchClient](/dotnet/api/azure.search.documents.searchclient) object.
 
-1. Add the following lines to Main(). Loading documents is done using SearchClient, but the operation also requires admin rights on the service, which is typically associated with SearchIndexClient. One way to set up this operation is to get SearchClient through SearchIndexClient (adminClient in this example).
+1. Add the following lines to `Main()`. Loading documents is done using SearchClient, but the operation also requires admin rights on the service, which is typically associated with SearchIndexClient. One way to set up this operation is to get SearchClient through `SearchIndexClient` (`adminClient` in this example).
 
    ```csharp
     SearchClient ingesterClient = adminClient.GetSearchClient(indexName);
@@ -309,7 +311,7 @@ This section adds two pieces of functionality: query logic, and results. For que
 
 The [SearchResults](/dotnet/api/azure.search.documents.models.searchresults-1) class represents the results.
 
-1. In **Program.cs**, create a **WriteDocuments** method that prints search results to the console.
+1. In *Program.cs*, create a `WriteDocuments` method that prints search results to the console.
 
     ```csharp
     // Write search results to console
@@ -334,7 +336,7 @@ The [SearchResults](/dotnet/api/azure.search.documents.models.searchresults-1) c
     }
     ```
 
-1. Create a **RunQueries** method to execute queries and return results. Results are Hotel objects. This sample shows the method signature and the first query. This query demonstrates the Select parameter that lets you compose the result using selected fields from the document.
+1. Create a `RunQueries` method to execute queries and return results. Results are Hotel objects. This sample shows the method signature and the first query. This query demonstrates the Select parameter that lets you compose the result using selected fields from the document.
 
     ```csharp
     // Run queries, use WriteDocuments to print output
@@ -361,7 +363,7 @@ The [SearchResults](/dotnet/api/azure.search.documents.models.searchresults-1) c
         WriteDocuments(response);
     ```
 
-1. In the second query, search on a term, add a filter that selects documents where Rating is greater than 4, and then sort by Rating in descending order. Filter is a boolean expression that is evaluated over [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable) fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
+1. In the second query, search on a term, add a filter that selects documents where *Rating* is greater than 4, and then sort by Rating in descending order. Filter is a boolean expression that is evaluated over [IsFilterable](/dotnet/api/azure.search.documents.indexes.models.searchfield.isfilterable) fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
 
     ```csharp
     // Query 2
@@ -381,7 +383,7 @@ The [SearchResults](/dotnet/api/azure.search.documents.models.searchresults-1) c
     WriteDocuments(response);
     ```
 
-1. The third query demonstrates searchFields, used to scope a full text search operation to specific fields.
+1. The third query demonstrates `searchFields`, used to scope a full text search operation to specific fields.
 
     ```csharp
     // Query 3
@@ -400,7 +402,7 @@ The [SearchResults](/dotnet/api/azure.search.documents.models.searchresults-1) c
     WriteDocuments(response);
     ```
 
-1. The fourth query demonstrates facets, which can be used to structure a faceted navigation structure.
+1. The fourth query demonstrates `facets`, which can be used to structure a faceted navigation structure.
 
    ```csharp
     // Query 4
@@ -421,7 +423,7 @@ The [SearchResults](/dotnet/api/azure.search.documents.models.searchresults-1) c
     WriteDocuments(response);
    ```
 
-1. In the fifth query, return a specific document. A document lookup is a typical response to OnClick event in a result set.
+1. In the fifth query, return a specific document. A document lookup is a typical response to `OnClick` event in a result set.
 
    ```csharp
     // Query 5
@@ -433,7 +435,7 @@ The [SearchResults](/dotnet/api/azure.search.documents.models.searchresults-1) c
     Console.WriteLine(lookupResponse.Value.HotelId);
    ```
 
-1. The last query shows the syntax for autocomplete, simulating a partial user input of "sa" that resolves to two possible matches in the sourceFields associated with the suggester you defined in the index.
+1. The last query shows the syntax for autocomplete, simulating a partial user input of *sa* that resolves to two possible matches in the sourceFields associated with the suggester you defined in the index.
 
    ```csharp
     // Query 6
@@ -443,7 +445,7 @@ The [SearchResults](/dotnet/api/azure.search.documents.models.searchresults-1) c
     WriteDocuments(autoresponse);
    ```
 
-1. Add **RunQueries** to Main().
+1. Add `RunQueries` to `Main()`.
 
     ```csharp
     // Call the RunQueries method to invoke a series of queries
@@ -461,6 +463,6 @@ Full text search and filters are performed using the [SearchClient.Search](/dotn
 
 #### Run the program
 
-Press F5 to rebuild the app and run the program in its entirety.
+Press **F5** to rebuild the app and run the program in its entirety.
 
 Output includes messages from [Console.WriteLine](/dotnet/api/system.console.writeline), with the addition of query information and results.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#でのAzure Searchクイックスタートに関するドキュメントの更新"
}
```

### Explanation
この変更は、C#クライアントライブラリを使用したAzure Cognitive Searchのクイックスタートに関連するドキュメントの更新を反映しています。主に文言の改善や、コードのサンプルの説明が明確化され、ユーザーが理解しやすくなるように配慮されています。

具体的には、いくつかの手順の説明が修正され、特にコードスニペットのフォーマットや説明が整ったことで、全体の可読性が向上しています。また、日付の更新や、手順に関連する説明がスムーズに流れるように調整されています。たとえば、"Program.cs" ファイルの変更内容や、クラス名の表記方法が一貫性を持たせ、ユーザーがコードを参照する際の便宜を図っています。

全体として、このアップデートは、開発者がAzure AI Searchを迅速に利用開始できるようにすることを目的としており、クイックスタートのガイドとしての役割をより強化する内容となっています。

## articles/search/includes/quickstarts/java.md{#item-bd5406}

<details>
<summary>Diff</summary>
````diff
@@ -5,14 +5,16 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 06/09/2023
+ms.date: 10/07/2024
 ---
 
-Build a Java console application using the [**Azure.Search.Documents**](/java/api/overview/azure/search) library to create, load, and query a search index. Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
+Build a Java console application using the [Azure.Search.Documents](/java/api/overview/azure/search) library to create, load, and query a search index. 
+
+Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-java-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
 
 #### Set up your environment
 
-We used the following tools to create this quickstart.
+Use the following tools to create this quickstart.
 
 + [Visual Studio Code with the Java extension](https://code.visualstudio.com/docs/java/extensions)
 
@@ -22,7 +24,7 @@ We used the following tools to create this quickstart.
 
 1. Start Visual Studio Code.
 
-1. Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) **Ctrl+Shift+P**. Search for **Create Java Project**.
+1. Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) by using **Ctrl+Shift+P**. Search for **Create Java Project**.
 
    :::image type="content" source="../../media/search-get-started-java/java-quickstart-create-project.png" alt-text="Screenshot of a Java project." border="true":::
 
@@ -56,7 +58,7 @@ We used the following tools to create this quickstart.
 
 #### Specify Maven dependencies
 
-1. Open the pom.xml file and add the following dependencies
+1. Open the *pom.xml* file and add the following dependencies.
 
     ```xml
     <dependencies>
@@ -79,7 +81,7 @@ We used the following tools to create this quickstart.
       </dependencies>
     ```
 
-1. Change the compiler Java version to 11
+1. Change the compiler Java version to 11.
 
     ```xml
     <maven.compiler.source>1.11</maven.compiler.source>
@@ -88,7 +90,7 @@ We used the following tools to create this quickstart.
 
 #### Create a search client
 
-1. Open the `App` class under **src**, **main**, **java**, **azure**, **search**, **sample**. Add the following import directives
+1. Open the `App` class under **src**, **main**, **java**, **azure**, **search**, **sample**. Add the following import directives.
 
     ```java
     import java.util.Arrays;
@@ -141,9 +143,9 @@ This quickstart builds a Hotels index that you'll load with hotel data and execu
 
 In this example, synchronous methods of the azure-search-documents library are used for simplicity and readability. However, for production scenarios, you should use asynchronous methods to keep your app scalable and responsive. For example, you would use [SearchAsyncClient](/java/api/com.azure.search.documents.searchasyncclient) instead of SearchClient.
 
-1. Add an empty class definition to your project: **Hotel.java**
+1. Add an empty class definition to your project: `Hotel.java`
 
-1. Copy the following code into **Hotel.java** to define the structure of a hotel document. Attributes on the field determine how it's used in an application. For example, the IsFilterable annotation must be assigned to every field that supports a filter expression
+1. Copy the following code into `Hotel.java` to define the structure of a hotel document. Attributes on the field determine how it's used in an application. For example, the IsFilterable annotation must be assigned to every field that supports a filter expression
 
     ```java
     // Copyright (c) Microsoft Corporation. All rights reserved.
@@ -256,9 +258,9 @@ In the Azure.Search.Documents client library, you can use [SearchableField](/jav
    * `SimpleField` can be any data type, is always non-searchable (it's ignored for full text search queries), and is retrievable (it's not hidden). Other attributes are off by default, but can be enabled. You might use a SimpleField for document IDs or fields used only in filters, facets, or scoring profiles. If so, be sure to apply any attributes that are necessary for the scenario, such as IsKey = true for a document ID.
    * `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties.
 
-Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, `isFilterable`, `isSortable`, and `isFacetable` must be explicitly attributed, as shown in the sample above.
+Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, `isFilterable`, `isSortable`, and `isFacetable` must be explicitly attributed, as shown in the previous sample.
 
-1. Add a second empty class definition to your project: **Address.cs**. Copy the following code into the class.
+1. Add a second empty class definition to your project: `Address.java`. Copy the following code into the class.
 
     ```java
     // Copyright (c) Microsoft Corporation. All rights reserved.
@@ -313,7 +315,7 @@ Whether you use the basic `SearchField` API or either one of the helper models,
     }
     ```
 
-1. In **App.java**, create a `SearchIndex` object in the **main** method, and then call the `createOrUpdateIndex` method to create the index in your search service. The index also includes a `SearchSuggester` to enable autocomplete on the specified fields.
+1. In `App.java`, create a `SearchIndex` object in the `main` method, and then call the `createOrUpdateIndex` method to create the index in your search service. The index also includes a `SearchSuggester` to enable autocomplete on the specified fields.
 
     ```java
     // Create Search Index for Hotel model
@@ -322,15 +324,15 @@ Whether you use the basic `SearchField` API or either one of the helper models,
         .setSuggesters(new SearchSuggester("sg", Arrays.asList("HotelName"))));
     ```
 
-#### Load Documents
+#### Load documents
 
 Azure AI Search searches over content stored in the service. In this step, you'll load JSON documents that conform to the hotel index you just created.
 
 In Azure AI Search, search documents are data structures that are both inputs to indexing and outputs from queries. As obtained from an external data source, document inputs might be rows in a database, blobs in Blob storage, or JSON documents on disk. In this example, we're taking a shortcut and embedding JSON documents for four hotels in the code itself.
 
 When uploading documents, you must use an [IndexDocumentsBatch](/java/api/com.azure.search.documents.indexes.models.indexdocumentsbatch) object. An `IndexDocumentsBatch` object contains a collection of [IndexActions](/java/api/com.azure.search.documents.models.indexaction), each of which contains a document and a property telling Azure AI Search what action to perform (upload, merge, delete, and mergeOrUpload).
 
-1. In **App.java**, create documents and index actions, and then pass them to `IndexDocumentsBatch`. The documents below conform to the hotels-quickstart index, as defined by the hotel class.
+1. In `App.java`, create documents and index actions, and then pass them to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
 
     ```java
     // Upload documents in a single Upload request.
@@ -457,7 +459,7 @@ You can get query results as soon as the first document is indexed, but actual t
 
 This section adds two pieces of functionality: query logic, and results. For queries, use the Search method. This method takes search text (the query string) and other options.
 
-1. In **App.java**, create a WriteDocuments method that prints search results to the console.
+1. In `App.java`, create a `WriteDocuments` method that prints search results to the console.
 
     ```java
     // Write search results to console
@@ -504,7 +506,7 @@ This section adds two pieces of functionality: query logic, and results. For que
     }
     ```
 
-1. In the second query, search on a term, add a filter that selects documents where Rating is greater than 4, and then sort by Rating in descending order. Filter is a boolean expression that is evaluated over `isFilterable` fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
+1. In the second query, search on a term, add a filter that selects documents where Rating is greater than 4, and then sort by *Rating* in descending order. Filter is a boolean expression that is evaluated over `isFilterable` fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
 
     ```java
     // Query 2
@@ -532,7 +534,7 @@ This section adds two pieces of functionality: query logic, and results. For que
     WriteSearchResults(searchClient.search("pool", options, Context.NONE));
     ```
 
-1. The fourth query demonstrates facets, which can be used to structure a faceted navigation structure.
+1. The fourth query demonstrates `facets`, which can be used to structure a faceted navigation structure.
 
     ```java
     // Query 4
@@ -557,7 +559,7 @@ This section adds two pieces of functionality: query logic, and results. For que
     System.out.println();
     ```
 
-1. The last query shows the syntax for autocomplete, simulating a partial user input of "s" that resolves to two possible matches in the `sourceFields` associated with the suggester you defined in the index.
+1. The last query shows the syntax for autocomplete, simulating a partial user input of *s* that resolves to two possible matches in the `sourceFields` associated with the suggester you defined in the index.
 
     ```java
     // Query 6
@@ -566,7 +568,7 @@ This section adds two pieces of functionality: query logic, and results. For que
     WriteAutocompleteResults(searchClient.autocomplete("s", "sg"));
     ```
 
-1. Add RunQueries to Main().
+1. Add `RunQueries` to `Main()`.
 
     ```java
     // Call the RunQueries method to invoke a series of queries
@@ -585,4 +587,4 @@ Full text search and filters are performed using the [SearchClient.search](/java
 
 Press F5 to rebuild the app and run the program in its entirety.
 
-Output includes messages from System.out.println, with the addition of query information and results.
+Output includes messages from `System.out.println`, with the addition of query information and results.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaでのAzure Searchクイックスタートに関するドキュメントの更新"
}
```

### Explanation
この変更は、Javaを使用したAzure Cognitive Searchのクイックスタートに関するドキュメントの内容を更新したもので、主に文言の明確化と可読性の向上が図られています。具体的には、手順やコードの説明が整理され、一貫性が保たれています。

主要な変更点としては、手順内の表現がより明確になり、特に「**」で強調されていた部分が通常のテキストに変更される一方で、コーディングやファイル名の記述は`` ` ``で囲まれ、一貫したフォーマットが採用されました。また、日付の更新が行われ、情報が新しくなっています。

内容としては、Javaコンソールアプリケーションを作成するために必要なライブラリの設定やMavenの依存関係の追加、クラス定義の方法、検索クライアントの作成に関する詳しい手順が記載されています。さらに、クエリの実行方法や結果の表示方法についても具体例が挙げられ、実際の開発者が実装しやすい構成になっています。

全体的に、このアップデートは、開発者がAzure Searchを利用してJavaアプリケーションを作成する際の手助けとなることを目的としており、より直感的に理解しやすい内容となっています。

## articles/search/includes/quickstarts/javascript.md{#item-85ec57}

<details>
<summary>Diff</summary>
````diff
@@ -5,38 +5,40 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 06/09/2023
+ms.date: 10/07/2024
 ---
 
-Build a Node.js application using the [**@azure/search-documents**](/javascript/api/overview/azure/search-documents-readme) library to create, load, and query a search index. Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
+Build a Node.js application using the [@azure/search-documents](/javascript/api/overview/azure/search-documents-readme) library to create, load, and query a search index. 
+
+Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
 
 #### Set up your environment
 
 We used the following tools to create this quickstart.
 
-+ [Visual Studio Code](https://code.visualstudio.com), which has built-in support for creating JavaScript apps.
++ [Visual Studio Code](https://code.visualstudio.com), which has built-in support for creating JavaScript apps
 
 + [Node.js](https://nodejs.org) and [npm](https://www.npmjs.com)
 
 #### Create the project
 
 1. Start Visual Studio Code.
 
-1. Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) **Ctrl+Shift+P** and open the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal).
+1. Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) by using **Ctrl+Shift+P** and open the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal).
 
-1. Create a development directory, giving it the name `quickstart` :
+1. Create a development directory, giving it the name *quickstart*:
 
     ```cmd
     mkdir quickstart
     cd quickstart
     ```
 
-1. Initialize an empty project with npm by running the following command. To fully initialize the project, press Enter multiple times to accept the default values, except for the License, which you should set to "MIT". 
+1. Initialize an empty project with npm by running the following command. To fully initialize the project, press Enter multiple times to accept the default values, except for the License, which you should set to *MIT*. 
 
     ```cmd
     npm init
     ```
-     
+
 1. Install `@azure/search-documents`, the [JavaScript/TypeScript SDK for Azure AI Search](/javascript/api/overview/azure/search-documents-readme). 
 
     ```cmd
@@ -49,7 +51,7 @@ We used the following tools to create this quickstart.
     npm install dotenv
     ```
 
-1. Confirm that you've configured the projects and its dependencies by checking that your  **package.json** file looks similar to the following json:
+1. Navigate to the *quickstart* directory, then confirm that you've configured the project and its dependencies by checking that your *package.json* file looks similar to the following json:
 
     ```json
     {
@@ -73,26 +75,26 @@ We used the following tools to create this quickstart.
     }
     ```
 
-1. Create a file **.env** to hold your search service parameters:
+1. Create a file *.env* to hold your search service parameters:
 
     ```
     SEARCH_API_KEY=<YOUR-SEARCH-ADMIN-API-KEY>
     SEARCH_API_ENDPOINT=<YOUR-SEARCH-SERVICE-URL>
     ```
 
-Replace the `<search-service-name>` value with the name of your search service. Replace `<search-admin-key>` with the key value you recorded earlier. 
+Replace the `YOUR-SEARCH-SERVICE-URL` value with the name of your search service endpoint URL. Replace `<YOUR-SEARCH-ADMIN-API-KEY>` with the admin key you recorded earlier. 
 
 #### Create index.js file
 
-Next we create an **index.js** file, which is the main file that will host our code.
+Next we create an *index.js* file, which is the main file that hosts our code.
 
 At the top of this file, we import the `@azure/search-documents` library:
 
 ```javascript
 const { SearchIndexClient, SearchClient, AzureKeyCredential, odata } = require("@azure/search-documents");
 ```
 
-Next, we need to require the `dotenv` package to read in the parameters from the **.env** file as follows:
+Next, we need to require the `dotenv` package to read in the parameters from the *.env* file as follows:
 
 ```javascript
 // Load the .env file if it exists
@@ -127,9 +129,9 @@ With that in place, we're ready to create an index.
 
 #### Create index 
 
-Create a file **hotels_quickstart_index.json**.  This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index.  You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
+Create a file *hotels_quickstart_index.json*. This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
 
-Add the following content to **hotels_quickstart_index.json** or [download the file](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels_quickstart_index.json). 
+Add the following content to *hotels_quickstart_index.json* or [download the file](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels_quickstart_index.json). 
 
 ```json
 {
@@ -263,7 +265,7 @@ Add the following content to **hotels_quickstart_index.json** or [download the f
 }
 ```
 
-With our index definition in place, we want to import  **hotels_quickstart_index.json** at the top of **index.js** so the main function can access the index definition.
+With our index definition in place, we want to import *hotels_quickstart_index.json* at the top of *index.js* so the main function can access the index definition.
 
 ```javascript
 const indexDefinition = require('./hotels_quickstart_index.json');
@@ -328,10 +330,9 @@ In the next step, you'll add data to index.
 
 #### Load documents 
 
-
 In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programatically push the documents to the index.
 
-Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. You can either download [hotels.json](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels.json) or create your own **hotels.json** file with the following content:
+Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. You can either download [hotels.json](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels.json) or create your own *hotels.json* file with the following content:
 
 ```json
 {
@@ -408,13 +409,12 @@ Document inputs might be rows in a database, blobs in Blob storage, or, as in th
 }
 ```
 
-Similar to what we did with the indexDefinition, we also need to import `hotels.json` at the top of **index.js** so that the data can be accessed in our main function.
+Similar to what we did with the `indexDefinition`, we also need to import `hotels.json` at the top of *index.js* so that the data can be accessed in our main function.
 
 ```javascript
 const hotelData = require('./hotels.json');
 ```
 
-
 To index data into the search index, we now need to create a `SearchClient`. While the `SearchIndexClient` is used to create and manage an index, the `SearchClient` is used to upload documents and query the index.
 
 There are two ways to create a `SearchClient`. The first option is to create a `SearchClient` from scratch:
@@ -429,7 +429,7 @@ Alternatively, you can use the `getSearchClient()` method of the `SearchIndexCli
 const searchClient = indexClient.getSearchClient(indexName);
 ```
 
-Now that the client is defined, upload the documents into the search index. In this case, we use the `mergeOrUploadDocuments()` method, which will upload the documents or merge them with an existing document if a document with the same key already exists.
+Now that the client is defined, upload the documents into the search index. In this case, we use the `mergeOrUploadDocuments()` method, which uploads the documents or merges them with an existing document if a document with the same key already exists.
 
 ```javascript
 console.log('Uploading documents...');
@@ -460,9 +460,9 @@ sleep(1000);
 
 #### Search an index
 
-With an index created and documents uploaded, you're ready to send queries to the index. In this section, we'll send five different queries to the search index to demonstrate different pieces of query functionality available to you.
+With an index created and documents uploaded, you're ready to send queries to the index. In this section, we send five different queries to the search index to demonstrate different pieces of query functionality available to you.
 
-The queries are written in a `sendQueries()` function that we'll call in the main function as follows:
+The queries are written in a `sendQueries()` function that we call in the main function as follows:
 
 ```javascript
 await sendQueries(searchClient);
@@ -472,7 +472,7 @@ Queries are sent using the `search()` method of `searchClient`. The first parame
 
 The first query searches `*`, which is equivalent to searching everything and selects three of the fields in the index. It's a best practice to only `select` the fields you need because pulling back unnecessary data can add latency to your queries.
 
-The `searchOptions` for this query also has `includeTotalCount` set to `true`, which will return the number of matching results found.
+The `searchOptions` for this query also has `includeTotalCount` set to `true`, which returns the number of matching results found.
 
 ```javascript
 async function sendQueries(searchClient) {
@@ -553,4 +553,4 @@ console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.Hot
 
 #### Run the sample
 
-Run the program with `node index.js`. Now, in addition to the previous steps, the queries will be sent and the results written to the console.
+Run the program by using `node index.js`. Now, in addition to the previous steps, the queries are sent and the results written to the console.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptでのAzure Searchクイックスタートに関するドキュメントの更新"
}
```

### Explanation
この変更は、JavaScriptを使用したAzure Cognitive Searchのクイックスタートに関連するドキュメントの内容を更新したもので、主に文言の明確化や可読性の向上が行われています。この更新では、手順内の表現が調整され、特にファイル名やコマンドの書き方が一貫したスタイルに整えられました。

具体的な変更点としては、特定のファイル名やコマンドが囲まれることで視認性が向上しており、手順の説明がよりスムーズに理解できるようになっています。また、日付が更新され、新しい情報を反映しています。

手順の内容には、Node.jsアプリケーションを作成するための準備、プロジェクトの初期化、依存関係の管理、そしてAzure Searchに関連するインデックスやドキュメントの設定について詳しく説明されています。また、クエリを実行するための方法も示されており、最終的に結果をコンソールに出力する手順が記されています。

全体として、この修正は、JavaScriptを使用してAzure Searchを迅速に利用開始するための明確で実用的なガイドを提供することを目的としており、開発者が迅速に実行できるような内容になっています。

## articles/search/includes/quickstarts/python.md{#item-162e74}

<details>
<summary>Diff</summary>
````diff
@@ -5,28 +5,28 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 03/11/2024
+ms.date: 10/07/2024
 ---
 
-Use a Jupyter notebook and the [**azure-search-documents**](/python/api/overview/azure/search-documents-readme) library in the Azure SDK for Python to create, load, and query a search index. 
+Use a Jupyter notebook and the [azure-search-documents](/python/api/overview/azure/search-documents-readme) library in the Azure SDK for Python to create, load, and query a search index. 
 
-Alternatively, [download and run a finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart).
+Alternatively, you can download and run a [finished notebook](https://github.com/Azure-Samples/azure-search-python-samples/tree/main/Quickstart).
 
 #### Set up your environment
 
-Use [Visual Studio Code with the Python extension](https://code.visualstudio.com/docs/languages/python), or equivalent IDE, with Python 3.10 or later.
+Use [Visual Studio Code with the Python extension](https://code.visualstudio.com/docs/languages/python), or an equivalent IDE, with Python 3.10 or later.
 
 We recommend a virtual environment for this quickstart:
 
 1. Start Visual Studio Code.
 
-1. Open the Command Palette (Ctrl+Shift+P).
+1. Open the Command Palette (**Ctrl+Shift+P**).
 
 1. Search for **Python: Create Environment**.
 
-1. Select **`Venv.`**
+1. Select `Venv.`
 
-1. Select a Python interpreter. Choose 3.10 or later.
+1. Select a Python interpreter. Choose version 3.10 or later.
 
 It can take a minute to set up. If you run into problems, see [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).
 
@@ -40,7 +40,7 @@ It can take a minute to set up. If you run into problems, see [Python environmen
     ! pip install python-dotenv --quiet
     ```
 
-1. Provide endpoint and API keys:
+1. Provide the endpoint and API key for your service:
 
     ```python
     search_endpoint: str = "PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE"
@@ -92,15 +92,15 @@ fields = [
 scoring_profiles = []
 suggester = [{'name': 'sg', 'source_fields': ['Tags', 'Address/City', 'Address/Country']}]
 
-# Create the search index=
+# Create the search index
 index = SearchIndex(name=index_name, fields=fields, suggesters=suggester, scoring_profiles=scoring_profiles)
 result = index_client.create_or_update_index(index)
 print(f' {result.name} created')
 ```
 
 #### Create a documents payload
 
-Use an [index action](/python/api/azure-search-documents/azure.search.documents.models.indexaction) for the operation type (upload, merge-and-upload, and so forth). Documents originate from [HotelsData](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureSearch.JSON) on GitHub.
+Use an [index action](/python/api/azure-search-documents/azure.search.documents.models.indexaction) for the operation type, such as upload or merge-and-upload. Documents originate from the [HotelsData](https://github.com/Azure-Samples/azure-search-sample-data/blob/main/hotels/HotelsData_toAzureSearch.JSON) sample on GitHub.
 
 ```python
 # Create a documents payload
@@ -203,7 +203,7 @@ except Exception as ex:
 
 #### Run your first query
 
-Use the **search** method of the [search.client class](/python/api/azure-search-documents/azure.search.documents.searchclient).
+Use the *search* method of the [search.client class](/python/api/azure-search-documents/azure.search.documents.searchclient).
 
 This example executes an empty search (`search=*`), returning an unranked list (search score = 1.0) of arbitrary documents. Because there are no criteria, all documents are included in results.
 
@@ -271,7 +271,7 @@ for result in results:
 
 #### Add facets
 
-Facets are generated for positive matches found in search results. There are no zero matches. If search results don't include the term `"wifi"`, then `"wifi"` doesn't appear in the faceted navigation structure.
+Facets are generated for positive matches found in search results. There are no zero matches. If search results don't include the term *wifi*, then *wifi* doesn't appear in the faceted navigation structure.
 
 ```python
 # Return facets
@@ -303,7 +303,7 @@ Autocomplete can provide potential matches as the user types into the search box
 
 Autocomplete uses a suggester (`sg`) to know which fields contain potential matches to suggester requests. In this quickstart, those fields are `Tags`, `Address/City`, `Address/Country`. 
 
-To simulate autocomplete, pass in the letters "sa" as a partial string. The autocomplete method of [SearchClient](/python/api/azure-search-documents/azure.search.documents.searchclient) sends back potential term matches.
+To simulate autocomplete, pass in the letters *sa* as a partial string. The autocomplete method of [SearchClient](/python/api/azure-search-documents/azure.search.documents.searchclient) sends back potential term matches.
 
 ```python
 # Autocomplete a query
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PythonでのAzure Searchクイックスタートに関するドキュメントの更新"
}
```

### Explanation
この変更は、Pythonを使用したAzure Cognitive Searchのクイックスタートのドキュメントに対する軽微な更新であり、内容の明確化や用語の一貫性が改善されています。特に、手順の表現がより正確で分かりやすいものに変更されており、開発者が実装を行う際に役立つ情報が整理されています。

具体的には、文中のファイル名やメソッド名が一貫してフォーマットされ、標準的なコードスタイルに準拠しています。また、操作手順がもう少し具体的に説明されており、特にパラメータの提示方法が改善されています。

更新の主なポイントには、Jupyterノートブックの使用、仮想環境の設定、APIキーやエンドポイントの指定、検索インデックスの作成方法、ドキュメントのペイロード作成、最初のクエリ実行の手順が含まれています。また、ファセットやオートコンプリートの機能についても具体的な説明がなされ、より実践的な内容になっています。

全体として、このドキュメントの更新は、Pythonを使用してAzure Searchを導入する際のユーザーエクスペリエンスを向上させ、開発者が効果的に作業を進められるようにすることを目的としています。

## articles/search/includes/quickstarts/typescript.md{#item-cded25}

<details>
<summary>Diff</summary>
````diff
@@ -5,16 +5,18 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: include
-ms.date: 08/05/2024
+ms.date: 10/07/2024
 ---
 
-Build a Node.js application using the [**@azure/search-documents**](/javascript/api/overview/azure/search-documents-readme) library to create, load, and query a search index. Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
+Build a Node.js application using the [@azure/search-documents](/javascript/api/overview/azure/search-documents-readme) library to create, load, and query a search index. 
+
+Alternatively, you can [download the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) to start with a finished project or follow these steps to create your own.
 
 #### Set up your environment
 
 We used the following tools to create this quickstart.
 
-+ [Visual Studio Code](https://code.visualstudio.com), which has built-in support for creating JavaScript apps.
++ [Visual Studio Code](https://code.visualstudio.com), which has built-in support for creating JavaScript apps
 
 + [Node.js LTS](https://nodejs.org) and [npm](https://www.npmjs.com)
 
@@ -24,21 +26,21 @@ We used the following tools to create this quickstart.
 
 1. Start Visual Studio Code.
 
-1. Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) **Ctrl+Shift+P** and open the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal).
+1. Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) by using **Ctrl+Shift+P** and open the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal).
 
-1. Create a development directory, giving it the name `quickstart` :
+1. Create a development directory, giving it the name *quickstart*:
 
     ```cmd
     mkdir quickstart
     cd quickstart
     ```
 
-1. Initialize an empty project with npm by running the following command. To fully initialize the project, press Enter multiple times to accept the default values, except for the License, which you should set to "MIT". 
+1. Initialize an empty project with npm by running the following command. To fully initialize the project, press Enter multiple times to accept the default values, except for the License, which you should set to *MIT*. 
 
     ```cmd
     npm init
     ```
-     
+
 1. Install `@azure/search-documents`, the [JavaScript/TypeScript SDK for Azure AI Search](/javascript/api/overview/azure/search-documents-readme). 
 
     ```cmd
@@ -51,7 +53,7 @@ We used the following tools to create this quickstart.
     npm install dotenv
     ```
 
-1. Confirm that you've configured the projects and its dependencies by checking that your  **package.json** file looks similar to the following json:
+1. Navigate to the *quickstart* directory, then confirm that you've configured the project and its dependencies by checking that your *package.json* file looks similar to the following json:
 
     ```json
     {
@@ -75,18 +77,18 @@ We used the following tools to create this quickstart.
     }
     ```
 
-1. Create a file **.env** to hold your search service parameters:
+1. Create a file *.env* to hold your search service parameters:
 
     ```
     SEARCH_API_KEY=<YOUR-SEARCH-ADMIN-API-KEY>
     SEARCH_API_ENDPOINT=<YOUR-SEARCH-SERVICE-URL>
     ```
 
-Replace the `<search-service-name>` value with the name of your search service. Replace `<search-admin-key>` with the key value you recorded earlier. 
+Replace the `YOUR-SEARCH-SERVICE-URL` value with the name of your search service endpoint URL. Replace `<YOUR-SEARCH-ADMIN-API-KEY>` with the admin key you recorded earlier. 
 
 #### Create index.ts file
 
-Next we create an **index.ts** file, which is the main file that will host our code.
+Next we create an *index.ts* file, which is the main file that hosts our code.
 
 At the top of this file, we import the `@azure/search-documents` library:
 
@@ -104,7 +106,7 @@ import {
 } from "@azure/search-documents";
 ```
 
-Next, we need to require the `dotenv` package to read in the parameters from the **.env** file as follows:
+Next, we need to require the `dotenv` package to read in the parameters from the *.env* file as follows:
 
 ```typescript
 // Load the .env file if it exists
@@ -138,11 +140,11 @@ main().catch((err) => {
 
 With that in place, we're ready to create an index.
 
-#### Create index 
+#### Create index
 
-Create a file **hotels_quickstart_index.json**.  This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index.  You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
+Create a file *hotels_quickstart_index.json*. This file defines how Azure AI Search works with the documents you'll be loading in the next step. Each field will be identified by a `name` and have a specified `type`. Each field also has a series of index attributes that specify whether Azure AI Search can search, filter, sort, and facet upon the field. Most of the fields are simple data types, but some, like `AddressType` are complex types that allow you to create rich data structures in your index. You can read more about [supported data types](/rest/api/searchservice/supported-data-types) and index attributes described in [Create Index (REST)](/rest/api/searchservice/indexes/create). 
 
-Add the following content to **hotels_quickstart_index.json** or [download the file](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels_quickstart_index.json). 
+Add the following content to *hotels_quickstart_index.json* or [download the file](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels_quickstart_index.json).
 
 ```json
 {
@@ -276,7 +278,7 @@ Add the following content to **hotels_quickstart_index.json** or [download the f
 }
 ```
 
-With our index definition in place, we want to import  **hotels_quickstart_index.json** at the top of **index.ts** so the main function can access the index definition.
+With our index definition in place, we want to import *hotels_quickstart_index.json* at the top of *index.ts* so the main function can access the index definition.
 
 ```typescript
 // Importing the index definition and sample data
@@ -336,7 +338,7 @@ At this point, you're ready to build and run the sample. Use a terminal window t
 
 ```cmd
 tsc
-node index.js
+node index.ts
 ```
 
 If you [downloaded the source code](https://github.com/Azure-Samples/azure-search-javascript-samples/tree/main/quickstart) and haven't installed the required packages yet, run `npm install` first.
@@ -351,10 +353,9 @@ In the next step, you'll add data to index.
 
 #### Load documents 
 
-
 In Azure AI Search, documents are data structures that are both inputs to indexing and outputs from queries. You can push such data to the index or use an [indexer](/azure/search/search-indexer-overview). In this case, we'll programatically push the documents to the index.
 
-Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. You can either download [hotels.json](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels.json) or create your own **hotels.json** file with the following content:
+Document inputs might be rows in a database, blobs in Blob storage, or, as in this sample, JSON documents on disk. You can either download [hotels.json](https://github.com/Azure-Samples/azure-search-javascript-samples/blob/main/quickstart/hotels.json) or create your own *hotels.json* file with the following content:
 
 ```json
 {
@@ -431,7 +432,7 @@ Document inputs might be rows in a database, blobs in Blob storage, or, as in th
 }
 ```
 
-Similar to what we did with the indexDefinition, we also need to import `hotels.json` at the top of **index.ts** so that the data can be accessed in our main function.
+Similar to what we did with the indexDefinition, we also need to import `hotels.json` at the top of *index.ts* so that the data can be accessed in our main function.
 
 ```typescript
 import hotelData from './hotels.json';
@@ -471,7 +472,7 @@ Alternatively, you can use the `getSearchClient()` method of the `SearchIndexCli
 const searchClient = indexClient.getSearchClient<Hotel>(indexName);
 ```
 
-Now that the client is defined, upload the documents into the search index. In this case, we use the `mergeOrUploadDocuments()` method, which will upload the documents or merge them with an existing document if a document with the same key already exists. Then check that the operation succeeded because at least the first document exists.
+Now that the client is defined, upload the documents into the search index. In this case, we use the `mergeOrUploadDocuments()` method, which uploads the documents or merges them with an existing document if a document with the same key already exists. Then check that the operation succeeded because at least the first document exists.
 
 ```typescript
 console.log("Uploading documents...");
@@ -480,7 +481,7 @@ const indexDocumentsResult = await searchClient.mergeOrUploadDocuments(hotels);
 console.log(`Index operations succeeded: ${JSON.stringify(indexDocumentsResult.results[0].succeeded)}`);
 ```
 
-Run the program again with `tsc && node index.js`. You should see a slightly different set of messages from those you saw in Step 1. This time, the index *does* exist, and you should see a message about deleting it before the app creates the new index and posts data to it. 
+Run the program again with `tsc && node index.ts`. You should see a slightly different set of messages from those you saw in Step 1. This time, the index *does* exist, and you should see a message about deleting it before the app creates the new index and posts data to it. 
 
 Before we run the queries in the next step, define a function to have the program wait for one second. This is done just for test/demo purposes to ensure the indexing finishes and that the documents are available in the index for our queries.
 
@@ -490,17 +491,17 @@ function sleep(ms: number): Promise<void> {
 }
 ```
 
-To have the program wait for one second, call the `sleep` function like below:
+To have the program wait for one second, call the `sleep` function:
 
 ```typescript
 sleep(1000);
 ```
 
 #### Search an index
 
-With an index created and documents uploaded, you're ready to send queries to the index. In this section, we'll send five different queries to the search index to demonstrate different pieces of query functionality available to you.
+With an index created and documents uploaded, you're ready to send queries to the index. In this section, we send five different queries to the search index to demonstrate different pieces of query functionality available to you.
 
-The queries are written in a `sendQueries()` function that we'll call in the main function as follows:
+The queries are written in a `sendQueries()` function that we call in the main function as follows:
 
 ```typescript
 await sendQueries(searchClient);
@@ -598,4 +599,4 @@ console.log(`HotelId: ${documentResult.HotelId}; HotelName: ${documentResult.Hot
 
 #### Rerun the sample
 
-Build and run the program with `tsc && node index.ts`. Now, in addition to the previous steps, the queries will be sent and the results written to the console.
+Build and run the program with `tsc && node index.ts`. Now, in addition to the previous steps, the queries are sent and the results written to the console.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptでのAzure Searchクイックスタートに関するドキュメントの更新"
}
```

### Explanation
この変更は、TypeScriptを使用したAzure Cognitive Searchのクイックスタートガイドに関するドキュメントの軽微な更新を反映しています。変更内容は、文の明確化と一貫性を高めることに焦点を当てており、読者が手順をより理解しやすくすることを目的としています。

主な変更点には、コマンドやファイル名のフォーマットの調整、手順中の表現の統一が含まれています。また、特定の操作に関する説明が改良され、より具体的になっています。たとえば、環境設定や依存関係の確認手順において、使用手順が細かく明記され、利用者にとって親しみやすい形式になっています。

具体的には、Node.jsアプリケーションの作成手順、APIキーやエンドポイントの設定、検索インデックスの作成とドキュメントのアップロード方法、そしてクエリの実行について説明されています。特に、コマンドやファイル名が強調されたりイタリック体で表示されたりすることで、情報が明確に区別されています。また、検索インデックスにデータを追加する際の方法についても詳細に記述されています。

全体として、これらの修正は、TypeScriptを使用してAzure Searchを導入する開発者にとっての利便性を向上させ、手続きに対する理解を深める内容となっています。

## articles/search/media/search-security-manage-encryption-keys/assign-key-vault-portal.png{#item-783436}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "キーボルトポータルの画像追加"
}
```

### Explanation
この変更は、Azureドキュメント内に「assign-key-vault-portal.png」という新しい画像ファイルが追加されたものです。この画像は、暗号化キーの管理に関連するキーボルトポータルの設定手順を視覚的にサポートするために使用されます。

この画像の追加により、読者はキーボルトの操作をより直感的に理解できるようになります。特に、セキュリティ管理や暗号化キーの割り当て作業において、視覚的なガイドが提供されることで、手順の明確さが向上します。

全体として、この画像の追加は、関連する手順の理解を深め、ユーザーが自分の環境で実行する際に参考にできる重要な補助資料となります。

## articles/search/resource-demo-sites.md{#item-af1bd0}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: cognitive-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 07/29/2024
+ms.date: 10/07/2024
 ---
 
 # Demos - Azure AI Search
@@ -20,7 +20,5 @@ The Azure AI Search currently builds and hosts the following demos.
 
 | Demo name | Description | Source code |
 |-----------|------------ |-------------|
-| [Conversational Knowledge Mining](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services) | Code and docs to create interactive solution to extract conversational insights from post-contact center transcripts in production environment. | [https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services) |
-| [Build your own copilot solution accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator) | Code and docs to build your own copilot to harness the power of generative AI across both structured and unstructured data for Client Advisor and Research Assistant business use case scenarios. | [https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator) |
 | [Chat with your data](https://entgptsearch.azurewebsites.net/) | An Azure web app that uses ChatGPT in Azure OpenAI with fictitious health plan data in a search index. | [https://github.com/Azure-Samples/azure-search-openai-demo/](https://github.com/Azure-Samples/azure-search-openai-demo/)  |
 | [Semantic ranking for retail](https://brave-meadow-0f59c9b1e.1.azurestaticapps.net/) | Web app for a fictitious online retailer, "Terra" | Not available |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デモサイトの情報更新"
}
```

### Explanation
この変更は、Azure AI Searchに関連するデモサイトの情報を含む文書「resource-demo-sites.md」の軽微な更新を示しています。変更内容には、文書の日付の修正とデモのリストの一部削除が含まれています。

具体的には、元の日付が「07/29/2024」から「10/07/2024」に更新され、これにより最新の情報を反映しています。また、2つのデモの詳細が削除され、新しい情報が追加されました。この更新により、読者は現在利用可能なデモサイトとその内容をより正確に把握できるようになります。

全体として、この変更は、Azure AI Searchに関するデモサイトの可用性と内容の最新性を保つことを目的としており、ユーザーにとって有用な情報を提供しています。

## articles/search/resource-tools.md{#item-0c6ac1}

<details>
<summary>Diff</summary>
````diff
@@ -7,17 +7,27 @@ manager: nitinme
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: conceptual
-ms.date: 07/02/2024
+ms.date: 10/08/2024
 ---
 
-# Productivity tools - Azure AI Search
+# Productivity tools and accelerators - Azure AI Search
 
 Productivity tools are built by engineers at Microsoft, but aren't part of the Azure AI Search service and aren't under Service Level Agreement (SLA). These tools are provided as source code that you can download, modify, and build to create an app that helps you develop or maintain a search solution.
 
+## Tools
+
 | Tool name | Description | Source code |
 |-----------|------------ |-------------|
-| [Back up and Restore](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore) | Download the retrievable fields of an index to your local device and then upload the index and its content to a new search service. | [https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore) |
-| [Chat with your data solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator/blob/main/README.md) |  Code and docs to create interactive search solution in production environments.  | [https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) |
-| [Knowledge Mining Accelerator](https://github.com/Azure-Samples/azure-search-knowledge-mining/blob/main/README.md) | Code and docs to jump start a knowledge store using your data. | [https://github.com/Azure-Samples/azure-search-knowledge-mining](https://github.com/Azure-Samples/azure-search-knowledge-mining) |
+| [Azure AI Search Lab](https://github.com/jelledruyts/azure-ai-search-lab) | Learning and experimentation lab to try out AI-enabled search scenarios in Azure. It provides a web application front-end which uses Azure AI Search and Azure OpenAI to execute searches with a variety of options - ranging from simple keyword search, to semantic ranking, vector and hybrid search, and using generative AI to answer search queries. | [https://github.com/jelledruyts/azure-ai-search-lab](https://github.com/jelledruyts/azure-ai-search-lab)  |
+| [Back up and Restore (C#)](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) | Download the retrievable fields of an index to your local device and then upload the index and its content to a new search service. | [https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore](https://github.com/Azure-Samples/azure-search-dotnet-utilities/blob/main/index-backup-restore) |
+| [Back up and Restore (Python)](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore) | Download the retrievable fields of an index to your local device and then upload the index and its content to a new search service. | [https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore) |
 | [Performance testing solution](https://github.com/Azure-Samples/azure-search-performance-testing/blob/main/README.md) | This solution helps you load test Azure AI Search. It uses Apache JMeter as an open source load and performance testing tool and Terraform to dynamically provision and destroy the required infrastructure on Azure. | [https://github.com/Azure-Samples/azure-search-performance-testing](https://github.com/Azure-Samples/azure-search-performance-testing) |
 | [Visual Studio Code extension](https://github.com/microsoft/vscode-azurecognitivesearch) | Although the extension is no longer available in the Visual Studio Code Marketplace, the code is open source. You can clone and modify the tool for your own use. | [https://github.com/microsoft/vscode-azurecognitivesearch](https://github.com/microsoft/vscode-azurecognitivesearch) |
+
+## Accelerators
+
+| Accelerator | Description | Source code |
+|-----------|------------ |-------------|
+| [Build your own copilot Solution Accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator) | Code and docs to build a copilot for specific use cases.| [Client advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ClientAdvisor/README.md) <br>[Generic document generator](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator) <br>[Research assistant](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ResearchAssistant/README.md) |
+| [Chat with your data solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator/blob/main/README.md) |  Code and docs to create interactive search solution in production environments.  | [https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) |
+| [Knowledge Mining accelerator](https://github.com/Azure-Samples/azure-search-knowledge-mining/blob/main/README.md) | Code and docs to jump start a knowledge store using your data. | [https://github.com/Azure-Samples/azure-search-knowledge-mining](https://github.com/Azure-Samples/azure-search-knowledge-mining) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースツールとアクセラレーターの情報更新"
}
```

### Explanation
この変更は、Azure AI Searchに関連するリソースツールに関する文書「resource-tools.md」の更新を示しています。主な内容は、文書の日付の修正、新しいツールの追加、およびツールとアクセラレーターの情報の整理です。

具体的には、文書の日付が「07/02/2024」から「10/08/2024」に更新され、製品名や説明に関する内容が拡充されています。「生産性向上ツール」のタイトルが「生産性向上ツールとアクセラレーター」に変更され、リストには新たに2つのツール（「Azure AI Search Lab」と「Back up and Restore (C#)」）が追加されています。

また、各ツールとアクセラレーターに対して詳細な説明が付加され、読者はこれらのリソースを利用して自分の検索ソリューションを構築、保守する際のサポートを受けやすくなっています。

全体として、この変更は Azure AI Search に関連する情報を最新の状態に保ち、ユーザーが効果的にリソースを利用できるようにすることを目的としています。

## articles/search/retrieval-augmented-generation-overview.md{#item-ec76e0}

<details>
<summary>Diff</summary>
````diff
@@ -226,15 +226,17 @@ A RAG solution that includes Azure AI Search can leverage [built-in data chunkin
 
 + Start with solution accelerators:
 
-  + ["Chat with your data" solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) helps you create a custom RAG solution over your content.
+  + [Chat with your data solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator)
   
-  + ["Conversational Knowledge Mining" solution accelerator](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services), helps you create an interactive solution to extract actionable insights from post-contact center transcripts.
+  + [Conversational Knowledge Mining solution accelerator](https://github.com/microsoft/Customer-Service-Conversational-Insights-with-Azure-OpenAI-Services)
 
-  + ["Build your own copilot" solution accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator), leverages Azure OpenAI Service, Azure AI Search and Microsoft Fabric, to create custom copilot solutions.
+  + [Build your own copilot solution accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator)
 
-    + [Client Advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ClientAdvisor/README.md) all-in-one custom copilot empowers Client Advisor to harness the power of generative AI across both structured and unstructured data. Help our customers to optimize daily tasks and foster better interactions with more clients
+    + [Client Advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ClientAdvisor/README.md)
 
-    + [Research Assistant](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ResearchAssistant/README.md) helps build your own AI Assistant to identify relevant documents, summarize and categorize vast amounts of unstructured information, and accelerate the overall document review and content generation.
+    + [Research Assistant](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ResearchAssistant/README.md)
+
+    + [Generic copilot](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator)
 
 + [Use enterprise chat app templates](https://aka.ms/azai) deploy Azure resources, code, and sample grounding data using fictitious health plan documents for Contoso and Northwind. This end-to-end solution gives you an operational chat app in as little as 15 minutes. Code for these templates is the **azure-search-openai-demo** featured in several presentations. The following links provide language-specific versions:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RAGソリューションアクセラレーターの情報更新"
}
```

### Explanation
この変更は、「retrieval-augmented-generation-overview.md」文書に対する軽微な更新を示します。主な更新内容は、RAG（Retrieval-Augmented Generation）ソリューションに関するアクセラレーターの情報の強化と再構成です。

具体的には、既存のソリューションアクセラレーターを説明する各項目の書き方が統一され、リンク表記が一貫性を持って整理されています。例えば、「Chat with your data」や「Conversational Knowledge Mining」、「Build your own copilot」など、各アクセラレーターの名前が一貫して表記され、ユーザーが情報を容易に把握できるようになっています。

さらに、新しい「Generic copilot」アクセラレーターが追加され、ユーザーはさまざまな生成AIの利用シナリオについてより幅広い選択肢を持つことができます。また、エンタープライズチャットアプリテンプレートに関する説明も追加され、リソースのデプロイ方法や実用的なアプリケーションの構築が可能であることが強調されています。

この更新は、RAGソリューションを利用する開発者やユーザーにとって、より効果的にリソースを活用できるようにするための内容を充実させることを目的としています。

## articles/search/samples-python.md{#item-d2bf09}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: conceptual
-ms.date: 09/19/2024
+ms.date: 10/07/2024
 ---
 
 # Python samples for Azure AI Search
@@ -55,6 +55,7 @@ The following samples are also published by the Azure AI Search team, but aren't
 
 | Repository | Description |
 |------------|-------------|
+| [aisearch-openai-rag-audio](https://github.com/Azure-Samples/aisearch-openai-rag-audio) | A simple architecture for voice-based generative AI applications that enables Azure AI Search RAG on top of the real-time audio API with full-duplex audio streaming from client devices, while securely handling access to both model and retrieval system. Backend code is written in Python. Frontend code is JavaScript. |
 | [azure-search-backup-and-restore.ipynb](https://github.com/Azure/azure-search-vector-samples/tree/main/demo-python/code/index-backup-restore) | Uses the **azure.search.documents** library in the Azure SDK for Python to make a local copy of the retrievable fields of a search index, and then push those fields to a new search index. |
 
 > [!TIP]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PythonサンプルにRAGオーディオアーキテクチャを追加"
}
```

### Explanation
この変更は、「samples-python.md」文書に対する軽微な更新を示しています。具体的には、リリース日の日付の更新と、新しいサンプルリポジトリの追加が行われました。

まず、文書の日付が「09/19/2024」から「10/07/2024」に変更され、最新の情報が反映されています。次に、Azure AI Searchチームによって公開された新しいリポジトリ「aisearch-openai-rag-audio」が追加されました。このリポジトリは、音声ベースの生成AIアプリケーションのためのシンプルなアーキテクチャを提供し、リアルタイムオーディオAPI上でAzure AI SearchのRAGを利用できることを特徴としています。バックエンドのコードはPythonで、フロントエンドのコードはJavaScriptで作成されています。

この更新により、ユーザーはPythonを使用したAzure AI Searchに関連する新しいサンプルを簡単に参照できるようになり、利用方法を理解しやすくなることを目的としています。全体的に、文書はユーザーに対して現在で役立つ情報を提供する内容となっています。

## articles/search/search-create-service-portal.md{#item-f90159}

<details>
<summary>Diff</summary>
````diff
@@ -212,15 +212,7 @@ Depending on region and datacenter capacity, you can automatically request more
 
    :::image type="content" source="media/search-create-service-portal/quota-pencil-edit.png" lightbox="media/search-create-service-portal/quota-pencil-edit.png" alt-text="Screenshot of the My Quotas page with a region at maximum quota.":::
 
-1. In **Quota details**, specify the location, tier, and a new limit for your subscription quota. None of the values can be empty. The new limit must be greater than the current limit, and equal to or lower than the number in the auto-approved quota increase column. For example, for the Basic tier in a given region, if the current limit is 16, your new limit can be between 17 and 80.
-
-   | Tier | Default limit | Auto-approved quota increase | Combined total |
-   |--|--|--|--|
-   | Basic | 16 | 80 | 96 |
-   | S1 | 16 | 30 | 46 |
-   | S2 | 8 | 10 | 18 |
-   | S3, S3HD | 6 | 10 | 16 |
-   | L1, L2 | 6 |  10 | 16 |
+1. In **Quota details**, specify the location, tier, and a new limit for your subscription quota. None of the values can be empty. The new limit must be greater than the current limit. If regional capacity is constrained, your request won't be automatically approved. In this scenario, an incident report is generated on your behalf for investigation and resolution.
 
 1. Submit the request.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービスポータルでのクォータ要求手順の簡略化"
}
```

### Explanation
この変更は、「search-create-service-portal.md」文書におけるクォータ要求手順の軽微な更新を示しています。具体的には、手順の明確化および簡略化が行われました。

元々は、ユーザーが**Quota details**で指定する必要がある情報について、地域やティア（プラン）の詳細に加えて、現在の制限値と新しい制限値に関する具体的なテーブルが含まれていました。しかし、新しい差分ではテーブルの詳細が削除され、代わりに、クォータ要求の承認に関する条件が強調されています。特に、地域の容量が制約されている場合には、リクエストが自動的に承認されない可能性があることが明示されています。この場合、調査および解決のためにインシデントレポートが生成されることが説明されています。

この更新により、手続きがより明確で簡潔になり、ユーザーがどのようにクォータを要求するかを理解しやすくなっています。また、重要な注意事項を強調することで、ユーザーが予期しない問題に直面する可能性を低減させる目的があります。全体として、文書はより効果的に情報を伝える内容に改善されています。

## articles/search/search-get-started-text.md{#item-935941}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: 'Quickstart: Use Azure SDKs'
+title: 'Quickstart: Full text search using the Azure SDKs'
 titleSuffix: Azure AI Search
-description: "Create, load, and query a search index using the Azure SDKs for .NET, Python, Java, and JavaScript."
+description: "Learn how to create, load, and query a search index using the Azure SDKs for .NET, Python, Java, and JavaScript."
 manager: nitinme
 author: HeidiSteen
 ms.author: heidist
@@ -14,41 +14,41 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: quickstart
-ms.date: 04/24/2024
+ms.date: 10/07/2024
 ---
 
 # Quickstart: Full text search using the Azure SDKs
 
-Learn how to use the **Azure.Search.Documents** client library in an Azure SDK to create, load, and query a search index using sample data for [**full text search**](search-lucene-query-architecture.md). Full text search uses Apache Lucene for indexing and queries, and a BM25 ranking algorithm for scoring results.
+Learn how to use the *Azure.Search.Documents* client library in an Azure SDK to create, load, and query a search index using sample data for [full text search](search-lucene-query-architecture.md). Full text search uses Apache Lucene for indexing and queries, and a BM25 ranking algorithm for scoring results.
 
 This quickstart has steps for the following SDKs:
 
 + [Azure SDK for .NET](?tabs=dotnet#create-load-and-query-an-index)
 + [Azure SDK for Python](?tabs=python#create-load-and-query-an-index)
 + [Azure SDK for Java](?tabs=java#create-load-and-query-an-index)
-+ [Azure SDK for JavaScript](?tabs=javascript#create-load-and-query-an-index)
++ [Azure SDK for JavaScript/Typescript](?tabs=javascript#create-load-and-query-an-index)
 
 ## Prerequisites
 
-+ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/).
++ An Azure account with an active subscription. You can [create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?icid=azurefreeaccount).
 
 + An Azure AI Search service. [Create a service](search-create-service-portal.md) if you don't have one. You can use a free tier for this quickstart.
 
-+ An API key and service endpoint. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Search%2FsearchServices).
++ An API key and service endpoint for your service. Sign in to the [Azure portal](https://portal.azure.com) and [find your search service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/CognitiveSearch).
 
-  In **Overview**, copy the URL and save it to Notepad for a later step. An example endpoint might look like `https://mydemo.search.windows.net`.
+  In the **Overview** section, copy the URL and save it to a text editor for a later step. An example endpoint might look like `https://mydemo.search.windows.net`.
 
-  In **Keys**, copy and save an admin key for full rights to create and delete objects. There are two interchangeable primary and secondary keys. Choose either one.
+  In the **Settings** > **Keys** section, copy and save an admin key for full rights to create and delete objects. There are two interchangeable primary and secondary keys. Choose either one.
 
-  ![Get an HTTP endpoint and access key](media/search-get-started-rest/get-url-key.png "Get an HTTP endpoint and access key")
+  :::image type="content" source="media/search-get-started-rest/get-url-key.png" alt-text="Screenshot that shows the HTTP endpoint and the primary and secondary API key locations.":::
 
 ## Create, load, and query an index
 
-Choose a programming language for the next step. The **Azure.Search.Documents** client libraries are available in Azure SDKs for .NET, Python, Java, and JavaScript.
+Choose a programming language for the next step. The **Azure.Search.Documents** client libraries are available in Azure SDKs for .NET, Python, Java, and JavaScript/Typescript.
 
 ## [**.NET**](#tab/dotnet)
 
-[!INCLUDE [python-sdk-quickstart](includes/quickstarts/dotnet.md)]
+[!INCLUDE [dotnet-sdk-quickstart](includes/quickstarts/dotnet.md)]
 
 ## [**Python**](#tab/python)
 
@@ -76,7 +76,7 @@ You can find and manage resources in the portal, using the **All resources** or
 
 If you're using a free service, remember that you're limited to three indexes, indexers, and data sources. You can delete individual items in the portal to stay under the limit.
 
-## Next steps
+## Next step
 
 In this quickstart, you worked through a set of tasks to create an index, load it with documents, and run queries. At different stages, we took shortcuts to simplify the code for readability and comprehension. Now that you're familiar with the basic concepts, try a tutorial that calls the Azure AI Search APIs in a web app.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドのタイトルと内容を更新"
}
```

### Explanation
この変更は、「search-get-started-text.md」文書の軽微な更新を示しています。主な内容として、タイトルと説明の拡張、SDKに関する情報の更新、そしていくつかの表現の改善が行われました。

最初に、ドキュメントのタイトルが「Quickstart: Use Azure SDKs」から「Quickstart: Full text search using the Azure SDKs」に変更され、検索機能の具体的な用途が強調されています。また、説明も改訂され、ユーザーが具体的に何を学ぶのかが明確に示されています。

この更新では、JavaScriptの表記が「Azure SDK for JavaScript」から「Azure SDK for JavaScript/Typescript」に変更され、両方の言語をサポートしていることが示されています。さらに、クォータとAPIキーに関する説明がより具体的になり、ユーザーが必要な手続きを容易に理解できるように調整されています。また、いくつかの表現が変更されており、テキストエディタへのURLコピーの指示が明確になりました。

最後に、次のステップの見出しが「Next steps」から「Next step」に変更され、文脈に合わせた表現の改善が図られています。この更新全体を通じて、ユーザーがAzure SDKを使用してフルテキスト検索を始める際のガイダンスがより明確かつ有益になるように工夫されています。

## articles/search/search-security-manage-encryption-keys.md{#item-db3487}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: how-to
-ms.date: 10/02/2024
+ms.date: 10/07/2024
 ms.custom:
   - references_regions
   - ignite-2023
@@ -69,8 +69,6 @@ Although double encryption is now available in all regions, support was rolled o
 
 + No support for Azure Key Vault Managed Hardware Security Model (HSM).
 
-+ No support for adding encryption keys in the Azure portal.
-
 + No cross-subscription support. Azure Key Vault and Azure AI Search must be in the same subscription.
 
 ## Key Vault tips
@@ -234,7 +232,9 @@ Wait a few minutes for the role assignment to become operational.
 
 ## Step 4: Encrypt content
 
-Encryption keys are added when you create an object. To add a customer-managed key on an index, synonym map, indexer, data source, or skillset, use the [Search REST API](/rest/api/searchservice/) or an Azure SDK to create an object that has encryption enabled. To add encryption using the Azure SDK, see the [Python example](#python-example-of-an-encryption-key-configuration) in this article.
+Encryption keys are added when you create an object. To add a customer-managed key on an index, synonym map, indexer, data source, or skillset, use the Azure portal, a [Search REST API](/rest/api/searchservice/), or an Azure SDK to create an object that has encryption enabled. To add encryption using the Azure SDK, see the [Python example](#python-example-of-an-encryption-key-configuration) in this article.
+
+### [**REST APIs**](#tab/rest)
 
 1. Call the creation APIs to specify the **encryptionKey** property:
 
@@ -291,6 +291,22 @@ None of these key vault details are considered secret and could be easily retrie
 > [!Important]
 > Encrypted content in Azure AI Search is configured to use a specific Azure Key Vault key with a specific *version*. If you change the key or version, the object must be updated to use it **before** you delete the previous one. Failing to do so renders the object unusable. You won't be able to decrypt the content if the key is lost.
 
+### [**Azure portal**](#tab/portal)
+
+When you create a new object in the Azure portal, you can specify a predefined customer-managed key in a key vault. You can enable CMK-encryption for:
+
++ Indexes
++ Data sources
++ Indexers
+
+Requirements for using the portal are that the key vault and key must exist, and you completed the previous steps for authorized access to the key.
+
+In the Azure portal, skillsets are defined in JSON view. Use the JSON shown in the REST API examples to provide a customer-managed key on a skillset.
+
+:::image type="content" source="media/search-security-manage-encryption-keys/assign-key-vault-portal.png" alt-text="Screenshot of the encryption key page in the Azure portal.":::
+
+---
+
 ## Step 5: Test encryption
 
 To verify encryption is working, revoke the encryption key, query the index (it should be unusable), and then reinstate the encryption key.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "暗号化キーの管理に関する手順の更新"
}
```

### Explanation
この変更は、「search-security-manage-encryption-keys.md」文書の更新を示しており、暗号化キーの管理に関する手順が明確化および拡充されています。具体的には、いくつかの新しい情報が追加され、既存の内容が改訂されています。

最初に、文書の更新日付が10月2日から10月7日に変更されており、最新の情報に合わせたものとなっています。さらに、Azureポータルを使用して顧客管理キー（CMK）を指定する手順に関する情報が追加され、ユーザーがAzureポータル内で新しいオブジェクトを作成する際の具体的な説明が盛り込まれました。

加えて、暗号化キーの追加方法について、REST APIの使用だけでなく、AzureポータルやAzure SDKを通じてのサポートも明示され、ユーザーにとって利便性が向上しています。特に、Azureポータルでのキー割り当てに関する新しいセクションが設けられ、具体的な要件や手順が説明されています。また、キーの設定ページのスクリーンショットが追加され、視覚的なガイドが提供されています。

一方で、削除された情報として、Azureポータルにおける暗号化キーの追加に関する記載があり、これが全体の手順の明確性を高めています。この更新によって、ユーザーは暗号化キーを使ったセキュリティ管理をより効果的に実施できるようになります。全体として、文書はユーザーが暗号化を設定する際の理解を深めるために改善されています。

## articles/search/search-what-is-azure-search.md{#item-93853a}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: cognitive-search
 ms.topic: overview
-ms.date: 08/15/2024
+ms.date: 10/08/2024
 ---
 
 # What's Azure AI Search?
@@ -77,6 +77,8 @@ For more information about specific functionality, see [Features of Azure AI Sea
 
 Functionality is exposed through the Azure portal, simple [REST APIs](/rest/api/searchservice/), or Azure SDKs like the [Azure SDK for .NET](search-howto-dotnet-sdk.md). The Azure portal supports service administration and content management, with tools for prototyping and querying your indexes and skillsets. 
 
+### Use the Azure portal
+
 An end-to-end exploration of core search features can be accomplished in four steps:
 
 1. [**Decide on a tier**](search-sku-tier.md) and region. One free search service is allowed per subscription. All quickstarts can be completed on the free tier. For more capacity and capabilities, you'll need a [billable tier](https://azure.microsoft.com/pricing/details/search/).
@@ -87,6 +89,8 @@ An end-to-end exploration of core search features can be accomplished in four st
 
 1. [**Finish with Search Explorer**](search-explorer.md), using a portal client to query the search index you just created.
 
+### Use APIs
+
 Alternatively, you can create, load, and query a search index in atomic steps:
 
 1. [**Create a search index**](search-what-is-an-index.md) using the portal, [REST API](/rest/api/searchservice/indexes/create), [.NET SDK](search-howto-dotnet-sdk.md), or another SDK. The index schema defines the structure of searchable content.
@@ -95,6 +99,8 @@ Alternatively, you can create, load, and query a search index in atomic steps:
 
 1. [**Query an index**](search-query-overview.md) using [Search explorer](search-explorer.md) in the portal, [REST API](search-get-started-rest.md), [.NET SDK](/dotnet/api/azure.search.documents.searchclient.search), or another SDK.
 
+### Use accelerators
+
 Or, try solution accelerators:
 
 + [**Chat with your data** solution accelerator](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) helps you create a custom RAG solution over your content.
@@ -103,6 +109,8 @@ Or, try solution accelerators:
 
 + [**Build your own copilot** solution accelerator](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator), leverages Azure OpenAI Service, Azure AI Search and Microsoft Fabric, to create custom copilot solutions.
 
+  + [Generic copilot](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator) helps you build your own copilot to identify relevant documents, summarize unstructured information, and generate Word document templates using your own data.
+
   + [Client Advisor](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ClientAdvisor/README.md) all-in-one custom copilot empowers Client Advisor to harness the power of generative AI across both structured and unstructured data. Help our customers to optimize daily tasks and foster better interactions with more clients
 
   + [Research Assistant](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator/blob/main/ResearchAssistant/README.md) helps build your own AI Assistant to identify relevant documents, summarize and categorize vast amounts of unstructured information, and accelerate the overall document review and content generation.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchに関する機能の追加"
}
```

### Explanation
この変更は、「search-what-is-azure-search.md」文書における軽微な更新を示しており、Azure AI Searchの機能に関する説明が追加されています。主な更新点として、文書の更新日が2024年8月15日から2024年10月8日に変更され、新しい情報がいくつか付加されました。

具体的には、Azureポータルを使用した検索機能の探索や、APIを活用したデータの作成・管理に関する新しいセクションが追加されました。ユーザーがAzureインデックスを作成する際の手順が、AzureポータルやREST APIを通じて明示され、さらに簡潔なプロセスとして説明されています。

また、解決策を加速するためのソリューションアクセラレーターに関する具体的な情報も提供され、ユーザーがさまざまな用途に応じてAzure AI Searchを活用できる方法が示されています。これにより、利用者は自分のデータに基づいたカスタムソリューションを構築したり、特定の業務ニーズに対処したりするための適切な手段を見つけやすくなっています。

全体として、この更新はAzure AI Searchの概要とその機能をより具体的に伝えるものであり、ユーザーにとって理解しやすく、実践的な情報が強化されています。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -28,6 +28,7 @@ ms.custom:
 | [**Target filters in a hybrid search to just the vector queries**](hybrid-search-how-to-query.md#hybrid-search-with-filters-targeting-vector-subqueries-preview) | Feature | A filter on a hybrid query involves all subqueries on the request, regardless of type. You can override the global filter to scope the filter to a specific subquery. The new `filterOverride` parameter is available on hybrid queries using the [2024-09-01-preview](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
 | [**Text Split skill (token chunking)**](cognitive-search-skill-textsplit.md) | Applied AI (skills) | This skill has new parameters that improve data chunking for embedding models. A new `unit` parameter lets you specify token chunking. You can now chunk by token length, setting the length to a value that makes sense for your embedding model. You can also specify the tokenizer and any tokens that shouldn't be split during data chunking. The new `unit` parameter and query subscore definitions are found in the [2024-09-01-preview](/rest/api/searchservice/skillsets/create-or-update?view=rest-searchservice-2024-09-01-preview&preserve-view=true). |
 | [**2024-09-01-preview**](/rest/api/searchservice/search-service-api-versions?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | API | Preview release of REST APIs for truncated dimensions in text-embedding-3 models, targeted vector filtering for hybrid queries, RRF subscore details for debugging, and token chunking for Text Split skill.|
+| [**Portal support for customer-managed key encryption (CMK)**](/azure/search/search-security-manage-encryption-keys?tabs=portal#step-4-encrypt-content) | Feature | When you create new objects in the Azure portal, you can now specify CMK-encryption and select an Azure Key Vault to provide the key. |
 
 ## August 2024
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルでの顧客管理キー暗号化のサポート追加"
}
```

### Explanation
この変更は、「whats-new.md」文書における軽微な更新を示しており、Azureポータルに新たに追加された機能についての情報が提供されています。主な更新点として、顧客管理キー（CMK）暗号化のサポートに関する内容が追加されました。

具体的には、Azureポータルで新しいオブジェクトを作成する際に、CMK暗号化を指定し、Azure Key Vaultから鍵を選択できるようになったことが記載されています。これにより、ユーザーは自身のセキュリティ要件を満たすために、より柔軟に暗号化を管理できるようになります。

この更新は、Azure AI Searchの機能強化として重要であり、セキュリティとデータ保護に関心を持つユーザーにとって役立つ情報です。全体として、この変更はAzureのユーザー体験を向上させるための重要な情報を提供しており、ユーザーが新しい機能を活用しやすくなっています。


