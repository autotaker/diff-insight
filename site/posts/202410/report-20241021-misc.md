---
date: '2024-10-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:418033b...MicrosoftDocs:96dd444
summary: このコードの変更では、医療AIに関連する複数のモジュールや新機能が追加され、特にCXRReportGen、MedImageInsight、MedImageParseの医療AIモデルのデプロイ方法が新たに提供されました。また、医療画像処理の視覚的リソースとしてGIFアニメーションも追加され、理解を助けています。さらに、ユーザーに法的サポートを提供するための免責事項が明文化されたファイルも導入されています。全体的に、これらの変更は医療業界におけるAIの利便性を向上させ、技術的な進展を促進します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:418033b...MicrosoftDocs:96dd444){target="_blank"}

# Highlights
このコードの変更点では、AIに関連する複数の医療モジュールや新しい機能が追加されたことが強調されています。主要な新機能として、CXRReportGenやMedImageInsight、MedImageParseといった医療AIモデルの展開方法が新たに提供されている点が挙げられます。また、医療画像処理と分析における新たな視覚的リソースとして、GIFアニメーションの追加が行われたことも重要です。

## New features
- 医療AIモデル「CXRReportGen」「MedImageInsight」「MedImageParse」のデプロイと使用方法の記事が新たに追加されました。
- AI Studioにおける医療に特化した基盤AIモデルに関する新しい記事が追加されました。
- ビジュアルガイドとして、医療画像の処理フローなどを説明する複数のGIFアニメーションが導入されました。
- 医療AIモデルにおける免責事項が明文化された新しいファイルが追加され、ユーザーを法的観点からサポートしています。

## Breaking changes
- 特に破壊的な変更は見受けられませんが、新機能の追加によるAPIの利用方法や免責事項に対する考慮が必要になります。

## Other updates
- PII（個人情報）の認識を強化するため、ドライバーライセンスとメディケア受給者識別番号が新たにエンティティとして追加されました。
- 医療AIモデルの一覧をモデルカタログに追加してわかりやすく整理されました。
- 既存のAIモデルおよびソリューションに医療特化のコンテンツを目次に追加し、ナビゲーションの利便性が向上しています。

# Insights
この一連の変更は、医療AIにおける技術的な向上と機能強化を示しています。まず、医療分野でのAIモデルのデプロイメントとその使用方法に関する詳細な説明が追加されたことにより、専門家や技術者がこれらのツールを活用しやすくなっています。それぞれのAIモデルは、具体的なリアルタイム推論のシナリオを主体としており、医療業界でのデジタル化を加速するための重要なステップとなるでしょう。

GIFアニメーションの追加は視覚的理解をサポートし、技術的なプロセスを直感的に説明しています。特に、画像解析や報告書生成といった複雑なタスクは、こうしたビジュアルリソースによって説明されることで、ユーザーにとっての学習曲線を低くする効果があります。

また、新しい免責事項の文書化は、ユーザーがAIモデルを利用する際の法的および倫理的なガイドラインを明確にし、潜在的なリスク管理の一助となっています。これにより、Microsoftの提供するAIソリューションの企業としての責任と透明性が強化されています。

