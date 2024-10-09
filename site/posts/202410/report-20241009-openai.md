---
date: '2024-10-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e9690f5...MicrosoftDocs:eb045a9
summary: 今回の変更は、Azure OpenAIサービスに関連する重要なドキュメントや画像ファイルの削除に関するものであり、特に画像データの使用方法やビジュアルガイドに関する情報が失われるため、ユーザーの体験や理解に大きな影響を与える可能性があります。新しい機能の追加はなく、主な変更点としては、画像データに関する資料の削除、補助画像の除去、およびTOCファイルの更新が挙げられます。これにより、ユーザーは設定や構成についての指針を失い、特に初めてサービスを利用する人にとっては、視覚的な資料の欠如が大きな障壁となる可能性があります。全体として、今後の文書の補強が求められます。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e9690f5...MicrosoftDocs:eb045a9){target="_blank"}

# Highlights
今回の変更は、Azure OpenAIサービスに関連する一連のドキュメントや画像ファイルの削除に伴う、重大な「破壊的変更」に焦点を当てています。特に、画像データを使用する方法や関連するビジュアルガイドを含むセクションが削除されており、ユーザーの体験や理解に大きな影響を与える可能性があります。

## New features
今回の変更には、新たな機能の追加についての記述は含まれていません。

## Breaking changes
1. 画像データ使用に関するドキュメントの削除。
2. 複数の補助画像（例：メタデータ追加、チャットプレイグラウンド、アップロード手順、CORS要件など）の削除。
3. TOCファイルの更新に伴い、いくつかの項目の削除と新たな項目の追加。

## Other updates
TOCファイルにおいて、新しい項目「データの使用に関する情報」が追加されています。これにより、ドキュメントの構成が再評価されています。

# Insights
今回のコード変更は広範囲にわたるガイダンスと視覚資料の削除を伴ったものであり、それがユーザー体験に与える影響は重要です。まず、画像データをAzure OpenAIサービスに統合する方法に関する詳細な指針が削除され、これによりユーザーはそれに関連する設定や構成方法についての手がかりを失うことになります。これは特に、画像やビジュアル要素に依存してプロセスを理解していたユーザーにとっては大きな問題となるでしょう。

また、補助画像の削除は、手順やインターフェースの視覚的理解を支援する機能を低下させることになります。具体例としては、CORS要件についての画像が削除されることで、セキュリティ設定の正確な適用が難しくなる可能性があります。

一方で、TOCの更新によって新しいコンテンツの重要性が再評価され、ドキュメントアクセスの容易さが改善されることが期待されています。しかし、このメリットは、削除されたリソースの損失による影響を打ち消すには十分ではないかもしれません。

