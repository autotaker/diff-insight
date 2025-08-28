---
date: '2025-08-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:85d4514...MicrosoftDocs:06c258e
summary: このコードの変更では、新機能の追加としてJavaでのセマンティックランカーのクイックスタートガイドが導入され、セマンティック検索に関する既存のドキュメントがJavaに対応して更新されました。また、Markdownブロブのインデックス化に関するドキュメントも改善されました。特に、大きな変更はなく、これらのアップデートは開発者がAzure
  AI Searchをより効果的に利用できるように設計されています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:85d4514...MicrosoftDocs:06c258e){target="_blank"}

# Highlights
このコードの変更では、主に新機能の追加とドキュメントの更新が行われました。特筆すべきは、Javaでのセマンティックランカーのクイックスタートガイドが新たに追加され、セマンティック検索に関する既存のドキュメントがJavaを含む形で更新されました。また、Markdownブロブのインデックス化に関するドキュメントも内容が改善されています。

## New features
- Javaでのセマンティックランクを利用するためのクイックスタートガイドが新たに追加された。

## Breaking changes
- 特にありません。

## Other updates
- セマンティック検索のガイドにJavaに関するクイックスタートのリンクが追加されました。
- Markdownブロブのインデックス化に関するドキュメントが内容を読みやすく整理され、ユーザーに一層の明確な指針を提供。

# Insights
Azure AI SearchにおけるセマンティックランカーのJavaクイックスタートは、検索エンジンをよりインテリジェントに活用したい開発者にとって重要な追加です。Javaは多くの企業で広く使われているため、このクイックスタートガイドの追加は多くの開発者にとって有益です。ガイドは具体的なコードサンプルを通じて、ユーザーがセマンティック機能を実装しやすくするための手順を詳述しています。

一方、Markdownブロブのインデックス化に関するドキュメントの改訂は、Markdownをどのように解析し、インデックスとして組み込むかについての説明を一層具体化しました。ユーザーは、これにより、Documentの管理や解析モードの選択といった、実際の運用面での課題に取り組む際の支援を得ることができます。