さらに、目次やモデルカタログの更新により、特定の情報に楽にアクセスできるようになることで、全体のユーザーエクスペリエンスが向上します。特に医療に焦点を当てたリソースの充実が、今後のAI導入において重要な役割を果たすでしょう。これらの更新は、AIを介した医療業務の効率化と革新を後押しする戦略的な実装の一部であると考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [conversations-entity-categories.md](#item-c268ff) | minor update | 個人を特定できる情報に関する会話エンティティカテゴリの更新 | modified | 2 | 0 | 2 | 
| [deploy-cxrreportgen.md](#item-377d15) | new feature | CXRReportGen 医療 AI モデルのデプロイと使用方法 | added | 209 | 0 | 209 | 
| [deploy-medimageinsight.md](#item-e9ab9e) | new feature | MedImageInsight 医療 AI モデルのデプロイと使用方法 | added | 242 | 0 | 242 | 
| [deploy-medimageparse.md](#item-611e84) | new feature | MedImageParse 医療 AI モデルのデプロイと使用方法 | added | 214 | 0 | 214 | 
| [healthcare-ai-models.md](#item-12fcfc) | new feature | AI Studio における医療のための基盤 AI モデル | added | 54 | 0 | 54 | 
| [model-catalog-overview.md](#item-278001) | minor update | 医療 AI モデルの追加 | modified | 1 | 0 | 1 | 
| [health-ai-models-meddev-disclaimer.md](#item-d90d1c) | new feature | 医療 AI モデルに関する免責事項の追加 | added | 14 | 0 | 14 | 
| [connect-modalities.gif](#item-28d70d) | new feature | 接続モダリティのGIFアニメーションの追加 | added | 0 | 0 | 0 | 
| [healthcare-embedding-capabilities.gif](#item-8d9d5b) | new feature | 医療埋め込み機能のGIFアニメーションの追加 | added | 0 | 0 | 0 | 
| [healthcare-reportgen.gif](#item-4a153d) | new feature | 医療レポート生成のGIFアニメーションの追加 | added | 0 | 0 | 0 | 
| [medimageparse-flow.gif](#item-59cd1a) | new feature | 医療画像解析フローのGIFアニメーションの追加 | added | 0 | 0 | 0 | 
| [toc.yml](#item-2745cd) | minor update | 医療AIモデルに関する新しい項目の追加 | modified | 10 | 0 | 10 | 


# Modified Contents
## articles/ai-services/language-service/personally-identifiable-information/concepts/conversations-entity-categories.md{#item-c268ff}

<details>
<summary>Diff</summary>
````diff
@@ -154,6 +154,8 @@ This category contains the following entities:
         Any numeric or alphanumeric identifier that could contain any PII information. 
         Examples:   
             * Case Number 
+            * Driver's license
+            * Medicare Beneficiary Identifier (MBI)
             * Member Number 
             * Ticket number 
             * Bank account number 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人を特定できる情報に関する会話エンティティカテゴリの更新"
}
```

### Explanation
この変更は、文書「会話エンティティカテゴリ」において、個人を特定できる情報（PII）に関連する情報を更新しています。具体的には、リストに「運転免許証」と「メディケア受給者識別番号（MBI）」の2つの新しいエンティティが追加されました。この修正により、ユーザーは該当するたける情報をより包括的に理解できるようになります。変更は2行追加され、文書の内容が増強されています。

## articles/ai-studio/how-to/healthcare-ai/deploy-cxrreportgen.md{#item-377d15}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,209 @@
+---
+title: How to deploy and use CXRReportGen healthcare AI model with AI Studio
+titleSuffix: Azure AI Studio
+description: Learn how to use CXRReportGen Healthcare AI Model with Azure AI Studio.
+ms.service: azure-ai-studio
+manager: scottpolly
+ms.topic: how-to
+ms.date: 10/20/2024
+ms.reviewer: itarapov
+reviewer: ivantarapov
+ms.author: mopeakande
+author: msakande
+#Customer intent: As a Data Scientist I want to learn how to use the CXRReportGen healthcare AI model to generate grounded findings.
+
+---
+
+# How to use CXRReportGen Healthcare AI model to generate grounded findings
+
+[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+
+[!INCLUDE [health-ai-models-meddev-disclaimer](../../includes/health-ai-models-meddev-disclaimer.md)]
+
+In this article, you learn how to deploy CXRReportGen as an online endpoint for real-time inference and issue a basic call to the API. The steps you take are:
+
+* Deploy the model to a self-hosted managed compute.
+* Grant permissions to the endpoint.
+* Send test data to the model, receive, and interpret results
+
+## CXRReportGen - grounded report generation model for chest X-rays
+Radiology reporting demands detailed image understanding, integration of multiple inputs (including comparisons with prior imaging), and precise language generation, making it an ideal candidate for generative multimodal models. CXRReportGen generates a list of findings from a chest X-ray study and also perform a _grounded report generation_ or _grounding_ task. That is, the CXRReportGen model also incorporates the localization of individual findings on the image. Grounding enhances the clarity of image interpretation and the transparency of AI-generated text, which end up improving the utility of automated report drafting.
+
+The following animation demonstrates the conceptual architecture of the CXRReportGen model, which consists of an embedding model paired with a general reasoner large language model (LLM). 
+
+:::image type="content" source="../../media/how-to/healthcare-ai/healthcare-reportgen.gif" alt-text="Animation of CXRReportGen architecture and data flow.":::
+
+The CXRReportGen model combines a radiology-specific image encoder with a large language model and takes as inputs a more comprehensive set of data than many traditional approaches. The input data includes the current frontal image, the current lateral image, the prior frontal image, the prior report, and the indication, technique, and comparison sections of the current report. These additions significantly enhance report quality and reduce incorrect information, ultimately demonstrating the feasibility of grounded reporting as a novel and richer task in automated radiology.
+
+## Prerequisites
+
+To use CXRReportGen model with Azure AI Studio or Azure Machine Learning studio, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to a self-hosted managed compute**
+
+CXRReportGen model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served. You can deploy the model through the model catalog UI or programmatically.
+
+To __deploy the model through the UI__:
+
+1. Go to the [model card in the catalog](https://aka.ms/cxrreportgenmodelcard). 
+1. On the model's overview page, select __Deploy__. 
+1. If given the option to choose between serverless API deployment and deployment using a managed compute, select **Managed Compute**.
+1. Fill out the details in the deployment window.
+
+    > [!NOTE]
+    > For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
+1. Select __Deploy__.
+
+To __deploy the model programmatically__, see [How to deploy and inference a managed compute deployment with code](../deploy-models-managed.md).
+
+
+## Work with a grounded report generation model for chest X-ray analysis
+
+In this section, you consume the model and make basic calls to it.
+
+### Use REST API to consume the model
+
+Consume the CXRReportGen report generation model as a REST API, using simple GET requests or by creating a client as follows:
+
+```python
+from azure.ai.ml import MLClient
+from azure.identity import DeviceCodeCredential
+
+credential = DefaultAzureCredential()
+
+ml_client_workspace = MLClient.from_config(credential)
+```
+
+In the deployment configuration, you get to choose the authentication method. This example uses Azure Machine Learning token-based authentication. For more authentication options, see the [corresponding documentation page](../../../machine-learning/how-to-setup-authentication.md). Also, note that the client is created from a configuration file that is created automatically for Azure Machine Learning virtual machines (VMs). Learn more on the [corresponding API documentation page](/python/api/azure-ai-ml/azure.ai.ml.mlclient#azure-ai-ml-mlclient-from-config).
+
+### Make basic calls to the model
+
+Once the model is deployed, use the following code to send data and retrieve a list of findings and corresponding bounding boxes.
+
+```python
+input_data = {
+        "frontal_image": base64.encodebytes(read_image(frontal_path)).decode("utf-8"),
+        "lateral_image": base64.encodebytes(read_image(lateral_path)).decode("utf-8"),
+        "indication": indication,
+        "technique": technique,
+        "comparison": comparison,
+    }
+
+    data = {
+        "input_data": {
+            "columns": list(input_data.keys()),
+            #  IMPORANT: Modify the index as needed
+            "index": [0],  # 1, 2],
+            "data": [
+                list(input_data.values()),
+            ],
+        }
+    }
+
+    # Create request json
+    request_file_name = "sample_request_data.json"
+    with open(request_file_name, "w") as request_file:
+        json.dump(data, request_file)
+
+    response = ml_client_workspace.online_endpoints.invoke(
+        endpoint_name=endpoint_name,
+        deployment_name=deployment_name,
+        request_file=request_file_name,
+    )
+```
+
+## Use CXRReportGen REST API
+CXRReportGen model assumes a simple single-turn interaction where one request produces one response. 
+
+### Request schema
+
+Request payload is a JSON formatted string containing the following parameters:
+
+| Key           | Type           | Required/Default | Description |
+| ------------- | -------------- | :-----------------:| ----------------- |
+| `input_data`       | `[object]`       | Y    | An object containing the input data payload | 
+
+The `input_data` object contains the following fields:
+
+| Key           | Type           | Required/Default | Allowed values    | Description |
+| ------------- | -------------- | :-----------------:| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `columns`       | `list[string]`       | Y    |  `"frontal_image"`, `"lateral_image"`, `"prior_image"`,`"indication"`, `"technique"`,  `"comparison"`, `"prior_report"`  | An object containing the strings mapping data to inputs passed to the model.|
+| `index`   | `integer` | Y | 0 - 10 | Count of inputs passed to the model. You're limited by how much GPU RAM you have on the VM where CxrReportGen is hosted, and by how much data can be passed in a single POST request—which depends on the size of your images. Therefore, it's reasonable to keep this number under 10. Check model logs if you're getting errors when passing multiple inputs. |
+| `data`   | `list[list[string]]` | Y | "" | The list contains the list of items passed to the model. The length of the list is defined by the index parameter. Each item is a list of several strings. The order and meaning are defined by the `columns` parameter. The text strings contain text. The image strings are the image bytes encoded using base64 and decoded as utf-8 string |
+
+
+### Request example
+
+**A simple inference requesting list of findings for a single frontal image with no indication provided** 
+```JSON
+{
+  "input_data": {
+    "columns": [
+      "frontal_image"
+    ],
+    "index":[0],
+    "data": [
+      ["iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAAXNSR0IArs4c6QAAAARnQU1BAACx\njwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAAbSURBVBhXY/gUoPS/fhfDfwaGJe///9/J8B8A\nVGwJ5VDvPeYAAAAASUVORK5CYII=\n"]
+    ]
+  }
+}
+```
+
+**More complex request passing frontal, lateral, indication and technique** 
+```JSON
+{
+  "input_data": {
+    "columns": [
+      "frontal_image",
+      "lateral_image",
+      "indication",
+      "technique"
+    ],
+    "index":[0],
+    "data": [
+      ["iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAAXNSR0IArs4c6QAAAARnQU1BAACx\njwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAAbSURBVBhXY/gUoPS/fhfDfwaGJe///9/J8B8A\nVGwJ5VDvPeYAAAAASUVORK5CYII=\n",
+        "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAAXNSR0IArs4c6QAAAARnQU1BAACx\njwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAAbSURBVBhXY/gUoPS/fhfDfwaGJe///9/J8B8A\nVGwJ5VDvPeYAAAAASUVORK5CYII=\n",
+       "Cough and wheezing for 5 months",
+       "PA and lateral views of the chest were obtained"]
+    ]
+  }
+}
+```
+
+### Response schema
+
+Response payload is a JSON formatted string containing the following fields:
+
+| Key           | Type           |  Description |
+| ------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `output`       | `list[list[string, list[list[float]]]]` | The list of findings. Each finding is an item in a list represented by a list that contains a string with the text of finding and a list that contains bounding boxes. Each bounding box is represented by a list of four coordinates of the bounding box related to the finding in the following order: `x_min`, `y_min`, `x_max`, `y_max`. Each coordinate value is between 0 and 1, thus to obtain coordinates in the space of the image for rendering or processing these values need to be multiplied by image width or height accordingly|
+
+### Response example
+**A simple inference requesting embedding of a single string** 
+```JSON
+{
+    "output": [
+        ["The heart size is normal.", null],
+        ["Lungs demonstrate blunting of both costophrenic angles.", [[0.005, 0.555, 0.965, 0.865]]],
+        ["There is an area of increased radiodensity overlying the left lower lung.", [[0.555, 0.405, 0.885, 0.745]]],
+        ["Healed fractures of the left fourth, fifth, sixth, seventh, and eighth posterior ribs are noted.", [[0.585, 0.135, 0.925, 0.725]]]
+    ]
+}
+```
+
+### Supported image formats
+
+The deployed model API supports images encoded in PNG or JPEG formats. For optimal results, we recommend using uncompressed/lossless PNGs with 8-bit monochromatic images.
+
+## Learn more from samples
+
+CXRReportGen is a versatile model that can be applied to a wide range of tasks and imaging modalities. For more examples see the following interactive Python notebook: 
+
+* [Deploying and Using CXRReportGen](https://aka.ms/healthcare-ai-examples-cxr-deploy): Learn how to deploy the CXRReportGen model and integrate it into your workflow. This notebook also covers bounding-box parsing and visualization techniques.
+
+## Related content
+
+* [MedImageParse for medical image segmentation](deploy-medimageparse.md)
+* [MedImageInsight for grounded report generation](deploy-medimageinsight.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "CXRReportGen 医療 AI モデルのデプロイと使用方法"
}
```

### Explanation
この修正は、新たに「CXRReportGen 医療 AI モデルのデプロイと使用方法」に関する記事を追加しました。記事では、CXRReportGenモデルをAzure AI Studioでデプロイし、リアルタイム推論のためのオンラインエンドポイントを作成する手順が詳しく説明されています。

新しく追加された内容には、モデルのデプロイ方法、APIの使用法、初期設定に必要な条件、および具体的なリクエストとレスポンスのスキーマが含まれています。特に、胸部X線に基づく自動レポート生成プロセスにおいて、CXRReportGenがどのように働くかが示されています。この情報はAIを用いた医療の文脈で重要であり、ユーザーがCXRReportGenを効果的に利用できるようサポートしています。

全体として、209行にわたる詳細なドキュメントとして構成されており、モデルの展開から実際の利用に至るまでのフローを包括的に案内しています。

## articles/ai-studio/how-to/healthcare-ai/deploy-medimageinsight.md{#item-e9ab9e}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,242 @@
+---
+title: How to deploy and use MedImageInsight healthcare AI model with AI Studio
+titleSuffix: Azure AI Studio
+description: Learn how to use MedImageInsight Healthcare AI Model with Azure AI Studio.
+ms.service: azure-ai-studio
+manager: scottpolly
+ms.topic: how-to
+ms.date: 10/20/2024
+ms.reviewer: itarapov
+reviewer: ivantarapov
+ms.author: mopeakande
+author: msakande
+
+#Customer intent: As a Data Scientist I want to learn how to use the MedImageInsight healthcare AI model to generate medical image embeddings.
+---
+
+# How to use MedImageInsight healthcare AI model for medical image embedding generation
+
+[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+
+[!INCLUDE [health-ai-models-meddev-disclaimer](../../includes/health-ai-models-meddev-disclaimer.md)]
+
+In this article, you learn how to deploy MedImageInsight from the model catalog as an online endpoint for real-time inference. You also learn to issue a basic call to the API. The steps you take are:
+
+* Deploy the model to a self-hosted managed compute.
+* Grant permissions to the endpoint.
+* Send test data to the model, receive, and interpret results
+
+## MedImageInsight - the medical imaging embedding model
+MedImageInsight foundational model for health is a powerful model that can process a wide variety of medical images. These images include X-Ray, CT, MRI, clinical photography, dermoscopy, histopathology, ultrasound, and mammography images. Rigorous evaluations demonstrate MedImageInsight's ability to achieve state-of-the-art (SOTA) or human expert-level performance across classification, image-to-image search, and fine-tuning tasks. Specifically, on public datasets, MedImageInsight achieves or exceeds SOTA performance in chest X-ray disease classification and search, dermatology classification and search, Optical coherence tomography (OCT) classification and search, and 3D medical image retrieval. The model also achieves near-SOTA performance for histopathology classification and search.  
+
+An embedding model is capable of serving as the basis of many different solutions—from classification to more complex scenarios like group matching or outlier detection. The following animation shows an embedding model being used for image similarity search and to detect images that are outliers.
+
+:::image type="content" source="../../media/how-to/healthcare-ai/healthcare-embedding-capabilities.gif" alt-text="Animation that shows an embedding model capable of supporting similarity search and quality control scenarios.":::
+
+## Prerequisites
+
+To use MedImageInsight models with Azure AI Studio or Azure Machine Learning studio, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to a self-hosted managed compute**
+
+MedImageInsight model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served. You can deploy the model through the model catalog UI or programmatically.
+
+To __deploy the model through the UI__:
+
+1. Go to the [model card in the catalog](https://aka.ms/mi2modelcard). 
+1. On the model's overview page, select __Deploy__. 
+1. If given the option to choose between serverless API deployment and deployment using a managed compute, select **Managed Compute**.
+1. Fill out the details in the deployment window.
+
+    > [!NOTE]
+    > For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
+
+1. Select __Deploy__.
+
+To __deploy the model programmatically__, see [How to deploy and inference a managed compute deployment with code](../deploy-models-managed.md).
+
+## Work with an embedding model
+
+In this section, you consume the model and make basic calls to it.
+
+### Use REST API to consume the model
+
+Consume the MedImageInsight embedding model as a REST API, using simple GET requests or by creating a client as follows:
+
+```python
+from azure.ai.ml import MLClient
+from azure.identity import DeviceCodeCredential
+
+credential = DefaultAzureCredential()
+
+ml_client_workspace = MLClient.from_config(credential)
+```
+
+In the deployment configuration, you get to choose the authentication method. This example uses Azure Machine Learning token-based authentication. For more authentication options, see the [corresponding documentation page](../../../machine-learning/how-to-setup-authentication.md). Also, note that the client is created from a configuration file that is created automatically for Azure Machine Learning virtual machines (VMs). Learn more on the [corresponding API documentation page](/python/api/azure-ai-ml/azure.ai.ml.mlclient#azure-ai-ml-mlclient-from-config).
+
+### Make basic calls to the model
+
+Once the model is deployed, use the following code to send data and retrieve embeddings.
+
+```python
+import base64
+import json
+import os
+
+endpoint_name = "medimageinsight"
+deployment_name = "medimageinsight-v1"
+
+sample_image_xray = os.path.join(image_path)
+
+def read_image(image_path):
+    with open(image_path, "rb") as f:
+        return f.read()
+
+data = {
+    "input_data": {
+        "columns": ["image", "text"],
+        #  IMPORTANT: Modify the index as needed
+        "index": [0],
+        "data": [
+            [
+                base64.encodebytes(read_image(sample_image_xray)).decode("utf-8"),
+                "x-ray chest anteroposterior Pneumonia",
+            ]
+        ],
+    },
+    "params": {"get_scaling_factor": True},
+}
+
+# Create request json
+request_file_name = "sample_request_data.json"
+with open(request_file_name, "w") as request_file:
+    json.dump(data, request_file)
+
+response = ml_client_workspace.online_endpoints.invoke(
+    endpoint_name=endpoint_name,
+    deployment_name=deployment_name,
+    request_file=request_file_name,
+)
+```
+
+## Use MedImageInsight REST API
+MedImageInsight model assumes a simple single-turn interaction where one request produces one response. 
+
+### Request schema
+
+Request payload is a JSON formatted string containing the following parameters:
+
+| Key           | Type           | Required/Default | Allowed values    | Description |
+| ------------- | -------------- | :-----------------:| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `input_data`       | `[object]`       | Y    | An object containing the input data payload | |
+| `params`   | `[object]` | N<br/>`null` | An object containing parameters passed to the model| |
+
+The `input_data` object contains the following fields:
+
+| Key           | Type           | Required/Default | Allowed values    | Description |
+| ------------- | -------------- | :-----------------:| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `columns`       | `list[string]`       | Y    |  `"text"`, `"image"` | An object containing the strings mapping data to inputs passed to the model.|
+| `index`   | `integer` | Y | 0 - 1024| Count of inputs passed to the model. You're limited by how much data can be passed in a single POST request, which depends on the size of your images. Therefore, you should keep this number in the dozens |
+| `data`   | `list[list[string]]` | Y | "" | The list contains the items passed to the model which is defined by the index parameter. Each item is a list of two strings. The order is defined by the `columns` parameter. The `text` string contains text to embed. The `image` strings are the image bytes encoded using base64 and decoded as utf-8 string |
+
+The `params` object contains the following fields:
+
+| Key           | Type           | Required/Default | Allowed values    | Description |
+| ------------- | -------------- | :-----------------:| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `get_scaling_factor`   | `boolean` | N<br/>`True` | `"True"` OR `"False"` | Whether the model should return "temperature" scaling factor. This factor is useful when you're planning to compare multiple cosine similarity values in an application like classification. It's essential for correct implementation of "zero-shot" type of scenarios. For usage, refer to the zero-shot classification example linked in the [Classification techniques](#classification-techniques) section. |
+
+### Request example
+
+**A simple inference requesting embedding of a single string** 
+```JSON
+{
+  "input_data": {
+    "columns": [
+      "image",
+      "text"
+    ],
+    "index":[0],
+    "data": [
+      ["", "a quick brown fox jumps over the lazy dog"]
+    ]
+  },
+  "params": {}
+}
+```
+
+**Request for embedding of an image and a string, requesting for return of the scaling factor** 
+```JSON
+{
+    "input_data": {
+        "columns": ["image", "text"],
+        "index": [0],
+        "data": [
+            [
+                "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAAXNSR0IArs4c6QAAAARnQU1BAACx\njwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAAbSURBVBhXY/gUoPS/fhfDfwaGJe///9/J8B8A\nVGwJ5VDvPeYAAAAASUVORK5CYII=\n",
+                "x-ray chest anteroposterior Pleural Effusion"
+            ]
+        ]
+    },
+    "params": {
+        "get_scaling_factor": "true"
+    }
+}
+```
+
+### Response schema
+
+Response payload is a JSON formatted string containing the following fields:
+
+| Key           | Type           |  Description |
+| ------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `image_features`       | `list[list[float]]` |  If requested, list of vectors, one per each submitted image. |
+| `text_features`   | `list[list[float]]` |  If requested, list of vectors, one per each submitted text string. |
+| `scaling_factor`   | `float` |  If requested, the scaling factor |
+
+### Response example
+**A simple inference requesting embedding of a single string** 
+```JSON
+{
+  "image_features": [[0.029661938548088074, -0.027228673920035362, ... , -0.0328846238553524]],
+  "text_features": [[0.0028937323950231075, 0.004354152828454971, -0.0227945726364851, ..., 0.002080598147585988]],
+  "scaling_factor": 4.516357
+}
+```
+
+### Other implementation considerations
+The maximum number of tokens processed in the input string is 77. Anything past 77 tokens would be cut off before being passed to the model. The model is using a Contrastive Language-Image Pre-Training (CLIP) tokenizer which uses about three Latin characters per token.
+
+The submitted text is embedded into the same latent space as the image. As a result, strings describing medical images of certain body parts obtained with certain imaging modalities are embedded close to such images. Also, when building systems on top of a MedImageInsight model, you should make sure that all your embedding strings are consistent with one another (word order and punctuation). For best results with base model, strings should follow the pattern `<image modality> <anatomy> <exam parameters> <condition/pathology>.`, for example: `x-ray chest anteroposterior Atelectasis.`. 
+
+If you're fine-tuning the model, you can change these parameters to better suit your application needs.
+
+### Supported image formats
+The deployed model API supports images encoded in PNG format. 
+
+When the model receives the images, it does preprocessing that involves compressing and resizing the images to `512x512` pixels.
+
+The preferred compression format is lossless PNG, containing either an 8-bit monochromatic or RGB image. For optimization purposes, you can perform resizing on the client side to reduce network traffic.
+
+## Learn more from samples
+MedImageInsight is a versatile model that can be applied to a wide range of tasks and imaging modalities. For more specific examples of solving various tasks with MedImageInsight, see the following interactive Python notebooks. 
+
+#### Getting started
+* [Deploying and Using MedImageInsight](https://aka.ms/healthcare-ai-examples-mi2-deploy): Learn how to deploy the MedImageInsight model programmatically and issue an API call to it.
+
+#### Classification techniques
+* [Building a Zero-Shot Classifier](https://aka.ms/healthcare-ai-examples-mi2-zero-shot): Discover how to use MedImageInsight to create a classifier without the need for training or large amount of labeled ground truth data.
+
+* [Enhancing Classification with Adapter Networks](https://aka.ms/healthcare-ai-examples-mi2-adapter): Improve classification performance by building a small adapter network on top of MedImageInsight.
+
+#### Advanced applications
+
+* [Inferring MRI Acquisition Parameters from Pixel Data](https://aka.ms/healthcare-ai-examples-mi2-exam-parameter): Understand how to extract MRI exam acquisition parameters directly from imaging data.
+
+* [Scalable MedImageInsight Endpoint Usage](https://aka.ms/healthcare-ai-examples-mi2-advanced-call): Learn how to generate embeddings of medical images at scale using the MedImageInsight API while handling potential network issues gracefully.
+
+## Related content
+
+* [MedImageParse for medical image segmentation](./deploy-medimageparse.md)
+* [CXRReportGen for grounded report generation](./deploy-cxrreportgen.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "MedImageInsight 医療 AI モデルのデプロイと使用方法"
}
```

### Explanation
この修正では、「MedImageInsight 医療 AI モデルのデプロイと使用方法」に関する記事が新たに追加されました。この文書では、MedImageInsightモデルをAzure AI Studioでデプロイし、リアルタイム推論のためのオンラインエンドポイントを作成する手順が示されています。

記事の内容には、モデルのデプロイ方法、APIを使用した基本的な呼び出し方、必要な前提条件、要求および応答のスキーマが含まれています。MedImageInsightモデルは、X線、CT、MRI、臨床写真などの多様な医療画像を処理できます。また、同モデルは、画像検索や分類、ファインチューニングタスクにおいて最先端のパフォーマンスを達成することが確認されています。

特に、モデルの利用方法に加えて、実装の考慮点や、サポートされる画像フォーマットについても触れられています。また、さまざまな用途に対する具体的な例や、デプロイメントの流れが詳細に説明されており、ユーザーがMedImageInsightを効果的に活用できるようサポートしています。大きな変更点としては、242行にもわたる詳細なドキュメントが提供されています。

## articles/ai-studio/how-to/healthcare-ai/deploy-medimageparse.md{#item-611e84}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,214 @@
+---
+title: How to deploy and use MedImageParse healthcare AI model with AI Studio
+titleSuffix: Azure AI Studio
+description: Learn how to use MedImageParse Healthcare AI Model with Azure AI Studio.
+ms.service: azure-ai-studio
+manager: scottpolly
+ms.topic: how-to
+ms.date: 10/20/2024
+ms.reviewer: itarapov
+reviewer: ivantarapov
+ms.author: mopeakande
+author: msakande
+#Customer intent: As a Data Scientist I want to learn how to use the MedImageParse healthcare AI model to segment medical images.
+
+---
+
+# How to use MedImageParse healthcare AI model for segmentation of medical images
+
+[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+
+[!INCLUDE [health-ai-models-meddev-disclaimer](../../includes/health-ai-models-meddev-disclaimer.md)]
+
+In this article, you learn how to deploy MedImageParse as an online endpoint for real-time inference and issue a basic call to the API. The steps you take are:
+
+* Deploy the model to a self-hosted managed compute.
+* Grant permissions to the endpoint.
+* Send test data to the model, receive, and interpret results.
+
+
+## MedImageParse - prompt-based segmentation of medical images
+Biomedical image analysis is crucial for discovery in fields like cell biology, pathology, and radiology. Traditionally, tasks such as segmentation, detection, and recognition of relevant objects are addressed separately, which can limit the overall effectiveness of image analysis. However, MedImageParse unifies these tasks through image parsing, by jointly conducting segmentation, detection, and recognition across numerous object types and imaging modalities. By applying the interdependencies among these subtasks—such as the semantic labels of segmented objects—the model enhances accuracy and enables novel applications. For example, it allows users to segment all relevant objects in an image, by using a simple text prompt. This approach eliminates the need to manually specify bounding boxes for each object.  
+
+The following image shows the conceptual architecture of the MedImageParse model where an image embedding model is augmented with a task adaptation layer to produce segmentation masks and textual descriptions.
+
+:::image type="content" source="../../media/how-to/healthcare-ai/medimageparse-flow.gif" alt-text="Animation of data flow through MedImageParse model showing image coming through the model paired with a task adaptor and turning into a set of segmentation masks.":::
+
+Remarkably, the segmentation masks and textual descriptions were achieved by using only standard segmentation datasets, augmented by natural-language labels, or descriptions harmonized with established biomedical object ontologies. This approach not only improved individual task performance but also offered an all-in-one tool for biomedical image analysis, paving the way for more efficient and accurate image-based biomedical discovery.
+
+## Prerequisites
+
+To use MedImageParse model with Azure AI Studio or Azure Machine Learning studio, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to a self-hosted managed compute**
+
+MedImageParse model can be deployed to our self-hosted managed inference solution, which allows you to customize and control all the details about how the model is served. You can deploy the model through the model catalog UI or programmatically. 
+
+To __deploy the model through the UI__:
+
+1. Go to the [model card in the catalog](https://aka.ms/medimageparsemodelcard). 
+1. On the model's overview page, select __Deploy__. 
+1. If given the option to choose between serverless API deployment and deployment using a managed compute, select **Managed Compute**.
+1. Fill out the details in the deployment window.
+
+    > [!NOTE]
+    > For deployment to a self-hosted managed compute, you must have enough quota in your subscription. If you don't have enough quota available, you can use our temporary quota access by selecting the option **I want to use shared quota and I acknowledge that this endpoint will be deleted in 168 hours.**
+1. Select __Deploy__.
+
+To __deploy the model programmatically__, see [How to deploy and inference a managed compute deployment with code](../deploy-models-managed.md).
+
+## Work with a segmentation model
+
+In this section, you consume the model and make basic calls to it.
+
+### Use REST API to consume the model
+
+Consume the MedImageParse segmentation model as a REST API, using simple GET requests or by creating a client as follows:
+
+```python
+from azure.ai.ml import MLClient
+from azure.identity import DeviceCodeCredential
+
+credential = DefaultAzureCredential()
+
+ml_client_workspace = MLClient.from_config(credential)
+```
+
+In the deployment configuration, you get to choose authentication method. This example uses Azure Machine Learning token-based authentication. For more authentication options, see the [corresponding documentation page](../../../machine-learning/how-to-setup-authentication.md). Also, note that the client is created from a configuration file that is created automatically for Azure Machine Learning virtual machines (VMs). Learn more on the [corresponding API documentation page](/python/api/azure-ai-ml/azure.ai.ml.mlclient#azure-ai-ml-mlclient-from-config).
+
+### Make basic calls to the model
+
+Once the model is deployed, use the following code to send data and retrieve segmentation masks.
+
+```python
+import base64
+import json
+import os
+
+sample_image_xray = os.path.join(image_path)
+
+def read_image(image_path):
+    with open(image_path, "rb") as f:
+        return f.read()
+
+sample_image =  "sample_image.png"
+data = {
+    "input_data": {
+        "columns": [ "image", "text" ],
+        "index": [ 0 ],
+        "data": [
+            [
+                base64.encodebytes(read_image(sample_image)).decode("utf-8"),
+                "neoplastic cells in breast pathology & inflammatory cells"
+            ]
+        ]
+    }
+}
+data_json = json.dumps(data)
+
+# Create request json
+request_file_name = "sample_request_data.json"
+with open(request_file_name, "w") as request_file:
+    json.dump(data, request_file)
+
+response = ml_client_workspace.online_endpoints.invoke(
+    endpoint_name=endpoint_name,
+    deployment_name=deployment_name,
+    request_file=request_file_name,
+)
+```
+
+## Use MedImageParse REST API
+MedImageParse model assumes a simple single-turn interaction where one request produces one response. 
+
+### Request schema
+
+Request payload is a JSON formatted string containing the following parameters:
+
+| Key           | Type           | Required/Default | Description |
+| ------------- | -------------- | :-----------------:| ----------------- |
+| `input_data`       | `[object]`       | Y    | An object containing the input data payload |
+
+The `input_data` object contains the following fields:
+
+| Key           | Type           | Required/Default | Allowed values    | Description |
+| ------------- | -------------- | :-----------------:| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `columns`       | `list[string]`       | Y    |  `"image"`, `"text"` | An object containing the strings mapping data to inputs passed to the model.|
+| `index`   | `integer` | Y | 0 - 256 | Count of inputs passed to the model. You're limited by how much data can be passed in a single POST request, which depends on the size of your images. Therefore, it's reasonable to keep this number in the dozens. |
+| `data`   | `list[list[string]]` | Y | "" | The list contains the items passed to the model which is defined by the index parameter. Each item is a list of two strings. The order is defined by the `columns` parameter. The `text` string contains the prompt text. The `image` string is the image bytes encoded using base64 and decoded as utf-8 string. <br/>**NOTE**: The image should be resized to `1024x1024` pixels before submitting to the model, preserving the aspect ratio. Empty space should be padded with black pixels. See the [Generating Segmentation for a Variety of Imaging Modalities](https://aka.ms/healthcare-ai-examples-mip-examples) sample notebook for an example of resizing and padding code.<br/><br/> The input text is a string containing multiple sentences separated by the special character `&`. For example: `tumor core & enhancing tumor & non-enhancing tumor`. In this case, there are three sentences, so the output consists of three images with segmentation masks. |
+
+### Request example
+
+**Requesting segmentation of all cells in a pathology image** 
+```JSON
+{
+  "input_data": {
+    "columns": [
+      "image",
+      "text"
+    ],
+    "index":[0],
+    "data": [
+      ["iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAAAAXNSR0IArs4c6QAAAARnQU1BAACx\njwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAAbSURBVBhXY/gUoPS/fhfDfwaGJe///9/J8B8A\nVGwJ5VDvPeYAAAAASUVORK5CYII=\n",
+      "neoplastic & inflammatory cells "]
+    ]
+  }
+}
+```
+
+### Response schema
+
+Response payload is a list of JSON-formatted strings, each corresponding to a submitted image. Each string contains a `segmentation_object` object.
+
+`segmentation_object` contains the following fields:
+
+| Key           | Type           |  Description |
+| ------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `image_features`       | `segmentation_mask` | An object representing the segmentation masks for a given image |
+| `text_features`       | `list[string]` |  List of strings, one per each submitted text string, classifying the segmentation masks into one of 16 biomedical segmentation categories each: `liver`, `lung`, `kidney`, `pancreas`, `heart anatomies`, `brain anatomies`, `eye anatomies`, `vessel`, `other organ`, `tumor`, `infection`, `other lesion`, `fluid disturbance`, `other abnormality`, `histology structure`, `other` |
+
+`segmentation_mask` contains the following fields:
+
+| Key           | Type           |  Description |
+| ------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
+| `data`       | `string` | A base64-encoded NumPy array containing the one-hot encoded segmentation mask. There could be multiple instances of objects in the returned array. Decode and use `np.frombuffer` to deserialize. The array contains a three-dimensional matrix. The array's size is `1024x1024` (matching the input image dimensions), with the third dimension representing the number of input sentences provided. See the provided [sample notebooks](#learn-more-from-samples) for decoding and usage examples. |
+| `shape`       | `list[int]` | A list representing the shape of the array (typically `[NUM_PROMPTS, 1024, 1024]`) |
+| `dtype`       | `string` | An instance of the [NumPy dtype class](https://numpy.org/doc/stable/reference/arrays.dtypes.html) serialized to a string. Describes the data packing in the data array. |
+
+### Response example
+**A simple inference requesting segmentation of two objects** 
+```JSON
+[
+  {
+    "image_features": "{ 
+    'data': '4oCwUE5HDQoa...',
+    'shape': [2, 1024, 1024], 
+    'dtype': 'uint8'}",
+    "text_features": ['liver', 'pancreas']
+  }
+]
+```
+
+### Supported image formats
+
+The deployed model API supports images encoded in PNG format. For optimal results, we recommend using uncompressed/lossless PNGs with RGB images.
+
+As described in the API specification, the model only accepts images in the resolution of `1024x1024`pixels. Images need to be resized and padded (in the case of non-square aspect ratio).
+
+See the [Generating Segmentation for a Variety of Imaging Modalities](https://aka.ms/healthcare-ai-examples-mip-examples) notebook for techniques and sample code useful for submitting images of various sizes stored using various biomedical imaging formats.
+
+## Learn more from samples
+MedImageParse is a versatile model that can be applied to a wide range of tasks and imaging modalities. For more examples see the following interactive Python Notebooks: 
+
+#### Getting started
+* [Deploying and Using MedImageParse](https://aka.ms/healthcare-ai-examples-mip-deploy): Learn how to deploy the MedImageParse model and integrate it into your workflow.
+
+#### Advanced inferencing techniques and samples
+* [Generating Segmentation for a Variety of Imaging Modalities](https://aka.ms/healthcare-ai-examples-mip-examples): Understand how to use MedImageParse to segment a wide variety of different medical images and learn some prompting techniques. 
+
+## Related content
+
+* [CXRReportGen for grounded report generation](deploy-cxrreportgen.md)
+* [MedImageInsight for grounded report generation](deploy-medimageinsight.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "MedImageParse 医療 AI モデルのデプロイと使用方法"
}
```

### Explanation
この修正には、MedImageParse 医療 AI モデルのデプロイと使用方法に関する新しい記事が追加されました。この文書では、MedImageParseモデルをリアルタイム推論用のオンラインエンドポイントとしてデプロイし、APIへの基本的な呼び出しを行う手順が説明されています。

記事の主な内容は、モデルのデプロイ方法、必要な前提条件、モデルとAPIの使用法、そして要求および応答のスキーマに関する詳細です。MedImageParseモデルは、医療画像のセグメンテーションを行うためのもので、特に生物医学画像分析において重要な役割を果たします。このモデルは、セグメンテーション、検出、認識を統一的に行い、ユーザーがテキストプロンプトを使用して所望の対象をセグメント化できるようにします。

記事には、具体的なコード例やリクエスト・レスポンスのスキーマが盛り込まれており、ユーザーがスムーズにモデルを使用できるように手助けしています。また、214行の詳細なドキュメントが提供され、図やサンプルノートブックへのリンクも含まれているため、実際の使用における指針が与えられています。

## articles/ai-studio/how-to/healthcare-ai/healthcare-ai-models.md{#item-12fcfc}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,54 @@
+---
+title: Foundational AI models for healthcare in AI Studio
+titleSuffix: Azure AI Studio
+description: Learn about AI models that are applicable to the health and life science industry.
+ms.service: azure-ai-studio
+manager: scottpolly
+ms.topic: concept-article
+ms.date: 10/20/2024
+ms.reviewer: itarapov
+reviewer: ivantarapov
+ms.author: mopeakande
+author: msakande
+
+#Customer intent: As a Data Scientist I want to learn what offerings are available within Health and Life Sciences AI Model offerings so that I can use them as the basis for my own AI solutions
+---
+
+# Foundational AI models for healthcare
+
+[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+
+[!INCLUDE [health-ai-models-meddev-disclaimer](../../includes/health-ai-models-meddev-disclaimer.md)]
+
+In this article, you learn about Microsoft's catalog of foundational multimodal healthcare AI models. The models were developed in collaboration with Microsoft Research, strategic partners, and leading healthcare institutions for healthcare organizations. Healthcare organizations can use the models to rapidly build and deploy AI solutions tailored to their specific needs, while minimizing the extensive compute and data requirements typically associated with building multimodal models from scratch. The intention isn't for these models to serve as standalone products; rather, they're designed for developers to use as a foundation to build upon. With these healthcare AI models, professionals have the tools they need to harness the full potential of AI to enhance biomedical research, clinical workflows, and ultimately care delivery.
+
+The healthcare industry is undergoing a revolutionary transformation driven by the power of artificial intelligence (AI). While existing large language models like GPT-4 show tremendous promise for clinical text-based tasks and general-purpose multimodal reasoning, they struggle to understand non-text multimodal healthcare data such as medical imaging—radiology, pathology, ophthalmology—and other specialized medical text like longitudinal electronic medical records. They also find it challenging to process non-text modalities like signal data, genomic data, and protein data, much of which isn't publicly available.
+
+:::image type="content" source="../../media/how-to/healthcare-ai/connect-modalities.gif" alt-text="Models that reason about various modalities come together to support discover, development and delivery of healthcare":::
+
+The [Azure AI model catalog](../model-catalog-overview.md) provides foundational healthcare AI models that facilitate AI-powered analysis of various medical data types and expand well beyond medical text comprehension into the multimodal reasoning about medical data. These AI models can integrate and analyze data from diverse sources that come in various modalities, such as medical imaging, genomics, clinical records, and other structured and unstructured data sources. The models also span several healthcare fields like dermatology, ophthalmology, radiology, and pathology. 
+
+The healthcare AI AI model pages refer to both Azure AI Studio and Azure Machine Learning studio. To learn more about differences between these two products and which one to use, see [AI Studio or Azure Machine Learning: Which experience should I choose?](/ai/ai-studio-experiences-overview).
+
+## Microsoft first-party models
+
+The following models are Microsoft's first party foundational multimodal healthcare AI models.
+
+#### [MedImageInsight](./deploy-medimageinsight.md)
+This model is an embedding model that enables sophisticated image analysis, including classification and similarity search in medical imaging. Researchers can use the model embeddings directly or build adapters for their specific tasks, thereby streamlining workflows in radiology, pathology, ophthalmology, dermatology, and other modalities. For example, the model can be used to  build tools that automatically route imaging scans to specialists or flag potential abnormalities for further review. These actions can improve efficiency and patient outcomes. Furthermore, the model can be used for Responsible AI (RAI) safeguards such as out-of-distribution (OOD) detection and drift monitoring, to maintain stability and reliability of AI tools and data pipelines in dynamic medical imaging environments.  
+
+#### [CXRReportGen](./deploy-cxrreportgen.md)
+Chest X-rays are the most common radiology procedure globally. They're crucial because they help doctors diagnose a wide range of conditions—from lung infections to heart problems. These images are often the first step in detecting health issues that affect millions of people. This multimodal AI model incorporates current and prior images along with key patient information to generate detailed, structured reports from chest X-rays. The reports highlight AI-generated findings directly on the images to align with human-in-the-loop workflows. This capability accelerates turnaround times while enhancing the diagnostic precision of radiologists. 
+
+#### [MedImageParse](./deploy-medimageparse.md)
+This model is designed for precise image segmentation, and it covers various imaging modalities, including X-Rays, CT scans, MRIs, ultrasounds, dermatology images, and pathology slides. The model can be fine-tuned for specific applications, such as tumor segmentation or organ delineation, allowing developers to build tools on top of this model that leverage AI for highly sophisticated medical image analysis.
+
+## Partner models
+
+The Azure AI model catalog also provides a curated collection of healthcare models from Microsoft partners with capabilities such as digital pathology slide analysis, biomedical research, and medical knowledge sharing. These models come from partners that include Paige.AI and Providence Healthcare. For a complete list of models, refer to the [model catalog page](https://aka.ms/healthcaremodelstudio). 
+
+## Related content
+
+- [Model catalog and collections in Azure AI Studio](../model-catalog-overview.md)
+- [How to deploy and inference a managed compute deployment with code](../deploy-models-managed.md)
+- [Overview: Deploy models, flows, and web apps with Azure AI Studio](../../concepts/deployments-overview.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "AI Studio における医療のための基盤 AI モデル"
}
```

### Explanation
この変更により、「AI Studio における医療のための基盤 AI モデル」に関する新しい記事が追加されました。この文書では、健康およびライフサイエンス産業に適用可能な AI モデルが紹介されています。Microsoft が開発したこれらのモデルは、医療機関が特定のニーズに合わせた AI ソリューションを迅速に構築しデプロイできるようにすることを目的としています。

記事では、Microsoft の基盤となるマルチモーダル医療 AI モデルのカタログについて説明があり、医療機関や研究者がどのようにこれらのモデルを活用できるかが示されています。また、特に非テキストの医療データに対する理解や処理の難しさについても触れられています。

新しいモデルの具体例として、MedImageInsight、CXRReportGen、およびMedImageParseが紹介されており、それぞれの機能や使用例が説明されています。さらに、Microsoft パートナーによる医療モデルのコレクションや、AI Studio と Azure Machine Learning の違いについてのリンクも含まれています。全体として、この文書は医療における AI モデルの基礎と応用を広くカバーしています。54行の詳細な説明が追加されたことで、ユーザーは健康関連の AI モデルの利用方法を理解しやすくなります。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -73,6 +73,7 @@ Llama family models | Llama-2-7b <br> Llama-2-7b-chat <br> Llama-2-13b <br> Llam
 Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Mistral-NeMo
 Cohere family models | Not available | Cohere-command-r-plus-08-2024 <br> Cohere-command-r-08-2024 <br> Cohere-command-r-plus <br> Cohere-command-r <br> Cohere-embed-v3-english <br> Cohere-embed-v3-multilingual <br> Cohere-rerank-v3-english <br> Cohere-rerank-v3-multilingual
 JAIS | Not available | jais-30b-chat
+Healthcare AI Family Models | MedImageInsight <br> CxrReportGen <br> MedImageParse | Not Available
 Phi-3 family models | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> Phi-3-vision-128k-Instruct <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct | Phi-3-mini-4k-Instruct <br> Phi-3-mini-128k-Instruct <br> Phi-3-small-8k-Instruct <br> Phi-3-small-128k-Instruct <br> Phi-3-medium-4k-instruct <br> Phi-3-medium-128k-instruct <br> <br> Phi-3.5-mini-Instruct <br> Phi-3.5-vision-Instruct <br> Phi-3.5-MoE-Instruct
 Nixtla | Not available | TimeGEN-1
 Other models | Available | Not available
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "医療 AI モデルの追加"
}
```

### Explanation
この変更では、「モデルカタログの概要」ドキュメントに医療に関連した AI モデルセクションが追加されました。具体的には、「Healthcare AI Family Models」として、以下のモデルがリストアップされています。

- MedImageInsight
- CxrReportGen
- MedImageParse

これらのモデルは、健康管理や医療分野に応じた AI ソリューションを提供することを目的としており、それぞれの特性や用途に応じて利用されることが期待されています。この追加によって、医療に関する AI モデルの選択肢が明確になり、ユーザーがこれらのリソースを活用しやすくなります。全体として、1行の変更により、モデルカタログがより充実し、特定の分野におけるモデルの明示的な利用可能性が向上しました。

## articles/ai-studio/includes/health-ai-models-meddev-disclaimer.md{#item-d90d1c}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,14 @@
+---
+title: Include file
+description: Include file
+author: msakande
+ms.reviewer: itarapov
+ms.author: mopeakande
+ms.service: azure-ai-studio
+ms.topic: include
+ms.date: 10/1/2024
+ms.custom: include
+---
+
+> [!IMPORTANT]
+> Microsoft provides these models on an "as is" basis.  Microsoft makes no warranties, express or implied, guarantees, or conditions with respect to your use of the models. To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses, including direct, consequential, special, indirect, incidental, or punitive, resulting from your use of the models. Microsoft products and services (1) are not designed, intended, or made available as a medical device, and (2) are not designed or intended to be a substitute for professional medical advice, diagnosis, treatment, or judgment and should not be used to replace or substitute for professional medical advice, diagnosis, treatment, or judgment.  You are responsible for ensuring solutions comply with applicable laws and regulations.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "医療 AI モデルに関する免責事項の追加"
}
```

### Explanation
この変更では、医療 AI モデルに関する重要な免責事項が含まれる新しいファイルが追加されました。このファイルには、Microsoft が提供するモデルの使用に関する明確な注意事項が記されています。

具体的には、Microsoft は、これらのモデルを「現状のまま」提供しており、ユーザーの利用に際していかなる保証も行わないことが強調されています。加えて、Microsoft の製品やサービスは医療機器として設計されておらず、専門的な医療のアドバイスや診断、治療の代替として使用されるべきではないことが明記されています。

この免責事項は、利用者がモデルを使用する際のリスクや責任を理解するのに役立つ重要な情報を提供しており、法律や規制に準拠する責任も利用者にあることを強調しています。この追加により、ユーザーは医療 AI モデルの使用に伴う法的および倫理的な観点を考慮することができるようになります。全体で14行の内容が追加されており、文書の透明性と責任を促進しています。

## articles/ai-studio/media/how-to/healthcare-ai/connect-modalities.gif{#item-28d70d}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "接続モダリティのGIFアニメーションの追加"
}
```

### Explanation
この変更では、医療 AI に関する「接続モダリティ」を示す新しい GIF アニメーションが追加されました。このアニメーションは、ユーザーが異なるデータソースやモダリティをどのように接続するかを視覚的に理解するのに役立つものです。

GIF アニメーションの追加により、テキストだけでは伝えきれない情報が補完され、学習や操作手順をより直感的に理解できるようになります。このビジュアルコンテンツは、特に医療や技術分野において、複雑なプロセスや相互作用を視覚的に説明するために非常に有効です。

全体として、この追加によって、ユーザーが医療 AI ソリューションを効果的に利用し、異なる技術やデータを統合する方法を理解しやすくするための支援が強化されました。

## articles/ai-studio/media/how-to/healthcare-ai/healthcare-embedding-capabilities.gif{#item-8d9d5b}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "医療埋め込み機能のGIFアニメーションの追加"
}
```

### Explanation
この変更では、医療 AI の「埋め込み機能」に関する新しい GIF アニメーションが追加されました。このアニメーションは、医療データの埋め込み処理がどのように行われるかを視覚的に示すもので、ユーザーがその機能をより良く理解できるように設計されています。

医療 AI の埋め込みリソースは、データを効果的に扱うための基盤として重要であり、このビジュアルコンテンツは、複雑なプロセスや技術的な側面を簡単に把握するために役立ちます。具体的には、埋め込み機能がどのようにデータを処理し、どのような利点があるかを直感的に示すことで、ユーザーの理解を促進します。

この新しい GIF コンテンツの追加により、医療 AI ソリューションの活用がさらに促進されることが期待され、ユーザーが技術の幅広い応用を把握しやすくなります。

## articles/ai-studio/media/how-to/healthcare-ai/healthcare-reportgen.gif{#item-4a153d}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "医療レポート生成のGIFアニメーションの追加"
}
```

### Explanation
この変更では、医療 AI に関連する「レポート生成」プロセスを示す新しい GIF アニメーションが追加されました。このアニメーションは、医療レポートがどのように自動生成されるかを視覚的に表現し、ユーザーがこのプロセスをより深く理解できるように設計されています。

レポート生成機能は、医療データの分析と結果の整理において重要な役割を果たします。この GIF アニメーションは、複雑な生成手順や出力フォーマットを直感的に把握できるようにし、ユーザーが技術を効果的に活用できるようにサポートします。具体的には、視覚的な説明により、操作の手順や結果の解釈が容易になります。

この追加により、医療 AI ソリューションが提供する機能の理解が促進され、ユーザーがレポート生成の価値をさらに感じることが期待されます。

## articles/ai-studio/media/how-to/healthcare-ai/medimageparse-flow.gif{#item-59cd1a}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "医療画像解析フローのGIFアニメーションの追加"
}
```

### Explanation
この変更では、医療画像解析の流れを表現する新しい GIF アニメーションが追加されました。このアニメーションは、医療画像がどのように解析され、処理されるのかを視覚的に示すもので、ユーザーがそのプロセスを理解しやすくすることを目的としています。

医療画像解析は、診断や治療計画において極めて重要な役割を果たしており、この GIF により、プロセスの各ステップを直感的に把握できるようになります。具体的には、画像の取得、処理、分析結果の表示といった流れが示され、ユーザーが各段階で期待される結果や操作をしっかりと理解できるようにサポートします。

この新しいコンテンツの追加により、医療 AI 分野での画像解析機能に対する理解が深化し、ユーザーがその技術を活用しやすくなることが期待されます。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -129,6 +129,16 @@ items:
         href: how-to/deploy-models-openai.md
       - name: Fine-tune Azure OpenAI models
         href: ../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context
+    - name: Healthcare AI models
+      items:
+        - name: Foundational AI models for healthcare
+          href: how-to/healthcare-ai/healthcare-ai-models.md
+        - name: MedImageInsight - embedding model
+          href: how-to/healthcare-ai/deploy-medimageinsight.md
+        - name: CXRReportGen - text generation model
+          href: how-to/healthcare-ai/deploy-cxrreportgen.md
+        - name: MedImageParse - prompted segmentation model
+          href: how-to/healthcare-ai/deploy-medimageparse.md
     - name: Phi-3 family models
       items:
         - name: Phi-3 family chat models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "医療AIモデルに関する新しい項目の追加"
}
```

### Explanation
この変更では、AI スタジオの目次ファイル (toc.yml) に医療 AI モデルに関連する新しい項目が追加されました。具体的には、医療 AI モデルに関する情報がセクションとして整理され、いくつかのサブ項目が設けられています。

追加された項目には、以下の内容が含まれています：

- 医療における基盤となる AI モデル
- MedImageInsight（埋め込みモデル）
- CXRReportGen（テキスト生成モデル）
- MedImageParse（プロンプトを使用した分割モデル）

これにより、医療 AI に関連するリソースがより明確に分類され、ユーザーは特定のモデルやそのデプロイ方法について容易にアクセスできるようになります。この追加は、ユーザーが医療関連の AI モデルを効果的に理解し、利用できるようサポートすることを目的としています。


