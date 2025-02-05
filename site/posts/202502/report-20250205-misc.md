---
date: '2025-02-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:89e0bdf...MicrosoftDocs:d46a0e8
summary: この差分では、「TensorFlow」の表記の修正やプライベートエンドポイントの説明の詳細化など、文書の一貫性とユーザビリティ向上を目的としたいくつかの改良が行われました。デプロイ手順の改善や画像の更新も行われ、視覚的なサポートが強化されていますが、一部の画像が削除され、ユーザーに影響を与える可能性があります。全体として、この更新はユーザーが提供された資料をより効率的かつ正確に利用できるよう、ドキュメントの精度を向上させることを目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:89e0bdf...MicrosoftDocs:d46a0e8){target="_blank"}

# ハイライト

この差分では、以下の主要な変更が行われています：
- 「TensorFlow」の表記に関する修正が行われ、文書の一貫性と正確性が向上しています。
- プライベートエンドポイントに関する説明が詳しくされ、設定の文脈が明確化されています。
- デプロイ手順の一部が改善され、手順の流れや表現が簡潔に整理されています。
- 複数のデプロイ関連画像の更新がなされ、視覚的なサポートが強化されています。
- 出力接続に関連する画像が削除され、文書構成に影響を与えています。

## 新機能

新しい機能の追加はありませんが、既存の機能がより明確に、または視覚的に改善されています。

## 破壊的変更

出力接続の画像「deploy-advanced-outputs-connections.png」の削除が破壊的変更として分類されます。この変更により、ユーザーは出力接続に関する視覚資料を参考にすることができなくなります。

## その他の更新

- 「TensorFlow」の表記が修正され、統一されています。
- プライベートエンドポイントの説明が詳細化されました。
- デプロイの手順と指示がより明確に、簡潔に表現されています。
- 「deploy-advanced-deployment.png」「deploy-advanced-endpoint.png」「deploy-basic-settings.png」などの画像が新しいバージョンに更新されています。

# 洞察

この差分では、ドキュメントの精度とユーザビリティを向上させるための一連の小規模な更新が行われています。特に、名称の統一や指示の明文化により、ユーザーが提供された資料を効率的かつ正確に利用できる環境が整備されています。

まず、「TensorFlow」の表記に関する修正は知識を一貫して正しく伝えるために重要です。ブランド名やツールの名称は正確であることが求められ、ドキュメント全体の信頼性に寄与します。加えて、プライベートエンドポイントのセクションでは、特定のロール割り当てに関する説明が詳細化され、誤解の余地が減りました。これにより、ユーザーが必要な設定環境を理解し設置することが容易になります。

デプロイ手順の部分では、ユーザーが手順を効率的に実行できるよう、流れを分かりやすく簡略化しています。特に、手順のページナビゲーションの変更やロール割り当てのタイミングが明文化されたことで、誤った設定を避ける助けとなります。