これらの updatesは、開発者がツールを効率的に使用し、Azure AI Searchをさまざまなシナリオで効果的に活用するために役立ちます。特に、Documentの検索精度向上や、ユーザーエクスペリエンスの向上に寄与するものと考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [semantic-ranker-java.md](#item-93a05a) | new feature | 新しい言語サポートの追加: Javaにおけるセマンティックランカーのクイックスタート | added | 611 | 0 | 611 | 
| [search-get-started-semantic.md](#item-2b3902) | minor update | Javaクイックスタートの追加: セマンティック検索ガイドの更新 | modified | 6 | 0 | 6 | 
| [search-how-to-index-markdown-blobs.md](#item-c94a20) | minor update | Markdownブロブのインデックス化に関するドキュメントの更新 | modified | 97 | 17 | 114 | 


# Modified Contents
## articles/search/includes/quickstarts/semantic-ranker-java.md{#item-93a05a}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,611 @@
+---
+author: KarlErickson
+ms.author: karler
+ms.service: azure-ai-search
+ms.custom: devx-track-java
+ms.topic: include
+ms.date: 08/22/2025
+ai-usage: ai-assisted
+---
+
+[!INCLUDE [Semantic ranker introduction](semantic-ranker-intro.md)]
+
+## Set up the client
+
+In this quickstart, you use an IDE and the [**Azure AI Search Java SDK**](https://search.maven.org/artifact/com.azure/azure-search-documents) client library to add semantic ranking to an existing search index.
+
+The quickstart assumes the following is available on your computer:
+- [Visual Studio Code](https://code.visualstudio.com/) with Java extensions or IntelliJ IDEA
+- [Java 21 (LTS)](/java/openjdk/install).
+- [Maven](https://maven.apache.org/download.cgi).
+
+### Set up local development environment
+
+1. Create a new Maven project directory.
+
+   ```bash
+   mkdir semantic-ranking-quickstart && cd semantic-ranking-quickstart
+   code .
+   ```
+
+1. Create a `pom.xml` file with required dependencies.
+
+   ```xml
+   <project xmlns="http://maven.apache.org/POM/4.0.0"
+            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
+            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
+            http://maven.apache.org/xsd/maven-4.0.0.xsd">
+       <modelVersion>4.0.0</modelVersion>
+   
+       <groupId>com.azure.search</groupId>
+       <artifactId>semantic-ranking-quickstart</artifactId>
+       <version>1.0-SNAPSHOT</version>
+   
+       <properties>
+           <maven.compiler.source>21</maven.compiler.source>
+           <maven.compiler.target>21</maven.compiler.target>
+           <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
+       </properties>
+   
+       <dependencies>
+           <dependency>
+               <groupId>com.azure</groupId>
+               <artifactId>azure-search-documents</artifactId>
+               <version>11.7.8</version>
+           </dependency>
+           <dependency>
+               <groupId>com.azure</groupId>
+               <artifactId>azure-identity</artifactId>
+               <version>1.17.0</version>
+           </dependency>
+       </dependencies>
+   </project>
+   ```
+
+1. Compile the project to resolve the dependencies:
+
+    ```bash
+    mvn compile
+    ```
+
+1. Create the source directory structure.
+
+   ```bash
+   mkdir -p src/main/java/com/azure/search/quickstart
+   mkdir -p src/main/resources
+   ```
+
+1. Create `src/main/resources/application.properties` and provide your search service endpoint. You can get the endpoint from the Azure portal on the search service **Overview** page.
+
+    ```properties
+    azure.search.endpoint=YOUR-SEARCH-SERVICE-ENDPOINT
+    azure.search.index.name=hotels-sample-index
+    semantic.configuration.name=semantic-config
+    ```
+
+### Sign in to Azure
+
+If you signed in to the [Azure portal](https://portal.azure.com), you're signed into Azure. If you aren't sure, use the Azure CLI to log in: `az login`. If you have multiple tenants and subscriptions, see [Quickstart: Connect without keys](../../search-get-started-rbac.md) for help on how to connect.
+
+## Create a common configuration class
+
+Create a file in `src/main/java/com/azure/search/quickstart` called `SearchConfig.java` to read the properties file and hold the environment variables and authentication credential.
+
+```java
+package com.azure.search.quickstart;
+
+import com.azure.identity.DefaultAzureCredential;
+import com.azure.identity.DefaultAzureCredentialBuilder;
+
+import java.io.IOException;
+import java.io.InputStream;
+import java.util.Properties;
+
+public class SearchConfig {
+    private static final Properties properties = new Properties();
+
+    static {
+        try (InputStream input = SearchConfig.class.getClassLoader()
+            .getResourceAsStream("application.properties")) {
+            properties.load(input);
+        } catch (IOException e) {
+            throw new RuntimeException(
+                "Failed to load application.properties", e);
+        }
+    }
+
+    public static final String SEARCH_ENDPOINT =
+        properties.getProperty("azure.search.endpoint");
+    public static final String INDEX_NAME =
+        properties.getProperty("azure.search.index.name");
+    public static final String SEMANTIC_CONFIG_NAME =
+        properties.getProperty("semantic.configuration.name");
+
+    public static final DefaultAzureCredential CREDENTIAL =
+        new DefaultAzureCredentialBuilder().build();
+
+    static {
+        System.out.println("Using Azure Search endpoint: " + SEARCH_ENDPOINT);
+        System.out.println("Using index name: " + INDEX_NAME + "\n");
+    }
+}
+```
+
+## Get the index schema
+
+In this section, you get settings for the existing `hotels-sample-index` index on your search service.
+
+1. Create a file in `src/main/java/com/azure/search/quickstart` called `GetIndexSettings.java`.
+
+    ```java
+    package com.azure.search.quickstart;
+    
+    import com.azure.search.documents.indexes.SearchIndexClientBuilder;
+    import com.azure.search.documents.indexes.models.SearchField;
+    import com.azure.search.documents.indexes.models.SearchIndex;
+    import com.azure.search.documents.indexes.models.SemanticConfiguration;
+    import com.azure.search.documents.indexes.models.SemanticField;
+    import com.azure.search.documents.indexes.models.SemanticSearch;
+    
+    public class GetIndexSettings {
+        public static void main(String[] args) {
+            var indexClient = new SearchIndexClientBuilder()
+                .endpoint(SearchConfig.SEARCH_ENDPOINT)
+                .credential(SearchConfig.CREDENTIAL)
+                .buildClient();
+    
+            System.out.println("Getting semantic search index settings...");
+    
+            SearchIndex index = indexClient.getIndex(SearchConfig.INDEX_NAME);
+    
+            System.out.println("Index name: " + index.getName());
+            System.out.println("Number of fields: " + index.getFields().size());
+    
+            for (SearchField field : index.getFields()) {
+                System.out.printf("Field: %s, Type: %s, Searchable: %s%n",
+                    field.getName(), field.getType(), field.isSearchable());
+            }
+    
+            SemanticSearch semanticSearch = index.getSemanticSearch();
+            if (semanticSearch != null &&
+                semanticSearch.getConfigurations() != null) {
+                System.out.println("Semantic search configurations: " +
+                    semanticSearch.getConfigurations().size());
+                for (SemanticConfiguration config :
+                    semanticSearch.getConfigurations()) {
+                    System.out.println("Configuration name: " + config.getName());
+                    SemanticField titleField = config.getPrioritizedFields().getTitleField();
+                    if (titleField != null) {
+                        System.out.println("Title field: " +
+                            titleField.getFieldName());
+                    }
+                }
+            } else {
+                System.out.println(
+                    "No semantic configuration exists for this index.");
+            }
+    
+            System.exit(0);
+        }
+    }
+    ```
+
+1. Compile and run the code:
+
+    ```bash
+    mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.GetIndexSettings"
+    ```
+
+1. Output is the name of the index, list of fields, and a statement indicating whether a semantic configuration exists. For the purposes of this quickstart, the message should say `No semantic configuration exists for this index`.
+
+## Update the index with a semantic configuration
+
+1. Create a file in `src/main/java/com/azure/search/quickstart` called `UpdateIndexSettings.java` to add a semantic configuration to the existing `hotels-sample-index` index on your search service.
+
+    ```java
+    package com.azure.search.quickstart;
+    
+    import com.azure.search.documents.indexes.SearchIndexClientBuilder;
+    import com.azure.search.documents.indexes.models.SearchIndex;
+    import com.azure.search.documents.indexes.models.SemanticConfiguration;
+    import com.azure.search.documents.indexes.models.SemanticField;
+    import com.azure.search.documents.indexes.models.SemanticPrioritizedFields;
+    import com.azure.search.documents.indexes.models.SemanticSearch;
+    
+    import java.util.ArrayList;
+    import java.util.List;
+    
+    public class UpdateIndexSettings {
+        public static void main(String[] args) {
+            try {
+                var indexClient = new SearchIndexClientBuilder()
+                    .endpoint(SearchConfig.SEARCH_ENDPOINT)
+                    .credential(SearchConfig.CREDENTIAL)
+                    .buildClient();
+    
+                SearchIndex existingIndex =
+                    indexClient.getIndex(SearchConfig.INDEX_NAME);
+    
+                // Create prioritized fields for semantic configuration
+                var prioritizedFields = new SemanticPrioritizedFields()
+                    .setTitleField(new SemanticField("HotelName"))
+                    .setKeywordsFields(List.of(new SemanticField("Tags")))
+                    .setContentFields(List.of(new SemanticField("Description")));
+    
+                var newSemanticConfiguration = new SemanticConfiguration(
+                    SearchConfig.SEMANTIC_CONFIG_NAME, prioritizedFields);
+    
+                // Add the semantic configuration to the index
+                SemanticSearch semanticSearch = existingIndex.getSemanticSearch();
+                if (semanticSearch == null) {
+                    semanticSearch = new SemanticSearch();
+                    existingIndex.setSemanticSearch(semanticSearch);
+                }
+    
+                List<SemanticConfiguration> configurations =
+                    semanticSearch.getConfigurations();
+                if (configurations == null) {
+                    configurations = new ArrayList<>();
+                    semanticSearch.setConfigurations(configurations);
+                }
+    
+                // Check if configuration already exists
+                boolean configExists = configurations.stream()
+                    .anyMatch(config -> SearchConfig.SEMANTIC_CONFIG_NAME
+                        .equals(config.getName()));
+    
+                if (!configExists) {
+                    configurations.add(newSemanticConfiguration);
+                }
+    
+                indexClient.createOrUpdateIndex(existingIndex);
+    
+                SearchIndex updatedIndex =
+                    indexClient.getIndex(SearchConfig.INDEX_NAME);
+    
+                System.out.println("Semantic configurations:");
+                System.out.println("-".repeat(40));
+    
+                SemanticSearch updatedSemanticSearch =
+                    updatedIndex.getSemanticSearch();
+                if (updatedSemanticSearch != null &&
+                    updatedSemanticSearch.getConfigurations() != null) {
+                    for (SemanticConfiguration config :
+                        updatedSemanticSearch.getConfigurations()) {
+                        System.out.println("Configuration name: " + config.getName());
+    
+                        SemanticPrioritizedFields fields =
+                            config.getPrioritizedFields();
+                        if (fields.getTitleField() != null) {
+                            System.out.println("Title field: " +
+                                fields.getTitleField().getFieldName());
+                        }
+                        if (fields.getKeywordsFields() != null) {
+                            List<String> keywords = fields.getKeywordsFields().stream()
+                                .map(SemanticField::getFieldName)
+                                .toList();
+                            System.out.println("Keywords fields: " +
+                                String.join(", ", keywords));
+                        }
+                        if (fields.getContentFields() != null) {
+                            List<String> content = fields.getContentFields().stream()
+                                .map(SemanticField::getFieldName)
+                                .toList();
+                            System.out.println("Content fields: " +
+                                String.join(", ", content));
+                        }
+                        System.out.println("-".repeat(40));
+                    }
+                } else {
+                    System.out.println("No semantic configurations found.");
+                }
+    
+                System.out.println("Semantic configuration updated successfully.");
+    
+                System.exit(0);
+            } catch (Exception e) {
+                System.err.println("Error updating semantic configuration: " +
+                    e.getMessage());
+            }
+        }
+    }
+    ```
+
+1. Run the code.
+
+    ```bash
+    mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.UpdateIndexSettings"
+    ```
+
+1. Output is the semantic configuration you just added, `Semantic configuration updated successfully.`.
+
+## Run semantic queries
+
+Once the `hotels-sample-index` index has a semantic configuration, you can run queries that include semantic parameters.
+
+1. Create a file in `src/main/java/com/azure/search/quickstart` called `SemanticQuery.java` to create a semantic query of the index.
+
+    ```java
+    package com.azure.search.quickstart;
+    
+    import com.azure.search.documents.SearchClientBuilder;
+    import com.azure.search.documents.SearchDocument;
+    import com.azure.search.documents.models.QueryType;
+    import com.azure.search.documents.models.SearchOptions;
+    import com.azure.search.documents.models.SearchResult;
+    import com.azure.search.documents.models.SemanticSearchOptions;
+    import com.azure.search.documents.util.SearchPagedIterable;
+    
+    public class SemanticQuery {
+        public static void main(String[] args) {
+            var searchClient = new SearchClientBuilder()
+                .endpoint(SearchConfig.SEARCH_ENDPOINT)
+                .indexName(SearchConfig.INDEX_NAME)
+                .credential(SearchConfig.CREDENTIAL)
+                .buildClient();
+    
+            var searchOptions = new SearchOptions()
+                .setQueryType(QueryType.SEMANTIC)
+                .setSemanticSearchOptions(new SemanticSearchOptions()
+                    .setSemanticConfigurationName(SearchConfig.SEMANTIC_CONFIG_NAME))
+                .setSelect("HotelId", "HotelName", "Description");
+    
+            SearchPagedIterable results = searchClient.search(
+                "walking distance to live music", searchOptions, null);
+    
+            int rowNumber = 1;
+            for (SearchResult result : results) {
+                var document = result.getDocument(SearchDocument.class);
+                double rerankerScore = result.getSemanticSearch().getRerankerScore();
+    
+                System.out.printf("Search result #%d:%n", rowNumber++);
+                System.out.printf("  Re-ranker Score: %.2f%n", rerankerScore);
+                System.out.printf("  HotelId: %s%n", document.get("HotelId"));
+                System.out.printf("  HotelName: %s%n", document.get("HotelName"));
+                System.out.printf("  Description: %s%n%n",
+                    document.get("Description") != null ?
+                        document.get("Description") : "N/A");
+            }
+    
+            System.exit(0);
+        }
+    }
+    ```
+
+1. Run the code.
+
+    ```bash
+    mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.SemanticQuery"
+    ```
+
+1. Output should consist of 13 documents, ordered by the reranker score.
+
+### Return captions
+
+Optionally, you can add captions to extract portions of the text and apply hit highlighting to the important terms and phrases.
+
+1. Create a file in `src/main/java/com/azure/search/quickstart` called `SemanticQueryWithCaptions.java`.
+
+    ```java
+    package com.azure.search.quickstart;
+    
+    import com.azure.search.documents.SearchClientBuilder;
+    import com.azure.search.documents.SearchDocument;
+    import com.azure.search.documents.models.QueryCaption;
+    import com.azure.search.documents.models.QueryCaptionResult;
+    import com.azure.search.documents.models.QueryCaptionType;
+    import com.azure.search.documents.models.QueryType;
+    import com.azure.search.documents.models.SearchOptions;
+    import com.azure.search.documents.models.SearchResult;
+    import com.azure.search.documents.models.SemanticSearchOptions;
+    import com.azure.search.documents.util.SearchPagedIterable;
+
+    import java.util.List;
+    
+    public class SemanticQueryWithCaptions {
+        public static void main(String[] args) {
+            var searchClient = new SearchClientBuilder()
+                .endpoint(SearchConfig.SEARCH_ENDPOINT)
+                .indexName(SearchConfig.INDEX_NAME)
+                .credential(SearchConfig.CREDENTIAL)
+                .buildClient();
+    
+            System.out.println("Using semantic configuration: " +
+                SearchConfig.SEMANTIC_CONFIG_NAME);
+            System.out.println("Search query: walking distance to live music");
+    
+            var searchOptions = new SearchOptions()
+                .setQueryType(QueryType.SEMANTIC)
+                .setSemanticSearchOptions(new SemanticSearchOptions()
+                    .setSemanticConfigurationName(SearchConfig.SEMANTIC_CONFIG_NAME)
+                    .setQueryCaption(new QueryCaption(QueryCaptionType.EXTRACTIVE)
+                        .setHighlightEnabled(true)))
+                .setSelect("HotelId", "HotelName", "Description");
+    
+            SearchPagedIterable results = searchClient.search(
+                "walking distance to live music", searchOptions, null);
+    
+            System.out.printf("Found results with semantic search%n%n");
+            int rowNumber = 1;
+    
+            for (SearchResult result : results) {
+                var document = result.getDocument(SearchDocument.class);
+                double rerankerScore = result.getSemanticSearch().getRerankerScore();
+    
+                System.out.printf("Search result #%d:%n", rowNumber++);
+                System.out.printf("  Re-ranker Score: %.2f%n", rerankerScore);
+                System.out.printf("  HotelName: %s%n", document.get("HotelName"));
+                System.out.printf("  Description: %s%n%n",
+                    document.get("Description") != null ?
+                        document.get("Description") : "N/A");
+    
+                // Handle captions
+                List<QueryCaptionResult> captions =
+                    result.getSemanticSearch().getQueryCaptions();
+                if (captions != null && !captions.isEmpty()) {
+                    QueryCaptionResult caption = captions.get(0);
+    
+                    if (caption.getHighlights() != null &&
+                        !caption.getHighlights().trim().isEmpty()) {
+                        System.out.printf("  Caption with highlights: %s%n",
+                            caption.getHighlights());
+                    } else if (caption.getText() != null &&
+                        !caption.getText().trim().isEmpty()) {
+                        System.out.printf("  Caption text: %s%n",
+                            caption.getText());
+                    } else {
+                        System.out.println(
+                            "  Caption exists but has no text or highlights content");
+                    }
+                } else {
+                    System.out.println("  No captions found for this result");
+                }
+                System.out.println("-".repeat(60));
+            }
+    
+            System.exit(0);
+        }
+    }
+    ```
+
+1. Run the code.
+
+    ```bash
+    mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.SemanticQueryWithCaptions"
+    ```
+
+1. Output should include a new caption element alongside search field. Captions are the most relevant passages in a result. If your index includes larger chunks of text, a caption is helpful for extracting the most interesting sentences.
+
+    ```console
+    Search result #1:
+      Re-ranker Score: 2.613231658935547
+      HotelName: Uptown Chic Hotel
+      Description: Chic hotel near the city. High-rise hotel in downtown, within walking distance to theaters, art galleries, restaurants and shops. Visit Seattle Art Museum by day, and then head over to Benaroya Hall to catch the evening's concert performance.
+
+      Caption with highlights: Chic hotel near the city. High-rise hotel in downtown, within walking distance to<em> theaters, </em>art galleries, restaurants and shops. Visit<em> Seattle Art Museum </em>by day, and then head over to<em> Benaroya Hall </em>to catch the evening's concert performance.
+    ```
+
+### Return semantic answers
+
+In this final query, return semantic answers.
+
+Semantic ranker can produce an answer to a query string that has the characteristics of a question. The generated answer is extracted verbatim from your content so it won't include composed content like what you might expect from a chat completion model.
+
+To produce a semantic answer, the question and answer must be closely aligned, and the model must find content that clearly answers the question. If potential answers fail to meet a confidence threshold, the model doesn't return an answer. For demonstration purposes, the question in this example is designed to get a response so that you can see the syntax.
+
+1. Create a file in `src/main/java/com/azure/search/quickstart` called `SemanticAnswer.java`.
+
+    ```java
+    package com.azure.search.quickstart;
+    
+    import com.azure.search.documents.SearchClientBuilder;
+    import com.azure.search.documents.SearchDocument;
+    import com.azure.search.documents.models.QueryAnswer;
+    import com.azure.search.documents.models.QueryAnswerResult;
+    import com.azure.search.documents.models.QueryAnswerType;
+    import com.azure.search.documents.models.QueryCaption;
+    import com.azure.search.documents.models.QueryCaptionResult;
+    import com.azure.search.documents.models.QueryCaptionType;
+    import com.azure.search.documents.models.QueryType;
+    import com.azure.search.documents.models.SearchOptions;
+    import com.azure.search.documents.models.SearchResult;
+    import com.azure.search.documents.models.SemanticSearchOptions;
+    import com.azure.search.documents.util.SearchPagedIterable;
+    
+    import java.util.List;
+    
+    public class SemanticAnswer {
+        public static void main(String[] args) {
+            var searchClient = new SearchClientBuilder()
+                .endpoint(SearchConfig.SEARCH_ENDPOINT)
+                .indexName(SearchConfig.INDEX_NAME)
+                .credential(SearchConfig.CREDENTIAL)
+                .buildClient();
+    
+            var searchOptions = new SearchOptions()
+                .setQueryType(QueryType.SEMANTIC)
+                .setSemanticSearchOptions(new SemanticSearchOptions()
+                    .setSemanticConfigurationName(SearchConfig.SEMANTIC_CONFIG_NAME)
+                    .setQueryCaption(new QueryCaption(QueryCaptionType.EXTRACTIVE))
+                    .setQueryAnswer(new QueryAnswer(QueryAnswerType.EXTRACTIVE)))
+                .setSelect("HotelName", "Description", "Category");
+    
+            SearchPagedIterable results = searchClient.search(
+                "What's a good hotel for people who like to read",
+                searchOptions, null);
+    
+            System.out.println("Answers:\n");
+    
+            // Extract semantic answers
+            List<QueryAnswerResult> semanticAnswers =
+                results.getSemanticResults().getQueryAnswers();
+            int answerNumber = 1;
+    
+            if (semanticAnswers != null) {
+                for (QueryAnswerResult answer : semanticAnswers) {
+                    System.out.printf("Semantic answer result #%d:%n",
+                        answerNumber++);
+    
+                    if (answer.getHighlights() != null &&
+                        !answer.getHighlights().trim().isEmpty()) {
+                        System.out.printf("Semantic Answer: %s%n",
+                            answer.getHighlights());
+                    } else {
+                        System.out.printf("Semantic Answer: %s%n", answer.getText());
+                    }
+                    System.out.printf("Semantic Answer Score: %.2f%n%n",
+                        answer.getScore());
+                }
+            }
+    
+            System.out.println("Search Results:\n");
+            int rowNumber = 1;
+    
+            // Iterate through search results
+            for (SearchResult result : results) {
+                var document = result.getDocument(SearchDocument.class);
+                double rerankerScore = result.getSemanticSearch().getRerankerScore();
+    
+                System.out.printf("Search result #%d:%n", rowNumber++);
+                System.out.printf("Re-ranker Score: %.2f%n", rerankerScore);
+                System.out.printf("Hotel: %s%n", document.get("HotelName"));
+                System.out.printf("Description: %s%n",
+                    document.get("Description") != null ?
+                        document.get("Description") : "N/A");
+    
+                List<QueryCaptionResult> captions =
+                    result.getSemanticSearch().getQueryCaptions();
+                if (captions != null && !captions.isEmpty()) {
+                    QueryCaptionResult caption = captions.get(0);
+                    if (caption.getHighlights() != null &&
+                        !caption.getHighlights().trim().isEmpty()) {
+                        System.out.printf("Caption: %s%n%n",
+                            caption.getHighlights());
+                    } else {
+                        System.out.printf("Caption: %s%n%n", caption.getText());
+                    }
+                } else {
+                    System.out.println();
+                }
+            }
+    
+            System.exit(0);
+        }
+    }
+    ```
+
+1. Run the code.
+
+    ```bash
+    mvn compile exec:java -Dexec.mainClass="com.azure.search.quickstart.SemanticAnswer"
+    ```
+
+1. Output should look similar to the following example, where the best answer to question is pulled from one of the results.
+
+    Recall that answers are *verbatim content* pulled from your index and might be missing phrases that a user would expect to see. To get *composed answers* as generated by a chat completion model, considering using a [RAG pattern](../../retrieval-augmented-generation-overview.md) or [agentic retrieval](../../search-agentic-retrieval-concept.md).
+
+    ```console
+    Semantic answer result #1:
+    Semantic Answer: Nature is Home on the beach. Explore the shore by day, and then come home to our shared living space to relax around a stone fireplace, sip something warm, and explore the<em> library </em>by night. Save up to 30 percent. Valid Now through the end of the year. Restrictions and blackouts may apply.
+    Semantic Answer Score: 0.9829999804496765
+    ```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい言語サポートの追加: Javaにおけるセマンティックランカーのクイックスタート"
}
```

### Explanation
このコードの変更は、新しい文書ファイル `semantic-ranker-java.md` の追加です。このファイルには、Azure AI Searchでのセマンティックランクを利用するためのJavaのクイックスタートガイドが含まれています。具体的には、クライアントのセットアップから、インデックスのスキーマを取得し、セマンティック構成を更新し、最終的にセマンティッククエリを実行する手順が細かく説明されています。

このガイドは、LuceneやElasticsearchといった他の検索エンジンの機能を強化するために設計されており、Azure AI Searchを使用する開発者が、効果的にセマンティック検索機能を実装できるようにすることを目的としています。全体で611行のコードと説明が含まれており、実際のコマンドやサンプルコードを通じてユーザーがステップバイステップで進められるようになっています。

## articles/search/search-get-started-semantic.md{#item-2b3902}

<details>
<summary>Diff</summary>
````diff
@@ -29,6 +29,12 @@ zone_pivot_groups: search-get-started-semantic
 
 ::: zone-end
 
+::: zone pivot="java"
+
+[!INCLUDE [Java quickstart](includes/quickstarts/semantic-ranker-java.md)]
+
+::: zone-end
+
 ::: zone pivot="python"
 
 [!INCLUDE [Python quickstart](includes/quickstarts/semantic-ranker-python.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaクイックスタートの追加: セマンティック検索ガイドの更新"
}
```

### Explanation
このコードの変更は、`search-get-started-semantic.md` ファイルに対しての軽微な更新であり、Javaに関するクイックスタートのリンクを追加しました。具体的には、ファイルの29行目に新たにJavaに関連するセクションを挿入し、そこにJavaのクイックスタートガイドへのインクルードを追加しています。この更新によって、ユーザーはセマンティック検索をJavaプログラミング言語を使用して開始するための明確なリソースを得ることができます。

この変更は、セマンティック検索に関連する他の言語（Pythonなど）に関するクイックスタートと同様に、Javaを使用する開発者にとって便利な情報源となります。全体として、セマンティック検索に関するドキュメントの使いやすさを向上させるものです。

## articles/search/search-how-to-index-markdown-blobs.md{#item-c94a20}

<details>
<summary>Diff</summary>
````diff
@@ -78,7 +78,7 @@ This setting can be changed after initial creation of the indexer, however the s
 
 ## Supported Markdown elements
 
-Markdown parsing will only split content based on headers. All other elements such as lists, code blocks, tables, and so forth, are treated as plain text and passed into a content field.
+Markdown parsing only splits content based on headers. All other elements such as lists, code blocks, tables, and so forth, are treated as plain text and passed into a content field.
 
 <a name="parsing-markdown-one-to-many"></a>
 
@@ -99,7 +99,7 @@ Content for section 2.
 
 ## Use one-to-many parsing mode
 
-The one-to-many parsing mode parses Markdown files into multiple search documents, where each document corresponds to a specific content section of the Markdown file based on the header metadata at that point in the document. The Markdown is parsed based on headers into search documents which contain the following content:
+The one-to-many parsing mode parses Markdown files into multiple search documents, where each document corresponds to a specific content section of the Markdown file based on the header metadata at that point in the document. The Markdown is parsed based on headers into search documents, which contain the following content:
 
 - `content`: A string that contains the raw Markdown found in a specific location, based on the header metadata at that point in the document.
 
@@ -169,7 +169,7 @@ api-key: [admin key]
 ```
 
 > [!NOTE]
-> The `submode` does not need to be set explicitly here because `oneToMany` is the default. 
+> The `submode` doesn't need to be set explicitly here because `oneToMany` is the default. 
 
 ### Indexer output for one-to-many parsing
 
@@ -249,7 +249,7 @@ In the one-to-one parsing mode, the entire Markdown document is indexed as a sin
 
 Within the indexer definition, set the `parsingMode` to `"markdown"` and use the optional `markdownHeaderDepth` parameter to define the maximum heading depth for chunking. If not specified, it defaults to `h6`, capturing all possible header depths.
 
-The Markdown is parsed based on headers into search documents which contain the following content: 
+The Markdown is parsed based on headers into search documents, which contain the following content: 
 
 - `document_content`: Contains the full Markdown text as a single string. This field serves as a raw representation of the input document. 
 
@@ -259,13 +259,13 @@ The Markdown is parsed based on headers into search documents which contain the
 
   - `header_name`: A string containing the text of the header as it appears in the Markdown document. This field provides a label or title for the section. 
 
-  - `content`: A string containing text content that immediately follows the header, up to the next header. This field captures the detailed information or description associated with the header. If there's no content directly under a header, this is an empty string. 
+  - `content`: A string containing text content that immediately follows the header, up to the next header. This field captures the detailed information or description associated with the header. If there's no content directly under a header, the value is an empty string. 
 
   - `ordinal_position`: An integer value indicating the position of the section within the document hierarchy. This field is used for ordering the sections in their original sequence as they appear in the document, beginning with an ordinal position of 1 and incrementing sequentially for each content block. 
 
   - `sections`: An array that contains objects representing subsections nested under the current section. This array follows the same structure as the top-level `sections` array, allowing for the representation of multiple levels of nested content. Each subsection object also includes `header_level`, `header_name`, `content`, and `ordinal_position` properties, enabling a recursive structure that represents and hierarchy of the Markdown content. 
 
-Here's the sample Markdown that we're using to explain an index schema that's designed around each parsing mode.
+Here's the sample Markdown that we're using to explain the index schemas designed around each parsing mode.
 
 ```md
 # Section 1
@@ -286,50 +286,56 @@ If you aren't utilizing field mappings, the shape of the index should reflect th
   "name": "my-markdown-index",
   "fields": [
   {
-    "name": "document_content",
+    "name": "id",
     "type": "Edm.String",
+    "key": true
+  },
+  {
+    "name": "document_content",
+    "type": "Edm.String"
+  },
   {
     "name": "sections",
-    "type": "Edm.ComplexType",
+    "type": "Collection(Edm.ComplexType)",
     "fields": [
     {
       "name": "header_level",
-      "type": "Edm.String",
+      "type": "Edm.String"
     },
     {
       "name": "header_name",
-      "type": "Edm.String",
+      "type": "Edm.String"
     },
     {
       "name": "content",
       "type": "Edm.String"
     },
     {
       "name": "ordinal_position",
-      "type": "Edm.Int"
+      "type": "Edm.Int32"
     },
     {
       "name": "sections",
-      "type": "Edm.ComplexType",
+      "type": "Collection(Edm.ComplexType)",
       "fields": [
       {
         "name": "header_level",
-        "type": "Edm.String",
+        "type": "Edm.String"
       },
       {
         "name": "header_name",
-        "type": "Edm.String",
+        "type": "Edm.String"
       },
       {
         "name": "content",
         "type": "Edm.String"
       },
       {
         "name": "ordinal_position",
-        "type": "Edm.Int"
+        "type": "Edm.Int32"
       }]
     }]
-  }
+  }]
 }
 ```
 
@@ -441,7 +447,81 @@ The resulting search document in the index would look as follows:
 ```
 
 > [!NOTE]
-> These examples specify how to use these parsing modes entirely with or without field mappings, but you can leverage both in one scenario if that suits your needs.
+> These examples specify how to use these parsing modes entirely with or without field mappings, but you can apply both in one scenario if it suits your needs.
+> 
+
+## Managing stale documents from Markdown re-indexing
+
+When using one-to-many parsing mode, re-indexing a modified Markdown file can result in stale or duplicate documents if sections are removed. This behavior is specific to one-to-many mode and doesn't apply to one-to-one parsing.
+
+### Behavior overview
+
+#### One-to-many parsing mode
+In `oneToMany` mode, each Markdown section (based on headers) is indexed as a separate search document. When the file is re-indexed:
+
+* **No automatic deletion**: The indexer overwrites existing documents with new ones, but it does not delete documents that no longer correspond to any content in the updated file.
+* **Potential for duplicates**: This issue specifically arises only when more sections are deleted than inserted between indexing runs. In such cases, leftover documents from the previous version remain in the index, leading to stale entries that no longer reflect the current state of the source file.
+
+#### One-to-one parsing mode
+In `oneToOne` mode, the entire Markdown file is indexed as a single search document. When the file is re-indexed:
+* **Overwrite behavior**: The existing document is replaced entirely with the new version.
+* **No stale sections**: When the file is re-indexed, the existing document is replaced with the updated version and removed content is no longer included. The only exception is if the file path or blob URI changes, which could result in a new document being created alongside the old one.
+
+### Workaround options
+
+To ensure the index reflects the current state of your Markdown files, consider one of the following approaches:
+
+#### Option 1. Soft delete with metadata
+This method uses a soft-delete to delete documents associated with a specific blob. For more information, see [Change and delete detection using indexers for Azure Storage in Azure AI Search](search-howto-index-changed-deleted-blobs.md#soft-delete-strategy-using-custom-metadata).
+
+Steps:
+
+1. Mark the blob as deleted by setting a metadata field.
+2. Let the indexer run. It deletes all documents in the index associated with that blob.
+3. Remove the soft-delete marker and re-index the file.
+     
+#### Option 2. Use the delete API
+
+Before re-indexing a modified Markdown file, explicitly delete the existing documents associated with that file using the [delete API](/rest/api/searchservice/documents#indexactiontype). You can either:
+
+* Manually indentify individual stale documents by identifying duplicates in the index to be deleted. This may be feasible for small, well-understood changes but can be time-consuming.
+* (**Recommended**) Remove all documents generated from the same parent file before re-indexing, ensuring inconsistencies are avoided.
+
+Steps:
+
+1. Identify the id  of the documents associated with the file. Use a query like the following example to retrieve the document key IDs (for example, `id`, `chunk_id`, etc.) for all documents tied to a specific file. Replace `metadata_storage_path` with the appropriate field in your index that maps to the file path or blob URI. This field must be a key.
+    ```http
+    GET https://[service name].search.windows.net/indexes/[index name]/docs?api-version=2025-05-01-preview
+    Content-Type: application/json
+    api-key: [admin key]
+
+
+      {  
+          "filter": "metadata_storage_path eq 'https://<storage-account>.blob.core.windows.net/<container-name>/<file-name>.md'",
+          "select": "id"
+      }
+    ```
+
+  2. Issue a delete request for the documents with the identified keys.
+      ```http
+      POST https://[service name].search.windows.net/indexes/[index name]/docs/index?api-version=2025-05-01-preview
+      Content-Type: application/json
+      api-key: [admin key]
+
+      {  
+        "value": [  
+          {  
+            "@search.action": "delete",  
+            "id": "aHR0c...jI1"  
+          },
+          {  
+            "@search.action": "delete",  
+            "id": "aHR0...MQ2"  
+          }  
+        ]  
+      }
+      ```
+  3. Re-index the updated file.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Markdownブロブのインデックス化に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、`search-how-to-index-markdown-blobs.md` ファイルに対する修正で、主に内容の明確化と改善に関するものであり、追加された97行と削除された17行を含んでいます。変更内容には、Markdownの解析に関する説明が具体的に整理され、目的に応じた一対多の解析モードと一対一の解析モードに関するセクションが強調されています。

特に、Markdownのセクションが検索ドキュメントとしてどのようにインデックス化されるか、またその際に発生する可能性のある古いドキュメントの問題に関する新しい管理戦略が追加されました。これらの変更により、ユーザーはMarkdownをインデックス化する際の動作や最適な管理方法に関して、より明確なガイダンスを受けることができます。

全体として、この更新は、Markdownドキュメントのインデックス化プロセスに関する情報を充実させ、ユーザーが抱える可能性のある問題への理解を深めることを目的としています。


