---
date: '2025-02-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:17e9068...MicrosoftDocs:f9aa01e
summary: この変更により、C#およびJavaのクイックスタートガイドのコードがリファクタリングされ、ドキュメントの更新が行われました。具体的には、画像ファイルが削除され、日付が更新され、説明が明確にされました。Javaのガイドではプロジェクト設定と依存関係が明示され、具体的なpom.xmlファイルの例が追加されました。また、セマンティック検索の機能も強化され、クエリリライト機能の詳細が紹介されています。これにより、開発者の理解が深まり、一貫したコーディングが促進されます。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:17e9068...MicrosoftDocs:f9aa01e){target="_blank"}

# ハイライト

C#およびJavaのクイックスタートガイドのコードがリファクタリングされ、画像ファイルの削除やドキュメントの日付更新、説明の明確化が行われました。また、Azure AI Search関連のドキュメントで、依存関係の簡略化やセマンティック検索に関する記述が更新され、ユーザーの理解を助ける内容となっています。

## 新機能
- Javaのクイックスタートガイドでプロジェクト設定および依存関係の明示が行われ、pom.xmlファイルの具体例を追加。
- セマンティック検索概要で、クエリリライト機能が紹介され、LLMを使用したクエリの拡張について説明。

## 破壊的変更
- 画像ファイルの削除により、視覚的補助が減少した。

## その他の更新
- C#コードでのクライアント名の一貫化。
- Azure AI SearchのドキュメントでAPIバージョン日付や説明の更新、JavaのAzure Identityライブラリの依存関係簡略化。

# インサイト

この変更により、開発者がAzure AI Searchを使用したコードを書く際の一貫性が向上し、JavaとC#両方で明確に示されたリファクタリングは保守性を高めています。

C#のクライアント名の統一は、コードの読みやすさを高め、理解しやすい変数名を通じて意味のある役割分担を視覚的に示しています。これにより、異なるクライアントの機能をより容易に識別できるようになりました。

Javaのクイックスタートガイドにおける大幅な更新は、新規ユーザーに対する敷居の低下を目指したもので、依存関係や環境設定の手順が明確化され、スムーズなセットアップを可能にします。また、画像ファイルの削除は、古い資料の整理や視覚的冗長性を除去することを意図しています。

