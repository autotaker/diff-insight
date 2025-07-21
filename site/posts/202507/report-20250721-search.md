---
date: '2025-07-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1217e71...MicrosoftDocs:043ab30
summary: このコード変更は、Azure AI Searchを利用したエージェントリトリーバルの実装に関する新しいクイックスタートガイドの追加を含む内容です。JavaScriptとTypeScriptのクイックスタートが新たに追加され、多言語サポートが強化されました。また、関連する記事のタイトルと内容も更新されています。この変更により、開発者はAzureを使った高度な検索体験をより簡単に実装できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1217e71...MicrosoftDocs:043ab30){target="_blank"}

<format>
# Highlights
このコード変更は、Azure AI Searchを用いたエージェントリトリーバルの実装に関連する新しいクイックスタートガイドの追加を含んでいます。JavaScriptとTypeScriptのクイックスタートが追加され、エージェントリトリーバルの多言語サポートが強化されました。さらに、エージェントリトリーバル関連の記事のタイトルと内容の更新が行われています。

## New features
- JavaScriptによるエージェントリトリーバルのクイックスタートガイドが追加されました。
- TypeScriptによるエージェントリトリーバルのクイックスタートガイドが追加されました。

## Breaking changes
特に重大な変更はありませんが、新しいクイックスタートガイドの追加が、ユーザーの選択肢を広げることに寄与しています。

## Other updates
- エージェントリトリーバルに関するクイックスタート記事のタイトルと説明が更新されました。

# Insights
このコード変更は、Azure AI Searchを活用したエージェントリトリーバルの実装を簡素化し、多様な言語でのサポートを強化することを目的としています。特に、エージェントリトリーバルは複雑なユーザークエリをサブクエリに分割して並行処理を行う手法を扱っており、多ターンの会話をより効果的に処理する能力を持ちます。JavaScriptとTypeScriptのクイックスタートを提供することで、JavaScript系の開発者が迅速にエージェントリトリーバルを試すことができるようになります。

また、エージェントリトリーバルのガイドに関しては、事前に必要なツールやサービスのセットアップ方法を詳細に示し、NASAのデータを用いた実用的なサンプルデータが含まれています。これにより、開発者は具体的な例を通じて機能の理解を深め、独自のプロジェクトに適用しやすくなります。