総じて、今回の変更はAzure OpenAIサービスのユーザーガイドラインにおいて、相当の理解困難を招くものであり、今後のアップデートやドキュメントの補強が必要不可欠です。特に、新規ユーザーや初めてサービスを利用するユーザーにとって、視覚資料の欠如は大きな障壁となり得ます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-your-image-data.md](#item-9eb4bd) | breaking change | 画像データの使用に関するドキュメントの削除 | removed | 0 | 187 | 187 | 
| [add-metadata.png](#item-99e402) | breaking change | 画像にメタデータを追加する画像の削除 | removed | 0 | 0 | 0 | 
| [chat-playground.png](#item-7e0990) | breaking change | チャットプレイグラウンドの画像の削除 | removed | 0 | 0 | 0 | 
| [chatgpt-playground-add-your-data.png](#item-adc192) | breaking change | ChatGPTプラットフォームにデータを追加する画像の削除 | removed | 0 | 0 | 0 | 
| [completed-data-source-cognitive-search.png](#item-487491) | breaking change | 完了したデータソースのコグニティブ検索に関する画像の削除 | removed | 0 | 0 | 0 | 
| [completed-data-source-file-upload.png](#item-1799d0) | breaking change | 完了したデータソースのファイルアップロードに関する画像の削除 | removed | 0 | 0 | 0 | 
| [completed-data-source.png](#item-d38757) | breaking change | 完了したデータソースに関する画像の削除 | removed | 0 | 0 | 0 | 
| [cross-origin-resource-sharing-requirement.png](#item-914e7f) | breaking change | クロスオリジンリソースシェアリング要件に関する画像の削除 | removed | 0 | 0 | 0 | 
| [data-source-fields-blob-storage.png](#item-872a6e) | breaking change | データソースフィールドに関する画像の削除 | removed | 0 | 0 | 0 | 
| [remove-data-source-warning.png](#item-54e33a) | breaking change | データソース警告に関する画像の削除 | removed | 0 | 0 | 0 | 
| [select-add-data-source.png](#item-1f540e) | breaking change | データソース追加選択に関する画像の削除 | removed | 0 | 0 | 0 | 
| [tent-chat-example.png](#item-f7df2e) | breaking change | テントチャットの例に関する画像の削除 | removed | 0 | 0 | 0 | 
| [uploaded-files.png](#item-aba3d6) | breaking change | アップロードされたファイルに関する画像の削除 | removed | 0 | 0 | 0 | 
| [toc.yml](#item-c945af) | minor update | TOCファイルの更新 | modified | 1 | 4 | 5 | 


# Modified Contents
## articles/ai-services/openai/concepts/use-your-image-data.md{#item-9eb4bd}

<details>
<summary>Diff</summary>
````diff
@@ -1,187 +0,0 @@
----
-title: 'Use your image data with Azure OpenAI Service in Azure OpenAI Studio'
-titleSuffix: Azure OpenAI Service
-description: Use this article to learn about using your image data for image generation in Azure OpenAI.
-services: cognitive-services
-manager: nitinme
-ms.service: azure-ai-openai
-ms.topic: quickstart
-author: aahill
-ms.author: aahi
-ms.date: 05/09/2024
-recommendations: false
----
-
-# Use your image data for Azure OpenAI by using GPT-4 Turbo with Vision (preview) in Azure OpenAI Studio
-
-Use this article to learn how to provide your own image data for GPT-4 Turbo with Vision, the vision model in Azure OpenAI Service. GPT-4 Turbo with Vision on your data allows the model to generate more customized and targeted answers by using Retrieval Augmented Generation (RAG), based on your own images and image metadata.
-
-> [!IMPORTANT]
-> After the GPT4-Turbo with Vision preview model is deprecated, you'll no longer be able to use Azure OpenAI on your image data. To implement a RAG solution with image data, see the [sample on GitHub](https://github.com/Azure-Samples/azure-search-openai-demo/).
-
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-- An Azure OpenAI resource with the GPT-4 Turbo with Vision model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
-* At least the [Cognitive Services Contributor role](../how-to/role-based-access-control.md#cognitive-services-contributor) assigned to you for the Azure OpenAI resource.
-
-## Add your data source
-
-Go to [Azure OpenAI Studio](https://oai.azure.com/) and sign in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
-
-:::image type="content" source="../media/use-your-image-data/chat-playground.png" alt-text="Screenshot that shows the chat playground in Azure OpenAI Studio." lightbox="../media/use-your-image-data/chat-playground.png":::
-
-On the **Assistant setup** tile, select **Add your data (preview)** > **+ Add a data source**.
-
-:::image type="content" source="../media/use-your-image-data/chatgpt-playground-add-your-data.png" alt-text="Screenshot that shows the button for adding data in Azure OpenAI Studio." lightbox="../media/use-your-image-data/chatgpt-playground-add-your-data.png":::
-
-In the pane that appears after you select **Add a data source**, you have three options for selecting a data source:
-
-* [Azure AI Search](#add-your-data-by-using-azure-ai-search)
-* [Azure Blob Storage](#add-your-data-by-using-azure-blob-storage)
-* [Your own image files and image metadata](#add-your-data-by-uploading-files)  
-
-:::image type="content" source="../media/use-your-image-data/select-add-data-source.png" alt-text="Screenshot that shows selection of a data source." lightbox="../media/use-your-image-data/select-add-data-source.png":::
-
-All three options use an Azure AI Search index to do an image-to-image search and retrieve the top search results for your input prompt image. For the **Azure Blob Storage** and **Upload files** options, Azure OpenAI generates an image search index for you. For **Azure AI Search**, you need to have an image search index. The following sections contain details on how to create the search index.
-
-### Turn on CORS
-
-When you're adding a data source for the first time, you might see a red notice that asks you to turn on cross-origin resource sharing (CORS). To stop the warning, select **Turn on CORS** so that Azure OpenAI can access the data source.
-
-:::image type="content" source="../media/use-your-image-data/cross-origin-resource-sharing-requirement.png" alt-text="Screenshot that shows an error stating that CORS is not turned on." lightbox="../media/use-your-image-data/cross-origin-resource-sharing-requirement.png":::
-
-## Add your data by uploading files
-
-You can manually upload your image files and enter metadata for them manually by using Azure OpenAI. This capability is especially useful if you're experimenting with a small set of images and want to build your data source.
-
-1. Go to and select the **Add a data source** button in Azure OpenAI as [described earlier](#add-your-data-source). Then select **Upload files**.
-
-1. Select your subscription. Select a Blob Storage account where you want to store your uploaded image files. Select an Azure AI Search resource that will contain your newly created image search index. Enter the image search index name of your choice.
-
-    After you fill in all the values, select the two checkboxes at the bottom to acknowledge incurring usage, and then select **Next**.
-
-    :::image type="content" source="../media/use-your-image-data/completed-data-source-file-upload.png" alt-text="Screenshot that shows the completed boxes for selecting an Azure Blob Storage subscription." lightbox="../media/use-your-image-data/completed-data-source-file-upload.png":::
-
-    The following file types are supported for your image files:
-    * .jpg
-    * .png
-    * .gif
-    * .bmp
-    * .tiff
-
-1. Select **Browse for a file** to select image files that you want to use from your local directory.
-
-1. After you select your image files, they appear in the table. Select **Upload files**. After you upload the files, confirm that the status for each is **Uploaded**. Then select **Next**.
-
-    :::image type="content" source="../media/use-your-image-data/uploaded-files.png" alt-text="Screenshot that shows uploaded files." lightbox="../media/use-your-image-data/uploaded-files.png":::
-
-1. For each image file, enter the metadata in the provided description boxes. Then select **Next**.
-
-    :::image type="content" source="../media/use-your-image-data/add-metadata.png" alt-text="Screenshot that shows boxes for metadata entry." lightbox="../media/use-your-image-data/add-metadata.png":::
-
-1. Review all the information to make sure that it's correct. Then select **Save and close**.
-
-## Add your data by using Azure AI Search
-
-If you have an existing [Azure AI Search](/azure/search/search-what-is-azure-search) index, you can use it as a data source. If you don't already have a search index created for your images, you can create one by using the [AI Search vector search repository on GitHub](https://github.com/Azure/cognitive-search-vector-pr). This repo provides you with scripts to create an index with your image files.
-
-This option is also useful if you want to create your data source by using your own files like the previous option, and then come back to the playground experience to select the data source that you created but haven't added yet.
-
-1. Go to and select the **Add a data source** button in Azure OpenAI as [described earlier](#add-your-data-source). Then select **Azure AI Search**.
-
-    > [!TIP]
-    > You can select an image search index that you created by using the **Azure Blob Storage** or **Upload files** option.  
-
-1. Select your subscription and the Azure AI Search service that you used to create the image search index.
-
-1. Select the Azure AI Search index that you created with your images.
-
-1. After you fill in all the values, select the two checkboxes at the bottom to acknowledge the charges incurred from using GPT-4 Turbo with Vision vector embeddings and Azure AI Search. Then select **Next**.
-
-    :::image type="content" source="../media/use-your-image-data/completed-data-source-cognitive-search.png" alt-text="Screenshot that shows the completed boxes for using an Azure AI Search index." lightbox="../media/use-your-image-data/completed-data-source-cognitive-search.png":::
-
-1. Review the details, and then select **Save and close**.
-
-## Add your data by using Azure Blob Storage
-
-If you have an existing [Azure Blob Storage](/azure/storage/blobs/storage-blobs-introduction) container, you can use it to create an image search index. If you want to create a new container, see the [Blob Storage quickstart](/azure/storage/blobs/storage-quickstart-blobs-portal) documentation.
-
-The option of using a Blob Storage container is especially useful if you have a large number of image files and you don't want to manually upload each one.
-
-If you don't already have a Blob Storage container populated with these files, and you want to upload your files one by one, you can upload the files by using Azure OpenAI Studio instead.
-
-Before you start adding your Blob Storage container as your data source, make sure that it contains all the images that you want to ingest. Also make sure that it contains a JSON file that includes the image file paths and metadata.
-
-> [!IMPORTANT]
-> Your metadata JSON file must:
->
-> * Have a file name that starts with the word *metadata*, all in lowercase without a space.
-> * Have a maximum of 10,000 image files. If you have more than this number of files in your container, you can have multiple JSON files each with up to this maximum.
-
-```json
-[
-    {
-        "image_blob_path": "image1.jpg",
-        "description": "description of image1"
-    },
-    {
-        "image_blob_path": "image2.jpg",
-        "description": "description of image2"
-    },
-    ...
-    {
-        "image_blob_path": "image50.jpg",
-        "description": "description of image50"
-    }
-]
-```
-
-After you have a Blob Storage container that's populated with image files and at least one metadata JSON file, you're ready to add the container as a data source:
-
-1. Go to and select the **Add a data source** button in Azure OpenAI as [described earlier](#add-your-data-source). Then select **Azure Blob Storage**.
-
-1. Select your subscription, Azure Blob Storage, and a storage container. You also need to select an Azure AI Search resource, because a new image search index will be created in this resource group. If you don't have an Azure AI Search resource, you can create a new one by using the link below the dropdown list.
-
-1. In the **Index name** box, enter a name for the search index.
-
-    > [!NOTE]
-    > The name of the index is suffixed with `–v`, to indicate that this index has image vectors extracted from the provided images. The description filed in *metadata.json* will be added as text metadata in the index.
-
-1. After you fill in all values, select the two checkboxes at the bottom to acknowledge the charges incurred from using GPT-4 Turbo with Vision vector embeddings and Azure AI Search. Then select **Next**.
-
-    :::image type="content" source="../media/use-your-image-data/data-source-fields-blob-storage.png" alt-text="Screenshot that shows the data source selection boxes for Blob Storage." lightbox="../media/use-your-image-data/data-source-fields-blob-storage.png":::
-
-1. Review the details, and then select **Save and close**.
-
-## Use your ingested data with your GPT-4 Turbo with Vision model
-
-After you connect your data source by using any of the three methods listed earlier, the data ingestion process takes some time to finish. An icon and a **Ingestion in progress** message appear as the process progresses.
-
-After the ingestion finishes, confirm that a data source is created. The details of your data source appear, along with the name of your image search index.
-
-:::image type="content" source="../media/use-your-image-data/completed-data-source.png" alt-text="Screenshot that shows a completed data source ingestion." lightbox="../media/use-your-image-data/completed-data-source.png":::
-
-Now this ingested data is ready to be used as the grounding data for your deployed GPT-4 Turbo with Vision model. Your model will use the top retrieval data from your image search index and generate a response specifically adhered to your ingested data.
-
-:::image type="content" source="../media/use-your-image-data/tent-chat-example.png" alt-text="Screenshot that shows a chat example with a tent image." lightbox="../media/use-your-image-data/tent-chat-example.png":::
-
-## Additional tips
-
-### Add and remove data sources
-
-Azure OpenAI currently allows only one data source to be used for each chat session. If you want to add a new data source, you must remove the existing data source first. Remove it by selecting **Remove data source** under your data source information.
-
-When you remove a data source, a warning message appears. Removing a data source clears the chat session and resets all playground settings.
-
-:::image type="content" source="../media/use-your-image-data/remove-data-source-warning.png" alt-text="Screenshot that shows a warning about removal of a data source." lightbox="../media/use-your-image-data/remove-data-source-warning.png":::
-
-> [!IMPORTANT]
-> If you switch to a model deployment that doesn't use the GPT-4 Turbo with Vision model, a warning message appears for removing a data source. Removing a data source clears the chat session and resets all playground settings.
-
-## Related content
-
-* [Azure OpenAI On Your Data](./use-your-data.md)
-* [Quickstart: Use images in your AI chats](../gpt-v-quickstart.md)
-* [GPT-4 Turbo with Vision frequently asked questions](../faq.yml#gpt-4-turbo-with-vision)
-* [GPT-4 Turbo with Vision API reference](https://aka.ms/gpt-v-api-ref)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "画像データの使用に関するドキュメントの削除"
}
```

### Explanation
この変更は、「画像データを使用する」についてのドキュメントを完全に削除するものであります。具体的には、Azure OpenAI サービスにおけるカスタマイズされた画像生成に関する情報が含まれていた記事が削除されました。これにより、ユーザーはその情報をもとに画像データを提供する方法、およびそれに関連する前提条件や手順についてのガイダンスを失います。特に、GPT-4 Turbo with Visionモデルを使用するためのデータソースの追加に関する具体的な手順や、Azure Blob StorageやAzure AI Searchを利用する方法が含まれていました。この変更は重要な通知として認識され、利用者は画像データとの相互作用において障害が生じる可能性があります。

## articles/ai-services/openai/media/use-your-image-data/add-metadata.png{#item-99e402}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "画像にメタデータを追加する画像の削除"
}
```

### Explanation
この変更は、「画像データを使用する」ガイドラインに関連して、特定の画像ファイル（`add-metadata.png`）が削除されたことを示しています。この画像は、Azure OpenAI における画像ファイルのメタデータを追加する手順を視覚的に表現していたと考えられます。画像が削除されたことにより、ユーザーはこの特定の手順を理解するための視覚的サポートを失い、メタデータを適切に追加する方法に関しての理解が難しくなる可能性があります。この変更は、関連ドキュメントの完全性に影響を与えるため、重要な影響を及ぼすと考えられます。

## articles/ai-services/openai/media/use-your-image-data/chat-playground.png{#item-7e0990}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "チャットプレイグラウンドの画像の削除"
}
```

### Explanation
この変更は、Azure OpenAI に関するアーティクルから「チャットプレイグラウンド」の画像ファイル（`chat-playground.png`）が削除されたことを示しています。この画像は、ユーザーがAzure OpenAI Studio内での体験を視覚的に理解するために役立つ重要なリソースであったと予測されます。画像の削除により、ユーザーはチャットプレイグラウンドのインターフェースやその利用方法についての明確なビジュアルガイドを失うことになり、コンテンツの理解が難しくなる可能性があります。この変更は、利用者にとって重要な情報の欠如をもたらすため、影響が大きいと考えられます。

## articles/ai-services/openai/media/use-your-image-data/chatgpt-playground-add-your-data.png{#item-adc192}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ChatGPTプラットフォームにデータを追加する画像の削除"
}
```

### Explanation
この変更は、「ChatGPTプラットフォームにデータを追加する」ことに関連する画像ファイル（`chatgpt-playground-add-your-data.png`）が削除されたことを示しています。この画像は、ユーザーがChatGPTの環境内で自分のデータを統合する手順を理解するためのガイドとして機能していたと考えられます。画像が削除されたことで、ユーザーは具体的な手順やインターフェースを把握するための視覚的な支援を失うことになり、学習や利用が困難になる可能性があります。この変更は全体的なドキュメントの理解に対して重要なインパクトを持つため、ユーザーにとっては大きな影響があると評価されます。

## articles/ai-services/openai/media/use-your-image-data/completed-data-source-cognitive-search.png{#item-487491}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "完了したデータソースのコグニティブ検索に関する画像の削除"
}
```

### Explanation
この変更は、完了したデータソースのコグニティブ検索に関連する画像ファイル（`completed-data-source-cognitive-search.png`）が削除されたことを示しています。この画像は、ユーザーがコグニティブ検索の利用方法や、データソースの取り扱いに関する具体的な例を理解するための視覚的なサポートを提供していたと考えられます。画像の削除により、ユーザーは関連する情報の理解が妨げられ、特にコグニティブ検索を利用する上での具体的な手順やベストプラクティスを把握するのが難しくなる可能性があります。この変更は、ドキュメント全体の有用性に対して重大な影響を与えるものと評価されます。

## articles/ai-services/openai/media/use-your-image-data/completed-data-source-file-upload.png{#item-1799d0}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "完了したデータソースのファイルアップロードに関する画像の削除"
}
```

### Explanation
この変更は、完了したデータソースのファイルアップロードに関連する画像ファイル（`completed-data-source-file-upload.png`）が削除されたことを示しています。この画像は、ユーザーがファイルをアップロードするプロセスに関する具体的なガイダンスを提供し、操作を視覚的に支援する役割を果たしていたと考えられます。画像が削除されることで、ユーザーはファイルアップロードの手順や方法を理解するための重要な参考資料を失い、結果としてそのプロセスがより難解になる可能性があります。このため、ドキュメントの価値や利便性に対する影響は大きく、全体的なユーザー体験に悪影響を及ぼすと評価されます。

## articles/ai-services/openai/media/use-your-image-data/completed-data-source.png{#item-d38757}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "完了したデータソースに関する画像の削除"
}
```

### Explanation
この変更は、完了したデータソースに関連する画像ファイル（`completed-data-source.png`）が削除されたことを示しています。この画像は、データソースの理解を助けるための視覚的な情報を提供していたと考えられます。画像の削除により、ユーザーはデータソースの概念や利用方法を把握するのが難しくなり、ドキュメントの有用性が低下する可能性があります。この変更は、特にデータソースに関する実践的な理解を要求される場合において、ユーザー体験に対して重要な影響を及ぼすと評価されます。

## articles/ai-services/openai/media/use-your-image-data/cross-origin-resource-sharing-requirement.png{#item-914e7f}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "クロスオリジンリソースシェアリング要件に関する画像の削除"
}
```

### Explanation
この変更は、クロスオリジンリソースシェアリング（CORS）要件に関連する画像ファイル（`cross-origin-resource-sharing-requirement.png`）が削除されたことを示しています。この画像は、ユーザーがCORSの理解を深めるための重要な視覚的ガイドとして機能していたと考えられます。画像の削除により、ユーザーはCORS要件を適切に把握するのが難しくなり、その結果として関連する作業や実装に対する理解が損なわれる可能性があります。この変更は、特にCORSが関連するアプリケーションの開発や設定において、ユーザー体験に深刻な影響を及ぼすことが予想されます。

## articles/ai-services/openai/media/use-your-image-data/data-source-fields-blob-storage.png{#item-872a6e}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "データソースフィールドに関する画像の削除"
}
```

### Explanation
この変更は、データソースフィールドに関連する画像ファイル（`data-source-fields-blob-storage.png`）が削除されたことを示しています。この画像は、Blobストレージにおけるデータソースのフィールドに関する視覚的な説明を提供していたと考えられます。画像の存在が、ユーザーがBlobストレージの操作や構成を理解するための助けになっていたため、その削除はユーザー体験にとって重要な影響を与える可能性があります。この変更により、Blobストレージを利用したデータ管理に関する実践的な情報の欠如が生じ、特に新しいユーザーにとっては理解しづらくなることが予想されます。

## articles/ai-services/openai/media/use-your-image-data/remove-data-source-warning.png{#item-54e33a}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "データソース警告に関する画像の削除"
}
```

### Explanation
この変更は、データソースに関する警告を示す画像ファイル（`remove-data-source-warning.png`）が削除されたことを示しています。この画像は、ユーザーがデータソースを管理する際の注意点や警告を視覚的に示していたと予想されます。削除されたことにより、ユーザーはデータソースの使用における重要な警告情報を失うことになります。これにより、特に初めてのユーザーや経験の浅いユーザーは、ミスを犯しやすくなる可能性があります。この変更は、システムの使用中に潜在的な問題を引き起こすリスクを高めることになりうるため、重要な影響があります。

## articles/ai-services/openai/media/use-your-image-data/select-add-data-source.png{#item-1f540e}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "データソース追加選択に関する画像の削除"
}
```

### Explanation
この変更は、データソースの追加を選択する際に使用される画像ファイル（`select-add-data-source.png`）が削除されたことを示しています。この画像は、ユーザーが新しいデータソースを追加する方法を視覚的に示す役割を果たしていたと思われます。画像の削除により、データソースを追加するプロセスの理解が難しくなる可能性があります。特に、新しい機能を体験するユーザーにとっては、視覚的なガイドが無いことで混乱を招き、操作ミスの原因となるかもしれません。この変更は、ユーザー体験に対して重要な影響を及ぼすため、注意が必要です。

## articles/ai-services/openai/media/use-your-image-data/tent-chat-example.png{#item-f7df2e}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "テントチャットの例に関する画像の削除"
}
```

### Explanation
この変更は、テントチャットの使用例を示す画像ファイル（`tent-chat-example.png`）が削除されたことを示しています。この画像は、ユーザーがテントチャット機能をどのように活用できるかを視覚的に理解するための重要な参考資料であったと考えられます。画像の削除により、ユーザーはこの機能の具体的な使用例を見失うことになり、理解が難しくなる可能性があります。特に、初心者や新しいユーザーにとっては、実際の利用シーンが欠けることで混乱を招き、機能の効果的な活用を妨げるリスクがあるため、この変更は重要な影響をもたらします。

## articles/ai-services/openai/media/use-your-image-data/uploaded-files.png{#item-aba3d6}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "アップロードされたファイルに関する画像の削除"
}
```

### Explanation
この変更は、アップロードされたファイルに関連する画像ファイル（`uploaded-files.png`）が削除されたことを示しています。この画像は、ユーザーがファイルをどのようにアップロードできるかを視覚的に説明する役割を果たしていたと考えられます。画像の削除により、ユーザーはファイルアップロードのプロセスについての理解を失う可能性があり、特に初めてこの機能を利用するユーザーにとっては、重要な情報源となるはずの視覚的ガイドが欠如することになります。この変更は、全体のユーザー体験に対して重大な影響を及ぼす可能性があるため、注意が必要です。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -168,8 +168,7 @@ items:
     items:
       - name: Text data
         href: ./concepts/use-your-data.md
-      - name: Image data (preview)
-        href: ./concepts/use-your-image-data.md
+        displayName: use your data, on your data
       - name: Use Azure OpenAI On Your Data securely
         href: ./how-to/use-your-data-securely.md
       - name: Deploy and use web apps
@@ -228,8 +227,6 @@ items:
       href: ./tutorials/embeddings.md
     - name: Fine-tuning GPT-4o mini
       href: ./tutorials/fine-tune.md
-    - name: Speech to speech chat
-      href: ../speech-service/openai-speech.md?context=%2fazure%2fcognitive-services%2fopenai%2fcontext%2fcontext
 - name: Responsible AI
   items:
     - name: Overview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCファイルの更新"
}
```

### Explanation
この変更は、オープンAIに関連する目次ファイル（`toc.yml`）の修正を示しています。具体的には、いくつかの項目が削除され、新たに1つの項目が追加されています。削除された項目には「画像データ（プレビュー）」と「音声から音声へのチャット」が含まれており、これにより、ユーザーはこれらのリソースへのアクセスが失われます。一方、追加された項目は「データの使用に関する情報」であり、これは新しいコンテンツやガイダンスを提供することを意図していると考えられます。この変更は、文書全体の構成を見直し、より関連性のある情報を強調するための一環として機能しています。結果として、ユーザーはアップデートされた目次を通じて、必要なリソースにより容易にアクセスできるようになることが期待されます。