セマンティック検索およびクエリに関する改訂では、生成的AIや大規模言語モデル（LLM）の理解を必要とする開発者に向け、具体的な技術的詳細を提示しています。これにより、Azure AI Searchの高度な機能の理解と応用が容易になると共に、効率的な検索体験の提供が可能となっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [full-text-csharp.md](#item-2e943a) | minor update | C#コードのクライアント名の統一 | modified | 32 | 32 | 64 | 
| [full-text-java.md](#item-d659f9) | minor update | Javaコードクイックスタートの更新 | modified | 545 | 322 | 867 | 
| [keyless-connections.md](#item-3f0d72) | minor update | キーレス接続の依存関係の更新 | modified | 0 | 2 | 2 | 
| [java-quickstart-artifact-id.png](#item-fe2374) | minor update | 画像ファイルの削除 | removed | 0 | 0 | 0 | 
| [java-quickstart-create-project.png](#item-dc3528) | minor update | 画像ファイルの削除 | removed | 0 | 0 | 0 | 
| [java-quickstart-finish-setup-terminal.png](#item-985794) | minor update | 画像ファイルの削除 | removed | 0 | 0 | 0 | 
| [java-quickstart-group-id.png](#item-de0a24) | minor update | 画像ファイルの削除 | removed | 0 | 0 | 0 | 
| [java-quickstart-select-maven-project-type.png](#item-cdc430) | minor update | 画像ファイルの削除 | removed | 0 | 0 | 0 | 
| [java-quickstart-select-maven.png](#item-6d5b91) | minor update | 画像ファイルの削除 | removed | 0 | 0 | 0 | 
| [search-api-versions.md](#item-69ca3e) | minor update | APIバージョンに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [search-get-started-portal-import-vectors.md](#item-7dae77) | minor update | ポータルでのベクターインポートに関するドキュメント修正 | modified | 1 | 1 | 2 | 
| [semantic-answers.md](#item-c3fee9) | minor update | セマンティック回答に関するドキュメントの更新 | modified | 2 | 3 | 5 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | セマンティッククエリリクエストに関するドキュメントの更新 | modified | 2 | 2 | 4 | 
| [semantic-search-overview.md](#item-b7497b) | minor update | セマンティック検索の概要に関するドキュメントの更新 | modified | 11 | 6 | 17 | 


# Modified Contents
## articles/search/includes/quickstarts/full-text-csharp.md{#item-2e943a}

<details>
<summary>Diff</summary>
````diff
@@ -108,21 +108,21 @@ AzureKeyCredential credential = new AzureKeyCredential("<Your search service adm
                 //AzureKeyCredential credential = new AzureKeyCredential("Your search service admin key");
     
                 // Create a SearchIndexClient to send create/delete index commands
-                SearchIndexClient adminClient = new SearchIndexClient(serviceEndpoint, credential);
+                SearchIndexClient searchIndexClient = new SearchIndexClient(serviceEndpoint, credential);
     
                 // Create a SearchClient to load and query documents
                 string indexName = "hotels-quickstart";
-                SearchClient srchclient = new SearchClient(serviceEndpoint, indexName, credential);
+                SearchClient searchClient = new SearchClient(serviceEndpoint, indexName, credential);
     
                 // Delete index if it exists
                 Console.WriteLine("{0}", "Deleting index...\n");
-                DeleteIndexIfExists(indexName, adminClient);
+                DeleteIndexIfExists(indexName, searchIndexClient);
     
                 // Create index
                 Console.WriteLine("{0}", "Creating index...\n");
-                CreateIndex(indexName, adminClient);
+                CreateIndex(indexName, searchIndexClient);
     
-                SearchClient ingesterClient = adminClient.GetSearchClient(indexName);
+                SearchClient ingesterClient = searchIndexClient.GetSearchClient(indexName);
     
                 // Load documents
                 Console.WriteLine("{0}", "Uploading documents...\n");
@@ -134,23 +134,23 @@ AzureKeyCredential credential = new AzureKeyCredential("<Your search service adm
     
                 // Call the RunQueries method to invoke a series of queries
                 Console.WriteLine("Starting queries...\n");
-                RunQueries(srchclient);
+                RunQueries(searchClient);
     
                 // End the program
                 Console.WriteLine("{0}", "Complete. Press any key to end this program...\n");
                 Console.ReadKey();
             }
     
             // Delete the hotels-quickstart index to reuse its name
-            private static void DeleteIndexIfExists(string indexName, SearchIndexClient adminClient)
+            private static void DeleteIndexIfExists(string indexName, SearchIndexClient searchIndexClient)
             {
-                adminClient.GetIndexNames();
+                searchIndexClient.GetIndexNames();
                 {
-                    adminClient.DeleteIndex(indexName);
+                    searchIndexClient.DeleteIndex(indexName);
                 }
             }
             // Create hotels-quickstart index
-            private static void CreateIndex(string indexName, SearchIndexClient adminClient)
+            private static void CreateIndex(string indexName, SearchIndexClient searchIndexClient)
             {
                 FieldBuilder fieldBuilder = new FieldBuilder();
                 var searchFields = fieldBuilder.Build(typeof(Hotel));
@@ -160,7 +160,7 @@ AzureKeyCredential credential = new AzureKeyCredential("<Your search service adm
                 var suggester = new SearchSuggester("sg", new[] { "HotelName", "Category", "Address/City", "Address/StateProvince" });
                 definition.Suggesters.Add(suggester);
     
-                adminClient.CreateOrUpdateIndex(definition);
+                searchIndexClient.CreateOrUpdateIndex(definition);
             }
     
             // Upload documents in a single Upload request.
@@ -266,7 +266,7 @@ AzureKeyCredential credential = new AzureKeyCredential("<Your search service adm
             }
     
             // Run queries, use WriteDocuments to print output
-            private static void RunQueries(SearchClient srchclient)
+            private static void RunQueries(SearchClient searchClient)
             {
                 SearchOptions options;
                 SearchResults<Hotel> response;
@@ -285,7 +285,7 @@ AzureKeyCredential credential = new AzureKeyCredential("<Your search service adm
                 options.Select.Add("HotelName");
                 options.Select.Add("Rating");
     
-                response = srchclient.Search<Hotel>("*", options);
+                response = searchClient.Search<Hotel>("*", options);
                 WriteDocuments(response);
     
                 // Query 2
@@ -301,7 +301,7 @@ AzureKeyCredential credential = new AzureKeyCredential("<Your search service adm
                 options.Select.Add("HotelName");
                 options.Select.Add("Rating");
     
-                response = srchclient.Search<Hotel>("hotels", options);
+                response = searchClient.Search<Hotel>("hotels", options);
                 WriteDocuments(response);
     
                 // Query 3
@@ -316,7 +316,7 @@ AzureKeyCredential credential = new AzureKeyCredential("<Your search service adm
                 options.Select.Add("HotelName");
                 options.Select.Add("Tags");
     
-                response = srchclient.Search<Hotel>("pool", options);
+                response = searchClient.Search<Hotel>("pool", options);
                 WriteDocuments(response);
     
                 // Query 4 - Use Facets to return a faceted navigation structure for a given query
@@ -334,22 +334,22 @@ AzureKeyCredential credential = new AzureKeyCredential("<Your search service adm
                 options.Select.Add("HotelName");
                 options.Select.Add("Category");
     
-                response = srchclient.Search<Hotel>("*", options);
+                response = searchClient.Search<Hotel>("*", options);
                 WriteDocuments(response);
     
                 // Query 5
                 Console.WriteLine("Query #5: Look up a specific document...\n");
     
                 Response<Hotel> lookupResponse;
-                lookupResponse = srchclient.GetDocument<Hotel>("3");
+                lookupResponse = searchClient.GetDocument<Hotel>("3");
     
                 Console.WriteLine(lookupResponse.Value.HotelId);
     
     
                 // Query 6
                 Console.WriteLine("Query #6: Call Autocomplete on HotelName...\n");
     
-                var autoresponse = srchclient.Autocomplete("sa", "sg");
+                var autoresponse = searchClient.Autocomplete("sa", "sg");
                 WriteDocuments(autoresponse);
     
             }
@@ -651,11 +651,11 @@ static void Main(string[] args)
     //AzureKeyCredential credential = new AzureKeyCredential("Your search service admin key");
 
     // Create a SearchIndexClient to send create/delete index commands
-    SearchIndexClient adminClient = new SearchIndexClient(serviceEndpoint, credential);
+    SearchIndexClient searchIndexClient = new SearchIndexClient(serviceEndpoint, credential);
 
     // Create a SearchClient to load and query documents
     string indexName = "hotels-quickstart";
-    SearchClient srchclient = new SearchClient(serviceEndpoint, indexName, credential);
+    SearchClient searchClient = new SearchClient(serviceEndpoint, indexName, credential);
     
     // REDACTED FOR BREVITY . . . 
 }
@@ -685,7 +685,7 @@ In *Program.cs*, you create a [SearchIndex](/dotnet/api/azure.search.documents.i
 
 ```csharp
 // Create hotels-quickstart index
-private static void CreateIndex(string indexName, SearchIndexClient adminClient)
+private static void CreateIndex(string indexName, SearchIndexClient searchIndexClient)
 {
     FieldBuilder fieldBuilder = new FieldBuilder();
     var searchFields = fieldBuilder.Build(typeof(Hotel));
@@ -695,7 +695,7 @@ private static void CreateIndex(string indexName, SearchIndexClient adminClient)
     var suggester = new SearchSuggester("sg", new[] { "HotelName", "Category", "Address/City", "Address/StateProvince" });
     definition.Suggesters.Add(suggester);
 
-    adminClient.CreateOrUpdateIndex(definition);
+    searchIndexClient.CreateOrUpdateIndex(definition);
 }
 ```
 
@@ -741,10 +741,10 @@ private static void UploadDocuments(SearchClient searchClient)
 
 Once you initialize the [IndexDocumentsBatch](/dotnet/api/azure.search.documents.models.indexdocumentsbatch-1) object, you can send it to the index by calling [IndexDocuments](/dotnet/api/azure.search.documents.searchclient.indexdocuments) on your [SearchClient](/dotnet/api/azure.search.documents.searchclient) object.
 
-You load documents using SearchClient in `Main()`, but the operation also requires admin rights on the service, which is typically associated with SearchIndexClient. One way to set up this operation is to get SearchClient through `SearchIndexClient` (`adminClient` in this example).
+You load documents using SearchClient in `Main()`, but the operation also requires admin rights on the service, which is typically associated with SearchIndexClient. One way to set up this operation is to get SearchClient through `SearchIndexClient` (`searchIndexClient` in this example).
 
 ```csharp
-SearchClient ingesterClient = adminClient.GetSearchClient(indexName);
+SearchClient ingesterClient = searchIndexClient.GetSearchClient(indexName);
 
 // Load documents
 Console.WriteLine("{0}", "Uploading documents...\n");
@@ -796,11 +796,11 @@ private static void WriteDocuments(AutocompleteResults autoResults)
 
 #### Query example 1
 
-The `RunQueries` method executes queries and returns results. Results are Hotel objects. This sample shows the method signature and the first query. This query demonstrates the Select parameter that lets you compose the result using selected fields from the document.
+The `RunQueries` method executes queries and returns results. Results are Hotel objects. This sample shows the method signature and the first query. This query demonstrates the `Select` parameter that lets you compose the result using selected fields from the document.
 
 ```csharp
 // Run queries, use WriteDocuments to print output
-private static void RunQueries(SearchClient srchclient)
+private static void RunQueries(SearchClient searchClient)
 {
     SearchOptions options;
     SearchResults<Hotel> response;
@@ -819,7 +819,7 @@ private static void RunQueries(SearchClient srchclient)
     options.Select.Add("HotelName");
     options.Select.Add("Address/City");
 
-    response = srchclient.Search<Hotel>("*", options);
+    response = searchClient.Search<Hotel>("*", options);
     WriteDocuments(response);
     // REDACTED FOR BREVITY
 }
@@ -843,7 +843,7 @@ options.Select.Add("HotelId");
 options.Select.Add("HotelName");
 options.Select.Add("Rating");
 
-response = srchclient.Search<Hotel>("hotels", options);
+response = searchClient.Search<Hotel>("hotels", options);
 WriteDocuments(response);
 ```
 
@@ -863,7 +863,7 @@ options.Select.Add("HotelId");
 options.Select.Add("HotelName");
 options.Select.Add("Tags");
 
-response = srchclient.Search<Hotel>("pool", options);
+response = searchClient.Search<Hotel>("pool", options);
 WriteDocuments(response);
 ```
 
@@ -886,7 +886,7 @@ options.Select.Add("HotelId");
 options.Select.Add("HotelName");
 options.Select.Add("Category");
 
-response = srchclient.Search<Hotel>("*", options);
+response = searchClient.Search<Hotel>("*", options);
 WriteDocuments(response);
 ```
 
@@ -899,7 +899,7 @@ In the fifth query, return a specific document. A document lookup is a typical r
 Console.WriteLine("Query #5: Look up a specific document...\n");
 
 Response<Hotel> lookupResponse;
-lookupResponse = srchclient.GetDocument<Hotel>("3");
+lookupResponse = searchClient.GetDocument<Hotel>("3");
 
 Console.WriteLine(lookupResponse.Value.HotelId);
 ```
@@ -912,7 +912,7 @@ The last query shows the syntax for autocomplete, simulating a partial user inpu
 // Query 6
 Console.WriteLine("Query #6: Call Autocomplete on HotelName that starts with 'sa'...\n");
 
-var autoresponse = srchclient.Autocomplete("sa", "sg");
+var autoresponse = searchClient.Autocomplete("sa", "sg");
 WriteDocuments(autoresponse);
 ```
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#コードのクライアント名の統一"
}
```

### Explanation
この変更では、C#コード内の`SearchIndexClient`と`SearchClient`のインスタンス名を一貫性のある名称に統一しました。具体的には、`adminClient`と`srchclient`という名前がそれぞれ`searchIndexClient`と`searchClient`に変更され、可読性が向上しています。これにより、コードのメンテナンスが容易になり、異なるクライアント間の役割を明確にし、ユーザーが実際の機能に基づいてクライアントの目的をより簡単に理解できるようになりました。変更点はすべてのインスタンスで反映され、合計で32行の追加と32行の削除が行われています。このリファクタリングにより、コードの可視性と一貫性が向上しました。

## articles/search/includes/quickstarts/full-text-java.md{#item-d659f9}

<details>
<summary>Diff</summary>
````diff
@@ -27,85 +27,94 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 [!INCLUDE [resource authentication](../resource-authentication.md)]
 
-## Set up your environment
+## Set up
 
-Use the following tools to create this quickstart.
+The sample in this quickstart works with the Java Runtime. Install a Java Development Kit such as [Azul Zulu OpenJDK](https://www.azul.com/downloads/?package=jdk). The [Microsoft Build of OpenJDK](https://www.microsoft.com/openjdk) or your preferred JDK should also work.
 
-+ [Visual Studio Code with the Java extension](https://code.visualstudio.com/docs/java/extensions)
+1. Install [Apache Maven](https://maven.apache.org/install.html). Then run `mvn -v` to confirm successful installation.
+1. Create a new `pom.xml` file in the root of your project, and copy the following code into it:
 
-+ [Java 11 SDK](/java/azure/jdk/)
-
-## Create the project
-
-1. Start Visual Studio Code.
-
-1. Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) by using **Ctrl+Shift+P**. Search for **Create Java Project**.
-
-   :::image type="content" source="../../media/search-get-started-java/java-quickstart-create-project.png" alt-text="Screenshot of a Java project." border="true":::
-
-1. Select **Maven**.
-
-   :::image type="content" source="../../media/search-get-started-java/java-quickstart-select-maven.png" alt-text="Screenshot of a maven project." border="true":::
-
-1. Select **maven-archetype-quickstart**.
-
-   :::image type="content" source="../../media/search-get-started-java/java-quickstart-select-maven-project-type.png" alt-text="Screenshot of a maven quickstart project." border="true":::
-
-1. Select the latest version, currently **1.4**.
-
-   :::image type="content" source="../../media/search-get-started-java/java-quickstart-group-id.png" alt-text="Screenshot of the group ID location." border="true":::
-
-1. Enter **azure.search.sample** as the group ID.
-
-   :::image type="content" source="../../media/search-get-started-java/java-quickstart-group-id.png" alt-text="Screenshot of the group ID for search." border="true":::
+    ```xml
+    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
+        <modelVersion>4.0.0</modelVersion>
+        <groupId>azure.search.sample</groupId>
+        <artifactId>azuresearchquickstart</artifactId>
+        <version>1.0.0-SNAPSHOT</version>
+        <build>
+            <sourceDirectory>src</sourceDirectory>
+            <plugins>
+            <plugin>
+                <artifactId>maven-compiler-plugin</artifactId>
+                <version>3.7.0</version>
+                <configuration>
+                <source>1.8</source>
+                <target>1.8</target>
+                </configuration>
+            </plugin>
+            </plugins>
+        </build>
+        <dependencies>
+            <dependency>
+                <groupId>junit</groupId>
+                <artifactId>junit</artifactId>
+                <version>4.11</version>
+                <scope>test</scope>
+            </dependency>
+            <dependency>
+                <groupId>com.azure</groupId>
+                <artifactId>azure-search-documents</artifactId>
+                <version>11.7.3</version>
+            </dependency>
+            <dependency>
+                <groupId>com.azure</groupId>
+                <artifactId>azure-core</artifactId>
+                <version>1.53.0</version>
+            </dependency>
+            <dependency>
+                <groupId>com.azure</groupId>
+                <artifactId>azure-identity</artifactId>
+                <version>1.15.1</version>
+            </dependency>
+        </dependencies>
+    </project>
+    ```
 
-1. Enter **azuresearchquickstart** as the artifact ID.
+1. Install the dependencies including the Azure AI Search client library ([Azure.Search.Documents](/java/api/overview/azure/search)) for Java and [Azure Identity client library for Java](https://mvnrepository.com/artifact/com.azure/azure-identity) with:
 
-   :::image type="content" source="../../media/search-get-started-java/java-quickstart-artifact-id.png" alt-text="Screenshot of an artifact ID." border="true":::
+   ```console
+   mvn clean dependency:copy-dependencies
+   ```
 
-1. Select the folder to create the project in.
+1. For the **recommended** keyless authentication with Microsoft Entra ID, sign in to Azure with the following command:
 
-1. Finish project creation in the [integrated terminal](https://code.visualstudio.com/docs/terminal/basics). Press enter to accept the default for "1.0-SNAPSHOT" and then type "y" to confirm the properties for your project.
+    ```console
+    az login
+    ```
 
-    :::image type="content" source="../../media/search-get-started-java/java-quickstart-finish-setup-terminal.png" alt-text="Screenshot of the finished project definition." border="true":::
+## Create, load, and query a search index
 
-1. Open the folder you created the project in.
+In the prior [set up](#set-up) section, you created a new console application and installed the Azure AI Search client library. 
 
-## Specify Maven dependencies
+In this section, you add code to create a search index, load it with documents, and run queries. You run the program to see the results in the console. For a detailed explanation of the code, see the [explaining the code](#explaining-the-code) section.
 
-1. Open the *pom.xml* file and add the following dependencies. This includes the [Azure.Search.Documents](/java/api/overview/azure/search) library.
+The sample code in this quickstart uses Microsoft Entra ID for authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
 
-    ```xml
-    <dependencies>
-        <dependency>
-          <groupId>com.azure</groupId>
-          <artifactId>azure-search-documents</artifactId>
-          <version>11.7.3</version>
-        </dependency>
-        <dependency>
-          <groupId>com.azure</groupId>
-          <artifactId>azure-core</artifactId>
-          <version>1.53.0</version>
-        </dependency>
-        <dependency>
-          <groupId>junit</groupId>
-          <artifactId>junit</artifactId>
-          <version>4.11</version>
-          <scope>test</scope>
-        </dependency>
-      </dependencies>
-    ```
+#### [Microsoft Entra ID](#tab/keyless)
 
-1. Change the compiler Java version to 11.
+```java
+String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();
+```
 
-    ```xml
-    <maven.compiler.source>1.11</maven.compiler.source>
-    <maven.compiler.target>1.11</maven.compiler.target>
-    ```
+#### [API key](#tab/api-key)
 
-## Create a search client
+```java
+String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
+```
+---
 
-1. Open the `App` class under **src**, **main**, **java**, **azure**, **search**, **sample**. Add the following import directives.
+1. Create a new file named *App.java* and paste the following code into *App.java*:
 
     ```java
     import java.util.Arrays;
@@ -115,59 +124,249 @@ Use the following tools to create this quickstart.
     import java.time.LocalDateTime;
     import java.time.LocalDate;
     import java.time.LocalTime;
-    
-    import com.azure.core.credential.AzureKeyCredential;
+    import com.azure.core.util.Configuration;
     import com.azure.core.util.Context;
+    import com.azure.identity.DefaultAzureCredential;
+    import com.azure.identity.DefaultAzureCredentialBuilder;
     import com.azure.search.documents.SearchClient;
     import com.azure.search.documents.SearchClientBuilder;
-    import com.azure.search.documents.models.SearchOptions;
     import com.azure.search.documents.indexes.SearchIndexClient;
     import com.azure.search.documents.indexes.SearchIndexClientBuilder;
     import com.azure.search.documents.indexes.models.IndexDocumentsBatch;
+    import com.azure.search.documents.models.SearchOptions;
     import com.azure.search.documents.indexes.models.SearchIndex;
     import com.azure.search.documents.indexes.models.SearchSuggester;
     import com.azure.search.documents.util.AutocompletePagedIterable;
     import com.azure.search.documents.util.SearchPagedIterable;
-    ```
-
-1. The following example includes placeholders for a search service name, admin API key that grants create and delete permissions, and index name. Substitute valid values for all three placeholders. Create two clients: [SearchIndexClient](/java/api/com.azure.search.documents.indexes.searchindexclient) creates the index, and [SearchClient](/java/api/com.azure.search.documents.searchclient) loads and queries an existing index. Both need the service endpoint and an admin API key for authentication with create and delete rights.
-
-
-    ```java
-    public static void main(String[] args) {
-        var searchServiceEndpoint = "<YOUR-SEARCH-SERVICE-URL>";
-        var adminKey = new AzureKeyCredential("<YOUR-SEARCH-SERVICE-ADMIN-KEY>");
-        String indexName = "<YOUR-SEARCH-INDEX-NAME>";
-
-        SearchIndexClient searchIndexClient = new SearchIndexClientBuilder()
-            .endpoint(searchServiceEndpoint)
-            .credential(adminKey)
-            .buildClient();
-
-        SearchClient searchClient = new SearchClientBuilder()
-            .endpoint(searchServiceEndpoint)
-            .credential(adminKey)
-            .indexName(indexName)
-            .buildClient();
+    
+    public class App {
+    
+        public static void main(String[] args) {
+            // Your search service endpoint
+            "https://<Put your search service NAME here>.search.windows.net/";
+    
+            // Use the recommended keyless credential instead of the AzureKeyCredential credential.
+            DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();
+            //AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
+    
+            // Create a SearchIndexClient to send create/delete index commands
+            SearchIndexClient searchIndexClient = new SearchIndexClientBuilder()
+                .endpoint(searchServiceEndpoint)
+                .credential(credential)
+                .buildClient();
+            
+            // Create a SearchClient to load and query documents
+            String indexName = "hotels-quickstart-java";
+            SearchClient searchClient = new SearchClientBuilder()
+                .endpoint(searchServiceEndpoint)
+                .credential(credential)
+                .indexName(indexName)
+                .buildClient();
+    
+            // Create Search Index for Hotel model
+            searchIndexClient.createOrUpdateIndex(
+                new SearchIndex(indexName, SearchIndexClient.buildSearchFields(Hotel.class, null))
+                .setSuggesters(new SearchSuggester("sg", Arrays.asList("HotelName"))));
+    
+            // Upload sample hotel documents to the Search Index
+            uploadDocuments(searchClient);
+    
+            // Wait 2 seconds for indexing to complete before starting queries (for demo and console-app purposes only)
+            System.out.println("Waiting for indexing...\n");
+            try
+            {
+                Thread.sleep(2000);
+            }
+            catch (InterruptedException e)
+            {
+            }
+    
+            // Call the RunQueries method to invoke a series of queries
+            System.out.println("Starting queries...\n");
+            RunQueries(searchClient);
+    
+            // End the program
+            System.out.println("Complete.\n");
+        }
+    
+        // Upload documents in a single Upload request.
+        private static void uploadDocuments(SearchClient searchClient)
+        {
+            var hotelList = new ArrayList<Hotel>();
+    
+            var hotel = new Hotel();
+            hotel.hotelId = "1";
+            hotel.hotelName = "Stay-Kay City Hotel";
+            hotel.description = "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.";
+            hotel.descriptionFr = "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.";
+            hotel.category = "Boutique";
+            hotel.tags = new String[] { "pool", "air conditioning", "concierge" };
+            hotel.parkingIncluded = false;
+            hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(1970, 1, 18), LocalTime.of(0, 0)), ZoneOffset.UTC);
+            hotel.rating = 3.6;
+            hotel.address = new Address();
+            hotel.address.streetAddress = "677 5th Ave";
+            hotel.address.city = "New York";
+            hotel.address.stateProvince = "NY";
+            hotel.address.postalCode = "10022";
+            hotel.address.country = "USA";
+            hotelList.add(hotel);
+    
+            hotel = new Hotel();
+            hotel.hotelId = "2";
+            hotel.hotelName = "Old Century Hotel";
+            hotel.description = "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.";
+            hotel.descriptionFr = "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.";
+            hotel.category = "Boutique";
+            hotel.tags = new String[] { "pool", "free wifi", "concierge" };
+            hotel.parkingIncluded = false;
+            hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(1979, 2, 18), LocalTime.of(0, 0)), ZoneOffset.UTC);
+            hotel.rating = 3.60;
+            hotel.address = new Address();
+            hotel.address.streetAddress = "140 University Town Center Dr";
+            hotel.address.city = "Sarasota";
+            hotel.address.stateProvince = "FL";
+            hotel.address.postalCode = "34243";
+            hotel.address.country = "USA";
+            hotelList.add(hotel);
+    
+            hotel = new Hotel();
+            hotel.hotelId = "3";
+            hotel.hotelName = "Gastronomic Landscape Hotel";
+            hotel.description = "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.";
+            hotel.descriptionFr = "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.";
+            hotel.category = "Resort and Spa";
+            hotel.tags = new String[] { "air conditioning", "bar", "continental breakfast" };
+            hotel.parkingIncluded = true;
+            hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(2015, 9, 20), LocalTime.of(0, 0)), ZoneOffset.UTC);
+            hotel.rating = 4.80;
+            hotel.address = new Address();
+            hotel.address.streetAddress = "3393 Peachtree Rd";
+            hotel.address.city = "Atlanta";
+            hotel.address.stateProvince = "GA";
+            hotel.address.postalCode = "30326";
+            hotel.address.country = "USA";
+            hotelList.add(hotel);
+    
+            hotel = new Hotel();
+            hotel.hotelId = "4";
+            hotel.hotelName = "Sublime Palace Hotel";
+            hotel.description = "Sublime Palace  Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.";
+            hotel.descriptionFr = "Le Sublime Palace Hotel est situé au coeur du centre historique de sublime dans un quartier extrêmement animé et vivant, à courte distance de marche des sites et monuments de la ville et est entouré par l'extraordinaire beauté des églises, des bâtiments, des commerces et Monuments. Sublime Palace fait partie d'un Palace 1800 restauré avec amour.";
+            hotel.category = "Boutique";
+            hotel.tags = new String[] { "concierge", "view", "24-hour front desk service" };
+            hotel.parkingIncluded = true;
+            hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(1960, 2, 06), LocalTime.of(0, 0)), ZoneOffset.UTC);
+            hotel.rating = 4.60;
+            hotel.address = new Address();
+            hotel.address.streetAddress = "7400 San Pedro Ave";
+            hotel.address.city = "San Antonio";
+            hotel.address.stateProvince = "TX";
+            hotel.address.postalCode = "78216";
+            hotel.address.country = "USA";
+            hotelList.add(hotel);
+    
+            var batch = new IndexDocumentsBatch<Hotel>();
+            batch.addMergeOrUploadActions(hotelList);
+            try
+            {
+                searchClient.indexDocuments(batch);
+            }
+            catch (Exception e)
+            {
+                e.printStackTrace();
+                // If for some reason any documents are dropped during indexing, you can compensate by delaying and
+                // retrying. This simple demo just logs failure and continues
+                System.err.println("Failed to index some of the documents");
+            }
+        }
+    
+        // Write search results to console
+        private static void WriteSearchResults(SearchPagedIterable searchResults)
+        {
+            searchResults.iterator().forEachRemaining(result ->
+            {
+                Hotel hotel = result.getDocument(Hotel.class);
+                System.out.println(hotel);
+            });
+    
+            System.out.println();
+        }
+    
+        // Write autocomplete results to console
+        private static void WriteAutocompleteResults(AutocompletePagedIterable autocompleteResults)
+        {
+            autocompleteResults.iterator().forEachRemaining(result ->
+            {
+                String text = result.getText();
+                System.out.println(text);
+            });
+    
+            System.out.println();
+        }
+    
+        // Run queries, use WriteDocuments to print output
+        private static void RunQueries(SearchClient searchClient)
+        {
+            // Query 1
+            System.out.println("Query #1: Search on empty term '*' to return all documents, showing a subset of fields...\n");
+    
+            SearchOptions options = new SearchOptions();
+            options.setIncludeTotalCount(true);
+            options.setFilter("");
+            options.setOrderBy("");
+            options.setSelect("HotelId", "HotelName", "Address/City");
+    
+            WriteSearchResults(searchClient.search("*", options, Context.NONE));
+    
+            // Query 2
+            System.out.println("Query #2: Search on 'hotels', filter on 'Rating gt 4', sort by Rating in descending order...\n");
+    
+            options = new SearchOptions();
+            options.setFilter("Rating gt 4");
+            options.setOrderBy("Rating desc");
+            options.setSelect("HotelId", "HotelName", "Rating");
+    
+            WriteSearchResults(searchClient.search("hotels", options, Context.NONE));
+    
+            // Query 3
+            System.out.println("Query #3: Limit search to specific fields (pool in Tags field)...\n");
+    
+            options = new SearchOptions();
+            options.setSearchFields("Tags");
+    
+            options.setSelect("HotelId", "HotelName", "Tags");
+    
+            WriteSearchResults(searchClient.search("pool", options, Context.NONE));
+    
+            // Query 4
+            System.out.println("Query #4: Facet on 'Category'...\n");
+    
+            options = new SearchOptions();
+            options.setFilter("");
+            options.setFacets("Category");
+            options.setSelect("HotelId", "HotelName", "Category");
+    
+            WriteSearchResults(searchClient.search("*", options, Context.NONE));
+    
+            // Query 5
+            System.out.println("Query #5: Look up a specific document...\n");
+    
+            Hotel lookupResponse = searchClient.getDocument("3", Hotel.class);
+            System.out.println(lookupResponse.hotelId);
+            System.out.println();
+    
+             // Query 6
+            System.out.println("Query #6: Call Autocomplete on HotelName that starts with 's'...\n");
+    
+            WriteAutocompleteResults(searchClient.autocomplete("s", "sg"));
+        }
     }
     ```
 
-## Create an index
-
-This quickstart builds a Hotels index that you'll load with hotel data and execute queries against. In this step, define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
-
-In this example, synchronous methods of the azure-search-documents library are used for simplicity and readability. However, for production scenarios, you should use asynchronous methods to keep your app scalable and responsive. For example, you would use [SearchAsyncClient](/java/api/com.azure.search.documents.searchasyncclient) instead of SearchClient.
-
-1. Add an empty class definition to your project: `Hotel.java`
-
-1. Copy the following code into `Hotel.java` to define the structure of a hotel document. Attributes on the field determine how it's used in an application. For example, the IsFilterable annotation must be assigned to every field that supports a filter expression
+1. Create a new file named *Hotel.java* and paste the following code into *Hotel.java*:
 
     ```java
-    // Copyright (c) Microsoft Corporation. All rights reserved.
-    // Licensed under the MIT License.
-    
-    package azure.search.sample;
-    
     import com.azure.search.documents.indexes.SearchableField;
     import com.azure.search.documents.indexes.SimpleField;
     import com.fasterxml.jackson.annotation.JsonInclude;
@@ -268,21 +467,9 @@ In this example, synchronous methods of the azure-search-documents library are u
     }
     ```
 
-In the Azure.Search.Documents client library, you can use [SearchableField](/java/api/com.azure.search.documents.indexes.searchablefield) and [SimpleField](/java/api/com.azure.search.documents.indexes.simplefield) to streamline field definitions.
-
-   * `SimpleField` can be any data type, is always non-searchable (it's ignored for full text search queries), and is retrievable (it's not hidden). Other attributes are off by default, but can be enabled. You might use a SimpleField for document IDs or fields used only in filters, facets, or scoring profiles. If so, be sure to apply any attributes that are necessary for the scenario, such as IsKey = true for a document ID.
-   * `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties.
-
-Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, `isFilterable`, `isSortable`, and `isFacetable` must be explicitly attributed, as shown in the previous sample.
-
-1. Add a second empty class definition to your project: `Address.java`. Copy the following code into the class.
+1. Create a new file named *Address.java* and paste the following code into *Address.java*:
 
     ```java
-    // Copyright (c) Microsoft Corporation. All rights reserved.
-    // Licensed under the MIT License.
-    
-    package azure.search.sample;
-    
     import com.azure.search.documents.indexes.SearchableField;
     import com.fasterxml.jackson.annotation.JsonInclude;
     import com.fasterxml.jackson.annotation.JsonProperty;
@@ -330,276 +517,312 @@ Whether you use the basic `SearchField` API or either one of the helper models,
     }
     ```
 
-1. In `App.java`, create a `SearchIndex` object in the `main` method, and then call the `createOrUpdateIndex` method to create the index in your search service. The index also includes a `SearchSuggester` to enable autocomplete on the specified fields.
 
-    ```java
+1. Run your new console application:
+
+    ```console
+    javac Address.java App.java Hotel.java -cp ".;target\dependency\*"
+    java -cp ".;target\dependency\*" App
+    ```
+
+## Explaining the code
+
+In the previous sections, you created a new console application and installed the Azure AI Search client library. You added code to create a search index, load it with documents, and run queries. You ran the program to see the results in the console. 
+
+In this section, we explain the code you added to the console application.
+
+### Create a search client
+
+In *App.java* you created two clients:
+
+- SearchIndexClient creates the index.
+- SearchClient loads and queries an existing index.
+
+Both clients need the search service endpoint and credentials described previously in the resource information section.
+
+The sample code in this quickstart uses Microsoft Entra ID for authentication. If you prefer to use an API key, you can replace the `DefaultAzureCredential` object with a `AzureKeyCredential` object. 
+
+#### [Microsoft Entra ID](#tab/keyless)
+
+```java
+String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();
+```
+
+#### [API key](#tab/api-key)
+
+```java
+String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+AzureKeyCredential credential = new AzureKeyCredential("<Your search service admin key>");
+```
+---
+
+```java
+public static void main(String[] args) {
+    // Your search service endpoint
+    String searchServiceEndpoint = "https://<Put your search service NAME here>.search.windows.net/";
+
+    // Use the recommended keyless credential instead of the AzureKeyCredential credential.
+    DefaultAzureCredential credential = new DefaultAzureCredentialBuilder().build();
+    //AzureKeyCredential credential = new AzureKeyCredential("Your search service admin key");
+
+    // Create a SearchIndexClient to send create/delete index commands
+    SearchIndexClient searchIndexClient = new SearchIndexClientBuilder()
+        .endpoint(searchServiceEndpoint)
+        .credential(credential)
+        .buildClient();
+    
+    // Create a SearchClient to load and query documents
+    String indexName = "hotels-quickstart-java";
+    SearchClient searchClient = new SearchClientBuilder()
+        .endpoint(searchServiceEndpoint)
+        .credential(credential)
+        .indexName(indexName)
+        .buildClient();
+
     // Create Search Index for Hotel model
     searchIndexClient.createOrUpdateIndex(
         new SearchIndex(indexName, SearchIndexClient.buildSearchFields(Hotel.class, null))
         .setSuggesters(new SearchSuggester("sg", Arrays.asList("HotelName"))));
-    ```
 
-## Load documents
+    // REDACTED FOR BREVITY . . . 
+}
+```
 
-Azure AI Search searches over content stored in the service. In this step, you'll load JSON documents that conform to the hotel index you just created.
 
-In Azure AI Search, search documents are data structures that are both inputs to indexing and outputs from queries. As obtained from an external data source, document inputs might be rows in a database, blobs in Blob storage, or JSON documents on disk. In this example, we're taking a shortcut and embedding JSON documents for four hotels in the code itself.
+### Create an index
 
-When uploading documents, you must use an [IndexDocumentsBatch](/java/api/com.azure.search.documents.indexes.models.indexdocumentsbatch) object. An `IndexDocumentsBatch` object contains a collection of [IndexActions](/java/api/com.azure.search.documents.models.indexaction), each of which contains a document and a property telling Azure AI Search what action to perform (upload, merge, delete, and mergeOrUpload).
+This quickstart builds a Hotels index that you load with hotel data and execute queries against. In this step, you define the fields in the index. Each field definition includes a name, data type, and attributes that determine how the field is used.
 
-1. In `App.java`, create documents and index actions, and then pass them to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
+In this example, synchronous methods of the *Azure.Search.Documents* library are used for simplicity and readability. However, for production scenarios, you should use asynchronous methods to keep your app scalable and responsive. For example, you would use [CreateIndexAsync](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindexasync) instead of [CreateIndex](/dotnet/api/azure.search.documents.indexes.searchindexclient.createindex).
 
-    ```java
-    // Upload documents in a single Upload request.
-    private static void uploadDocuments(SearchClient searchClient)
-    {
-        var hotelList = new ArrayList<Hotel>();
-
-        var hotel = new Hotel();
-        hotel.hotelId = "1";
-        hotel.hotelName = "Stay-Kay City Hotel";
-        hotel.description = "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.";
-        hotel.descriptionFr = "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.";
-        hotel.category = "Boutique";
-        hotel.tags = new String[] { "pool", "air conditioning", "concierge" };
-        hotel.parkingIncluded = false;
-        hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(1970, 1, 18), LocalTime.of(0, 0)), ZoneOffset.UTC);
-        hotel.rating = 3.6;
-        hotel.address = new Address();
-        hotel.address.streetAddress = "677 5th Ave";
-        hotel.address.city = "New York";
-        hotel.address.stateProvince = "NY";
-        hotel.address.postalCode = "10022";
-        hotel.address.country = "USA";
-        hotelList.add(hotel);
-
-        hotel = new Hotel();
-        hotel.hotelId = "2";
-        hotel.hotelName = "Old Century Hotel";
-        hotel.description = "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.";
-        hotel.descriptionFr = "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.";
-        hotel.category = "Boutique";
-        hotel.tags = new String[] { "pool", "free wifi", "concierge" };
-        hotel.parkingIncluded = false;
-        hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(1979, 2, 18), LocalTime.of(0, 0)), ZoneOffset.UTC);
-        hotel.rating = 3.60;
-        hotel.address = new Address();
-        hotel.address.streetAddress = "140 University Town Center Dr";
-        hotel.address.city = "Sarasota";
-        hotel.address.stateProvince = "FL";
-        hotel.address.postalCode = "34243";
-        hotel.address.country = "USA";
-        hotelList.add(hotel);
-
-        hotel = new Hotel();
-        hotel.hotelId = "3";
-        hotel.hotelName = "Gastronomic Landscape Hotel";
-        hotel.description = "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel’s restaurant services.";
-        hotel.descriptionFr = "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.";
-        hotel.category = "Resort and Spa";
-        hotel.tags = new String[] { "air conditioning", "bar", "continental breakfast" };
-        hotel.parkingIncluded = true;
-        hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(2015, 9, 20), LocalTime.of(0, 0)), ZoneOffset.UTC);
-        hotel.rating = 4.80;
-        hotel.address = new Address();
-        hotel.address.streetAddress = "3393 Peachtree Rd";
-        hotel.address.city = "Atlanta";
-        hotel.address.stateProvince = "GA";
-        hotel.address.postalCode = "30326";
-        hotel.address.country = "USA";
-        hotelList.add(hotel);
-
-        hotel = new Hotel();
-        hotel.hotelId = "4";
-        hotel.hotelName = "Sublime Palace Hotel";
-        hotel.description = "Sublime Palace Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Palace is part of a lovingly restored 1800 palace.";
-        hotel.descriptionFr = "Le Sublime Palace Hotel est situé au coeur du centre historique de sublime dans un quartier extrêmement animé et vivant, à courte distance de marche des sites et monuments de la ville et est entouré par l'extraordinaire beauté des églises, des bâtiments, des commerces et Monuments. Sublime Palace fait partie d'un Palace 1800 restauré avec amour.";
-        hotel.category = "Boutique";
-        hotel.tags = new String[] { "concierge", "view", "24-hour front desk service" };
-        hotel.parkingIncluded = true;
-        hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(1960, 2, 06), LocalTime.of(0, 0)), ZoneOffset.UTC);
-        hotel.rating = 4.60;
-        hotel.address = new Address();
-        hotel.address.streetAddress = "7400 San Pedro Ave";
-        hotel.address.city = "San Antonio";
-        hotel.address.stateProvince = "TX";
-        hotel.address.postalCode = "78216";
-        hotel.address.country = "USA";
-        hotelList.add(hotel);
-
-        var batch = new IndexDocumentsBatch<Hotel>();
-        batch.addMergeOrUploadActions(hotelList);
-        try
-        {
-            searchClient.indexDocuments(batch);
-        }
-        catch (Exception e)
-        {
-            e.printStackTrace();
-            // If for some reason any documents are dropped during indexing, you can compensate by delaying and
-            // retrying. This simple demo just logs failure and continues
-            System.err.println("Failed to index some of the documents");
-        }
-    }
-    ```
+#### Define the structures
 
-Once you initialize the `IndexDocumentsBatch` object, you can send it to the index by calling [indexDocuments](/java/api/com.azure.search.documents.searchclient#com-azure-search-documents-searchclient-indexdocuments(com-azure-search-documents-indexes-models-indexdocumentsbatch(-))) on your `SearchClient` object.
+You created two helper classes, *Hotel.java* and *Address.java*, to define the structure of a hotel document and its address. The Hotel class includes fields for a hotel ID, name, description, category, tags, parking, renovation date, rating, and address. The Address class includes fields for street address, city, state/province, postal code, and country/region.
 
-1. Add the following lines to `Main()`. Loading documents is done using `SearchClient`.
+In the Azure.Search.Documents client library, you can use [SearchableField](/java/api/com.azure.search.documents.indexes.searchablefield) and [SimpleField](/java/api/com.azure.search.documents.indexes.simplefield) to streamline field definitions.
 
-    ```java
-    // Upload sample hotel documents to the Search Index
-    uploadDocuments(searchClient);
-    ```
+* `SimpleField` can be any data type, is always non-searchable (ignored for full text search queries), and is retrievable (not hidden). Other attributes are off by default, but can be enabled. You might use a SimpleField for document IDs or fields used only in filters, facets, or scoring profiles. If so, be sure to apply any attributes that are necessary for the scenario, such as IsKey = true for a document ID.
+* `SearchableField` must be a string, and is always searchable and retrievable. Other attributes are off by default, but can be enabled. Because this field type is searchable, it supports synonyms and the full complement of analyzer properties.
 
-1. Because this is a console app that runs all commands sequentially, add a 2-second wait time between indexing and queries.
+Whether you use the basic `SearchField` API or either one of the helper models, you must explicitly enable filter, facet, and sort attributes. For example, `isFilterable`, `isSortable`, and `isFacetable` must be explicitly attributed, as shown in the previous sample.
 
-    ```java
-    // Wait 2 seconds for indexing to complete before starting queries (for demo and console-app purposes only)
-    System.out.println("Waiting for indexing...\n");
+#### Create the search index
+
+In `App.java`, you create a `SearchIndex` object in the `main` method, and then call the `createOrUpdateIndex` method to create the index in your search service. The index also includes a `SearchSuggester` to enable autocomplete on the specified fields.
+
+```java
+// Create Search Index for Hotel model
+searchIndexClient.createOrUpdateIndex(
+    new SearchIndex(indexName, SearchIndexClient.buildSearchFields(Hotel.class, null))
+    .setSuggesters(new SearchSuggester("sg", Arrays.asList("HotelName"))));
+```
+
+### Load documents
+
+Azure AI Search searches over content stored in the service. In this step, you load JSON documents that conform to the hotel index you created.
+
+In Azure AI Search, search documents are data structures that are both inputs to indexing and outputs from queries. As obtained from an external data source, document inputs might be rows in a database, blobs in Blob storage, or JSON documents on disk. In this example, we're taking a shortcut and embedding JSON documents for four hotels in the code itself.
+
+When uploading documents, you must use an [IndexDocumentsBatch](/java/api/com.azure.search.documents.indexes.models.indexdocumentsbatch) object. An `IndexDocumentsBatch` object contains a collection of [IndexActions](/java/api/com.azure.search.documents.models.indexaction), each of which contains a document and a property telling Azure AI Search what action to perform (upload, merge, delete, and mergeOrUpload).
+
+In `App.java`, you create documents and index actions, and then pass them to `IndexDocumentsBatch`. The following documents conform to the hotels-quickstart index, as defined by the hotel class.
+
+```java
+private static void uploadDocuments(SearchClient searchClient)
+{
+    var hotelList = new ArrayList<Hotel>();
+
+    var hotel = new Hotel();
+    hotel.hotelId = "1";
+    hotel.hotelName = "Stay-Kay City Hotel";
+    hotel.description = "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.";
+    hotel.descriptionFr = "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.";
+    hotel.category = "Boutique";
+    hotel.tags = new String[] { "pool", "air conditioning", "concierge" };
+    hotel.parkingIncluded = false;
+    hotel.lastRenovationDate = OffsetDateTime.of(LocalDateTime.of(LocalDate.of(1970, 1, 18), LocalTime.of(0, 0)), ZoneOffset.UTC);
+    hotel.rating = 3.6;
+    hotel.address = new Address();
+    hotel.address.streetAddress = "677 5th Ave";
+    hotel.address.city = "New York";
+    hotel.address.stateProvince = "NY";
+    hotel.address.postalCode = "10022";
+    hotel.address.country = "USA";
+    hotelList.add(hotel);
+    
+    // REDACTED FOR BREVITY
+
+    var batch = new IndexDocumentsBatch<Hotel>();
+    batch.addMergeOrUploadActions(hotelList);
     try
     {
-        Thread.sleep(2000);
+        searchClient.indexDocuments(batch);
     }
-    catch (InterruptedException e)
+    catch (Exception e)
     {
+        e.printStackTrace();
+        // If for some reason any documents are dropped during indexing, you can compensate by delaying and
+        // retrying. This simple demo just logs failure and continues
+        System.err.println("Failed to index some of the documents");
     }
-    ```
+}
+```
+
+Once you initialize the `IndexDocumentsBatch` object, you can send it to the index by calling [indexDocuments](/java/api/com.azure.search.documents.searchclient#com-azure-search-documents-searchclient-indexdocuments(com-azure-search-documents-indexes-models-indexdocumentsbatch(-))) on your `SearchClient` object.
+
+You load documents using SearchClient in `main()`, but the operation also requires admin rights on the service, which is typically associated with SearchIndexClient. One way to set up this operation is to get SearchClient through `SearchIndexClient` (`searchIndexClient` in this example).
+
+```java
+uploadDocuments(searchClient);
+```
+
+Because we have a console app that runs all commands sequentially, we add a 2-second wait time between indexing and queries.
+
+```java
+// Wait 2 seconds for indexing to complete before starting queries (for demo and console-app purposes only)
+System.out.println("Waiting for indexing...\n");
+try
+{
+    Thread.sleep(2000);
+}
+catch (InterruptedException e)
+{
+}
+```
 
 The 2-second delay compensates for indexing, which is asynchronous, so that all documents can be indexed before the queries are executed. Coding in a delay is typically only necessary in demos, tests, and sample applications.
 
-## Search an index
+### Search an index
 
 You can get query results as soon as the first document is indexed, but actual testing of your index should wait until all documents are indexed.
 
-This section adds two pieces of functionality: query logic, and results. For queries, use the Search method. This method takes search text (the query string) and other options.
+This section adds two pieces of functionality: query logic and results. For queries, use the Search method. This method takes search text (the query string) and other options.
 
-1. In `App.java`, create a `WriteDocuments` method that prints search results to the console.
+In `App.java`, the `WriteDocuments` method prints search results to the console.
 
-    ```java
-    // Write search results to console
-    private static void WriteSearchResults(SearchPagedIterable searchResults)
+```java
+// Write search results to console
+private static void WriteSearchResults(SearchPagedIterable searchResults)
+{
+    searchResults.iterator().forEachRemaining(result ->
     {
-        searchResults.iterator().forEachRemaining(result ->
-        {
-            Hotel hotel = result.getDocument(Hotel.class);
-            System.out.println(hotel);
-        });
+        Hotel hotel = result.getDocument(Hotel.class);
+        System.out.println(hotel);
+    });
 
-        System.out.println();
-    }
+    System.out.println();
+}
 
-    // Write autocomplete results to console
-    private static void WriteAutocompleteResults(AutocompletePagedIterable autocompleteResults)
+// Write autocomplete results to console
+private static void WriteAutocompleteResults(AutocompletePagedIterable autocompleteResults)
+{
+    autocompleteResults.iterator().forEachRemaining(result ->
     {
-        autocompleteResults.iterator().forEachRemaining(result ->
-        {
-            String text = result.getText();
-            System.out.println(text);
-        });
+        String text = result.getText();
+        System.out.println(text);
+    });
 
-        System.out.println();
-    }
-    ```
+    System.out.println();
+}
+```
 
-1. Create a `RunQueries` method to execute queries and return results. Results are `Hotel` objects. This sample shows the method signature and the first query. This query demonstrates the `Select` parameter that lets you compose the result using selected fields from the document.
+#### Query example 1
 
-    ```java
-    // Run queries, use WriteDocuments to print output
-    private static void RunQueries(SearchClient searchClient)
-    {
-        // Query 1
-        System.out.println("Query #1: Search on empty term '*' to return all documents, showing a subset of fields...\n");
+The `RunQueries` method executes queries and returns results. Results are Hotel objects. This sample shows the method signature and the first query. This query demonstrates the `Select` parameter that lets you compose the result using selected fields from the document.
 
-        SearchOptions options = new SearchOptions();
-        options.setIncludeTotalCount(true);
-        options.setFilter("");
-        options.setOrderBy("");
-        options.setSelect("HotelId", "HotelName", "Address/City");
+```java
+// Run queries, use WriteDocuments to print output
+private static void RunQueries(SearchClient searchClient)
+{
+    // Query 1
+    System.out.println("Query #1: Search on empty term '*' to return all documents, showing a subset of fields...\n");
 
-        WriteSearchResults(searchClient.search("*", options, Context.NONE));
-    }
-    ```
+    SearchOptions options = new SearchOptions();
+    options.setIncludeTotalCount(true);
+    options.setFilter("");
+    options.setOrderBy("");
+    options.setSelect("HotelId", "HotelName", "Address/City");
 
-1. In the second query, search on a term, add a filter that selects documents where Rating is greater than 4, and then sort by *Rating* in descending order. Filter is a boolean expression that is evaluated over `isFilterable` fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
+    WriteSearchResults(searchClient.search("*", options, Context.NONE));
+}
+```
 
-    ```java
-    // Query 2
-    System.out.println("Query #2: Search on 'hotels', filter on 'Rating gt 4', sort by Rating in descending order...\n");
+#### Query example 2
 
-    options = new SearchOptions();
-    options.setFilter("Rating gt 4");
-    options.setOrderBy("Rating desc");
-    options.setSelect("HotelId", "HotelName", "Rating");
+In the second query, search on a term, add a filter that selects documents where Rating is greater than 4, and then sort by *Rating* in descending order. Filter is a boolean expression that is evaluated over `isFilterable` fields in an index. Filter queries either include or exclude values. As such, there's no relevance score associated with a filter query.
 
-    WriteSearchResults(searchClient.search("hotels", options, Context.NONE));
-    ```
+```java
+// Query 2
+System.out.println("Query #2: Search on 'hotels', filter on 'Rating gt 4', sort by Rating in descending order...\n");
 
-1. The third query demonstrates `searchFields`, used to scope a full text search operation to specific fields.
+options = new SearchOptions();
+options.setFilter("Rating gt 4");
+options.setOrderBy("Rating desc");
+options.setSelect("HotelId", "HotelName", "Rating");
 
-    ```java
-    // Query 3
-    System.out.println("Query #3: Limit search to specific fields (pool in Tags field)...\n");
+WriteSearchResults(searchClient.search("hotels", options, Context.NONE));
+```
 
-    options = new SearchOptions();
-    options.setSearchFields("Tags");
+#### Query example 3
 
-    options.setSelect("HotelId", "HotelName", "Tags");
+The third query demonstrates `searchFields`, used to scope a full text search operation to specific fields.
 
-    WriteSearchResults(searchClient.search("pool", options, Context.NONE));
-    ```
+```java
+// Query 3
+System.out.println("Query #3: Limit search to specific fields (pool in Tags field)...\n");
 
-1. The fourth query demonstrates `facets`, which can be used to structure a faceted navigation structure.
+options = new SearchOptions();
+options.setSearchFields("Tags");
 
-    ```java
-    // Query 4
-    System.out.println("Query #4: Facet on 'Category'...\n");
+options.setSelect("HotelId", "HotelName", "Tags");
 
-    options = new SearchOptions();
-    options.setFilter("");
-    options.setFacets("Category");
-    options.setSelect("HotelId", "HotelName", "Category");
+WriteSearchResults(searchClient.search("pool", options, Context.NONE));
+```
 
-    WriteSearchResults(searchClient.search("*", options, Context.NONE));
-    ```
+#### Query example 4
 
-1. In the fifth query, return a specific document.
+The fourth query demonstrates `facets`, which can be used to structure a faceted navigation structure.
 
-    ```java
-    // Query 5
-    System.out.println("Query #5: Look up a specific document...\n");
+```java
+// Query 4
+System.out.println("Query #4: Facet on 'Category'...\n");
 
-    Hotel lookupResponse = searchClient.getDocument("3", Hotel.class);
-    System.out.println(lookupResponse.hotelId);
-    System.out.println();
-    ```
+options = new SearchOptions();
+options.setFilter("");
+options.setFacets("Category");
+options.setSelect("HotelId", "HotelName", "Category");
 
-1. The last query shows the syntax for autocomplete, simulating a partial user input of *s* that resolves to two possible matches in the `sourceFields` associated with the suggester you defined in the index.
+WriteSearchResults(searchClient.search("*", options, Context.NONE));
+```
 
-    ```java
-    // Query 6
-    System.out.println("Query #6: Call Autocomplete on HotelName that starts with 's'...\n");
+#### Query example 5
 
-    WriteAutocompleteResults(searchClient.autocomplete("s", "sg"));
-    ```
+In the fifth query, return a specific document.
 
-1. Add `RunQueries` to `Main()`.
+```java
+// Query 5
+System.out.println("Query #5: Look up a specific document...\n");
 
-    ```java
-    // Call the RunQueries method to invoke a series of queries
-    System.out.println("Starting queries...\n");
-    RunQueries(searchClient);
+Hotel lookupResponse = searchClient.getDocument("3", Hotel.class);
+System.out.println(lookupResponse.hotelId);
+System.out.println();
+```
 
-    // End the program
-    System.out.println("Complete.\n");
-    ```
+#### Query example 6
 
-The previous queries show multiple ways of matching terms in a query: full-text search, filters, and autocomplete.
+The last query shows the syntax for autocomplete, simulating a partial user input of *s* that resolves to two possible matches in the `sourceFields` associated with the suggester you defined in the index.
 
-Full text search and filters are performed using the [SearchClient.search](/java/api/com.azure.search.documents.searchclient#com-azure-search-documents-searchclient-search(java-lang-string)) method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the `filter` property of the [SearchOptions](/java/api/com.azure.search.documents.models.searchoptions) class. To filter without searching, just pass "*" for the `searchText` parameter of the `search` method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
+```java
+// Query 6
+System.out.println("Query #6: Call Autocomplete on HotelName that starts with 's'...\n");
+
+WriteAutocompleteResults(searchClient.autocomplete("s", "sg"));
+```
 
-## Run the program
+#### Summary of queries
 
-Press F5 to rebuild the app and run the program in its entirety.
+The previous queries show multiple ways of matching terms in a query: full-text search, filters, and autocomplete.
+
+Full text search and filters are performed using the [SearchClient.search](/java/api/com.azure.search.documents.searchclient#com-azure-search-documents-searchclient-search(java-lang-string)) method. A search query can be passed in the `searchText` string, while a filter expression can be passed in the `filter` property of the [SearchOptions](/java/api/com.azure.search.documents.models.searchoptions) class. To filter without searching, just pass "*" for the `searchText` parameter of the `search` method. To search without filtering, leave the `filter` property unset, or don't pass in a `SearchOptions` instance at all.
 
-Output includes messages from `System.out.println`, with the addition of query information and results.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaコードクイックスタートの更新"
}
```

### Explanation
この変更では、Javaを使用したAzure AI Searchのクイックスタートガイドが大幅に更新されました。主要な改良点には、環境設定の手順や依存関係の明記、プロジェクトの作成手順の新しい方法が含まれています。新たに`pom.xml`ファイルの例が追加され、必要な依存関係が含まれていることが示されています。

コードの例も刷新され、SearchIndexClientとSearchClientを使用して検索インデックスの作成やドキュメントのアップロード、検索の実行が詳細に説明されています。特に、Microsoft Entra IDによる認証方法が強調され、APIキーによる代替手段も記載されています。また、サンプルデータの定義やドキュメントのインデックス方法も詳しく説明されています。

新たに追加されたメソッドやクラスを通じて、実践的なコード体験を提供するとともに、ユーザーがAzure AI Searchの利点をより理解しやすくなる内容にアップデートされています。このリファクタリングによって、クイックスタートガイド全体が現代的なコーディングスタイルに適合し、ユーザーにとっての使いやすさが向上しています。変更により、合計で545行の追加と322行の削除が行われ、全体で867行の変更が加えられています。

## articles/search/keyless-connections.md{#item-3f0d72}

<details>
<summary>Diff</summary>
````diff
@@ -54,8 +54,6 @@ Install the [Azure Identity client library for Java](https://mvnrepository.com/a
             <groupId>com.azure</groupId>
             <artifactId>azure-identity</artifactId>
             <version>1.15.1</version>
-            <type>pom</type>
-            <scope>import</scope>
         </dependency>
     </dependencies>
 </dependencyManagement>
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キーレス接続の依存関係の更新"
}
```

### Explanation
この変更では、Azure AI Searchに関連する「キーレス接続」ガイドラインの内容が一部修正されました。具体的には、Java用のAzure Identityライブラリの依存関係部分から、`<type>`要素と`<scope>`要素が削除されました。これにより、依存関係が簡略化され、コードの可読性が向上しました。変更は合計2行で、0行の追加が行われ、2行の削除がありました。この修正により、依存関係の設定がよりシンプルで明確になり、利用者にとって理解しやすい内容となっています。

## articles/search/media/search-get-started-java/java-quickstart-artifact-id.png{#item-fe2374}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの削除"
}
```

### Explanation
この変更では、「Javaクイックスタート」ガイドに関連する画像ファイル（`java-quickstart-artifact-id.png`）が削除されました。削除されたファイルはデモや説明を補完するために使用されていたと考えられますが、最新の編集内容においては不要であると判断されたようです。この変更は追加や削除がなく、変更内容自体はありませんが、情報の整理や一貫性を保つための措置とみられます。これにより、ドキュメントの内容がより明確になり、無駄を省くことができます。

## articles/search/media/search-get-started-java/java-quickstart-create-project.png{#item-dc3528}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの削除"
}
```

### Explanation
この変更では、「Javaクイックスタート」ガイドに関連する画像ファイル（`java-quickstart-create-project.png`）が削除されました。この画像は、プロジェクトの作成に関する手順を視覚的に説明するために使用されていたと考えられますが、最新の内容変更においては必要がないと判断されたため削除されました。変更自体には追加や具体的な内容の変更はなく、ファイルの削除のみとなります。このような措置により、ドキュメントがより明瞭にし、関連のない情報を排除することが目的とされている可能性があります。

## articles/search/media/search-get-started-java/java-quickstart-finish-setup-terminal.png{#item-985794}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの削除"
}
```

### Explanation
この変更では、「Javaクイックスタート」に関連する画像ファイル（`java-quickstart-finish-setup-terminal.png`）が削除されました。この画像は、セットアップの完了に関する手順を示すために利用されていた可能性がありますが、最新の内容編集においては不要であると判断されたため削除されました。具体的な追加や変更はなく、このファイルの削除のみであるため、ドキュメント全体の整理や情報の一貫性を高めることを目的とした措置と考えられます。この変更によって、関連のない情報や重複を避け、ユーザーにとっての利便性が向上することが期待されます。

## articles/search/media/search-get-started-java/java-quickstart-group-id.png{#item-de0a24}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの削除"
}
```

### Explanation
この変更では、「Javaクイックスタート」に関連する画像ファイル（`java-quickstart-group-id.png`）が削除されました。この画像は、グループIDを設定する手順を視覚的にサポートするために使用されていた可能性がありますが、最新の編集においてはその必要がなくなったため削除されました。具体的な追加や内容の変更は行われておらず、削除のみが実施されています。この措置により、ドキュメントがよりクリーンで整理された状態を保ち、ユーザーにとってわかりやすい情報を提供することを目的としています。不要な素材を排除することで、ドキュメント全体の品質向上が図られています。

## articles/search/media/search-get-started-java/java-quickstart-select-maven-project-type.png{#item-cdc430}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの削除"
}
```

### Explanation
この変更では、「Javaクイックスタート」に関連する画像ファイル（`java-quickstart-select-maven-project-type.png`）が削除されました。この画像は、Mavenプロジェクトタイプを選択する手順を視覚的に説明するために利用されていた可能性がありますが、最新のコンテンツレビューにおいてその重要性が低下したと判断されたため、削除されました。具体的な追加や変更はなく、ファイルの削除のみが行われています。この更新によって、ドキュメントの内容が整理され、ユーザーにとっての情報の明確性が向上することが期待されます。不要な素材を取り除くことで、よりシンプルで効果的な情報提供を目指しています。

## articles/search/media/search-get-started-java/java-quickstart-select-maven.png{#item-6d5b91}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像ファイルの削除"
}
```

### Explanation
この変更では、「Javaクイックスタート」に関連する画像ファイル（`java-quickstart-select-maven.png`）が削除されました。この画像は、Mavenの選択プロセスを説明するために使用されていた可能性がありますが、内容の見直しに伴い、その必要性がなくなったと考えられます。具体的なコードの追加や変更はなく、削除のみが行われています。この更新により、ドキュメントはより一貫性を持ち、情報が整理された状態を維持することができるため、ユーザーにとっての理解を助ける役割を果たします。内容の明確化を図るため、不要な要素を取り除くことが目的です。

## articles/search/search-api-versions.md{#item-69ca3e}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: conceptual
-ms.date: 01/16/2025
+ms.date: 02/18/2025
 ---
 
 # API versions in Azure AI Search
@@ -35,7 +35,7 @@ This was the first REST API that offered vector search support. Newer API versio
 
 ## Discontinued versions
 
-Some API versions are discontinued and are rejected by a search service:
+Some API versions are discontinued and are no longer documented or supported:
 
 + **2015-02-28**
 + **2015-02-28-Preview**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンに関するドキュメントの更新"
}
```

### Explanation
この変更では、「検索APIバージョン」に関するMarkdownファイルが修正されました。具体的には、ドキュメントの日付が「2025年1月16日」から「2025年2月18日」に更新されたほか、いくつかの文言が変更されています。特に、「廃止されたバージョン」に関する説明が改善され、サポートされなくなったAPIバージョンについての表現が明確にされました。具体的な変更点としては、廃止されたAPIの説明が「廃止され、ドキュメント化されなくなった」とされ、より正確な情報が反映されています。また、新たに「2015-02-28」と「2015-02-28-Preview」のバージョンが明記されました。この更新により、ユーザーに提供される情報の正確性と透明性が向上しています。

## articles/search/search-get-started-portal-import-vectors.md{#item-7dae77}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ This quickstart helps you get started with [integrated vectorization](vector-sea
 
 + An Azure subscription. [Create one for free](https://azure.microsoft.com/free/).
 
-+ [An Azure AI Search service](search-create-service-portal.md) in the same region as Azure AI. We recommend the Basic tier or higher.
++ [An Azure AI Search service](search-create-service-portal.md) in the same region as your Azure AI multi-service resource. We recommend the Basic tier or higher.
 
 + [A supported data source](#supported-data-sources) with the [Health Plan PDF](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/health-plan) sample documents.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ポータルでのベクターインポートに関するドキュメント修正"
}
```

### Explanation
この変更では、「ポータルでのベクターインポート」に関するMarkdownファイルが更新されました。具体的には、Azure AI Searchサービスに関連する説明が少し修正されています。以前は「Azure AIの同じリージョンにある」と表現されていた部分が、「あなたのAzure AIマルチサービスリソースがある同じリージョンに」と改訂され、より明確にリソースの関連性を示しています。この修正により、ユーザーは必要なリソースを正確に理解し、適切な設定を行う際の指針が改善されることになります。全体的に、内容は簡素化され、ユーザーにとっての使いやすさが向上しています。

## articles/search/semantic-answers.md{#item-c3fee9}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 12/10/2024
+ms.date: 02/18/2025
 ---
 
 # Return a semantic answer in Azure AI Search
@@ -48,7 +48,6 @@ Answers are returned as an independent, top-level object in the query response p
 
 To return a semantic answer, the query must have the semantic `"queryType"`, `"queryLanguage"`, `"semanticConfiguration"`, and the `"answers"` parameters. Specifying these parameters doesn't guarantee an answer, but the request must include them for answer processing to occur.
 
-
 ```json
 {
     "search": "how do clouds form",
@@ -81,7 +80,7 @@ Answers are provided in the `"@search.answers"` array, which appears first in th
 
 If an answer is indeterminate, the response shows up as `"@search.answers": []`. The answers array is followed by the value array, which is the standard response in a semantic query.
 
-Given the query "how do clouds form", the following example illustrates an answer:
+Given the query "how do clouds form" which can be directed at an index built on [content from the NASA Earth Book](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book), the following example illustrates a verbatim answer (found on page 38):
 
 ```json
 {
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック回答に関するドキュメントの更新"
}
```

### Explanation
この変更では、「Azure AI Searchにおけるセマンティック回答」に関するMarkdownファイルが修正されました。主な変更点は、ドキュメントの日付が「2024年12月10日」から「2025年2月18日」に更新されたことです。また、いくつかの文が改訂され、内容が明確さを増しています。具体的には、セマンティック回答を取得するために必要なパラメータの説明が保持され、回答の例がより具体的な文脈を提供するようになりました。例えば、「NASA Earth Book」のコンテンツに基づいた質問についての例が追加されることで、ユーザーは具体的な使用ケースを容易に理解できるようになりました。この更新により、ユーザーがセマンティック機能の利用方法をより明確に把握できるよう努められています。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: how-to
-ms.date: 12/10/2024
+ms.date: 02/18/2025
 ---
 
 # Add semantic ranking to queries in Azure AI Search
@@ -29,7 +29,7 @@ This article explains how to invoke the semantic ranker on queries. It assumes y
 + Review [semantic ranking](semantic-search-overview.md) if you need an introduction to the feature.
 
 > [!NOTE]
-> Captions and answers are extracted verbatim from text in the search document. The semantic subsystem uses machine reading comprehension to recognize content having the characteristics of a caption or answer, but doesn't compose new sentences or phrases. For this reason, content that includes explanations or definitions work best for semantic ranking. If you want chat-style interaction with generated responses, see [Retrieval Augmented Generation (RAG)](retrieval-augmented-generation-overview.md).
+> Captions and answers are extracted verbatim from text in the search document. The semantic subsystem uses machine reading comprehension to recognize content having the characteristics of a caption or answer, but doesn't compose new sentences or phrases except in the case of [query rewrite](semantic-how-to-query-rewrite.md). For this reason, content that includes explanations or definitions work best for semantic ranking. If you want chat-style interaction with generated responses, see [Retrieval Augmented Generation (RAG)](retrieval-augmented-generation-overview.md).
 
 ## Choose a client
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティッククエリリクエストに関するドキュメントの更新"
}
```

### Explanation
この変更では、Azure AI Searchにおけるセマンティッククエリリクエストに関するMarkdownファイルが修正されました。最も重要な変更点は、ドキュメントの日付が「2024年12月10日」から「2025年2月18日」に更新されたことです。また、セマンティックランキングに関する説明がわずかに改訂され、内容の一部が明確化されています。

具体的には、キャプションや回答がどのように検索ドキュメントから抽出されるかについての説明が補足され、「クエリリライト」の場合を除いて、新しい文章やフレーズが生成されないことが明記されました。この追加情報により、ユーザーはセマンティックランキング機能の仕組みをより理解しやすくなります。全体として、ドキュメントはセマンティッククエリの利用に関する指針をさらに明確にしています。

## articles/search/semantic-search-overview.md{#item-b7497b}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 12/10/2024
+ms.date: 02/18/2025
 ---
 
 # Semantic ranking in Azure AI Search
@@ -20,15 +20,19 @@ In Azure AI Search, *semantic ranker* is a feature that measurably improves sear
 Semantic ranker is a premium feature, billed by usage. We recommend this article for background, but if you'd rather get started, [follow these steps](#how-to-get-started-with-semantic-ranker).
 
 > [!NOTE]
-> Semantic ranker doesn't use generative AI or vectors. If you're looking for vectors and similarity search, see [Vector search in Azure AI Search](vector-search-overview.md) for details.
+> Semantic ranker doesn't use generative AI or vectors for secondary level 2 (L2) ranking. If you're looking for vectors and similarity search, see [Vector search in Azure AI Search](vector-search-overview.md).
 
 ## What is semantic ranking?
 
-Semantic ranker is a collection of query-side capabilities that improve the quality of an initial [BM25-ranked](index-similarity-and-scoring.md) or [RRF-ranked](hybrid-search-ranking.md) search result for text-based queries, vector queries, and hybrid queries. When you enable it on your search service, semantic ranking extends the query execution pipeline in two ways:
+Semantic ranker calls LLMs at query time. LLms are used to improve the quality of an initial [BM25-ranked](index-similarity-and-scoring.md) or [RRF-ranked](hybrid-search-ranking.md) search result for text-based queries, the text portion of vector queries, and hybrid queries. When you enable it on your search service, semantic ranking extends the query execution pipeline in three ways:
 
-* First, it adds secondary ranking over an initial result set that was scored using BM25 or Reciprocal Rank Fusion (RRF). This secondary ranking uses multi-lingual, deep learning models adapted from Microsoft Bing to promote the most semantically relevant results.
+* First, it always adds secondary ranking over an initial result set that was scored using BM25 or Reciprocal Rank Fusion (RRF). This secondary ranking uses multi-lingual, deep learning models adapted from Microsoft Bing to promote the most semantically relevant results.
 
-* Second, it extracts and returns captions and answers in the response, which you can render on a search page to improve the user's search experience.
+* Second, it returns captions and optionally extracts answers in the response, which you can render on a search page to improve the user's search experience.
+
+* Third, if you enable query rewrite, it calls an LLM to expand an initial query string into multiple semantically similar query strings. 
+
+Secondary ranking and "answers" apply to the query response. Query rewrite is part of the query request.
 
 Here are the capabilities of the semantic reranker.
 
@@ -37,6 +41,7 @@ Here are the capabilities of the semantic reranker.
 | L2 ranking | Uses the context or semantic meaning of a query to compute a new relevance score over preranked results. |
 | [Semantic captions and highlights](semantic-how-to-query-request.md) | Extracts verbatim sentences and phrases from fields that best summarize the content, with highlights over key passages for easy scanning. Captions that summarize a result are useful when individual content fields are too dense for the search results page. Highlighted text elevates the most relevant terms and phrases so that users can quickly determine why a match was considered relevant. |
 | [Semantic answers](semantic-answers.md) | An optional and extra substructure returned from a semantic query. It provides a direct answer to a query that looks like a question. It requires that a document has text with the characteristics of an answer. |
+| [Query rewrite](semantic-how-to-query-rewrite.md) | Using text queries or the text portion of a vector query, semantic ranker creates up to 10 variants of the query, perhaps correcting typos or spelling errors, or rephrasing a query using synonyms generated by the LLM. The rewritten query runs on the search engine. The results are scored using BM25 or RRF scoring, and then rescored by semantic ranker.  |
 
 ## How semantic ranker works
 
@@ -58,7 +63,7 @@ There are three steps to semantic ranking:
 
 In semantic ranking, the query subsystem passes search results as an input to summarization and ranking models. Because the ranking models have input size constraints and are processing intensive, search results must be sized and structured (summarized) for efficient handling.
 
-1. Semantic ranker starts with a [BM25-ranked result](index-ranking-similarity.md) from a text query or an [RRF-ranked result](hybrid-search-ranking.md) from a vector or hybrid query. Only text fields are used in the reranking exercise, and only the top 50 results progress to semantic ranking, even if results include more than 50. Typically, fields used in semantic ranking are informational and descriptive.
+1. Semantic ranker starts with a [BM25-ranked result](index-ranking-similarity.md) from a text query or an [RRF-ranked result](hybrid-search-ranking.md) from a vector or hybrid query. Only text is used in the reranking exercise, and only the top 50 results progress to semantic ranking, even if results include more than 50. Typically, fields used in semantic ranking are informational and descriptive.
 
 1. For each document in the search result, the summarization model accepts up to 2,000 tokens, where a token is approximately 10 characters. Inputs are assembled from the "title", "keyword", and "content" fields listed in the [semantic configuration](semantic-how-to-configure.md). 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティック検索の概要に関するドキュメントの更新"
}
```

### Explanation
この変更では、Azure AI Searchにおけるセマンティック検索の概要に関するMarkdownファイルが修正されました。主な変更点は、ドキュメントの日付が「2024年12月10日」から「2025年2月18日」に更新されたことです。また、セマンティックランキング機能の説明が大幅に充実し、いくつかの重要なポイントが追加されました。

具体的には、セマンティックランカーがどのようにクエリ処理を行うかについての情報が明確化されています。従来の内容に加え、セマンティックランカーが生成AIやベクトルを使用しないことの説明が補足され、L2ランキングの具体的な役割や、キャプションと回答の返却方法も明示されています。また、クエリリライト機能が追加され、LLM（大規模言語モデル）を使用して初期クエリを複数のセマンティックに類似したクエリに拡張することについても言及されています。

全体として、この更新により、セマンティック検索の機能やその利用方法について、より具体的で実用的な情報が提供され、ユーザーがこの機能を理解しやすくなっています。