画像更新に関しては、視覚的なサポートの刷新が試みられましたが、出力接続に関する画像の削除については、関連する文書の補足情報が失われる可能性があります。ユーザーが適切にデプロイ情報を把握できるように、将来的に代替ビジュアルまたは詳細な文章による補完が望まれます。このような修正は、Azure AI Platformを使用する際の読者の理解を深め、エクスペリエンスを向上させるものとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [configure-managed-network.md](#item-dc9c50) | minor update | TensorFlowの表記の修正 | modified | 1 | 1 | 2 | 
| [configure-private-link.md](#item-bbf93d) | minor update | プライベートエンドポイントに関する説明の明確化 | modified | 1 | 1 | 2 | 
| [flow-deploy.md](#item-e7fc64) | minor update | デプロイ手順の一部変更と表現の改善 | modified | 5 | 7 | 12 | 
| [deploy-advanced-deployment.png](#item-abbf9c) | minor update | デプロイの画像更新 | modified | 0 | 0 | 0 | 
| [deploy-advanced-endpoint.png](#item-bb561c) | minor update | エンドポイントの画像更新 | modified | 0 | 0 | 0 | 
| [deploy-advanced-outputs-connections.png](#item-649e16) | breaking change | 出力接続の画像削除 | removed | 0 | 0 | 0 | 
| [deploy-basic-settings.png](#item-e37e4d) | minor update | 基本設定の画像更新 | modified | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-studio/how-to/configure-managed-network.md{#item-dc9c50}

<details>
<summary>Diff</summary>
````diff
@@ -768,7 +768,7 @@ To allow installation of __Python packages for training and deployment__, add ou
 | `*.anaconda.org` | Used to get repo data. |
 | `pypi.org` | Used to list dependencies from the default index, if any, and the index isn't overwritten by user settings. If the index is overwritten, you must also allow `*.pythonhosted.org`. |
 | `pytorch.org`<br>`*.pytorch.org` | Used by some examples based on PyTorch. |
-| `*.tensorflow.org` | Used by some examples based on Tensorflow. |
+| `*.tensorflow.org` | Used by some examples based on TensorFlow. |
 
 ### Scenario: Use Visual Studio Code
 Visual Studio Code relies on specific hosts and ports to establish a remote connection.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TensorFlowの表記の修正"
}
```

### Explanation
この修正では、Markdownファイルの中のテキストにおける「Tensorflow」という表記が「TensorFlow」に修正されました。この変更は、文書の一貫性を持たせ、正しい名称を使用するためのものです。具体的には、サポートされているホストのリストにあるTensorFlowに関する記述が更新されました。これにより、読者に提供される情報の信頼性が向上します。修正内容は、全体で2つの変更があり、1行追加され、1行削除されています。詳細については、修正されたファイルの[こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/d46a0e8799ee74d06db332c28676cd57dceb0f9b/articles%2Fai-studio%2Fhow-to%2Fconfigure-managed-network.md)をご覧ください。

## articles/ai-studio/how-to/configure-private-link.md{#item-bbf93d}

<details>
<summary>Diff</summary>
````diff
@@ -272,7 +272,7 @@ If your storage account is private (uses a private endpoint to communicate with
     | `Storage Blob Data Contributor` | Azure AI Search | Storage Account | Read blob and write knowledge store | [Search doc](/azure/search/search-howto-managed-identities-data-sources). |
 
     > [!TIP]
-    > Your storage account may have multiple private endpoints. You need to assign the `Reader` role to each private endpoint.
+    > Your storage account may have multiple private endpoints. You need to assign the `Reader` role to each private endpoint for your Azure AI Foundry project managed identity.
 
 1. Assign the `Storage Blob Data reader` role to your developers. This role allows them to read data from the storage account.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートエンドポイントに関する説明の明確化"
}
```

### Explanation
この修正では、プライベートエンドポイントに関連する説明が明確化されました。具体的には、ユーザーがストレージアカウントに複数のプライベートエンドポイントを持つ場合、その各プライベートエンドポイントに対して「Reader」ロールを割り当てる必要があることが説明されています。従来の記述では単に「Reader」ロールを割り当てる必要があるとだけ記載されていましたが、今回の変更により、「Azure AI FoundryプロジェクトのマネージドIDに対して」という具体的な文脈が追加されました。これにより、読者は設定が必要なロールの文脈をより理解しやすくなります。変更内容は、全体で2つの変更があり、1行追加され、1行削除されています。詳細については、修正されたファイルの[こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/d46a0e8799ee74d06db332c28676cd57dceb0f9b/articles%2Fai-studio%2Fhow-to%2Fconfigure-private-link.md)をご覧ください。

## articles/ai-studio/how-to/flow-deploy.md{#item-e7fc64}

<details>
<summary>Diff</summary>
````diff
@@ -158,8 +158,6 @@ You can also specify the connections used by the endpoint when it performs infer
 
 Once you configured and reviewed all the steps above, you can select **Review + Create** to finish the creation.
 
-:::image type="content" source="../media/prompt-flow/how-to-deploy-for-real-time-inference/deploy-advanced-outputs-connections.png" alt-text="Screenshot of the advanced output and connections settings." lightbox = "../media/prompt-flow/how-to-deploy-for-real-time-inference/deploy-advanced-outputs-connections.png":::
-
 > [!NOTE]
 > Expect the endpoint creation to take approximately more than 15 minutes, as it contains several stages including creating endpoint, registering model, creating deployment, etc.
 >
@@ -174,7 +172,7 @@ If you enable this, tracing data and system metrics during inference time (such
 > [!IMPORTANT]
 > Granting permissions (adding role assignment) is only enabled to the **Owner** of the specific Azure resources. You might need to ask your Azure subscription owner (who might be your IT admin) for help.
 >
-> It's recommended to grant roles to the **user-assigned** identity **before the deployment creation**.
+> It's recommended to grant roles to the **user-assigned** identity as soon as the endpoint creation completes.
 > It might take more than 15 minutes for the granted permission to take effect.
 
 You can grant the required permissions in Azure portal UI by following steps.
@@ -200,7 +198,7 @@ You can grant the required permissions in Azure portal UI by following steps.
        
     :::image type="content" source="../media/prompt-flow/how-to-deploy-for-real-time-inference/storage-container-registry.png" alt-text="Screenshot of the overview page with storage and container registry highlighted." lightbox = "../media/prompt-flow/how-to-deploy-for-real-time-inference/storage-container-registry.png":::
 
-    Go to the hub container registry overview page, select **Access control**, and select **Add role assignment**, and assign **ACR pull |Pull container image** to the endpoint identity.
+    Go to the hub container registry overview page, select **Access control**, and select **Add role assignment**, and assign **ACR Pull** to the endpoint identity.
 
     Go to the hub default storage overview page, select **Access control**, and select **Add role assignment**, and assign **Storage Blob Data Reader** to the endpoint identity.
 
@@ -210,7 +208,7 @@ You can grant the required permissions in Azure portal UI by following steps.
 
 There will be notifications after you finish the deploy wizard. After the endpoint and deployment are created successfully, you can select **View details** in the notification to deployment detail page.
 
-You can also directly go to the **Deployments** page from the left navigation, select the deployment, and check the status.
+You can also directly go to the **Model + endpoints** page from the left navigation, select the deployment, and check the status.
 
 ## Test the endpoint
 
@@ -246,8 +244,8 @@ If you aren't going use the endpoint after completing this tutorial, you should
 > [!NOTE]
 > The complete deletion might take approximately 20 minutes.
 
-## Next Steps
+## Next steps
 
 - Learn more about what you can do in [Azure AI Foundry](../what-is-ai-studio.md)
 - Get answers to frequently asked questions in the [Azure AI FAQ article](../faq.yml)
-- [Enable trace and collect feedback for your deployment] (./develop/trace-production-sdk.md)
+- [Enable trace and collect feedback for your deployment](./develop/trace-production-sdk.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイ手順の一部変更と表現の改善"
}
```

### Explanation
この修正では、Azure AI Studioのデプロイメント手順に関するいくつかの表現が改善され、手順が明確化されました。具体的には、エンドポイント作成後に「user-assigned」IDにロールを付与するタイミングが、「エンドポイント作成が完了したらすぐに」へと変更されました。また、ストレージとコンテナレジストリへのロール割り当てに関する指示が一部簡略化され、表記が「ACR Pull」へと修正されました。さらに、「Deployments」ページに代わって「Model + endpoints」ページに直接移動するように指示が変更されています。これらの修正により、ユーザーが必要な手順をより簡単に理解し、実行できるように情報が整理されています。全体で12の変更があり、5行追加され、7行削除されています。詳細については、修正されたファイルの[こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/d46a0e8799ee74d06db332c28676cd57dceb0f9b/articles%2Fai-studio%2Fhow-to%2Fflow-deploy.md)をご覧ください。

## articles/ai-studio/media/prompt-flow/how-to-deploy-for-real-time-inference/deploy-advanced-deployment.png{#item-abbf9c}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイの画像更新"
}
```

### Explanation
この修正では、リアルタイム推論のためのデプロイに関する画像ファイルが更新されました。具体的には、ファイル「deploy-advanced-deployment.png」に変更が加えられていますが、内容の追加や削除はありませんでした。画像が新しいバージョンに置き換えられることで、ユーザーが手順を理解するための視覚的サポートが強化されます。しかし、変更の具体的な内容や理由についての詳細は記載されていません。更新された画像は、以下のリンクからご覧いただけます：[ここをクリック](https://github.com/MicrosoftDocs/azure-ai-docs/blob/d46a0e8799ee74d06db332c28676cd57dceb0f9b/articles%2Fai-studio%2Fmedia%2Fprompt-flow%2Fhow-to-deploy-for-real-time-inference%2Fdeploy-advanced-deployment.png)。

## articles/ai-studio/media/prompt-flow/how-to-deploy-for-real-time-inference/deploy-advanced-endpoint.png{#item-bb561c}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンドポイントの画像更新"
}
```

### Explanation
この修正では、リアルタイム推論のためのデプロイに関連するエンドポイントの画像「deploy-advanced-endpoint.png」が更新されました。具体的には、画像自体に変更は加えられていないものの、ファイルが新しいバージョンに置き換えられています。この更新により、ユーザーは最新の情報に基づいたビジュアルコンテンツを参照できるようになります。詳細な変更内容は記載されていませんが、更新された画像は以下のリンクから確認できます：[ここをクリック](https://github.com/MicrosoftDocs/azure-ai-docs/blob/d46a0e8799ee74d06db332c28676cd57dceb0f9b/articles%2Fai-studio%2Fmedia%2Fprompt-flow%2Fhow-to-deploy-for-real-time-inference%2Fdeploy-advanced-endpoint.png)。

## articles/ai-studio/media/prompt-flow/how-to-deploy-for-real-time-inference/deploy-advanced-outputs-connections.png{#item-649e16}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "出力接続の画像削除"
}
```

### Explanation
この修正では、リアルタイム推論のためのデプロイに関連する「deploy-advanced-outputs-connections.png」という画像が削除されました。この変更により、ユーザーは出力接続に関する視覚的な情報を参照できなくなります。画像が削除された理由についての具体的な説明はありませんが、削除された画像は以下のリンクから確認可能でした：[ここをクリック](https://github.com/MicrosoftDocs/azure-ai-docs/blob/89e0bdf53eaaf8544c349b16aa6510eceb2ae4f9/articles%2Fai-studio%2Fmedia%2Fprompt-flow%2Fhow-to-deploy-for-real-time-inference%2Fdeploy-advanced-outputs-connections.png)。この変更は、関連する資料や説明に影響を与える可能性があります。

## articles/ai-studio/media/prompt-flow/how-to-deploy-for-real-time-inference/deploy-basic-settings.png{#item-e37e4d}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "基本設定の画像更新"
}
```

### Explanation
この修正では、リアルタイム推論のためのデプロイに関連する基本設定の画像「deploy-basic-settings.png」が更新されました。画像に具体的な変更内容はありませんが、新しいバージョンに置き換えられたことにより、最新の情報が反映されていると考えられます。ユーザーはこの更新を通じて、より正確なビジュアルコンテンツを参照できるようになっています。更新された画像は以下のリンクから確認可能です：[ここをクリック](https://github.com/MicrosoftDocs/azure-ai-docs/blob/d46a0e8799ee74d06db332c28676cd57dceb0f9b/articles%2Fai-studio%2Fmedia%2Fprompt-flow%2Fhow-to-deploy-for-real-time-inference%2Fdeploy-basic-settings.png)。