この変更は、Azureを利用した高度な検索体験の実装方法を、より幅広い開発者コミュニティに提供するものであり、その便益は顕著です。新たなリソースを通じて、エージェントリトリーバルを身近な技術とし、多様なプロジェクトに活用できるよう支援しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [agentic-retrieval-javascript.md](#item-715283) | new feature | エージェントリトリーバル用のJavaScriptクイックスタートの追加 | added | 1083 | 0 | 1083 | 
| [agentic-retrieval-typescript.md](#item-e6370b) | new feature | エージェントリトリーバル用のTypeScriptクイックスタートの追加 | added | 1294 | 0 | 1294 | 
| [search-get-started-agentic-retrieval.md](#item-4a40f4) | minor update | エージェントリトリーバルのクイックスタート記事のタイトルと内容の更新 | modified | 10 | 7 | 17 | 


# Modified Contents
## articles/search/includes/quickstarts/agentic-retrieval-javascript.md{#item-715283}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,1083 @@
+---
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 7/21/2025
+---
+[!INCLUDE [Feature preview](../previews/preview-generic.md)]
+
+In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by large language models (LLMs) and your proprietary data. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries in parallel, and extracts grounding data from documents indexed in Azure AI Search. The output is intended for integration with agentic and custom chat solutions.
+
+Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
+
+## Prerequisites
+
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
++ An [Azure AI Search service](../../search-create-service-portal.md) on the Basic tier or higher with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
+
++ An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects). You get an Azure AI Foundry resource (that you need for model deployments) when you create an Azure AI Foundry project.
+
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
+
+[!INCLUDE [Setup](./agentic-retrieval-setup.md)]
+
+## Setup
+
+1. Create a new folder `quickstart-agentic-retrieval` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir quickstart-agentic-retrieval && cd quickstart-agentic-retrieval
+    ```
+
+1. Create the `package.json` with the following command:
+
+    ```shell
+    npm init -y
+    ```
+
+1. Install the Azure AI Search client library ([Azure.Search.Documents](/javascript/api/overview/azure/search-documents-readme)) for JavaScript with:
+
+    ```console
+    npm install @azure/search-documents --version 12.2.0-alpha.20250606.1
+    ```
+1. Install the Azure OpenAI client library with:
+
+    ```console
+    npm install @azure/openai --version 5.10.1
+    ```
+
+1. Install the `dotenv` package to load environment variables from a `.env` file with:
+
+    ```console
+    npm install dotenv
+    ```
+
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the Azure Identity client library with:
+
+    ```console
+    npm install @azure/identity
+    ```
+
+## Create the index and knowledge agent
+
+1. Create a new file named `.env` in the `quickstart-agentic-retrieval` folder and add the following environment variables:
+
+    ```plaintext
+    AZURE_OPENAI_ENDPOINT=https://<your-ai-foundry-resource-name>.openai.azure.com/
+    AZURE_OPENAI_GPT_DEPLOYMENT=gpt-4.1-mini
+    AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-large
+    AZURE_SEARCH_ENDPOINT=https://<your-search-service-name>.search.windows.net
+    AZURE_SEARCH_INDEX_NAME=agentic-retrieval-sample
+    ```
+
+    Replace `<your-search-service-name>` and `<your-ai-foundry-resource-name>` with your actual Azure AI Search service name and Azure AI Foundry resource name.
+
+1. Paste the following code into a new file named `index.js`:
+
+    ```javascript
+    import { DefaultAzureCredential, getBearerTokenProvider } from '@azure/identity';
+    import { SearchIndexClient, SearchClient } from '@azure/search-documents';
+    import { AzureOpenAI } from "openai/index.mjs";
+    // Load the .env file if it exists
+    import * as dotenv from "dotenv";
+    dotenv.config();
+    // Configuration - Update these values for your environment
+    const config = {
+        searchEndpoint: process.env.AZURE_SEARCH_ENDPOINT || "https://your-search-service.search.windows.net",
+        azureOpenAIEndpoint: process.env.AZURE_OPENAI_ENDPOINT || "https://your-ai-foundry-resource.openai.azure.com/",
+        azureOpenAIGptDeployment: process.env.AZURE_OPENAI_GPT_DEPLOYMENT || "gpt-4.1-mini",
+        azureOpenAIGptModel: "gpt-4.1-mini",
+        azureOpenAIApiVersion: process.env.OPENAI_API_VERSION || "2025-03-01-preview",
+        azureOpenAIEmbeddingDeployment: process.env.AZURE_OPENAI_EMBEDDING_DEPLOYMENT || "text-embedding-3-large",
+        azureOpenAIEmbeddingModel: "text-embedding-3-large",
+        indexName: "earth_at_night",
+        agentName: "earth-search-agent",
+        searchApiVersion: "2025-05-01-Preview"
+    };
+    async function main() {
+        try {
+            console.log("🚀 Starting Azure AI Search agentic retrieval quickstart...\n");
+            // Initialize Azure credentials using managed identity (recommended)
+            const credential = new DefaultAzureCredential();
+            // Create search clients
+            const searchIndexClient = new SearchIndexClient(config.searchEndpoint, credential);
+            const searchClient = new SearchClient(config.searchEndpoint, config.indexName, credential);
+            // Create Azure OpenAI client
+            const scope = "https://cognitiveservices.azure.com/.default";
+            const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+            const openAIClient = new AzureOpenAI({
+                endpoint: config.azureOpenAIEndpoint,
+                apiVersion: config.azureOpenAIApiVersion,
+                azureADTokenProvider,
+            });
+            // Create search index with vector and semantic capabilities
+            await createSearchIndex(searchIndexClient);
+            // Upload sample documents
+            await uploadDocuments(searchClient);
+            // Create knowledge agent for agentic retrieval
+            await createKnowledgeAgent(credential);
+            // Run agentic retrieval with conversation
+            await runAgenticRetrieval(credential, openAIClient);
+            // Clean up - Delete knowledge agent and search index
+            await deleteKnowledgeAgent(credential);
+            await deleteSearchIndex(searchIndexClient);
+            console.log("✅ Quickstart completed successfully!");
+        }
+        catch (error) {
+            console.error("❌ Error in main execution:", error);
+            throw error;
+        }
+    }
+    async function createSearchIndex(indexClient) {
+        console.log("📊 Creating search index...");
+        const index = {
+            name: config.indexName,
+            fields: [
+                {
+                    name: "id",
+                    type: "Edm.String",
+                    key: true,
+                    filterable: true,
+                    sortable: true,
+                    facetable: true
+                },
+                {
+                    name: "page_chunk",
+                    type: "Edm.String",
+                    searchable: true,
+                    filterable: false,
+                    sortable: false,
+                    facetable: false
+                },
+                {
+                    name: "page_embedding_text_3_large",
+                    type: "Collection(Edm.Single)",
+                    searchable: true,
+                    filterable: false,
+                    sortable: false,
+                    facetable: false,
+                    vectorSearchDimensions: 3072,
+                    vectorSearchProfileName: "hnsw_text_3_large"
+                },
+                {
+                    name: "page_number",
+                    type: "Edm.Int32",
+                    filterable: true,
+                    sortable: true,
+                    facetable: true
+                }
+            ],
+            vectorSearch: {
+                profiles: [
+                    {
+                        name: "hnsw_text_3_large",
+                        algorithmConfigurationName: "alg",
+                        vectorizerName: "azure_openai_text_3_large"
+                    }
+                ],
+                algorithms: [
+                    {
+                        name: "alg",
+                        kind: "hnsw"
+                    }
+                ],
+                vectorizers: [
+                    {
+                        vectorizerName: "azure_openai_text_3_large",
+                        kind: "azureOpenAI",
+                        parameters: {
+                            resourceUrl: config.azureOpenAIEndpoint,
+                            deploymentId: config.azureOpenAIEmbeddingDeployment,
+                            modelName: config.azureOpenAIEmbeddingModel
+                        }
+                    }
+                ]
+            },
+            semanticSearch: {
+                defaultConfigurationName: "semantic_config",
+                configurations: [
+                    {
+                        name: "semantic_config",
+                        prioritizedFields: {
+                            contentFields: [
+                                { name: "page_chunk" }
+                            ]
+                        }
+                    }
+                ]
+            }
+        };
+        try {
+            await indexClient.createOrUpdateIndex(index);
+            console.log(`✅ Index '${config.indexName}' created or updated successfully.`);
+        }
+        catch (error) {
+            console.error("❌ Error creating index:", error);
+            throw error;
+        }
+    }
+    async function deleteSearchIndex(indexClient) {
+        console.log("🗑️ Deleting search index...");
+        try {
+            await indexClient.deleteIndex(config.indexName);
+            console.log(`✅ Search index '${config.indexName}' deleted successfully.`);
+        }
+        catch (error) {
+            if (error?.statusCode === 404 || error?.code === 'IndexNotFound') {
+                console.log(`ℹ️ Search index '${config.indexName}' does not exist or was already deleted.`);
+                return;
+            }
+            console.error("❌ Error deleting search index:", error);
+            throw error;
+        }
+    }
+    // Fetch Earth at Night documents from GitHub
+    async function fetchEarthAtNightDocuments() {
+        console.log("📡 Fetching Earth at Night documents from GitHub...");
+        const documentsUrl = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json";
+        try {
+            const response = await fetch(documentsUrl);
+            if (!response.ok) {
+                throw new Error(`Failed to fetch documents: ${response.status} ${response.statusText}`);
+            }
+            const documents = await response.json();
+            console.log(`✅ Fetched ${documents.length} documents from GitHub`);
+            // Validate and transform documents to match our interface
+            const transformedDocuments = documents.map((doc, index) => {
+                return {
+                    id: doc.id || String(index + 1),
+                    page_chunk: doc.page_chunk || doc.content || '',
+                    page_embedding_text_3_large: doc.page_embedding_text_3_large || new Array(3072).fill(0.1),
+                    page_number: doc.page_number || index + 1
+                };
+            });
+            return transformedDocuments;
+        }
+        catch (error) {
+            console.error("❌ Error fetching documents from GitHub:", error);
+            console.log("🔄 Falling back to sample documents...");
+            // Fallback to sample documents if fetch fails
+            return [
+                {
+                    id: "1",
+                    page_chunk: "The Earth at night reveals the patterns of human settlement and economic activity. City lights trace the contours of civilization, creating a luminous map of where people live and work.",
+                    page_embedding_text_3_large: new Array(3072).fill(0.1),
+                    page_number: 1
+                },
+                {
+                    id: "2",
+                    page_chunk: "From space, the aurora borealis appears as shimmering curtains of green and blue light dancing across the polar regions.",
+                    page_embedding_text_3_large: new Array(3072).fill(0.2),
+                    page_number: 2
+                }
+                // Add more fallback documents as needed
+            ];
+        }
+    }
+    async function uploadDocuments(searchClient) {
+        console.log("📄 Uploading documents...");
+        try {
+            // Fetch documents from GitHub
+            const documents = await fetchEarthAtNightDocuments();
+            const result = await searchClient.uploadDocuments(documents);
+            console.log(`✅ Uploaded ${result.results.length} documents successfully.`);
+            // Wait for indexing to complete
+            console.log("⏳ Waiting for document indexing to complete...");
+            await new Promise(resolve => setTimeout(resolve, 5000));
+            console.log("✅ Document indexing completed.");
+        }
+        catch (error) {
+            console.error("❌ Error uploading documents:", error);
+            throw error;
+        }
+    }
+    async function createKnowledgeAgent(credential) {
+        // In case the agent already exists, delete it first
+        await deleteKnowledgeAgent(credential);
+        console.log("🤖 Creating knowledge agent...");
+        const agentDefinition = {
+            name: config.agentName,
+            description: "Knowledge agent for Earth at Night e-book content",
+            models: [
+                {
+                    kind: "azureOpenAI",
+                    azureOpenAIParameters: {
+                        resourceUri: config.azureOpenAIEndpoint,
+                        deploymentId: config.azureOpenAIGptDeployment,
+                        modelName: config.azureOpenAIGptModel
+                    }
+                }
+            ],
+            targetIndexes: [
+                {
+                    indexName: config.indexName,
+                    defaultRerankerThreshold: 2.5
+                }
+            ]
+        };
+        try {
+            const token = await getAccessToken(credential, "https://search.azure.com/.default");
+            const response = await fetch(`${config.searchEndpoint}/agents/${config.agentName}?api-version=${config.searchApiVersion}`, {
+                method: 'PUT',
+                headers: {
+                    'Content-Type': 'application/json',
+                    'Authorization': `Bearer ${token}`
+                },
+                body: JSON.stringify(agentDefinition)
+            });
+            if (!response.ok) {
+                const errorText = await response.text();
+                throw new Error(`Failed to create knowledge agent: ${response.status} ${response.statusText}\n${errorText}`);
+            }
+            console.log(`✅ Knowledge agent '${config.agentName}' created successfully.`);
+        }
+        catch (error) {
+            console.error("❌ Error creating knowledge agent:", error);
+            throw error;
+        }
+    }
+    async function runAgenticRetrieval(credential, openAIClient) {
+        console.log("🔍 Running agentic retrieval...");
+        const messages = [
+            {
+                role: "system",
+                content: `A Q&A agent that can answer questions about the Earth at night.
+    Sources have a JSON format with a ref_id that must be cited in the answer.
+    If you do not have the answer, respond with "I don't know".`
+            },
+            {
+                role: "user",
+                content: "Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown? Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?"
+            }
+        ];
+        try {
+            // Call agentic retrieval API
+            const userMessages = messages.filter(m => m.role !== "system");
+            const retrievalResponse = await callAgenticRetrieval(credential, userMessages);
+            // Extract the assistant response from agentic retrieval
+            let assistantContent = '';
+            if (typeof retrievalResponse.response === 'string') {
+                assistantContent = retrievalResponse.response;
+            }
+            else if (Array.isArray(retrievalResponse.response)) {
+                assistantContent = JSON.stringify(retrievalResponse.response);
+            }
+            // Add assistant response to conversation history
+            messages.push({
+                role: "assistant",
+                content: assistantContent
+            });
+            console.log(assistantContent);
+            // Log activities and results...
+            console.log("\nActivities:");
+            if (retrievalResponse.activity && Array.isArray(retrievalResponse.activity)) {
+                retrievalResponse.activity.forEach((activity) => {
+                    const activityType = activity.activityType || activity.type || 'UnknownActivityRecord';
+                    console.log(`Activity Type: ${activityType}`);
+                    console.log(JSON.stringify(activity, null, 2));
+                });
+            }
+            console.log("Results");
+            if (retrievalResponse.references && Array.isArray(retrievalResponse.references)) {
+                retrievalResponse.references.forEach((reference) => {
+                    const referenceType = reference.referenceType || reference.type || 'AzureSearchDoc';
+                    console.log(`Reference Type: ${referenceType}`);
+                    console.log(JSON.stringify(reference, null, 2));
+                });
+            }
+            // Now do chat completion with full conversation history
+            await generateFinalAnswer(openAIClient, messages);
+            // Continue conversation with second question
+            await continueConversation(credential, openAIClient, messages);
+        }
+        catch (error) {
+            console.error("❌ Error in agentic retrieval:", error);
+            throw error;
+        }
+    }
+    async function generateFinalAnswer(openAIClient, messages) {
+        console.log("\n[ASSISTANT]: ");
+        try {
+            const completion = await openAIClient.chat.completions.create({
+                model: config.azureOpenAIGptDeployment,
+                messages: messages.map(m => ({ role: m.role, content: m.content })),
+                max_tokens: 1000,
+                temperature: 0.7
+            });
+            const answer = completion.choices[0].message.content;
+            console.log(answer?.replace(/\./g, "\n"));
+            // Add this response to conversation history
+            if (answer) {
+                messages.push({
+                    role: "assistant",
+                    content: answer
+                });
+            }
+        }
+        catch (error) {
+            console.error("❌ Error generating final answer:", error);
+            throw error;
+        }
+    }
+    async function callAgenticRetrieval(credential, messages) {
+        // Convert messages to the correct format expected by the Knowledge agent
+        const agentMessages = messages.map(msg => ({
+            role: msg.role,
+            content: [
+                {
+                    type: "text",
+                    text: msg.content
+                }
+            ]
+        }));
+        const retrievalRequest = {
+            messages: agentMessages,
+            targetIndexParams: [
+                {
+                    indexName: config.indexName,
+                    rerankerThreshold: 2.5,
+                    maxDocsForReranker: 100,
+                    includeReferenceSourceData: true
+                }
+            ]
+        };
+        const token = await getAccessToken(credential, "https://search.azure.com/.default");
+        const response = await fetch(`${config.searchEndpoint}/agents/${config.agentName}/retrieve?api-version=${config.searchApiVersion}`, {
+            method: 'POST',
+            headers: {
+                'Content-Type': 'application/json',
+                'Authorization': `Bearer ${token}`
+            },
+            body: JSON.stringify(retrievalRequest)
+        });
+        if (!response.ok) {
+            const errorText = await response.text();
+            throw new Error(`Agentic retrieval failed: ${response.status} ${response.statusText}\n${errorText}`);
+        }
+        return await response.json();
+    }
+    async function deleteKnowledgeAgent(credential) {
+        console.log("🗑️ Deleting knowledge agent...");
+        try {
+            const token = await getAccessToken(credential, "https://search.azure.com/.default");
+            const response = await fetch(`${config.searchEndpoint}/agents/${config.agentName}?api-version=${config.searchApiVersion}`, {
+                method: 'DELETE',
+                headers: {
+                    'Authorization': `Bearer ${token}`
+                }
+            });
+            if (!response.ok) {
+                if (response.status === 404) {
+                    console.log(`ℹ️ Knowledge agent '${config.agentName}' does not exist or was already deleted.`);
+                    return;
+                }
+                const errorText = await response.text();
+                throw new Error(`Failed to delete knowledge agent: ${response.status} ${response.statusText}\n${errorText}`);
+            }
+            console.log(`✅ Knowledge agent '${config.agentName}' deleted successfully.`);
+        }
+        catch (error) {
+            console.error("❌ Error deleting knowledge agent:", error);
+            throw error;
+        }
+    }
+    async function continueConversation(credential, openAIClient, messages) {
+        console.log("\n💬 === Continuing Conversation ===");
+        // Add follow-up question
+        const followUpQuestion = "How do I find lava at night?";
+        console.log(`❓ Follow-up question: ${followUpQuestion}`);
+        messages.push({
+            role: "user",
+            content: followUpQuestion
+        });
+        try {
+            // Don't include system messages in this retrieval
+            const userAssistantMessages = messages.filter((m) => m.role !== "system");
+            const newRetrievalResponse = await callAgenticRetrieval(credential, userAssistantMessages);
+            // Extract assistant response and add to conversation
+            let assistantContent = '';
+            if (typeof newRetrievalResponse.response === 'string') {
+                assistantContent = newRetrievalResponse.response;
+            }
+            else if (Array.isArray(newRetrievalResponse.response)) {
+                assistantContent = JSON.stringify(newRetrievalResponse.response);
+            }
+            // Add assistant response to conversation history
+            messages.push({
+                role: "assistant",
+                content: assistantContent
+            });
+            console.log(assistantContent);
+            // Log activities and results like the first retrieval
+            console.log("\nActivities:");
+            if (newRetrievalResponse.activity && Array.isArray(newRetrievalResponse.activity)) {
+                newRetrievalResponse.activity.forEach((activity) => {
+                    const activityType = activity.activityType || activity.type || 'UnknownActivityRecord';
+                    console.log(`Activity Type: ${activityType}`);
+                    console.log(JSON.stringify(activity, null, 2));
+                });
+            }
+            console.log("Results");
+            if (newRetrievalResponse.references && Array.isArray(newRetrievalResponse.references)) {
+                newRetrievalResponse.references.forEach((reference) => {
+                    const referenceType = reference.referenceType || reference.type || 'AzureSearchDoc';
+                    console.log(`Reference Type: ${referenceType}`);
+                    console.log(JSON.stringify(reference, null, 2));
+                });
+            }
+            // Generate final answer for follow-up
+            await generateFinalAnswer(openAIClient, messages);
+            console.log("\n🎉 === Conversation Complete ===");
+        }
+        catch (error) {
+            console.error("❌ Error in conversation continuation:", error);
+            throw error;
+        }
+    }
+    async function getAccessToken(credential, scope) {
+        const tokenResponse = await credential.getToken(scope);
+        return tokenResponse.token;
+    }
+    // Error handling wrapper
+    async function runWithErrorHandling() {
+        try {
+            await main();
+        }
+        catch (error) {
+            console.error("💥 Application failed:", error);
+            process.exit(1);
+        }
+    }
+    // Execute the application - ES module style
+    runWithErrorHandling();
+    export { main, createSearchIndex, deleteSearchIndex, fetchEarthAtNightDocuments, uploadDocuments, createKnowledgeAgent, deleteKnowledgeAgent, runAgenticRetrieval };
+    ```
+
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
+## Output
+
+The output of the application should look similar to the following:
+
+```plaintext
+[dotenv@17.2.0] injecting env (0) from .env (tip: ⚙️  override existing env vars with { override: true })
+🚀 Starting Azure AI Search agentic retrieval quickstart...
+
+📊 Creating search index...
+✅ Index 'earth_at_night' created or updated successfully.
+📄 Uploading documents...
+📡 Fetching Earth at Night documents from GitHub...
+✅ Fetched 194 documents from GitHub
+✅ Uploaded 194 documents successfully.
+⏳ Waiting for document indexing to complete...
+✅ Document indexing completed.
+🗑️ Deleting knowledge agent...
+ℹ️ Knowledge agent 'earth-search-agent' does not exist or was already deleted.
+🤖 Creating knowledge agent...
+✅ Knowledge agent 'earth-search-agent' created successfully.
+🔍 Running agentic retrieval...
+[{"role":"assistant","content":[{"type":"text","text":"[]"}]}]
+
+Activities:
+Activity Type: ModelQueryPlanning
+{
+  "type": "ModelQueryPlanning",
+  "id": 0,
+  "inputTokens": 1379,
+  "outputTokens": 551
+}
+Activity Type: AzureSearchQuery
+{
+  "type": "AzureSearchQuery",
+  "id": 1,
+  "targetIndex": "earth_at_night",
+  "query": {
+    "search": "Why do suburban areas show greater December brightening compared to urban cores despite higher absolute light levels downtown?",
+    "filter": null
+  },
+  "queryTime": "2025-07-20T16:12:59.804Z",
+  "count": 0,
+  "elapsedMs": 549
+}
+Activity Type: AzureSearchQuery
+{
+  "type": "AzureSearchQuery",
+  "id": 2,
+  "targetIndex": "earth_at_night",
+  "query": {
+    "search": "Why is the Phoenix nighttime street grid sharply visible from space, while large stretches of interstate highways between Midwestern cities appear comparatively dim?",
+    "filter": null
+  },
+  "queryTime": "2025-07-20T16:13:00.061Z",
+  "count": 0,
+  "elapsedMs": 256
+}
+Activity Type: AzureSearchSemanticRanker
+{
+  "type": "AzureSearchSemanticRanker",
+  "id": 3,
+  "inputTokens": 47630
+}
+Results
+
+[ASSISTANT]: 
+Suburban belts show larger December brightening than urban cores despite higher absolute light levels downtown because suburban areas often have more seasonal variation in lighting usage, such as increased decorative and outdoor lighting during the holiday season in December
+ Urban cores typically have more constant and dense lighting throughout the year, so the relative increase in brightness during December is less pronounced compared to suburban areas
+\n\nThe Phoenix nighttime street grid is sharply visible from space because the city has a well-planned, extensive grid of streets with consistent and bright street lighting
+ In contrast, large stretches of interstate highways between Midwestern cities appear comparatively dim because these highways have less continuous lighting and lower intensity lights, making them less visible from space
+\n\n(Note: These explanations are based on general knowledge about urban lighting patterns and visibility from space; specific studies or sources were not provided
+)
+
+💬 === Continuing Conversation ===
+❓ Follow-up question: How do I find lava at night?
+[{"role":"assistant","content":[{"type":"text","text":"[{\"ref_id\":0,\"content\":\"<!-- PageHeader=\\\"Volcanoes\\\" -->\\n\\n### Nighttime Glow at Mount Etna - Italy\\n\\nAt about 2:30 a.m. local time on March 16, 2017, the VIIRS DNB on the Suomi NPP satellite captured this nighttime image of lava flowing on Mount Etna in Sicily, Italy. Etna is one of the world's most active volcanoes.\\n\\n#### Figure: Location of Mount Etna\\nA world globe is depicted, with a marker indicating the location of Mount Etna in Sicily, Italy, in southern Europe near the center of the Mediterranean Sea.\\n\\n<!-- PageFooter=\\\"Earth at Night\\\" -->\\n<!-- PageNumber=\\\"48\\\" -->\"},{\"ref_id\":1,\"content\":\"<!-- PageHeader=\\\"Volcanoes\\\" -->\\n\\n## Volcanoes\\n\\n### The Infrared Glows of Kilauea's Lava Flows—Hawaii\\n\\nIn early May 2018, an eruption on Hawaii's Kilauea volcano began to unfold. The eruption took a dangerous turn on May 3, 2018, when new fissures opened in the residential neighborhood of Leilani Estates. During the summer-long eruptive event, other fissures emerged along the East Rift Zone. Lava from vents along the rift zone flowed downslope, reaching the ocean in several areas, and filling in Kapoho Bay.\\n\\nA time series of Landsat 8 imagery shows the progression of the lava flows from May 16 to August 13. The night view combines thermal, shortwave infrared, and near-infrared wavelengths to tease out the very hot lava (bright white), cooling lava (red), and lava flows obstructed by clouds (purple).\\n\\n#### Figure: Location of Kilauea Volcano, Hawaii\\n\\nA globe is shown centered on North America, with a marker placed in the Pacific Ocean indicating the location of Hawaii, to the southwest of the mainland United States.\\n\\n<!-- PageFooter=\\\"Earth at Night\\\" -->\\n<!-- PageNumber=\\\"44\\\" -->\"},{\"ref_id\":2,\"content\":\"For the first time in perhaps a decade, Mount Etna experienced a \\\"flank eruption\\\"—erupting from its side instead of its summit—on December 24, 2018. The activity was accompanied by 130 earthquakes occurring over three hours that morning. Mount Etna, Europe’s most active volcano, has seen periodic activity on this part of the mountain since 2013. The Operational Land Imager (OLI) on the Landsat 8 satellite acquired the main image of Mount Etna on December 28, 2018.\\n\\nThe inset image highlights the active vent and thermal infrared signature from lava flows, which can be seen near the newly formed fissure on the southeastern side of the volcano. The inset was created with data from OLI and the Thermal Infrared Sensor (TIRS) on Landsat 8. Ash spewing from the fissure cloaked adjacent villages and delayed aircraft from landing at the nearby Catania airport. Earthquakes occurred in the subsequent days after the initial eruption and displaced hundreds of people from their homes.\\n\\nFor nighttime images of Mount Etna’s March 2017 eruption, see pages 48–51.\\n\\n---\\n\\n### Hazards of Volcanic Ash Plumes and Satellite Observation\\n\\nWith the help of moonlight, satellite instruments can track volcanic ash plumes, which present significant hazards to airplanes in flight. The volcanic ash—composed of tiny pieces of glass and rock—is abrasive to engine turbine blades, and can melt on the blades and other engine parts, causing damage and even engine stalls. This poses a danger to both the plane’s integrity and passenger safety. Volcanic ash also reduces visibility for pilots and can cause etching of windshields, further reducing pilots’ ability to see. Nightlight images can be combined with thermal images to provide a more complete view of volcanic activity on Earth’s surface.\\n\\nThe VIIRS Day/Night Band (DNB) on polar-orbiting satellites uses faint light sources such as moonlight, airglow (the atmosphere’s self-illumination through chemical reactions), zodiacal light (sunlight scattered by interplanetary dust), and starlight from the Milky Way. Using these dim light sources, the DNB can detect changes in clouds, snow cover, and sea ice:\\n\\n#### Table: Light Sources Used by VIIRS DNB\\n\\n| Light Source         | Description                                                                  |\\n|----------------------|------------------------------------------------------------------------------|\\n| Moonlight            | Reflected sunlight from the Moon, illuminating Earth's surface at night      |\\n| Airglow              | Atmospheric self-illumination from chemical reactions                        |\\n| Zodiacal Light       | Sunlight scattered by interplanetary dust                                    |\\n| Starlight/Milky Way  | Faint illumination provided by stars in the Milky Way                        |\\n\\nGeostationary Operational Environmental Satellites (GOES), managed by NOAA, orbit over Earth’s equator and offer uninterrupted observations of North America. High-latitude areas such as Alaska benefit from polar-orbiting satellites like Suomi NPP, which provide overlapping coverage at the poles, enabling more data collection in these regions. During polar darkness (winter months), VIIRS DNB data allow scientists to:\\n\\n- Observe sea ice formation\\n- Monitor snow cover extent at the highest latitudes\\n- Detect open water for ship navigation\\n\\n#### Table: Satellite Coverage Overview\\n\\n| Satellite Type          | Orbit           | Coverage Area         | Special Utility                              |\\n|------------------------|-----------------|----------------------|----------------------------------------------|\\n| GOES                   | Geostationary   | Equatorial/North America | Continuous regional monitoring              |\\n| Polar-Orbiting (e.g., Suomi NPP) | Polar-orbiting    | Poles/high latitudes      | Overlapping passes; useful during polar night|\\n\\n---\\n\\n### Weather Forecasting and Nightlight Data\\n\\nThe use of nightlight data by weather forecasters is growing as the VIIRS instrument enables observation of clouds at night illuminated by sources such as moonlight and lightning. Scientists use these data to study the nighttime behavior of weather systems, including severe storms, which can develop and strike populous areas at night as well as during the day. Combined with thermal data, visible nightlight data allow the detection of clouds at various heights in the atmosphere, such as dense marine fog. This capability enables weather forecasters to issue marine advisories with higher confidence, leading to greater utility. (See \\\"Marine Layer Clouds—California\\\" on page 56.)\\n\\nIn this section of the book, you will see how nightlight data are used to observe nature’s spectacular light shows across a wide range of sources.\\n\\n---\\n\\n#### Notable Data from Mount Etna Flank Eruption (December 2018)\\n\\n| Event/Observation                  | Details                                                                    |\\n|-------------------------------------|----------------------------------------------------------------------------|\\n| Date of Flank Eruption              | December 24, 2018                                                          |\\n| Number of Earthquakes               | 130 earthquakes within 3 hours                                              |\\n| Image Acquisition                   | December 28, 2018 by Landsat 8 OLI                                         |\\n| Location of Eruption                | Southeastern side of Mount Etna                                            |\\n| Thermal Imaging Data                | From OLI and TIRS (Landsat 8), highlighting active vent and lava flows     |\\n| Impact on Villages/Air Transport    | Ash covered villages; delayed aircraft at Catania airport                  |\\n| Displacement                        | Hundreds of residents displaced                                            |\\n| Ongoing Seismic Activity            | Earthquakes continued after initial eruption                               |\\n\\n---\\n\\n<!-- PageFooter=\\\"Earth at Night\\\" -->\\n<!-- PageNumber=\\\"30\\\" -->\"},{\"ref_id\":3,\"content\":\"# Volcanoes\\n\\n---\\n\\n### Mount Etna Erupts - Italy\\n\\nThe highly active Mount Etna in Italy sent red lava rolling down its flank on March 19, 2017. An astronaut onboard the ISS took the photograph below of the volcano and its environs that night. City lights surround the mostly dark volcanic area.\\n\\n---\\n\\n#### Figure 1: Location of Mount Etna, Italy\\n\\nA world map highlighting the location of Mount Etna in southern Italy. The marker indicates its geographic placement on the east coast of Sicily, Italy, in the Mediterranean region, south of mainland Europe and north of northern Africa.\\n\\n---\\n\\n#### Figure 2: Nighttime View of Mount Etna's Eruption and Surrounding Cities\\n\\nThis is a nighttime satellite image taken on March 19, 2017, showing the eruption of Mount Etna (southeastern cone) with visible bright red and orange coloring indicating flowing lava from a lateral vent. The surrounding areas are illuminated by city lights, with the following geographic references labeled:\\n\\n| Location        | Position in Image         | Visible Characteristics                    |\\n|-----------------|--------------------------|--------------------------------------------|\\n| Mt. Etna (southeastern cone) | Top center-left | Bright red/orange lava flow                |\\n| Lateral vent    | Left of the volcano       | Faint red/orange flow extending outwards   |\\n| Resort          | Below the volcano, to the left   | Small cluster of lights                    |\\n| Giarre          | Top right                 | Bright cluster of city lights              |\\n| Acireale        | Center right              | Large, bright area of city lights          |\\n| Biancavilla     | Bottom left               | Smaller cluster of city lights             |\\n\\nAn arrow pointing north is shown on the image for orientation.\\n\\n---\\n\\n<!-- Earth at Night Page Footer -->\\n<!-- Page Number: 50 -->\"},{\"ref_id\":4,\"content\":\"## Nature's Light Shows\\n\\nAt night, with the light of the Sun removed, nature's brilliant glow from Earth's surface becomes visible to the naked eye from space. Some of Earth's most spectacular light shows are natural, like the aurora borealis, or Northern Lights, in the Northern Hemisphere (aurora australis, or Southern Lights, in the Southern Hemisphere). The auroras are natural electrical phenomena caused by charged particles that race from the Sun toward Earth, inducing chemical reactions in the upper atmosphere and creating the appearance of streamers of reddish or greenish light in the sky, usually near the northern or southern magnetic pole. Other natural lights can indicate danger, like a raging forest fire encroaching on a city, town, or community, or lava spewing from an erupting volcano.\\n\\nWhatever the source, the ability of humans to monitor nature's light shows at night has practical applications for society. For example, tracking fires during nighttime hours allows for continuous monitoring and enhances our ability to protect humans and other animals, plants, and infrastructure. Combined with other data sources, our ability to observe the light of fires at night allows emergency managers to more efficiently and accurately issue warnings and evacuation orders and allows firefighting efforts to continue through the night. With enough moonlight (e.g., full-Moon phase), it's even possible to track the movement of smoke plumes at night, which can impact air quality, regardless of time of day.\\n\\nAnother natural source of light at night is emitted from glowing lava flows at the site of active volcanoes. Again, with enough moonlight, these dramatic scenes can be tracked and monitored for both scientific research and public safety.\\n\\n\\n### Figure: The Northern Lights Viewed from Space\\n\\n**September 17, 2011**\\n\\nThis photo, taken from the International Space Station on September 17, 2011, shows a spectacular display of the aurora borealis (Northern Lights) as green and reddish light in the night sky above Earth. In the foreground, part of a Soyuz spacecraft is visible, silhouetted against the bright auroral light. The green glow is generated by energetic charged particles from the Sun interacting with Earth's upper atmosphere, exciting oxygen and nitrogen atoms, and producing characteristic colors. The image demonstrates the vividness and grandeur of natural night-time light phenomena as seen from orbit.\"}]"}]}]
+
+Activities:
+Activity Type: ModelQueryPlanning
+{
+  "type": "ModelQueryPlanning",
+  "id": 0,
+  "inputTokens": 1598,
+  "outputTokens": 159
+}
+Activity Type: AzureSearchQuery
+{
+  "type": "AzureSearchQuery",
+  "id": 1,
+  "targetIndex": "earth_at_night",
+  "query": {
+    "search": "How can I locate lava flows during nighttime?",
+    "filter": null
+  },
+  "queryTime": "2025-07-20T16:13:10.659Z",
+  "count": 5,
+  "elapsedMs": 260
+}
+Activity Type: AzureSearchSemanticRanker
+{
+  "type": "AzureSearchSemanticRanker",
+  "id": 2,
+  "inputTokens": 24146
+}
+Results
+Reference Type: AzureSearchDoc
+{
+  "type": "AzureSearchDoc",
+  "id": "0",
+  "activitySource": 1,
+  "docKey": "earth_at_night_508_page_64_verbalized",
+  "sourceData": {
+    "id": "earth_at_night_508_page_64_verbalized",
+    "page_chunk": "<!-- PageHeader=\"Volcanoes\" -->\n\n### Nighttime Glow at Mount Etna - Italy\n\nAt about 2:30 a.m. local time on March 16, 2017, the VIIRS DNB on the Suomi NPP satellite captured this nighttime image of lava flowing on Mount Etna in Sicily, Italy. Etna is one of the world's most active volcanoes.\n\n#### Figure: Location of Mount Etna\nA world globe is depicted, with a marker indicating the location of Mount Etna in Sicily, Italy, in southern Europe near the center of the Mediterranean Sea.\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"48\" -->"
+  }
+}
+Reference Type: AzureSearchDoc
+{
+  "type": "AzureSearchDoc",
+  "id": "1",
+  "activitySource": 1,
+  "docKey": "earth_at_night_508_page_60_verbalized",
+  "sourceData": {
+    "id": "earth_at_night_508_page_60_verbalized",
+    "page_chunk": "<!-- PageHeader=\"Volcanoes\" -->\n\n## Volcanoes\n\n### The Infrared Glows of Kilauea's Lava Flows—Hawaii\n\nIn early May 2018, an eruption on Hawaii's Kilauea volcano began to unfold. The eruption took a dangerous turn on May 3, 2018, when new fissures opened in the residential neighborhood of Leilani Estates. During the summer-long eruptive event, other fissures emerged along the East Rift Zone. Lava from vents along the rift zone flowed downslope, reaching the ocean in several areas, and filling in Kapoho Bay.\n\nA time series of Landsat 8 imagery shows the progression of the lava flows from May 16 to August 13. The night view combines thermal, shortwave infrared, and near-infrared wavelengths to tease out the very hot lava (bright white), cooling lava (red), and lava flows obstructed by clouds (purple).\n\n#### Figure: Location of Kilauea Volcano, Hawaii\n\nA globe is shown centered on North America, with a marker placed in the Pacific Ocean indicating the location of Hawaii, to the southwest of the mainland United States.\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"44\" -->"
+  }
+}
+Reference Type: AzureSearchDoc
+{
+  "type": "AzureSearchDoc",
+  "id": "2",
+  "activitySource": 1,
+  "docKey": "earth_at_night_508_page_46_verbalized",
+  "sourceData": {
+    "id": "earth_at_night_508_page_46_verbalized",
+    "page_chunk": "For the first time in perhaps a decade, Mount Etna experienced a \"flank eruption\"—erupting from its side instead of its summit—on December 24, 2018. The activity was accompanied by 130 earthquakes occurring over three hours that morning. Mount Etna, Europe’s most active volcano, has seen periodic activity on this part of the mountain since 2013. The Operational Land Imager (OLI) on the Landsat 8 satellite acquired the main image of Mount Etna on December 28, 2018.\n\nThe inset image highlights the active vent and thermal infrared signature from lava flows, which can be seen near the newly formed fissure on the southeastern side of the volcano. The inset was created with data from OLI and the Thermal Infrared Sensor (TIRS) on Landsat 8. Ash spewing from the fissure cloaked adjacent villages and delayed aircraft from landing at the nearby Catania airport. Earthquakes occurred in the subsequent days after the initial eruption and displaced hundreds of people from their homes.\n\nFor nighttime images of Mount Etna’s March 2017 eruption, see pages 48–51.\n\n---\n\n### Hazards of Volcanic Ash Plumes and Satellite Observation\n\nWith the help of moonlight, satellite instruments can track volcanic ash plumes, which present significant hazards to airplanes in flight. The volcanic ash—composed of tiny pieces of glass and rock—is abrasive to engine turbine blades, and can melt on the blades and other engine parts, causing damage and even engine stalls. This poses a danger to both the plane’s integrity and passenger safety. Volcanic ash also reduces visibility for pilots and can cause etching of windshields, further reducing pilots’ ability to see. Nightlight images can be combined with thermal images to provide a more complete view of volcanic activity on Earth’s surface.\n\nThe VIIRS Day/Night Band (DNB) on polar-orbiting satellites uses faint light sources such as moonlight, airglow (the atmosphere’s self-illumination through chemical reactions), zodiacal light (sunlight scattered by interplanetary dust), and starlight from the Milky Way. Using these dim light sources, the DNB can detect changes in clouds, snow cover, and sea ice:\n\n#### Table: Light Sources Used by VIIRS DNB\n\n| Light Source         | Description                                                                  |\n|----------------------|------------------------------------------------------------------------------|\n| Moonlight            | Reflected sunlight from the Moon, illuminating Earth's surface at night      |\n| Airglow              | Atmospheric self-illumination from chemical reactions                        |\n| Zodiacal Light       | Sunlight scattered by interplanetary dust                                    |\n| Starlight/Milky Way  | Faint illumination provided by stars in the Milky Way                        |\n\nGeostationary Operational Environmental Satellites (GOES), managed by NOAA, orbit over Earth’s equator and offer uninterrupted observations of North America. High-latitude areas such as Alaska benefit from polar-orbiting satellites like Suomi NPP, which provide overlapping coverage at the poles, enabling more data collection in these regions. During polar darkness (winter months), VIIRS DNB data allow scientists to:\n\n- Observe sea ice formation\n- Monitor snow cover extent at the highest latitudes\n- Detect open water for ship navigation\n\n#### Table: Satellite Coverage Overview\n\n| Satellite Type          | Orbit           | Coverage Area         | Special Utility                              |\n|------------------------|-----------------|----------------------|----------------------------------------------|\n| GOES                   | Geostationary   | Equatorial/North America | Continuous regional monitoring              |\n| Polar-Orbiting (e.g., Suomi NPP) | Polar-orbiting    | Poles/high latitudes      | Overlapping passes; useful during polar night|\n\n---\n\n### Weather Forecasting and Nightlight Data\n\nThe use of nightlight data by weather forecasters is growing as the VIIRS instrument enables observation of clouds at night illuminated by sources such as moonlight and lightning. Scientists use these data to study the nighttime behavior of weather systems, including severe storms, which can develop and strike populous areas at night as well as during the day. Combined with thermal data, visible nightlight data allow the detection of clouds at various heights in the atmosphere, such as dense marine fog. This capability enables weather forecasters to issue marine advisories with higher confidence, leading to greater utility. (See \"Marine Layer Clouds—California\" on page 56.)\n\nIn this section of the book, you will see how nightlight data are used to observe nature’s spectacular light shows across a wide range of sources.\n\n---\n\n#### Notable Data from Mount Etna Flank Eruption (December 2018)\n\n| Event/Observation                  | Details                                                                    |\n|-------------------------------------|----------------------------------------------------------------------------|\n| Date of Flank Eruption              | December 24, 2018                                                          |\n| Number of Earthquakes               | 130 earthquakes within 3 hours                                              |\n| Image Acquisition                   | December 28, 2018 by Landsat 8 OLI                                         |\n| Location of Eruption                | Southeastern side of Mount Etna                                            |\n| Thermal Imaging Data                | From OLI and TIRS (Landsat 8), highlighting active vent and lava flows     |\n| Impact on Villages/Air Transport    | Ash covered villages; delayed aircraft at Catania airport                  |\n| Displacement                        | Hundreds of residents displaced                                            |\n| Ongoing Seismic Activity            | Earthquakes continued after initial eruption                               |\n\n---\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"30\" -->"
+  }
+}
+Reference Type: AzureSearchDoc
+{
+  "type": "AzureSearchDoc",
+  "id": "3",
+  "activitySource": 1,
+  "docKey": "earth_at_night_508_page_66_verbalized",
+  "sourceData": {
+    "id": "earth_at_night_508_page_66_verbalized",
+    "page_chunk": "# Volcanoes\n\n---\n\n### Mount Etna Erupts - Italy\n\nThe highly active Mount Etna in Italy sent red lava rolling down its flank on March 19, 2017. An astronaut onboard the ISS took the photograph below of the volcano and its environs that night. City lights surround the mostly dark volcanic area.\n\n---\n\n#### Figure 1: Location of Mount Etna, Italy\n\nA world map highlighting the location of Mount Etna in southern Italy. The marker indicates its geographic placement on the east coast of Sicily, Italy, in the Mediterranean region, south of mainland Europe and north of northern Africa.\n\n---\n\n#### Figure 2: Nighttime View of Mount Etna's Eruption and Surrounding Cities\n\nThis is a nighttime satellite image taken on March 19, 2017, showing the eruption of Mount Etna (southeastern cone) with visible bright red and orange coloring indicating flowing lava from a lateral vent. The surrounding areas are illuminated by city lights, with the following geographic references labeled:\n\n| Location        | Position in Image         | Visible Characteristics                    |\n|-----------------|--------------------------|--------------------------------------------|\n| Mt. Etna (southeastern cone) | Top center-left | Bright red/orange lava flow                |\n| Lateral vent    | Left of the volcano       | Faint red/orange flow extending outwards   |\n| Resort          | Below the volcano, to the left   | Small cluster of lights                    |\n| Giarre          | Top right                 | Bright cluster of city lights              |\n| Acireale        | Center right              | Large, bright area of city lights          |\n| Biancavilla     | Bottom left               | Smaller cluster of city lights             |\n\nAn arrow pointing north is shown on the image for orientation.\n\n---\n\n<!-- Earth at Night Page Footer -->\n<!-- Page Number: 50 -->"
+  }
+}
+Reference Type: AzureSearchDoc
+{
+  "type": "AzureSearchDoc",
+  "id": "4",
+  "activitySource": 1,
+  "docKey": "earth_at_night_508_page_44_verbalized",
+  "sourceData": {
+    "id": "earth_at_night_508_page_44_verbalized",
+    "page_chunk": "## Nature's Light Shows\n\nAt night, with the light of the Sun removed, nature's brilliant glow from Earth's surface becomes visible to the naked eye from space. Some of Earth's most spectacular light shows are natural, like the aurora borealis, or Northern Lights, in the Northern Hemisphere (aurora australis, or Southern Lights, in the Southern Hemisphere). The auroras are natural electrical phenomena caused by charged particles that race from the Sun toward Earth, inducing chemical reactions in the upper atmosphere and creating the appearance of streamers of reddish or greenish light in the sky, usually near the northern or southern magnetic pole. Other natural lights can indicate danger, like a raging forest fire encroaching on a city, town, or community, or lava spewing from an erupting volcano.\n\nWhatever the source, the ability of humans to monitor nature's light shows at night has practical applications for society. For example, tracking fires during nighttime hours allows for continuous monitoring and enhances our ability to protect humans and other animals, plants, and infrastructure. Combined with other data sources, our ability to observe the light of fires at night allows emergency managers to more efficiently and accurately issue warnings and evacuation orders and allows firefighting efforts to continue through the night. With enough moonlight (e.g., full-Moon phase), it's even possible to track the movement of smoke plumes at night, which can impact air quality, regardless of time of day.\n\nAnother natural source of light at night is emitted from glowing lava flows at the site of active volcanoes. Again, with enough moonlight, these dramatic scenes can be tracked and monitored for both scientific research and public safety.\n\n\n### Figure: The Northern Lights Viewed from Space\n\n**September 17, 2011**\n\nThis photo, taken from the International Space Station on September 17, 2011, shows a spectacular display of the aurora borealis (Northern Lights) as green and reddish light in the night sky above Earth. In the foreground, part of a Soyuz spacecraft is visible, silhouetted against the bright auroral light. The green glow is generated by energetic charged particles from the Sun interacting with Earth's upper atmosphere, exciting oxygen and nitrogen atoms, and producing characteristic colors. The image demonstrates the vividness and grandeur of natural night-time light phenomena as seen from orbit."
+  }
+}
+
+[ASSISTANT]: 
+To find lava at night, satellite instruments like the VIIRS Day/Night Band (DNB) and thermal infrared sensors are used to detect the glow of very hot lava flows on the Earth's surface
+ For example, nighttime satellite images have captured lava flowing from active volcanoes such as Mount Etna in Italy and Kilauea in Hawaii, where the hot lava emits bright light visible from space even at night
+ Scientists combine thermal, shortwave infrared, and near-infrared data to distinguish very hot lava (bright white), cooling lava (red), and areas obscured by clouds
+ Additionally, moonlight and other faint natural light sources help illuminate the surroundings to improve observation of volcanic activity at night
+ Monitoring lava flow at night is important for scientific research and public safety, as it helps track volcanic eruptions and associated hazards such as ash plumes that can affect air travel and nearby communities [refs 0,1,2,3,4]
+
+
+🎉 === Conversation Complete ===
+🗑️ Deleting knowledge agent...
+✅ Knowledge agent 'earth-search-agent' deleted successfully.
+🗑️ Deleting search index...
+✅ Search index 'earth_at_night' deleted successfully.
+✅ Quickstart completed successfully!
+```
+
+## Explaining the code
+
+Now that you have the code, let's break down the key components:
+
+- [Create a search index](#create-a-search-index)
+- [Upload documents to the index](#upload-documents-to-the-index)
+- [Create a knowledge agent](#create-a-knowledge-agent)
+- [Set up messages](#set-up-messages)
+- [Run the retrieval pipeline](#run-the-retrieval-pipeline)
+- [Review the response, activity, and results](#review-the-response-activity-and-results)
+- [Create the Azure OpenAI client](#create-the-azure-openai-client)
+- [Use the Chat Completions API to generate an answer](#use-the-chat-completions-api-to-generate-an-answer)
+- [Continue the conversation](#continue-the-conversation)
+
+### Create a search index
+
+In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth_at_night` to contain plain text and vector content. You can use an existing index, but it must meet the criteria for [agentic retrieval workloads](../../search-agentic-retrieval-how-to-index.md). 
+
+```javascript
+const index = {
+    name: config.indexName,
+    fields: [
+        {
+            name: "id",
+            type: "Edm.String",
+            key: true,
+            filterable: true,
+            sortable: true,
+            facetable: true
+        },
+        {
+            name: "page_chunk",
+            type: "Edm.String",
+            searchable: true,
+            filterable: false,
+            sortable: false,
+            facetable: false
+        },
+        {
+            name: "page_embedding_text_3_large",
+            type: "Collection(Edm.Single)",
+            searchable: true,
+            filterable: false,
+            sortable: false,
+            facetable: false,
+            vectorSearchDimensions: 3072,
+            vectorSearchProfileName: "hnsw_text_3_large"
+        },
+        {
+            name: "page_number",
+            type: "Edm.Int32",
+            filterable: true,
+            sortable: true,
+            facetable: true
+        }
+    ],
+    vectorSearch: {
+        profiles: [
+            {
+                name: "hnsw_text_3_large",
+                algorithmConfigurationName: "alg",
+                vectorizerName: "azure_openai_text_3_large"
+            }
+        ],
+        algorithms: [
+            {
+                name: "alg",
+                kind: "hnsw"
+            }
+        ],
+        vectorizers: [
+            {
+                vectorizerName: "azure_openai_text_3_large",
+                kind: "azureOpenAI",
+                parameters: {
+                    resourceUrl: config.azureOpenAIEndpoint,
+                    deploymentId: config.azureOpenAIEmbeddingDeployment,
+                    modelName: config.azureOpenAIEmbeddingModel
+                }
+            }
+        ]
+    },
+    semanticSearch: {
+        defaultConfigurationName: "semantic_config",
+        configurations: [
+            {
+                name: "semantic_config",
+                prioritizedFields: {
+                    contentFields: [
+                        { name: "page_chunk" }
+                    ]
+                }
+            }
+        ]
+    }
+};
+```
+
+The index schema contains fields for document identification and page content, embeddings, and numbers. It also includes configurations for semantic ranking and vector queries, which use the `text-embedding-3-large` model you previously deployed.
+
+### Upload documents to the index
+
+Currently, the `earth_at_night` index is empty. Run the following code to populate the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
+
+```javascript
+console.log("📡 Fetching Earth at Night documents from GitHub...");
+const documentsUrl = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json";
+try {
+    const response = await fetch(documentsUrl);
+    if (!response.ok) {
+        throw new Error(`Failed to fetch documents: ${response.status} ${response.statusText}`);
+    }
+    const documents = await response.json();
+    console.log(`✅ Fetched ${documents.length} documents from GitHub`);
+    // Validate and transform documents to match our interface
+    const transformedDocuments = documents.map((doc, index) => {
+        return {
+            id: doc.id || String(index + 1),
+            page_chunk: doc.page_chunk || doc.content || '',
+            page_embedding_text_3_large: doc.page_embedding_text_3_large || new Array(3072).fill(0.1),
+            page_number: doc.page_number || index + 1
+        };
+    });
+    return transformedDocuments;
+}
+```
+
+### Create a knowledge agent
+
+To connect Azure AI Search to your `gpt-4.1-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent` that uses the agent definition to process queries and retrieve relevant documents from the `earth_at_night` index.
+
+To ensure relevant and semantically meaningful responses, `defaultRerankerThreshold` is set to exclude responses with a reranker score of `2.5` or lower.
+
+```javascript
+const agentDefinition = {
+    name: config.agentName,
+    description: "Knowledge agent for Earth at Night e-book content",
+    models: [
+        {
+            kind: "azureOpenAI",
+            azureOpenAIParameters: {
+                resourceUri: config.azureOpenAIEndpoint,
+                deploymentId: config.azureOpenAIGptDeployment,
+                modelName: config.azureOpenAIGptModel
+            }
+        }
+    ],
+    targetIndexes: [
+        {
+            indexName: config.indexName,
+            defaultRerankerThreshold: 2.5
+        }
+    ]
+};
+```
+
+### Set up messages
+
+Messages are the input for the retrieval route and contain the conversation history. Each message includes a role that indicates its origin, such as assistant or user, and content in natural language. The LLM you use determines which roles are valid.
+
+A user message represents the query to be processed, while an assistant message guides the knowledge agent on how to respond. During the retrieval process, these messages are sent to an LLM to extract relevant responses from indexed documents.
+
+This assistant message instructs `earth-search-agent` to answer questions about the Earth at night, cite sources using their `ref_id`, and respond with "I don't know" when answers are unavailable.
+
+```javascript
+const messages = [
+    {
+        role: "system",
+        content: `A Q&A agent that can answer questions about the Earth at night.
+Sources have a JSON format with a ref_id that must be cited in the answer.
+If you do not have the answer, respond with "I don't know".`
+    },
+    {
+        role: "user",
+        content: "Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown? Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?"
+    }
+];
+```
+
+### Run the retrieval pipeline
+
+This step runs the retrieval pipeline to extract relevant information from your search index. Based on the messages and parameters on the retrieval request, the LLM:
+1. Analyzes the entire conversation history to determine the underlying information need.
+1. Breaks down the compound user query into focused subqueries.
+1. Runs each subquery simultaneously against text fields and vector embeddings in your index.
+1. Uses semantic ranker to rerank the results of all subqueries.
+1. Merges the results into a single string.
+
+The following code sends a two-part user query to `earth-search-agent`, which deconstructs the query into subqueries, runs the subqueries against both text fields and vector embeddings in the `earth_at_night` index, and ranks and merges the results. The response is then appended to the `messages` list.
+
+```javascript
+const agentMessages = messages.map(msg => ({
+    role: msg.role,
+    content: [
+        {
+            type: "text",
+            text: msg.content
+        }
+    ]
+}));
+const retrievalRequest = {
+    messages: agentMessages,
+    targetIndexParams: [
+        {
+            indexName: config.indexName,
+            rerankerThreshold: 2.5,
+            maxDocsForReranker: 100,
+            includeReferenceSourceData: true
+        }
+    ]
+};
+const token = await getAccessToken(credential, "https://search.azure.com/.default");
+const response = await fetch(`${config.searchEndpoint}/agents/${config.agentName}/retrieve?api-version=${config.searchApiVersion}`, {
+    method: 'POST',
+    headers: {
+        'Content-Type': 'application/json',
+        'Authorization': `Bearer ${token}`
+    },
+    body: JSON.stringify(retrievalRequest)
+});
+if (!response.ok) {
+    const errorText = await response.text();
+    throw new Error(`Agentic retrieval failed: ${response.status} ${response.statusText}\n${errorText}`);
+}
+return await response.json();
+```
+
+### Review the response, activity, and results
+
+Now you want to display the response, activity, and results of the retrieval pipeline.
+
+Each retrieval response from Azure AI Search includes:
+
++ A unified string that represents grounding data from the search results.
+
++ The query plan.
+
++ Reference data that shows which chunks of the source documents contributed to the unified string.
+
+```javascript
+console.log("\nActivities:");
+if (retrievalResponse.activity && Array.isArray(retrievalResponse.activity)) {
+    retrievalResponse.activity.forEach((activity) => {
+        const activityType = activity.activityType || activity.type || 'UnknownActivityRecord';
+        console.log(`Activity Type: ${activityType}`);
+        console.log(JSON.stringify(activity, null, 2));
+    });
+}
+console.log("Results");
+if (retrievalResponse.references && Array.isArray(retrievalResponse.references)) {
+    retrievalResponse.references.forEach((reference) => {
+        const referenceType = reference.referenceType || reference.type || 'AzureSearchDoc';
+        console.log(`Reference Type: ${referenceType}`);
+        console.log(JSON.stringify(reference, null, 2));
+    });
+}
+```
+
+The output should include:
+
++ `Response` provides a text string of the most relevant documents (or chunks) in the search index based on the user query. As shown later in this quickstart, you can pass this string to an LLM for answer generation.
+
++ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for query planning and execution.
+
++ `Results` lists the documents that contributed to the response, each one identified by their `DocKey`.
+
+### Create the Azure OpenAI client
+
+To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-4.1-mini` deployment.
+
+```javascript
+const scope = "https://cognitiveservices.azure.com/.default";
+const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+const openAIClient = new AzureOpenAI({
+    endpoint: config.azureOpenAIEndpoint,
+    apiVersion: config.azureOpenAIApiVersion,
+    azureADTokenProvider,
+});
+```
+
+### Use the Chat Completions API to generate an answer
+
+One option for answer generation is the Chat Completions API, which passes the conversation history to the LLM for processing.
+
+```javascript
+const completion = await openAIClient.chat.completions.create({
+    model: config.azureOpenAIGptDeployment,
+    messages: messages.map(m => ({ role: m.role, content: m.content })),
+    max_tokens: 1000,
+    temperature: 0.7
+});
+const answer = completion.choices[0].message.content;
+console.log(answer?.replace(/\./g, "\n"));
+```
+
+### Continue the conversation
+
+Continue the conversation by sending another user query to `earth-search-agent`. The following code reruns the retrieval pipeline, fetching relevant content from the `earth_at_night` index and appending the response to the `messages` list. However, unlike before, you can now use the Azure OpenAI client to generate an answer based on the retrieved content.
+
+```javascript
+const followUpQuestion = "How do I find lava at night?";
+console.log(`❓ Follow-up question: ${followUpQuestion}`);
+messages.push({
+    role: "user",
+    content: followUpQuestion
+});
+```
+
+## Clean up resources
+
+When working in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money. You can delete resources individually, or you can delete the resource group to delete the entire set of resources.
+
+In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane. You can also run the following code to delete the objects you created in this quickstart.
+
+### Delete the knowledge agent
+
+The knowledge agent created in this quickstart was deleted using the following code snippet:
+
+```javascript
+const token = await getAccessToken(credential, "https://search.azure.com/.default");
+const response = await fetch(`${config.searchEndpoint}/agents/${config.agentName}?api-version=${config.searchApiVersion}`, {
+    method: 'DELETE',
+    headers: {
+        'Authorization': `Bearer ${token}`
+    }
+});
+```
+
+### Delete the search index
+
+The search index created in this quickstart was deleted using the following code snippet:
+
+```javascript
+await indexClient.deleteIndex(config.indexName);
+console.log(`✅ Search index '${config.indexName}' deleted successfully.`);
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "エージェントリトリーバル用のJavaScriptクイックスタートの追加"
}
```

### Explanation
このコード変更は、Azure AI Searchを使用してエージェント的リトリーバルを実装するための新しいクイックスタートガイドを含むMarkdownファイルの追加を示しています。このクイックスタートでは、ユーザーが大規模言語モデル（LLM）と独自のデータを使用して会話型検索体験を作成する方法を説明しています。具体的には、複雑なユーザークエリをサブクエリに分割し、同時にそれを実行して、Azure AI Searchにインデックスされたドキュメントからグラウンディングデータを抽出する方法が解説されています。

このドキュメントでは、事前に必要なAzureアカウント、Azure AI Searchサービス、Azure OpenAIクライアントライブラリ、および関連ツールのインストールについても詳細に説明されており、ユーザーがプロジェクトをセットアップするステップバイステップの手順を提供します。また、サンプルデータとしてNASAの「Earth at Night」電子書籍からのJSONドキュメントを使用し、特定の環境変数の設定、検索インデックスの作成、知識エージェントのセットアップに関する詳細が提供されています。

全体として、この変更は、Azureを利用した新しい検索機能を実装するための非常に実用的で詳細なリソースを提供することを目的としています。

## articles/search/includes/quickstarts/agentic-retrieval-typescript.md{#item-e6370b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,1294 @@
+---
+manager: nitinme
+author: haileytap
+ms.author: haileytapia
+ms.service: azure-ai-search
+ms.topic: include
+ms.date: 7/21/2025
+---
+[!INCLUDE [Feature preview](../previews/preview-generic.md)]
+
+In this quickstart, you use [agentic retrieval](../../search-agentic-retrieval-concept.md) to create a conversational search experience powered by large language models (LLMs) and your proprietary data. Agentic retrieval breaks down complex user queries into subqueries, runs the subqueries in parallel, and extracts grounding data from documents indexed in Azure AI Search. The output is intended for integration with agentic and custom chat solutions.
+
+Although you can provide your own data, this quickstart uses [sample JSON documents](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/nasa-e-book/earth-at-night-json) from NASA's Earth at Night e-book. The documents describe general science topics and images of Earth at night as observed from space.
+
+## Prerequisites
+
++ An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
+
++ An [Azure AI Search service](../../search-create-service-portal.md) on the Basic tier or higher with [semantic ranker enabled](../../semantic-how-to-enable-disable.md).
+
++ An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects). You get an Azure AI Foundry resource (that you need for model deployments) when you create an Azure AI Foundry project.
+
++ The [Azure CLI](/cli/azure/install-azure-cli) for keyless authentication with Microsoft Entra ID.
+
+[!INCLUDE [Setup](./agentic-retrieval-setup.md)]
+
+## Setup
+
+1. Create a new folder `quickstart-agentic-retrieval` to contain the application and open Visual Studio Code in that folder with the following command:
+
+    ```shell
+    mkdir quickstart-agentic-retrieval && cd quickstart-agentic-retrieval
+    ```
+
+1. Create the `package.json` with the following command:
+
+    ```shell
+    npm init -y
+    ```
+
+1. Update the `package.json` to ECMAScript with the following command: 
+
+    ```shell
+    npm pkg set type=module
+    ```
+
+1. Install the Azure AI Search client library ([Azure.Search.Documents](/javascript/api/overview/azure/search-documents-readme)) for JavaScript with:
+
+    ```console
+    npm install @azure/search-documents --version 12.2.0-alpha.20250606.1
+    ```
+1. Install the Azure OpenAI client library with:
+
+    ```console
+    npm install @azure/openai --version 5.10.1
+    ```
+
+1. Install the `dotenv` package to load environment variables from a `.env` file with:
+
+    ```console
+    npm install dotenv
+    ```
+
+1. For the **recommended** keyless authentication with Microsoft Entra ID, install the Azure Identity client library with:
+
+    ```console
+    npm install @azure/identity
+    ```
+
+## Create the index and knowledge agent
+
+1. Create a new file named `.env` in the `quickstart-agentic-retrieval` folder and add the following environment variables:
+
+    ```plaintext
+    AZURE_OPENAI_ENDPOINT=https://<your-ai-foundry-resource-name>.openai.azure.com/
+    AZURE_OPENAI_GPT_DEPLOYMENT=gpt-4.1-mini
+    AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-large
+    AZURE_SEARCH_ENDPOINT=https://<your-search-service-name>.search.windows.net
+    AZURE_SEARCH_INDEX_NAME=agentic-retrieval-sample
+    ```
+
+    Replace `<your-search-service-name>` and `<your-ai-foundry-resource-name>` with your actual Azure AI Search service name and Azure AI Foundry resource name.
+
+1. Paste the following code into a new file named `index.ts`:
+
+    ```typescript
+    import { DefaultAzureCredential, getBearerTokenProvider } from '@azure/identity';
+    import { 
+        SearchIndexClient, 
+        SearchClient,
+        SearchIndex,
+        SearchField,
+        VectorSearch,
+        VectorSearchProfile,
+        HnswAlgorithmConfiguration,
+        AzureOpenAIVectorizer,
+        AzureOpenAIParameters,
+        SemanticSearch,
+        SemanticConfiguration,
+        SemanticPrioritizedFields,
+        SemanticField
+    } from '@azure/search-documents';
+    import { AzureOpenAI } from "openai/index.mjs";
+    
+    // Load the .env file if it exists
+    import * as dotenv from "dotenv";
+    dotenv.config();
+    
+    // Configuration - Update these values for your environment
+    const config = {
+        searchEndpoint: process.env.AZURE_SEARCH_ENDPOINT || "https://your-search-service.search.windows.net",
+        azureOpenAIEndpoint: process.env.AZURE_OPENAI_ENDPOINT || "https://your-ai-foundry-resource.openai.azure.com/",
+        azureOpenAIGptDeployment: process.env.AZURE_OPENAI_GPT_DEPLOYMENT || "gpt-4.1-mini",
+        azureOpenAIGptModel: "gpt-4.1-mini",
+        azureOpenAIApiVersion: process.env.OPENAI_API_VERSION || "2025-03-01-preview",
+        azureOpenAIEmbeddingDeployment: process.env.AZURE_OPENAI_EMBEDDING_DEPLOYMENT || "text-embedding-3-large",
+        azureOpenAIEmbeddingModel: "text-embedding-3-large",
+        indexName: "earth_at_night",
+        agentName: "earth-search-agent",
+        searchApiVersion: "2025-05-01-Preview"
+    };
+    
+    // Earth at Night document interface
+    interface EarthAtNightDocument {
+        id: string;
+        page_chunk: string;
+        page_embedding_text_3_large: number[];
+        page_number: number;
+    }
+    
+    // Knowledge agent message interface
+    interface KnowledgeAgentMessage {
+        role: 'user' | 'assistant' | 'system';
+        content: string;
+    }
+    
+    // Agentic retrieval response interface
+    interface AgenticRetrievalResponse {
+        response?: string | any[];
+        references?: Array<{
+            docKey?: string;
+            content?: string;
+            score?: number;
+            referenceType?: string;
+            type?: string;
+            SourceData?: any;
+            Id?: string;
+            ActivitySource?: number;
+            // Allow any additional properties
+            [key: string]: any;
+        }>;
+        activity?: Array<{
+            step?: string;
+            description?: string;
+            tokensUsed?: number;
+            activityType?: string;
+            type?: string;
+            InputTokens?: number;
+            OutputTokens?: number;
+            TargetIndex?: string;
+            QueryTime?: string;
+            Query?: any;
+            Count?: number;
+            ElapsedMs?: number | null;
+            Id?: number;
+            // Allow any additional properties
+            [key: string]: any;
+        }>;
+        // Add any other possible response fields
+        [key: string]: any;
+    }
+    
+    async function main(): Promise<void> {
+        try {
+            console.log("🚀 Starting Azure AI Search agentic retrieval quickstart...\n");
+    
+            // Initialize Azure credentials using managed identity (recommended)
+            const credential = new DefaultAzureCredential();
+            
+            // Create search clients
+            const searchIndexClient = new SearchIndexClient(config.searchEndpoint, credential);
+            const searchClient = new SearchClient<EarthAtNightDocument>(config.searchEndpoint, config.indexName, credential);
+            
+            // Create Azure OpenAI client
+            const scope = "https://cognitiveservices.azure.com/.default";
+            const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+            const openAIClient = new AzureOpenAI({
+                endpoint: config.azureOpenAIEndpoint,
+                apiVersion: config.azureOpenAIApiVersion,
+                azureADTokenProvider,
+            });
+    
+            // Create search index with vector and semantic capabilities
+            await createSearchIndex(searchIndexClient);
+    
+            // Upload sample documents
+            await uploadDocuments(searchClient);
+    
+            // Create knowledge agent for agentic retrieval
+            await createKnowledgeAgent(credential);
+    
+            // Run agentic retrieval with conversation
+            await runAgenticRetrieval(credential, openAIClient);
+    
+            // Clean up - Delete knowledge agent and search index
+            await deleteKnowledgeAgent(credential);
+            await deleteSearchIndex(searchIndexClient);
+    
+            console.log("✅ Quickstart completed successfully!");
+    
+        } catch (error) {
+            console.error("❌ Error in main execution:", error);
+            throw error;
+        }
+    }
+    
+    async function createSearchIndex(indexClient: SearchIndexClient): Promise<void> {
+        console.log("📊 Creating search index...");
+        
+        const index: SearchIndex = {
+            name: config.indexName,
+            fields: [
+                {
+                    name: "id",
+                    type: "Edm.String",
+                    key: true,
+                    filterable: true,
+                    sortable: true,
+                    facetable: true
+                } as SearchField,
+                {
+                    name: "page_chunk",
+                    type: "Edm.String",
+                    searchable: true,
+                    filterable: false,
+                    sortable: false,
+                    facetable: false
+                } as SearchField,
+                {
+                    name: "page_embedding_text_3_large",
+                    type: "Collection(Edm.Single)",
+                    searchable: true,
+                    filterable: false,
+                    sortable: false,
+                    facetable: false,
+                    vectorSearchDimensions: 3072,
+                    vectorSearchProfileName: "hnsw_text_3_large"
+                } as SearchField,
+                {
+                    name: "page_number",
+                    type: "Edm.Int32",
+                    filterable: true,
+                    sortable: true,
+                    facetable: true
+                } as SearchField
+            ],
+            vectorSearch: {
+                profiles: [
+                    {
+                        name: "hnsw_text_3_large",
+                        algorithmConfigurationName: "alg",
+                        vectorizerName: "azure_openai_text_3_large"
+                    } as VectorSearchProfile
+                ],
+                algorithms: [
+                    {
+                        name: "alg",
+                        kind: "hnsw"
+                    } as HnswAlgorithmConfiguration
+                ],
+                vectorizers: [
+                    {
+                        vectorizerName: "azure_openai_text_3_large",
+                        kind: "azureOpenAI",
+                        parameters: {
+                            resourceUrl: config.azureOpenAIEndpoint,
+                            deploymentId: config.azureOpenAIEmbeddingDeployment,
+                            modelName: config.azureOpenAIEmbeddingModel
+                        } as AzureOpenAIParameters
+                    } as AzureOpenAIVectorizer
+                ]
+            } as VectorSearch,
+            semanticSearch: {
+                defaultConfigurationName: "semantic_config",
+                configurations: [
+                    {
+                        name: "semantic_config",
+                        prioritizedFields: {
+                            contentFields: [
+                                { name: "page_chunk" } as SemanticField
+                            ]
+                        } as SemanticPrioritizedFields
+                    } as SemanticConfiguration
+                ]
+            } as SemanticSearch
+        };
+    
+        try {
+            await indexClient.createOrUpdateIndex(index);
+            console.log(`✅ Index '${config.indexName}' created or updated successfully.`);
+        } catch (error) {
+            console.error("❌ Error creating index:", error);
+            throw error;
+        }
+    }
+    
+    async function deleteSearchIndex(indexClient: SearchIndexClient): Promise<void> {
+        console.log("🗑️ Deleting search index...");
+        
+        try {
+            await indexClient.deleteIndex(config.indexName);
+            console.log(`✅ Search index '${config.indexName}' deleted successfully.`);
+            
+        } catch (error: any) {
+            if (error?.statusCode === 404 || error?.code === 'IndexNotFound') {
+                console.log(`ℹ️ Search index '${config.indexName}' does not exist or was already deleted.`);
+                return;
+            }
+            console.error("❌ Error deleting search index:", error);
+            throw error;
+        }
+    }
+    
+    // Fetch Earth at Night documents from GitHub
+    async function fetchEarthAtNightDocuments(): Promise<EarthAtNightDocument[]> {
+        console.log("📡 Fetching Earth at Night documents from GitHub...");
+        
+        const documentsUrl = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json";
+        
+        try {
+            const response = await fetch(documentsUrl);
+            
+            if (!response.ok) {
+                throw new Error(`Failed to fetch documents: ${response.status} ${response.statusText}`);
+            }
+            
+            const documents = await response.json();
+            console.log(`✅ Fetched ${documents.length} documents from GitHub`);
+            
+            // Validate and transform documents to match our interface
+            const transformedDocuments: EarthAtNightDocument[] = documents.map((doc: any, index: number) => {
+                return {
+                    id: doc.id || String(index + 1),
+                    page_chunk: doc.page_chunk || doc.content || '',
+                    page_embedding_text_3_large: doc.page_embedding_text_3_large || new Array(3072).fill(0.1),
+                    page_number: doc.page_number || index + 1
+                };
+            });
+            
+            return transformedDocuments;
+            
+        } catch (error) {
+            console.error("❌ Error fetching documents from GitHub:", error);
+            console.log("🔄 Falling back to sample documents...");
+            
+            // Fallback to sample documents if fetch fails
+            return [
+                {
+                    id: "1",
+                    page_chunk: "The Earth at night reveals the patterns of human settlement and economic activity. City lights trace the contours of civilization, creating a luminous map of where people live and work.",
+                    page_embedding_text_3_large: new Array(3072).fill(0.1),
+                    page_number: 1
+                },
+                {
+                    id: "2", 
+                    page_chunk: "From space, the aurora borealis appears as shimmering curtains of green and blue light dancing across the polar regions.",
+                    page_embedding_text_3_large: new Array(3072).fill(0.2),
+                    page_number: 2
+                }
+                // Add more fallback documents as needed
+            ];
+        }
+    }
+    
+    async function uploadDocuments(searchClient: SearchClient<EarthAtNightDocument>): Promise<void> {
+        console.log("📄 Uploading documents...");
+        
+        try {
+            // Fetch documents from GitHub
+            const documents = await fetchEarthAtNightDocuments();
+            
+            const result = await searchClient.uploadDocuments(documents);
+            console.log(`✅ Uploaded ${result.results.length} documents successfully.`);
+            
+            // Wait for indexing to complete
+            console.log("⏳ Waiting for document indexing to complete...");
+            await new Promise(resolve => setTimeout(resolve, 5000));
+            console.log("✅ Document indexing completed.");
+            
+        } catch (error) {
+            console.error("❌ Error uploading documents:", error);
+            throw error;
+        }
+    }
+    
+    async function createKnowledgeAgent(credential: DefaultAzureCredential): Promise<void> {
+        
+        // In case the agent already exists, delete it first
+        await deleteKnowledgeAgent(credential);
+        
+        console.log("🤖 Creating knowledge agent...");
+        
+        const agentDefinition = {
+            name: config.agentName,
+            description: "Knowledge agent for Earth at Night e-book content",
+            models: [
+                {
+                    kind: "azureOpenAI",
+                    azureOpenAIParameters: {
+                        resourceUri: config.azureOpenAIEndpoint,
+                        deploymentId: config.azureOpenAIGptDeployment,
+                        modelName: config.azureOpenAIGptModel
+                    }
+                }
+            ],
+            targetIndexes: [
+                {
+                    indexName: config.indexName,
+                    defaultRerankerThreshold: 2.5
+                }
+            ]
+        };
+    
+        try {
+            const token = await getAccessToken(credential, "https://search.azure.com/.default");
+            const response = await fetch(`${config.searchEndpoint}/agents/${config.agentName}?api-version=${config.searchApiVersion}`, {
+                method: 'PUT',
+                headers: {
+                    'Content-Type': 'application/json',
+                    'Authorization': `Bearer ${token}`
+                },
+                body: JSON.stringify(agentDefinition)
+            });
+    
+            if (!response.ok) {
+                const errorText = await response.text();
+                throw new Error(`Failed to create knowledge agent: ${response.status} ${response.statusText}\n${errorText}`);
+            }
+    
+            console.log(`✅ Knowledge agent '${config.agentName}' created successfully.`);
+            
+        } catch (error) {
+            console.error("❌ Error creating knowledge agent:", error);
+            throw error;
+        }
+    }
+    
+    async function runAgenticRetrieval(credential: DefaultAzureCredential, openAIClient: AzureOpenAI): Promise<void> {
+        console.log("🔍 Running agentic retrieval...");
+        
+        const messages: KnowledgeAgentMessage[] = [
+            {
+                role: "system",
+                content: `A Q&A agent that can answer questions about the Earth at night.
+    Sources have a JSON format with a ref_id that must be cited in the answer.
+    If you do not have the answer, respond with "I don't know".`
+            },
+            {
+                role: "user",
+                content: "Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown? Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?"
+            }
+        ];
+    
+        try {
+            // Call agentic retrieval API
+            const userMessages = messages.filter(m => m.role !== "system");
+            const retrievalResponse = await callAgenticRetrieval(credential, userMessages);
+            
+            // Extract the assistant response from agentic retrieval
+            let assistantContent = '';
+            if (typeof retrievalResponse.response === 'string') {
+                assistantContent = retrievalResponse.response;
+            } else if (Array.isArray(retrievalResponse.response)) {
+                assistantContent = JSON.stringify(retrievalResponse.response);
+            }
+            
+            // Add assistant response to conversation history
+            messages.push({
+                role: "assistant",
+                content: assistantContent
+            });
+            
+            console.log(assistantContent);
+            
+            // Log activities and results...
+            console.log("\nActivities:");
+            if (retrievalResponse.activity && Array.isArray(retrievalResponse.activity)) {
+                retrievalResponse.activity.forEach((activity) => {
+                    const activityType = activity.activityType || activity.type || 'UnknownActivityRecord';
+                    console.log(`Activity Type: ${activityType}`);
+                    console.log(JSON.stringify(activity, null, 2));
+                });
+            }
+    
+            console.log("Results");
+            if (retrievalResponse.references && Array.isArray(retrievalResponse.references)) {
+                retrievalResponse.references.forEach((reference) => {
+                    const referenceType = reference.referenceType || reference.type || 'AzureSearchDoc';
+                    console.log(`Reference Type: ${referenceType}`);
+                    console.log(JSON.stringify(reference, null, 2));
+                });
+            }
+            
+            // Now do chat completion with full conversation history
+            await generateFinalAnswer(openAIClient, messages);
+    
+            // Continue conversation with second question
+            await continueConversation(credential, openAIClient, messages);
+    
+        } catch (error) {
+            console.error("❌ Error in agentic retrieval:", error);
+            throw error;
+        }
+    }
+    
+    async function generateFinalAnswer(
+        openAIClient: AzureOpenAI,
+        messages: KnowledgeAgentMessage[]
+    ): Promise<void> {
+        
+        console.log("\n[ASSISTANT]: ");
+        
+        try {
+            const completion = await openAIClient.chat.completions.create({
+                model: config.azureOpenAIGptDeployment,
+                messages: messages.map(m => ({ role: m.role, content: m.content })) as any,
+                max_tokens: 1000,
+                temperature: 0.7
+            });
+    
+            const answer = completion.choices[0].message.content;
+            console.log(answer?.replace(/\./g, "\n"));
+    
+            // Add this response to conversation history
+            if (answer) {
+                messages.push({
+                    role: "assistant",
+                    content: answer
+                });
+            }
+    
+        } catch (error) {
+            console.error("❌ Error generating final answer:", error);
+            throw error;
+        }
+    }
+    
+    async function callAgenticRetrieval(
+        credential: DefaultAzureCredential, 
+        messages: KnowledgeAgentMessage[]
+    ): Promise<AgenticRetrievalResponse> {
+        
+        // Convert messages to the correct format expected by the Knowledge agent
+        const agentMessages = messages.map(msg => ({
+            role: msg.role,
+            content: [
+                {
+                    type: "text",
+                    text: msg.content
+                }
+            ]
+        }));
+        
+        const retrievalRequest = {
+            messages: agentMessages,
+            targetIndexParams: [
+                {
+                    indexName: config.indexName,
+                    rerankerThreshold: 2.5,
+                    maxDocsForReranker: 100,
+                    includeReferenceSourceData: true
+                }
+            ]
+        };
+    
+        const token = await getAccessToken(credential, "https://search.azure.com/.default");
+        const response = await fetch(
+            `${config.searchEndpoint}/agents/${config.agentName}/retrieve?api-version=${config.searchApiVersion}`,
+            {
+                method: 'POST',
+                headers: {
+                    'Content-Type': 'application/json',
+                    'Authorization': `Bearer ${token}`
+                },
+                body: JSON.stringify(retrievalRequest)
+            }
+        );
+    
+        if (!response.ok) {
+            const errorText = await response.text();
+            throw new Error(`Agentic retrieval failed: ${response.status} ${response.statusText}\n${errorText}`);
+        }
+    
+        return await response.json() as AgenticRetrievalResponse;
+    }
+    
+    async function deleteKnowledgeAgent(credential: DefaultAzureCredential): Promise<void> {
+        console.log("🗑️ Deleting knowledge agent...");
+        
+        try {
+            const token = await getAccessToken(credential, "https://search.azure.com/.default");
+            const response = await fetch(`${config.searchEndpoint}/agents/${config.agentName}?api-version=${config.searchApiVersion}`, {
+                method: 'DELETE',
+                headers: {
+                    'Authorization': `Bearer ${token}`
+                }
+            });
+    
+            if (!response.ok) {
+                if (response.status === 404) {
+                    console.log(`ℹ️ Knowledge agent '${config.agentName}' does not exist or was already deleted.`);
+                    return;
+                }
+                const errorText = await response.text();
+                throw new Error(`Failed to delete knowledge agent: ${response.status} ${response.statusText}\n${errorText}`);
+            }
+    
+            console.log(`✅ Knowledge agent '${config.agentName}' deleted successfully.`);
+            
+        } catch (error) {
+            console.error("❌ Error deleting knowledge agent:", error);
+            throw error;
+        }
+    }
+    
+    async function continueConversation(
+        credential: DefaultAzureCredential,
+        openAIClient: AzureOpenAI,
+        messages: KnowledgeAgentMessage[]
+    ): Promise<void> {
+        console.log("\n💬 === Continuing Conversation ===");
+        
+        // Add follow-up question
+        const followUpQuestion = "How do I find lava at night?"; 
+        console.log(`❓ Follow-up question: ${followUpQuestion}`);
+        
+        messages.push({
+            role: "user",
+            content: followUpQuestion
+        });
+    
+        try {
+            // Don't include system messages in this retrieval
+            const userAssistantMessages = messages.filter((m: KnowledgeAgentMessage) => m.role !== "system");
+            const newRetrievalResponse = await callAgenticRetrieval(credential, userAssistantMessages);
+            
+            // Extract assistant response and add to conversation
+            let assistantContent = '';
+            if (typeof newRetrievalResponse.response === 'string') {
+                assistantContent = newRetrievalResponse.response;
+            } else if (Array.isArray(newRetrievalResponse.response)) {
+                assistantContent = JSON.stringify(newRetrievalResponse.response);
+            }
+            
+            // Add assistant response to conversation history
+            messages.push({
+                role: "assistant",
+                content: assistantContent
+            });
+            
+            console.log(assistantContent);
+            
+            // Log activities and results like the first retrieval
+            console.log("\nActivities:");
+            if (newRetrievalResponse.activity && Array.isArray(newRetrievalResponse.activity)) {
+                newRetrievalResponse.activity.forEach((activity) => {
+                    const activityType = activity.activityType || activity.type || 'UnknownActivityRecord';
+                    console.log(`Activity Type: ${activityType}`);
+                    console.log(JSON.stringify(activity, null, 2));
+                });
+            }
+    
+            console.log("Results");
+            if (newRetrievalResponse.references && Array.isArray(newRetrievalResponse.references)) {
+                newRetrievalResponse.references.forEach((reference) => {
+                    const referenceType = reference.referenceType || reference.type || 'AzureSearchDoc';
+                    console.log(`Reference Type: ${referenceType}`);
+                    console.log(JSON.stringify(reference, null, 2));
+                });
+            }
+            
+            // Generate final answer for follow-up
+            await generateFinalAnswer(openAIClient, messages);
+            
+            console.log("\n🎉 === Conversation Complete ===");
+            
+        } catch (error) {
+            console.error("❌ Error in conversation continuation:", error);
+            throw error;
+        }
+    }
+    
+    async function getAccessToken(credential: DefaultAzureCredential, scope: string): Promise<string> {
+        const tokenResponse = await credential.getToken(scope);
+        return tokenResponse.token;
+    }
+    
+    // Error handling wrapper
+    async function runWithErrorHandling(): Promise<void> {
+        try {
+            await main();
+        } catch (error) {
+            console.error("💥 Application failed:", error);
+            process.exit(1);
+        }
+    }
+    
+    // Execute the application - ES module style
+    runWithErrorHandling();
+    
+    export {
+        main,
+        createSearchIndex,
+        deleteSearchIndex,
+        fetchEarthAtNightDocuments,
+        uploadDocuments,
+        createKnowledgeAgent,
+        deleteKnowledgeAgent,
+        runAgenticRetrieval,
+        EarthAtNightDocument,
+        KnowledgeAgentMessage,
+        AgenticRetrievalResponse
+    };
+    ```
+
+1. Create the `tsconfig.json` file to transpile the TypeScript code and copy the following code for ECMAScript.
+
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
+    }
+    ```
+
+1. Transpile from TypeScript to JavaScript.
+
+    ```shell
+    tsc
+    ```
+    
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
+## Output
+
+The output of the application should look similar to the following:
+
+```plaintext
+[dotenv@17.2.0] injecting env (0) from .env (tip: ⚙️  override existing env vars with { override: true })
+🚀 Starting Azure AI Search agentic retrieval quickstart...
+
+📊 Creating search index...
+✅ Index 'earth_at_night' created or updated successfully.
+📄 Uploading documents...
+📡 Fetching Earth at Night documents from GitHub...
+✅ Fetched 194 documents from GitHub
+✅ Uploaded 194 documents successfully.
+⏳ Waiting for document indexing to complete...
+✅ Document indexing completed.
+🗑️ Deleting knowledge agent...
+ℹ️ Knowledge agent 'earth-search-agent' does not exist or was already deleted.
+🤖 Creating knowledge agent...
+✅ Knowledge agent 'earth-search-agent' created successfully.
+🔍 Running agentic retrieval...
+[{"role":"assistant","content":[{"type":"text","text":"[]"}]}]
+
+Activities:
+Activity Type: ModelQueryPlanning
+{
+  "type": "ModelQueryPlanning",
+  "id": 0,
+  "inputTokens": 1379,
+  "outputTokens": 551
+}
+Activity Type: AzureSearchQuery
+{
+  "type": "AzureSearchQuery",
+  "id": 1,
+  "targetIndex": "earth_at_night",
+  "query": {
+    "search": "Why do suburban areas show greater December brightening compared to urban cores despite higher absolute light levels downtown?",
+    "filter": null
+  },
+  "queryTime": "2025-07-20T16:12:59.804Z",
+  "count": 0,
+  "elapsedMs": 549
+}
+Activity Type: AzureSearchQuery
+{
+  "type": "AzureSearchQuery",
+  "id": 2,
+  "targetIndex": "earth_at_night",
+  "query": {
+    "search": "Why is the Phoenix nighttime street grid sharply visible from space, while large stretches of interstate highways between Midwestern cities appear comparatively dim?",
+    "filter": null
+  },
+  "queryTime": "2025-07-20T16:13:00.061Z",
+  "count": 0,
+  "elapsedMs": 256
+}
+Activity Type: AzureSearchSemanticRanker
+{
+  "type": "AzureSearchSemanticRanker",
+  "id": 3,
+  "inputTokens": 47630
+}
+Results
+
+[ASSISTANT]: 
+Suburban belts show larger December brightening than urban cores despite higher absolute light levels downtown because suburban areas often have more seasonal variation in lighting usage, such as increased decorative and outdoor lighting during the holiday season in December
+ Urban cores typically have more constant and dense lighting throughout the year, so the relative increase in brightness during December is less pronounced compared to suburban areas
+\n\nThe Phoenix nighttime street grid is sharply visible from space because the city has a well-planned, extensive grid of streets with consistent and bright street lighting
+ In contrast, large stretches of interstate highways between Midwestern cities appear comparatively dim because these highways have less continuous lighting and lower intensity lights, making them less visible from space
+\n\n(Note: These explanations are based on general knowledge about urban lighting patterns and visibility from space; specific studies or sources were not provided
+)
+
+💬 === Continuing Conversation ===
+❓ Follow-up question: How do I find lava at night?
+[{"role":"assistant","content":[{"type":"text","text":"[{\"ref_id\":0,\"content\":\"<!-- PageHeader=\\\"Volcanoes\\\" -->\\n\\n### Nighttime Glow at Mount Etna - Italy\\n\\nAt about 2:30 a.m. local time on March 16, 2017, the VIIRS DNB on the Suomi NPP satellite captured this nighttime image of lava flowing on Mount Etna in Sicily, Italy. Etna is one of the world's most active volcanoes.\\n\\n#### Figure: Location of Mount Etna\\nA world globe is depicted, with a marker indicating the location of Mount Etna in Sicily, Italy, in southern Europe near the center of the Mediterranean Sea.\\n\\n<!-- PageFooter=\\\"Earth at Night\\\" -->\\n<!-- PageNumber=\\\"48\\\" -->\"},{\"ref_id\":1,\"content\":\"<!-- PageHeader=\\\"Volcanoes\\\" -->\\n\\n## Volcanoes\\n\\n### The Infrared Glows of Kilauea's Lava Flows—Hawaii\\n\\nIn early May 2018, an eruption on Hawaii's Kilauea volcano began to unfold. The eruption took a dangerous turn on May 3, 2018, when new fissures opened in the residential neighborhood of Leilani Estates. During the summer-long eruptive event, other fissures emerged along the East Rift Zone. Lava from vents along the rift zone flowed downslope, reaching the ocean in several areas, and filling in Kapoho Bay.\\n\\nA time series of Landsat 8 imagery shows the progression of the lava flows from May 16 to August 13. The night view combines thermal, shortwave infrared, and near-infrared wavelengths to tease out the very hot lava (bright white), cooling lava (red), and lava flows obstructed by clouds (purple).\\n\\n#### Figure: Location of Kilauea Volcano, Hawaii\\n\\nA globe is shown centered on North America, with a marker placed in the Pacific Ocean indicating the location of Hawaii, to the southwest of the mainland United States.\\n\\n<!-- PageFooter=\\\"Earth at Night\\\" -->\\n<!-- PageNumber=\\\"44\\\" -->\"},{\"ref_id\":2,\"content\":\"For the first time in perhaps a decade, Mount Etna experienced a \\\"flank eruption\\\"—erupting from its side instead of its summit—on December 24, 2018. The activity was accompanied by 130 earthquakes occurring over three hours that morning. Mount Etna, Europe’s most active volcano, has seen periodic activity on this part of the mountain since 2013. The Operational Land Imager (OLI) on the Landsat 8 satellite acquired the main image of Mount Etna on December 28, 2018.\\n\\nThe inset image highlights the active vent and thermal infrared signature from lava flows, which can be seen near the newly formed fissure on the southeastern side of the volcano. The inset was created with data from OLI and the Thermal Infrared Sensor (TIRS) on Landsat 8. Ash spewing from the fissure cloaked adjacent villages and delayed aircraft from landing at the nearby Catania airport. Earthquakes occurred in the subsequent days after the initial eruption and displaced hundreds of people from their homes.\\n\\nFor nighttime images of Mount Etna’s March 2017 eruption, see pages 48–51.\\n\\n---\\n\\n### Hazards of Volcanic Ash Plumes and Satellite Observation\\n\\nWith the help of moonlight, satellite instruments can track volcanic ash plumes, which present significant hazards to airplanes in flight. The volcanic ash—composed of tiny pieces of glass and rock—is abrasive to engine turbine blades, and can melt on the blades and other engine parts, causing damage and even engine stalls. This poses a danger to both the plane’s integrity and passenger safety. Volcanic ash also reduces visibility for pilots and can cause etching of windshields, further reducing pilots’ ability to see. Nightlight images can be combined with thermal images to provide a more complete view of volcanic activity on Earth’s surface.\\n\\nThe VIIRS Day/Night Band (DNB) on polar-orbiting satellites uses faint light sources such as moonlight, airglow (the atmosphere’s self-illumination through chemical reactions), zodiacal light (sunlight scattered by interplanetary dust), and starlight from the Milky Way. Using these dim light sources, the DNB can detect changes in clouds, snow cover, and sea ice:\\n\\n#### Table: Light Sources Used by VIIRS DNB\\n\\n| Light Source         | Description                                                                  |\\n|----------------------|------------------------------------------------------------------------------|\\n| Moonlight            | Reflected sunlight from the Moon, illuminating Earth's surface at night      |\\n| Airglow              | Atmospheric self-illumination from chemical reactions                        |\\n| Zodiacal Light       | Sunlight scattered by interplanetary dust                                    |\\n| Starlight/Milky Way  | Faint illumination provided by stars in the Milky Way                        |\\n\\nGeostationary Operational Environmental Satellites (GOES), managed by NOAA, orbit over Earth’s equator and offer uninterrupted observations of North America. High-latitude areas such as Alaska benefit from polar-orbiting satellites like Suomi NPP, which provide overlapping coverage at the poles, enabling more data collection in these regions. During polar darkness (winter months), VIIRS DNB data allow scientists to:\\n\\n- Observe sea ice formation\\n- Monitor snow cover extent at the highest latitudes\\n- Detect open water for ship navigation\\n\\n#### Table: Satellite Coverage Overview\\n\\n| Satellite Type          | Orbit           | Coverage Area         | Special Utility                              |\\n|------------------------|-----------------|----------------------|----------------------------------------------|\\n| GOES                   | Geostationary   | Equatorial/North America | Continuous regional monitoring              |\\n| Polar-Orbiting (e.g., Suomi NPP) | Polar-orbiting    | Poles/high latitudes      | Overlapping passes; useful during polar night|\\n\\n---\\n\\n### Weather Forecasting and Nightlight Data\\n\\nThe use of nightlight data by weather forecasters is growing as the VIIRS instrument enables observation of clouds at night illuminated by sources such as moonlight and lightning. Scientists use these data to study the nighttime behavior of weather systems, including severe storms, which can develop and strike populous areas at night as well as during the day. Combined with thermal data, visible nightlight data allow the detection of clouds at various heights in the atmosphere, such as dense marine fog. This capability enables weather forecasters to issue marine advisories with higher confidence, leading to greater utility. (See \\\"Marine Layer Clouds—California\\\" on page 56.)\\n\\nIn this section of the book, you will see how nightlight data are used to observe nature’s spectacular light shows across a wide range of sources.\\n\\n---\\n\\n#### Notable Data from Mount Etna Flank Eruption (December 2018)\\n\\n| Event/Observation                  | Details                                                                    |\\n|-------------------------------------|----------------------------------------------------------------------------|\\n| Date of Flank Eruption              | December 24, 2018                                                          |\\n| Number of Earthquakes               | 130 earthquakes within 3 hours                                              |\\n| Image Acquisition                   | December 28, 2018 by Landsat 8 OLI                                         |\\n| Location of Eruption                | Southeastern side of Mount Etna                                            |\\n| Thermal Imaging Data                | From OLI and TIRS (Landsat 8), highlighting active vent and lava flows     |\\n| Impact on Villages/Air Transport    | Ash covered villages; delayed aircraft at Catania airport                  |\\n| Displacement                        | Hundreds of residents displaced                                            |\\n| Ongoing Seismic Activity            | Earthquakes continued after initial eruption                               |\\n\\n---\\n\\n<!-- PageFooter=\\\"Earth at Night\\\" -->\\n<!-- PageNumber=\\\"30\\\" -->\"},{\"ref_id\":3,\"content\":\"# Volcanoes\\n\\n---\\n\\n### Mount Etna Erupts - Italy\\n\\nThe highly active Mount Etna in Italy sent red lava rolling down its flank on March 19, 2017. An astronaut onboard the ISS took the photograph below of the volcano and its environs that night. City lights surround the mostly dark volcanic area.\\n\\n---\\n\\n#### Figure 1: Location of Mount Etna, Italy\\n\\nA world map highlighting the location of Mount Etna in southern Italy. The marker indicates its geographic placement on the east coast of Sicily, Italy, in the Mediterranean region, south of mainland Europe and north of northern Africa.\\n\\n---\\n\\n#### Figure 2: Nighttime View of Mount Etna's Eruption and Surrounding Cities\\n\\nThis is a nighttime satellite image taken on March 19, 2017, showing the eruption of Mount Etna (southeastern cone) with visible bright red and orange coloring indicating flowing lava from a lateral vent. The surrounding areas are illuminated by city lights, with the following geographic references labeled:\\n\\n| Location        | Position in Image         | Visible Characteristics                    |\\n|-----------------|--------------------------|--------------------------------------------|\\n| Mt. Etna (southeastern cone) | Top center-left | Bright red/orange lava flow                |\\n| Lateral vent    | Left of the volcano       | Faint red/orange flow extending outwards   |\\n| Resort          | Below the volcano, to the left   | Small cluster of lights                    |\\n| Giarre          | Top right                 | Bright cluster of city lights              |\\n| Acireale        | Center right              | Large, bright area of city lights          |\\n| Biancavilla     | Bottom left               | Smaller cluster of city lights             |\\n\\nAn arrow pointing north is shown on the image for orientation.\\n\\n---\\n\\n<!-- Earth at Night Page Footer -->\\n<!-- Page Number: 50 -->\"},{\"ref_id\":4,\"content\":\"## Nature's Light Shows\\n\\nAt night, with the light of the Sun removed, nature's brilliant glow from Earth's surface becomes visible to the naked eye from space. Some of Earth's most spectacular light shows are natural, like the aurora borealis, or Northern Lights, in the Northern Hemisphere (aurora australis, or Southern Lights, in the Southern Hemisphere). The auroras are natural electrical phenomena caused by charged particles that race from the Sun toward Earth, inducing chemical reactions in the upper atmosphere and creating the appearance of streamers of reddish or greenish light in the sky, usually near the northern or southern magnetic pole. Other natural lights can indicate danger, like a raging forest fire encroaching on a city, town, or community, or lava spewing from an erupting volcano.\\n\\nWhatever the source, the ability of humans to monitor nature's light shows at night has practical applications for society. For example, tracking fires during nighttime hours allows for continuous monitoring and enhances our ability to protect humans and other animals, plants, and infrastructure. Combined with other data sources, our ability to observe the light of fires at night allows emergency managers to more efficiently and accurately issue warnings and evacuation orders and allows firefighting efforts to continue through the night. With enough moonlight (e.g., full-Moon phase), it's even possible to track the movement of smoke plumes at night, which can impact air quality, regardless of time of day.\\n\\nAnother natural source of light at night is emitted from glowing lava flows at the site of active volcanoes. Again, with enough moonlight, these dramatic scenes can be tracked and monitored for both scientific research and public safety.\\n\\n\\n### Figure: The Northern Lights Viewed from Space\\n\\n**September 17, 2011**\\n\\nThis photo, taken from the International Space Station on September 17, 2011, shows a spectacular display of the aurora borealis (Northern Lights) as green and reddish light in the night sky above Earth. In the foreground, part of a Soyuz spacecraft is visible, silhouetted against the bright auroral light. The green glow is generated by energetic charged particles from the Sun interacting with Earth's upper atmosphere, exciting oxygen and nitrogen atoms, and producing characteristic colors. The image demonstrates the vividness and grandeur of natural night-time light phenomena as seen from orbit.\"}]"}]}]
+
+Activities:
+Activity Type: ModelQueryPlanning
+{
+  "type": "ModelQueryPlanning",
+  "id": 0,
+  "inputTokens": 1598,
+  "outputTokens": 159
+}
+Activity Type: AzureSearchQuery
+{
+  "type": "AzureSearchQuery",
+  "id": 1,
+  "targetIndex": "earth_at_night",
+  "query": {
+    "search": "How can I locate lava flows during nighttime?",
+    "filter": null
+  },
+  "queryTime": "2025-07-20T16:13:10.659Z",
+  "count": 5,
+  "elapsedMs": 260
+}
+Activity Type: AzureSearchSemanticRanker
+{
+  "type": "AzureSearchSemanticRanker",
+  "id": 2,
+  "inputTokens": 24146
+}
+Results
+Reference Type: AzureSearchDoc
+{
+  "type": "AzureSearchDoc",
+  "id": "0",
+  "activitySource": 1,
+  "docKey": "earth_at_night_508_page_64_verbalized",
+  "sourceData": {
+    "id": "earth_at_night_508_page_64_verbalized",
+    "page_chunk": "<!-- PageHeader=\"Volcanoes\" -->\n\n### Nighttime Glow at Mount Etna - Italy\n\nAt about 2:30 a.m. local time on March 16, 2017, the VIIRS DNB on the Suomi NPP satellite captured this nighttime image of lava flowing on Mount Etna in Sicily, Italy. Etna is one of the world's most active volcanoes.\n\n#### Figure: Location of Mount Etna\nA world globe is depicted, with a marker indicating the location of Mount Etna in Sicily, Italy, in southern Europe near the center of the Mediterranean Sea.\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"48\" -->"
+  }
+}
+Reference Type: AzureSearchDoc
+{
+  "type": "AzureSearchDoc",
+  "id": "1",
+  "activitySource": 1,
+  "docKey": "earth_at_night_508_page_60_verbalized",
+  "sourceData": {
+    "id": "earth_at_night_508_page_60_verbalized",
+    "page_chunk": "<!-- PageHeader=\"Volcanoes\" -->\n\n## Volcanoes\n\n### The Infrared Glows of Kilauea's Lava Flows—Hawaii\n\nIn early May 2018, an eruption on Hawaii's Kilauea volcano began to unfold. The eruption took a dangerous turn on May 3, 2018, when new fissures opened in the residential neighborhood of Leilani Estates. During the summer-long eruptive event, other fissures emerged along the East Rift Zone. Lava from vents along the rift zone flowed downslope, reaching the ocean in several areas, and filling in Kapoho Bay.\n\nA time series of Landsat 8 imagery shows the progression of the lava flows from May 16 to August 13. The night view combines thermal, shortwave infrared, and near-infrared wavelengths to tease out the very hot lava (bright white), cooling lava (red), and lava flows obstructed by clouds (purple).\n\n#### Figure: Location of Kilauea Volcano, Hawaii\n\nA globe is shown centered on North America, with a marker placed in the Pacific Ocean indicating the location of Hawaii, to the southwest of the mainland United States.\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"44\" -->"
+  }
+}
+Reference Type: AzureSearchDoc
+{
+  "type": "AzureSearchDoc",
+  "id": "2",
+  "activitySource": 1,
+  "docKey": "earth_at_night_508_page_46_verbalized",
+  "sourceData": {
+    "id": "earth_at_night_508_page_46_verbalized",
+    "page_chunk": "For the first time in perhaps a decade, Mount Etna experienced a \"flank eruption\"—erupting from its side instead of its summit—on December 24, 2018. The activity was accompanied by 130 earthquakes occurring over three hours that morning. Mount Etna, Europe’s most active volcano, has seen periodic activity on this part of the mountain since 2013. The Operational Land Imager (OLI) on the Landsat 8 satellite acquired the main image of Mount Etna on December 28, 2018.\n\nThe inset image highlights the active vent and thermal infrared signature from lava flows, which can be seen near the newly formed fissure on the southeastern side of the volcano. The inset was created with data from OLI and the Thermal Infrared Sensor (TIRS) on Landsat 8. Ash spewing from the fissure cloaked adjacent villages and delayed aircraft from landing at the nearby Catania airport. Earthquakes occurred in the subsequent days after the initial eruption and displaced hundreds of people from their homes.\n\nFor nighttime images of Mount Etna’s March 2017 eruption, see pages 48–51.\n\n---\n\n### Hazards of Volcanic Ash Plumes and Satellite Observation\n\nWith the help of moonlight, satellite instruments can track volcanic ash plumes, which present significant hazards to airplanes in flight. The volcanic ash—composed of tiny pieces of glass and rock—is abrasive to engine turbine blades, and can melt on the blades and other engine parts, causing damage and even engine stalls. This poses a danger to both the plane’s integrity and passenger safety. Volcanic ash also reduces visibility for pilots and can cause etching of windshields, further reducing pilots’ ability to see. Nightlight images can be combined with thermal images to provide a more complete view of volcanic activity on Earth’s surface.\n\nThe VIIRS Day/Night Band (DNB) on polar-orbiting satellites uses faint light sources such as moonlight, airglow (the atmosphere’s self-illumination through chemical reactions), zodiacal light (sunlight scattered by interplanetary dust), and starlight from the Milky Way. Using these dim light sources, the DNB can detect changes in clouds, snow cover, and sea ice:\n\n#### Table: Light Sources Used by VIIRS DNB\n\n| Light Source         | Description                                                                  |\n|----------------------|------------------------------------------------------------------------------|\n| Moonlight            | Reflected sunlight from the Moon, illuminating Earth's surface at night      |\n| Airglow              | Atmospheric self-illumination from chemical reactions                        |\n| Zodiacal Light       | Sunlight scattered by interplanetary dust                                    |\n| Starlight/Milky Way  | Faint illumination provided by stars in the Milky Way                        |\n\nGeostationary Operational Environmental Satellites (GOES), managed by NOAA, orbit over Earth’s equator and offer uninterrupted observations of North America. High-latitude areas such as Alaska benefit from polar-orbiting satellites like Suomi NPP, which provide overlapping coverage at the poles, enabling more data collection in these regions. During polar darkness (winter months), VIIRS DNB data allow scientists to:\n\n- Observe sea ice formation\n- Monitor snow cover extent at the highest latitudes\n- Detect open water for ship navigation\n\n#### Table: Satellite Coverage Overview\n\n| Satellite Type          | Orbit           | Coverage Area         | Special Utility                              |\n|------------------------|-----------------|----------------------|----------------------------------------------|\n| GOES                   | Geostationary   | Equatorial/North America | Continuous regional monitoring              |\n| Polar-Orbiting (e.g., Suomi NPP) | Polar-orbiting    | Poles/high latitudes      | Overlapping passes; useful during polar night|\n\n---\n\n### Weather Forecasting and Nightlight Data\n\nThe use of nightlight data by weather forecasters is growing as the VIIRS instrument enables observation of clouds at night illuminated by sources such as moonlight and lightning. Scientists use these data to study the nighttime behavior of weather systems, including severe storms, which can develop and strike populous areas at night as well as during the day. Combined with thermal data, visible nightlight data allow the detection of clouds at various heights in the atmosphere, such as dense marine fog. This capability enables weather forecasters to issue marine advisories with higher confidence, leading to greater utility. (See \"Marine Layer Clouds—California\" on page 56.)\n\nIn this section of the book, you will see how nightlight data are used to observe nature’s spectacular light shows across a wide range of sources.\n\n---\n\n#### Notable Data from Mount Etna Flank Eruption (December 2018)\n\n| Event/Observation                  | Details                                                                    |\n|-------------------------------------|----------------------------------------------------------------------------|\n| Date of Flank Eruption              | December 24, 2018                                                          |\n| Number of Earthquakes               | 130 earthquakes within 3 hours                                              |\n| Image Acquisition                   | December 28, 2018 by Landsat 8 OLI                                         |\n| Location of Eruption                | Southeastern side of Mount Etna                                            |\n| Thermal Imaging Data                | From OLI and TIRS (Landsat 8), highlighting active vent and lava flows     |\n| Impact on Villages/Air Transport    | Ash covered villages; delayed aircraft at Catania airport                  |\n| Displacement                        | Hundreds of residents displaced                                            |\n| Ongoing Seismic Activity            | Earthquakes continued after initial eruption                               |\n\n---\n\n<!-- PageFooter=\"Earth at Night\" -->\n<!-- PageNumber=\"30\" -->"
+  }
+}
+Reference Type: AzureSearchDoc
+{
+  "type": "AzureSearchDoc",
+  "id": "3",
+  "activitySource": 1,
+  "docKey": "earth_at_night_508_page_66_verbalized",
+  "sourceData": {
+    "id": "earth_at_night_508_page_66_verbalized",
+    "page_chunk": "# Volcanoes\n\n---\n\n### Mount Etna Erupts - Italy\n\nThe highly active Mount Etna in Italy sent red lava rolling down its flank on March 19, 2017. An astronaut onboard the ISS took the photograph below of the volcano and its environs that night. City lights surround the mostly dark volcanic area.\n\n---\n\n#### Figure 1: Location of Mount Etna, Italy\n\nA world map highlighting the location of Mount Etna in southern Italy. The marker indicates its geographic placement on the east coast of Sicily, Italy, in the Mediterranean region, south of mainland Europe and north of northern Africa.\n\n---\n\n#### Figure 2: Nighttime View of Mount Etna's Eruption and Surrounding Cities\n\nThis is a nighttime satellite image taken on March 19, 2017, showing the eruption of Mount Etna (southeastern cone) with visible bright red and orange coloring indicating flowing lava from a lateral vent. The surrounding areas are illuminated by city lights, with the following geographic references labeled:\n\n| Location        | Position in Image         | Visible Characteristics                    |\n|-----------------|--------------------------|--------------------------------------------|\n| Mt. Etna (southeastern cone) | Top center-left | Bright red/orange lava flow                |\n| Lateral vent    | Left of the volcano       | Faint red/orange flow extending outwards   |\n| Resort          | Below the volcano, to the left   | Small cluster of lights                    |\n| Giarre          | Top right                 | Bright cluster of city lights              |\n| Acireale        | Center right              | Large, bright area of city lights          |\n| Biancavilla     | Bottom left               | Smaller cluster of city lights             |\n\nAn arrow pointing north is shown on the image for orientation.\n\n---\n\n<!-- Earth at Night Page Footer -->\n<!-- Page Number: 50 -->"
+  }
+}
+Reference Type: AzureSearchDoc
+{
+  "type": "AzureSearchDoc",
+  "id": "4",
+  "activitySource": 1,
+  "docKey": "earth_at_night_508_page_44_verbalized",
+  "sourceData": {
+    "id": "earth_at_night_508_page_44_verbalized",
+    "page_chunk": "## Nature's Light Shows\n\nAt night, with the light of the Sun removed, nature's brilliant glow from Earth's surface becomes visible to the naked eye from space. Some of Earth's most spectacular light shows are natural, like the aurora borealis, or Northern Lights, in the Northern Hemisphere (aurora australis, or Southern Lights, in the Southern Hemisphere). The auroras are natural electrical phenomena caused by charged particles that race from the Sun toward Earth, inducing chemical reactions in the upper atmosphere and creating the appearance of streamers of reddish or greenish light in the sky, usually near the northern or southern magnetic pole. Other natural lights can indicate danger, like a raging forest fire encroaching on a city, town, or community, or lava spewing from an erupting volcano.\n\nWhatever the source, the ability of humans to monitor nature's light shows at night has practical applications for society. For example, tracking fires during nighttime hours allows for continuous monitoring and enhances our ability to protect humans and other animals, plants, and infrastructure. Combined with other data sources, our ability to observe the light of fires at night allows emergency managers to more efficiently and accurately issue warnings and evacuation orders and allows firefighting efforts to continue through the night. With enough moonlight (e.g., full-Moon phase), it's even possible to track the movement of smoke plumes at night, which can impact air quality, regardless of time of day.\n\nAnother natural source of light at night is emitted from glowing lava flows at the site of active volcanoes. Again, with enough moonlight, these dramatic scenes can be tracked and monitored for both scientific research and public safety.\n\n\n### Figure: The Northern Lights Viewed from Space\n\n**September 17, 2011**\n\nThis photo, taken from the International Space Station on September 17, 2011, shows a spectacular display of the aurora borealis (Northern Lights) as green and reddish light in the night sky above Earth. In the foreground, part of a Soyuz spacecraft is visible, silhouetted against the bright auroral light. The green glow is generated by energetic charged particles from the Sun interacting with Earth's upper atmosphere, exciting oxygen and nitrogen atoms, and producing characteristic colors. The image demonstrates the vividness and grandeur of natural night-time light phenomena as seen from orbit."
+  }
+}
+
+[ASSISTANT]: 
+To find lava at night, satellite instruments like the VIIRS Day/Night Band (DNB) and thermal infrared sensors are used to detect the glow of very hot lava flows on the Earth's surface
+ For example, nighttime satellite images have captured lava flowing from active volcanoes such as Mount Etna in Italy and Kilauea in Hawaii, where the hot lava emits bright light visible from space even at night
+ Scientists combine thermal, shortwave infrared, and near-infrared data to distinguish very hot lava (bright white), cooling lava (red), and areas obscured by clouds
+ Additionally, moonlight and other faint natural light sources help illuminate the surroundings to improve observation of volcanic activity at night
+ Monitoring lava flow at night is important for scientific research and public safety, as it helps track volcanic eruptions and associated hazards such as ash plumes that can affect air travel and nearby communities [refs 0,1,2,3,4]
+
+
+🎉 === Conversation Complete ===
+🗑️ Deleting knowledge agent...
+✅ Knowledge agent 'earth-search-agent' deleted successfully.
+🗑️ Deleting search index...
+✅ Search index 'earth_at_night' deleted successfully.
+✅ Quickstart completed successfully!
+```
+
+## Explaining the code
+
+Now that you have the code, let's break down the key components:
+
+- [Create a search index](#create-a-search-index)
+- [Upload documents to the index](#upload-documents-to-the-index)
+- [Create a knowledge agent](#create-a-knowledge-agent)
+- [Set up messages](#set-up-messages)
+- [Run the retrieval pipeline](#run-the-retrieval-pipeline)
+- [Review the response, activity, and results](#review-the-response-activity-and-results)
+- [Create the Azure OpenAI client](#create-the-azure-openai-client)
+- [Use the Chat Completions API to generate an answer](#use-the-chat-completions-api-to-generate-an-answer)
+- [Continue the conversation](#continue-the-conversation)
+
+### Create a search index
+
+In Azure AI Search, an index is a structured collection of data. The following code defines an index named `earth_at_night` to contain plain text and vector content. You can use an existing index, but it must meet the criteria for [agentic retrieval workloads](../../search-agentic-retrieval-how-to-index.md). 
+
+```typescript
+const index: SearchIndex = {
+    name: config.indexName,
+    fields: [
+        {
+            name: "id",
+            type: "Edm.String",
+            key: true,
+            filterable: true,
+            sortable: true,
+            facetable: true
+        } as SearchField,
+        {
+            name: "page_chunk",
+            type: "Edm.String",
+            searchable: true,
+            filterable: false,
+            sortable: false,
+            facetable: false
+        } as SearchField,
+        {
+            name: "page_embedding_text_3_large",
+            type: "Collection(Edm.Single)",
+            searchable: true,
+            filterable: false,
+            sortable: false,
+            facetable: false,
+            vectorSearchDimensions: 3072,
+            vectorSearchProfileName: "hnsw_text_3_large"
+        } as SearchField,
+        {
+            name: "page_number",
+            type: "Edm.Int32",
+            filterable: true,
+            sortable: true,
+            facetable: true
+        } as SearchField
+    ],
+    vectorSearch: {
+        profiles: [
+            {
+                name: "hnsw_text_3_large",
+                algorithmConfigurationName: "alg",
+                vectorizerName: "azure_openai_text_3_large"
+            } as VectorSearchProfile
+        ],
+        algorithms: [
+            {
+                name: "alg",
+                kind: "hnsw"
+            } as HnswAlgorithmConfiguration
+        ],
+        vectorizers: [
+            {
+                vectorizerName: "azure_openai_text_3_large",
+                kind: "azureOpenAI",
+                parameters: {
+                    resourceUrl: config.azureOpenAIEndpoint,
+                    deploymentId: config.azureOpenAIEmbeddingDeployment,
+                    modelName: config.azureOpenAIEmbeddingModel
+                } as AzureOpenAIParameters
+            } as AzureOpenAIVectorizer
+        ]
+    } as VectorSearch,
+    semanticSearch: {
+        defaultConfigurationName: "semantic_config",
+        configurations: [
+            {
+                name: "semantic_config",
+                prioritizedFields: {
+                    contentFields: [
+                        { name: "page_chunk" } as SemanticField
+                    ]
+                } as SemanticPrioritizedFields
+            } as SemanticConfiguration
+        ]
+    } as SemanticSearch
+};
+
+try {
+    await indexClient.createOrUpdateIndex(index);
+    console.log(`✅ Index '${config.indexName}' created or updated successfully.`);
+} catch (error) {
+    console.error("❌ Error creating index:", error);
+    throw error;
+}
+```
+
+The index schema contains fields for document identification and page content, embeddings, and numbers. It also includes configurations for semantic ranking and vector queries, which use the `text-embedding-3-large` model you previously deployed.
+
+### Upload documents to the index
+
+Currently, the `earth_at_night` index is empty. Run the following code to populate the index with JSON documents from [NASA's Earth at Night e-book](https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json). As required by Azure AI Search, each document conforms to the fields and data types defined in the index schema.
+
+```typescript
+const documentsUrl = "https://raw.githubusercontent.com/Azure-Samples/azure-search-sample-data/refs/heads/main/nasa-e-book/earth-at-night-json/documents.json";
+    
+try {
+    const response = await fetch(documentsUrl);
+    
+    if (!response.ok) {
+        throw new Error(`Failed to fetch documents: ${response.status} ${response.statusText}`);
+    }
+    
+    const documents = await response.json();
+    console.log(`✅ Fetched ${documents.length} documents from GitHub`);
+    
+    // Validate and transform documents to match our interface
+    const transformedDocuments: EarthAtNightDocument[] = documents.map((doc: any, index: number) => {
+        return {
+            id: doc.id || String(index + 1),
+            page_chunk: doc.page_chunk || doc.content || '',
+            page_embedding_text_3_large: doc.page_embedding_text_3_large || new Array(3072).fill(0.1),
+            page_number: doc.page_number || index + 1
+        };
+    });
+    
+    return transformedDocuments;
+    
+}
+```
+
+### Create a knowledge agent
+
+To connect Azure AI Search to your `gpt-4.1-mini` deployment and target the `earth_at_night` index at query time, you need a knowledge agent. The following code defines a knowledge agent named `earth-search-agent` that uses the agent definition to process queries and retrieve relevant documents from the `earth_at_night` index.
+
+To ensure relevant and semantically meaningful responses, `defaultRerankerThreshold` is set to exclude responses with a reranker score of `2.5` or lower.
+
+```typescript
+const agentDefinition = {
+    name: config.agentName,
+    description: "Knowledge agent for Earth at Night e-book content",
+    models: [
+        {
+            kind: "azureOpenAI",
+            azureOpenAIParameters: {
+                resourceUri: config.azureOpenAIEndpoint,
+                deploymentId: config.azureOpenAIGptDeployment,
+                modelName: config.azureOpenAIGptModel
+            }
+        }
+    ],
+    targetIndexes: [
+        {
+            indexName: config.indexName,
+            defaultRerankerThreshold: 2.5
+        }
+    ]
+};   
+```
+
+### Set up messages
+
+Messages are the input for the retrieval route and contain the conversation history. Each message includes a role that indicates its origin, such as assistant or user, and content in natural language. The LLM you use determines which roles are valid.
+
+A user message represents the query to be processed, while an assistant message guides the knowledge agent on how to respond. During the retrieval process, these messages are sent to an LLM to extract relevant responses from indexed documents.
+
+This assistant message instructs `earth-search-agent` to answer questions about the Earth at night, cite sources using their `ref_id`, and respond with "I don't know" when answers are unavailable.
+
+```typescript
+const messages: KnowledgeAgentMessage[] = [
+    {
+        role: "system",
+        content: `A Q&A agent that can answer questions about the Earth at night.
+Sources have a JSON format with a ref_id that must be cited in the answer.
+If you do not have the answer, respond with "I don't know".`
+    },
+    {
+        role: "user",
+        content: "Why do suburban belts display larger December brightening than urban cores even though absolute light levels are higher downtown? Why is the Phoenix nighttime street grid is so sharply visible from space, whereas large stretches of the interstate between midwestern cities remain comparatively dim?"
+    }
+];
+```
+
+### Run the retrieval pipeline
+
+This step runs the retrieval pipeline to extract relevant information from your search index. Based on the messages and parameters on the retrieval request, the LLM:
+1. Analyzes the entire conversation history to determine the underlying information need.
+1. Breaks down the compound user query into focused subqueries.
+1. Runs each subquery simultaneously against text fields and vector embeddings in your index.
+1. Uses semantic ranker to rerank the results of all subqueries.
+1. Merges the results into a single string.
+
+The following code sends a two-part user query to `earth-search-agent`, which deconstructs the query into subqueries, runs the subqueries against both text fields and vector embeddings in the `earth_at_night` index, and ranks and merges the results. The response is then appended to the `messages` list.
+
+```typescript
+const agentMessages = messages.map(msg => ({
+    role: msg.role,
+    content: [
+        {
+            type: "text",
+            text: msg.content
+        }
+    ]
+}));
+
+const retrievalRequest = {
+    messages: agentMessages,
+    targetIndexParams: [
+        {
+            indexName: config.indexName,
+            rerankerThreshold: 2.5,
+            maxDocsForReranker: 100,
+            includeReferenceSourceData: true
+        }
+    ]
+};
+
+const token = await getAccessToken(credential, "https://search.azure.com/.default");
+const response = await fetch(
+    `${config.searchEndpoint}/agents/${config.agentName}/retrieve?api-version=${config.searchApiVersion}`,
+    {
+        method: 'POST',
+        headers: {
+            'Content-Type': 'application/json',
+            'Authorization': `Bearer ${token}`
+        },
+        body: JSON.stringify(retrievalRequest)
+    }
+);
+
+if (!response.ok) {
+    const errorText = await response.text();
+    throw new Error(`Agentic retrieval failed: ${response.status} ${response.statusText}\n${errorText}`);
+}
+
+return await response.json() as AgenticRetrievalResponse;
+```
+
+### Review the response, activity, and results
+
+Now you want to display the response, activity, and results of the retrieval pipeline.
+
+Each retrieval response from Azure AI Search includes:
+
++ A unified string that represents grounding data from the search results.
+
++ The query plan.
+
++ Reference data that shows which chunks of the source documents contributed to the unified string.
+
+```typescript
+console.log("\nActivities:");
+if (retrievalResponse.activity && Array.isArray(retrievalResponse.activity)) {
+    retrievalResponse.activity.forEach((activity) => {
+        const activityType = activity.activityType || activity.type || 'UnknownActivityRecord';
+        console.log(`Activity Type: ${activityType}`);
+        console.log(JSON.stringify(activity, null, 2));
+    });
+}
+
+console.log("Results");
+if (retrievalResponse.references && Array.isArray(retrievalResponse.references)) {
+    retrievalResponse.references.forEach((reference) => {
+        const referenceType = reference.referenceType || reference.type || 'AzureSearchDoc';
+        console.log(`Reference Type: ${referenceType}`);
+        console.log(JSON.stringify(reference, null, 2));
+    });
+}
+```
+
+The output should include:
+
++ `Response` provides a text string of the most relevant documents (or chunks) in the search index based on the user query. As shown later in this quickstart, you can pass this string to an LLM for answer generation.
+
++ `Activity` tracks the steps that were taken during the retrieval process, including the subqueries generated by your `gpt-4.1-mini` deployment and the tokens used for query planning and execution.
+
++ `Results` lists the documents that contributed to the response, each one identified by their `DocKey`.
+
+### Create the Azure OpenAI client
+
+To extend the retrieval pipeline from answer *extraction* to answer *generation*, set up the Azure OpenAI client to interact with your `gpt-4.1-mini` deployment.
+
+```typescript
+const scope = "https://cognitiveservices.azure.com/.default";
+const azureADTokenProvider = getBearerTokenProvider(credential, scope);
+const openAIClient = new AzureOpenAI({
+    endpoint: config.azureOpenAIEndpoint,
+    apiVersion: config.azureOpenAIApiVersion,
+    azureADTokenProvider,
+});
+```
+
+### Use the Chat Completions API to generate an answer
+
+One option for answer generation is the Chat Completions API, which passes the conversation history to the LLM for processing.
+
+```typescript
+const completion = await openAIClient.chat.completions.create({
+    model: config.azureOpenAIGptDeployment,
+    messages: messages.map(m => ({ role: m.role, content: m.content })) as any,
+    max_tokens: 1000,
+    temperature: 0.7
+});
+
+const answer = completion.choices[0].message.content;
+console.log(answer?.replace(/\./g, "\n"));
+```
+
+### Continue the conversation
+
+Continue the conversation by sending another user query to `earth-search-agent`. The following code reruns the retrieval pipeline, fetching relevant content from the `earth_at_night` index and appending the response to the `messages` list. However, unlike before, you can now use the Azure OpenAI client to generate an answer based on the retrieved content.
+
+```typescript
+const followUpQuestion = "How do I find lava at night?"; 
+console.log(`❓ Follow-up question: ${followUpQuestion}`);
+
+messages.push({
+    role: "user",
+    content: followUpQuestion
+}); 
+```
+
+## Clean up resources
+
+When working in your own subscription, it's a good idea to finish a project by determining whether you still need the resources you created. Resources that are left running can cost you money. You can delete resources individually, or you can delete the resource group to delete the entire set of resources.
+
+In the Azure portal, you can find and manage resources by selecting **All resources** or **Resource groups** from the left pane. You can also run the following code to delete the objects you created in this quickstart.
+
+### Delete the knowledge agent
+
+The knowledge agent created in this quickstart was deleted using the following code snippet:
+
+```typescript
+const token = await getAccessToken(credential, "https://search.azure.com/.default");
+const response = await fetch(`${config.searchEndpoint}/agents/${config.agentName}?api-version=${config.searchApiVersion}`, {
+    method: 'DELETE',
+    headers: {
+        'Authorization': `Bearer ${token}`
+    }
+});
+```
+
+### Delete the search index
+
+The search index created in this quickstart was deleted using the following code snippet:
+
+```typescript
+await indexClient.deleteIndex(config.indexName);
+console.log(`✅ Search index '${config.indexName}' deleted successfully.`);
+```
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "エージェントリトリーバル用のTypeScriptクイックスタートの追加"
}
```

### Explanation
このコード変更は、Azure AI Searchを利用してエージェントリトリーバルを実装するための新しいTypeScriptクイックスタートガイドを追加するものです。このクイックスタートでは、ユーザーが大規模言語モデル（LLM）と独自のデータを使用して会話型検索体験を作成する方法が説明されています。エージェントリトリーバルは、複雑なユーザークエリをサブクエリに分割し、それらを並行して実行し、Azure AI Searchにインデックスされたドキュメントからグラウンディングデータを抽出する機能を提供します。

この文書は、ユーザーが必要とするAzureアカウント、Azure AI Searchサービス、およびセットアップ手順を詳しく説明しており、サンプルデータとしてNASAの「Earth at Night」電子書籍からのJSONドキュメントを使用しています。クイックスタートでは、インデックスの作成、知識エージェントのセットアップ、サンプルドキュメントのアップロード、エージェントリトリーバルの実行などの手順が含まれています。

全体として、この変更は、タスクに必要な技術的なリソースと手順を提供し、Azureを利用した新しい検索機能を実装するための利便性を高めることを目的としています。

## articles/search/search-get-started-agentic-retrieval.md{#item-4a40f4}

<details>
<summary>Diff</summary>
````diff
@@ -1,34 +1,37 @@
 ---
-title: "Quickstart: Agentic Retrieval Using Python or REST APIs"
+title: "Quickstart: Run agentic retrieval in Azure AI Search"
 titleSuffix: Azure AI Search
-description: Learn how to create a knowledge agent that processes multi-turn conversations, retrieves relevant information from an Azure AI Search index, and extracts answers using an Azure OpenAI chat model.
+description: Learn how to use agentic retrieval to create a knowledge agent that processes multi-turn conversations.
 author: haileytap
 ms.author: haileytapia
 ms.service: azure-ai-search
 ms.update-cycle: 90-days
 ms.topic: quickstart
-ms.date: 6/24/2025
+ms.date: 7/21/2025
 zone_pivot_groups: search-get-started-agentic-retrieval
+#User intent: I want to learn how to use agentic retrieval to create a knowledge agent that processes multi-turn conversations. It should retrieve relevant information from an Azure AI Search index and extract answers using an Azure OpenAI chat model.
 ---
 
 # Quickstart: Run agentic retrieval in Azure AI Search
 
 ::: zone pivot="programming-language-csharp"
-
 [!INCLUDE [C# quickstart](includes/quickstarts/agentic-retrieval-csharp.md)]
+::: zone-end
 
+::: zone pivot="programming-language-javascript"
+[!INCLUDE [JavaScript quickstart](includes/quickstarts/agentic-retrieval-javascript.md)]
 ::: zone-end
 
 ::: zone pivot="programming-language-python"
-
 [!INCLUDE [Python quickstart](includes/quickstarts/agentic-retrieval-python.md)]
+::: zone-end
 
+::: zone pivot="programming-language-typescript"
+[!INCLUDE [TypeScript quickstart](includes/quickstarts/agentic-retrieval-typescript.md)]
 ::: zone-end
 
 ::: zone pivot="programming-language-rest"
-
 [!INCLUDE [REST quickstart](includes/quickstarts/agentic-retrieval-rest.md)]
-
 ::: zone-end
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エージェントリトリーバルのクイックスタート記事のタイトルと内容の更新"
}
```

### Explanation
このコードの変更では、エージェントリトリーバルに関するクイックスタート記事のタイトルと説明が更新されています。具体的には、記事のタイトルが「Quickstart: Agentic Retrieval Using Python or REST APIs」から「Quickstart: Run agentic retrieval in Azure AI Search」に変更され、説明文もより具体的な内容に修正されています。更新された説明は、エージェントリトリーバルを使用して知識エージェントを作成する方法に焦点を当てており、多ターンの会話処理に関連した情報をAzure AI Searchインデックスから取得することについて言及しています。

また、クイックスタートに関連するプログラミング言語のセクションが追加され、JavaScriptおよびTypeScriptのクイックスタートが含まれています。その結果、ユーザーが異なるプログラミング言語でエージェントリトリーバルを実装できるリソースが提供されているのが特徴です。

全体として、この変更はコンテンツの明確化と最新の情報提供を目的としており、ユーザーがAzure AI Searchを使用したエージェントリトリーバルの実装に関する理解を深めるのに役立つ情報を強調しています。


