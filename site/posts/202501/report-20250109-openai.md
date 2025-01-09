---
date: '2025-01-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:058aad5...MicrosoftDocs:6c9883f
summary: 今回のコードの更新では、主にAzure OpenAIサービスに関連するドキュメントの更新と修正が行われました。新しいAPIバージョンや機能の追加、用語の一貫性の確保が図られ、既存のコンテンツが改善されています。一部の文書は完全に削除され、内容が刷新されました。主な変更点としては、APIリリース日の変更、Microsoft
  Entra IDによるキーレス認証の導入、Azure AI Foundryポータルへの名称変更があります。これにより、ユーザー体験の向上やセキュリティの強化が実現されていますが、削除された文書に起因する不便さも懸念されます。全体として、最新の情報やツールの利用が促進され、Azureの利便性とパフォーマンスが向上しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:058aad5...MicrosoftDocs:6c9883f){target="_blank"}

<format>
# Highlights
今回のコードの更新は、主にAzure OpenAIサービスに関連するドキュメントの更新および修正です。新しいAPIバージョンや機能の追加、用語の一貫性の確保といった新機能の実装および既存のコンテンツの改善が図られています。一部の文書に対しては完全なファイル削除がなされ、内容が刷新されています。

## New features
- Azure OpenAI APIリリース日が2024年10月1日から2024年12月1日に変更され、新機能の追加がされています。
- Microsoft Entra IDを利用した、よりセキュアでシームレスなキーレス認証の導入。
- Azure AI Foundryポータルへの名称変更に伴うドキュメントの調整と、ナビゲーションが向上しました。

## Breaking changes
- 「アシスタント環境変数キー」に関する文書が削除され、設定情報が得られなくなっています。
- Azure OpenAI Studioに関連する情報の提供が全削除され、新たなリソースが必要です。
- 画像ファイル `studio-deployment-status.png` の削除により、ファインチューニングチュートリアルが影響を受けています。

## Other updates
- Azure OpenAIに関する新しいnpmパッケージが用意されることで、最新情報に基づくスムーズな開発が可能に。
- ドキュメント中の記事が時代に即したプラットフォームに合うよう更新。

# Insights
今回の更新は、Azure OpenAIサービスにおける利用者の体験を向上させるためのもので、新機能の追加や改善が大きな役割を果たしています。多くの修正は、ユーザーがよりスムーズに最新の環境で操作を続けることができるようにするために行われました。

たとえば、APIバージョンの更新は、最新の推論モデルおよび保存されたデータの扱い方がより豊富でシンプルになるための重要なステップといえます。また、Microsoft Entra IDによるキーレス認証の導入は、セキュリティの観点から非常に価値があります。これにより、従来のAPIキー認証に関する管理や懸念が軽減されます。

一方で、Breaking Changesに含まれる文書の削除は、関連情報を新たに他のドキュメントやリソースから拾う必要が出てくるため、ユーザーにとっては少し不便になる部分もあります。かつてのインターフェースや手続きに関する明確な指針が失われることで、初めてのユーザーには戸惑いが生じるかもしれません。

全体として今回の更新は、Azure OpenAIの利用を効率的にするとともに、それに伴う新しい挑戦を示唆しています。ユーザーが新しい情報やツールを利用しやすくするために、ドキュメントの鮮度や精度が向上しています。これにより、Microsoftがクラウド経由でAIサービスを拡大する一環として、Azureが提供する利便性とパフォーマンスの向上に寄与しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [api-version-deprecation.md](#item-1cad50) | minor update | APIバージョンの更新と新機能追加 | modified | 11 | 3 | 14 | 
| [provisioned-migration.md](#item-68e143) | minor update | プロビジョニング移行に関する更新 | modified | 22 | 22 | 44 | 
| [provisioned-reservation-update.md](#item-53236b) | minor update | Azure Reservationに関する注意点の更新 | modified | 1 | 1 | 2 | 
| [red-teaming.md](#item-0916c9) | minor update | レッドチーミングのテストに関する表現の更新 | modified | 1 | 1 | 2 | 
| [use-your-data.md](#item-455d6e) | minor update | Azure AI Foundryポータルへの移行 | modified | 19 | 19 | 38 | 
| [dall-e-quickstart.md](#item-fcd528) | minor update | Azure AI Foundryポータルの参照追加と表現修正 | modified | 3 | 3 | 6 | 
| [fine-tuning.md](#item-5c0e85) | minor update | Azure AI Foundryポータルへの移行 | modified | 3 | 3 | 6 | 
| [monitor-openai.md](#item-fcba4d) | minor update | Azure AI Foundryのリンク修正 | modified | 1 | 1 | 2 | 
| [on-your-data-configuration.md](#item-4875d3) | minor update | Azure AI Foundryポータルの名称変更 | modified | 11 | 11 | 22 | 
| [provisioned-get-started.md](#item-c8df1c) | minor update | Azure AI Foundryポータルへの参照を更新 | modified | 14 | 17 | 31 | 
| [risks-safety-monitor.md](#item-b2be0b) | minor update | Azure AI FoundryポータルのURLを更新 | modified | 3 | 3 | 6 | 
| [structured-outputs.md](#item-cc2557) | minor update | Pydanticバージョン更新の表現を統一 | modified | 2 | 2 | 4 | 
| [use-blocklists.md](#item-e99db7) | minor update | フィルター表現の変更 | modified | 1 | 1 | 2 | 
| [use-web-app.md](#item-802413) | minor update | 用語の統一と日付の更新 | modified | 15 | 21 | 36 | 
| [working-with-models.md](#item-7ec098) | minor update | 用語の統一と文書の明確化 | modified | 4 | 4 | 8 | 
| [api-surface.md](#item-a25fa2) | minor update | APIバージョンの更新と日付修正 | modified | 3 | 3 | 6 | 
| [latest-inference-preview.md](#item-24bf0f) | minor update | 最新の推論APIバージョンに関する内容の大幅な更新 | modified | 227 | 163 | 390 | 
| [assistants-env-var-key.md](#item-670ce2) | breaking change | 環境変数に関する文書の削除 | removed | 0 | 17 | 17 | 
| [assistants-env-var-without-key.md](#item-039e55) | breaking change | APIキーなしのアシスタント環境変数に関する文書の削除 | removed | 0 | 16 | 16 | 
| [assistants-javascript.md](#item-ad3627) | minor update | JavaScriptアシスタントに関するドキュメントの修正 | modified | 8 | 18 | 26 | 
| [assistants-python.md](#item-82d745) | minor update | Pythonアシスタントに関するドキュメントの文言修正 | modified | 1 | 1 | 2 | 
| [assistants-studio.md](#item-23d0ea) | breaking change | Azure OpenAI Studioに関するドキュメントの削除 | removed | 0 | 126 | 126 | 
| [assistants-typescript.md](#item-3195a9) | minor update | Microsoft Entra IDを用いたキーレス認証に関する文言修正 | modified | 5 | 18 | 23 | 
| [chatgpt-javascript.md](#item-cbf09f) | minor update | Azure OpenAI向けの最新のnpmパッケージ使用に関する文言修正 | modified | 13 | 6 | 19 | 
| [chatgpt-studio.md](#item-ab43f3) | minor update | Azure OpenAIサービスの機能に関する文言修正 | modified | 1 | 1 | 2 | 
| [chatgpt-typescript.md](#item-6d2f1f) | minor update | Azure OpenAI向けの最新のnpmパッケージ使用に関する文言修正 | modified | 11 | 7 | 18 | 
| [connect-your-data-studio.md](#item-c34da8) | minor update | Azure AI Foundryポータルに関する表現修正 | modified | 3 | 3 | 6 | 
| [create-resource-portal.md](#item-cb2503) | minor update | Azure AI Foundryポータルの表現を修正 | modified | 1 | 1 | 2 | 
| [dall-e-javascript.md](#item-6cffcf) | minor update | Microsoft Entra IDの要件に関する追加 | modified | 8 | 4 | 12 | 
| [dall-e-studio.md](#item-439729) | minor update | Azure AI FoundryのURL修正 | modified | 1 | 1 | 2 | 
| [dall-e-typescript.md](#item-57b205) | minor update | Microsoft Entra IDの要件に関する追加 | modified | 8 | 5 | 13 | 
| [deploy-web-app.md](#item-d61fc3) | minor update | デプロイメントに関する表現の修正 | modified | 2 | 3 | 5 | 
| [env-var-without-key.md](#item-56a8e2) | breaking change | 環境変数に関するドキュメントの削除 | removed | 0 | 15 | 15 | 
| [fine-tuning-openai-in-ai-studio.md](#item-723c8d) | minor update | Azure AI StudioからAzure AI Foundryへの用語変更 | modified | 1 | 1 | 2 | 
| [fine-tuning-python.md](#item-976f58) | minor update | 表現の変更による文の調整 | modified | 2 | 2 | 4 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | Azure AI Foundryにおける用語の修正 | modified | 9 | 9 | 18 | 
| [gpt-v-javascript.md](#item-a128c9) | minor update | Microsoft Entra IDに関する前提条件の追加 | modified | 10 | 5 | 15 | 
| [gpt-v-typescript.md](#item-03ec34) | minor update | Microsoft Entra IDによる認証に関する前提条件の追加 | modified | 10 | 3 | 13 | 
| [javascript.md](#item-f4828f) | minor update | OpenAI npmパッケージの更新に関するガイドの修正 | modified | 8 | 9 | 17 | 
| [on-your-data-authentication.md](#item-43fc01) | minor update | Azure AI Foundryポータルにおける認証オプションの説明変更 | modified | 1 | 2 | 3 | 
| [realtime-javascript.md](#item-3c125e) | minor update | Microsoft Entra IDに関する初心者向け手順の整理 | modified | 4 | 12 | 16 | 
| [realtime-python.md](#item-1291c0) | minor update | 無鍵認証およびAPIキーに関するセクションの整理 | modified | 3 | 11 | 14 | 
| [realtime-typescript.md](#item-eacc9c) | minor update | 無鍵認証とAPIキーに関するセクションの整理 | modified | 5 | 13 | 18 | 
| [resource-auth.md](#item-cd425d) | minor update | 環境変数に関するドキュメントの名前変更と内容追加 | renamed | 21 | 2 | 23 | 
| [safety-evaluation.md](#item-09609f) | minor update | 文書内の文言修正 | modified | 1 | 1 | 2 | 
| [text-to-speech-javascript.md](#item-e9b653) | minor update | テキスト読み上げのJavaScriptに関する文書の更新 | modified | 8 | 48 | 56 | 
| [text-to-speech-typescript.md](#item-1335d5) | minor update | テキスト読み上げのTypeScriptに関する文書の更新 | modified | 8 | 48 | 56 | 
| [typescript.md](#item-ee5b93) | minor update | TypeScriptに関するガイドの更新 | modified | 9 | 7 | 16 | 
| [use-your-data-common-variables.md](#item-c35afc) | minor update | データ利用の共通変数に関するガイドの更新 | modified | 22 | 81 | 103 | 
| [use-your-data-javascript.md](#item-786699) | minor update | JavaScriptデータ利用ガイドの修正 | modified | 0 | 1 | 1 | 
| [use-your-data-powershell.md](#item-2d7fe4) | minor update | PowerShellデータ利用ガイドの更新 | modified | 1 | 1 | 2 | 
| [use-your-data-rest.md](#item-d1e071) | minor update | REST APIデータ利用ガイドの更新 | modified | 1 | 1 | 2 | 
| [use-your-data-studio.md](#item-705daf) | minor update | Azure AI Foundryポータルに関するガイドの更新 | modified | 2 | 2 | 4 | 
| [whisper-javascript.md](#item-3ee990) | minor update | Whisper JavaScriptガイドの認証手順の更新 | modified | 8 | 58 | 66 | 
| [whisper-python.md](#item-e61179) | minor update | Whisper Pythonガイドの文章修正 | modified | 1 | 1 | 2 | 
| [whisper-typescript.md](#item-eafedb) | minor update | Whisper TypeScriptガイドの認証手順の更新 | modified | 8 | 55 | 63 | 
| [studio-deployment-status.png](#item-3cdf5c) | breaking change | ファインチューニングチュートリアルにおける画像の削除 | removed | 0 | 0 | 0 | 
| [fine-tune.md](#item-8f87b5) | minor update | ファインチューニングチュートリアルの内容更新 | modified | 21 | 23 | 44 | 
| [use-your-data-quickstart.md](#item-52c1f4) | minor update | データ利用クイックスタートの前提条件に関する更新 | modified | 12 | 5 | 17 | 
| [whats-new.md](#item-53303b) | minor update | Azure OpenAI Studioのユーザーエクスペリエンス更新日付の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/api-version-deprecation.md{#item-1cad50}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 11/01/2024
+ms.date: 01/08/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -24,11 +24,13 @@ This article is to help you understand the support lifecycle for the Azure OpenA
 
 Azure OpenAI API latest release:
 
-- Inference: [2024-10-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference/preview/2024-10-01-preview/inference.json)
-- Authoring: [2024-10-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-10-01-preview/azureopenai.json)
+- Inference: [2024-12-01-preview](reference-preview.md)
+- Authoring: [2024-12-01-preview](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring/preview/2024-10-01-preview/azureopenai.json)
 
 This version contains support for the latest Azure OpenAI features including:
 
+- [Reasoning models](./how-to/reasoning.md) [**Added in 2024-12-01-preview**]
+- [Stored completions/distillation](./how-to/stored-completions.md) [**Added in 2024-12-01-preview**]
 - Assistants V2 [**Added in 2024-05-01-preview**]
 - Embeddings `encoding_format` and `dimensions` parameters [**Added in 2024-03-01-preview**]
 - [Assistants API](./assistants-reference.md). [**Added in 2024-02-15-preview**]
@@ -39,6 +41,12 @@ This version contains support for the latest Azure OpenAI features including:
 - [Function calling](./how-to/function-calling.md)  [**Added in 2023-07-01-preview**]
 - [Retrieval augmented generation with your data feature](./use-your-data-quickstart.md).  [**Added in 2023-06-01-preview**]
 
+## Changes between 2024-12-01-preview and 2024-10-01-preview
+
+- `store`, and `metadata` parameters added for [stored completions support](./how-to/stored-completions.md).
+- `reasoning_effort` added for latest [reasoning models](./how-to/reasoning.md).
+- `user_security_context` added for [Microsoft Defender for Cloud integration](https://aka.ms/TP4AI/Documentation/EndUserContext).
+
 ## Changes between 2024-09-01-preview and 2024-08-01-preview
 
 - `max_completion_tokens` added to support `o1-preview` and `o1-mini` models. `max_tokens` does not work with the **o1 series** models.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新と新機能追加"
}
```

### Explanation
このコードの変更は、Azure OpenAI APIに関するドキュメントの更新を含んでいます。主な変更点は、APIリリース日が2024年10月1日から2024年12月1日に変更され、新しい機能のサポートが追加されたことです。これには、推論モデルや保存された完了のサポートに関連する新しいパラメータが含まれています。

さらに、2024年12月1日プレビュー版と2024年10月1日プレビュー版の間の変更点が詳細に記載され、これによりユーザーが最新の機能を理解しやすくなっています。具体的には、`store`および`metadata`パラメータが保存された完了のサポートに追加され、最新の推論モデルには`reasoning_effort`が追加されました。また、Microsoft Defender for Cloudとの統合のために`user_security_context`も追加されています。 

全体として、これらの変更は、最新機能の利用やユーザーがAPIのバージョンと機能の更新を把握するために重要な情報を提供しています。

## articles/ai-services/openai/concepts/provisioned-migration.md{#item-68e143}

<details>
<summary>Diff</summary>
````diff
@@ -7,9 +7,9 @@ ms.service: azure-ai-openai
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/11/2024
-author: mrbullwinkle
-ms.author: mbullwin
+ms.date: 01/08/2025
+author: aahill
+ms.author: aahi
 recommendations: false
 ---
 
@@ -51,11 +51,11 @@ Provisioned quota granularity is changing from model-specific to model-independe
 
 ## Model-independent quota
 
-Starting on August 12, 2024, existing customers' current, model-specific quota has been converted to model-independent. This happens automatically. No quota is lost in the transition. Existing quota limits are summed and assigned to a new model-independent quota item.
+As of August 12, 2024, existing customers' current, model-specific quota has been converted to model-independent. This happens automatically. No quota is lost in the transition. Existing quota limits are summed and assigned to a new model-independent quota item.
 
 :::image type="content" source="../media/provisioned/consolidation.png" alt-text="Diagram showing quota consolidation." lightbox="../media/provisioned/consolidation.png":::
 
-The new model-independent quota shows up as a quota item named **Provisioned Managed Throughput Unit**, with model and version no longer included in the name. In the Studio Quota pane, expanding the quota item still shows all of the deployments that contribute to the quota item. 
+The new model-independent quota shows up as a quota item named **Provisioned Managed Throughput Unit**, with model and version no longer included in the name. In the Azure AI Foundry's quota pane, expanding the quota item still shows all of the deployments that contribute to the quota item. 
 
 ### Default quota
 
@@ -67,15 +67,15 @@ For existing customers, if the region already contains a quota assignment, the q
 
 Customers no longer obtain quota by contacting their sales teams. Instead, they use the self-service quota request form and specify the PTU-Managed quota type. The form is accessible from a link to the right of the quota item. The target is to respond to all quota requests within two business days.  
 
-The following quota screenshot shows model-independent quota being used by deployments of different types, as well as the link for requesting additional quota. 
+The following quota screenshot shows model-independent quota being used by deployments of different types, and the link for requesting additional quota. 
 
 :::image type="content" source="../media/provisioned/quota-request-type.png" alt-text="Screenshot of new request type UI for Azure OpenAI provisioned for requesting more quota." lightbox="../media/provisioned/quota-request-type.png":::
 
 ## Quota as a limit
 
-Prior to the August update, Azure OpenAI Provisioned was only available to a few customers, and quota was allocated to maximize the ability for them to deploy and use it. With these changes, the process of acquiring quota is simplified for all users, and there is a greater likelihood of running into service capacity limitations when deployments are attempted. A new API and Studio experience are available to help users find regions where the subscription has quota and the service has capacity to support deployments of a desired model.
+Prior to the August update, Azure OpenAI Provisioned was only available to a few customers, and quota was allocated to maximize the ability for them to deploy and use it. With these changes, the process of acquiring quota is simplified for all users, and there is a greater likelihood of running into service capacity limitations when deployments are attempted. A new API and portal experience are available to help users find regions where the subscription has quota and the service has capacity to support deployments of a desired model.
 
-We also recommend that customers using commitments now create their deployments before creating or expanding commitments to cover them. This guarantees that capacity is available before creating a commitment and prevents over-purchase of the commitment. To support this, the restriction that prevented deployments from being created larger than their commitments has been removed. This new approach to quota, capacity availability and commitments matches what is provided under the hourly/reservation model, and the guidance to deploy before purchasing a commitment (or reservation, for the hourly model) is the same for both.
+We also recommend that customers using commitments now create their deployments before creating or expanding commitments to cover them. This guarantees that capacity is available before creating a commitment and prevents over-purchase of the commitment. To support this, the restriction that prevented deployments from being created larger than their commitments has been removed. This new approach to quota, capacity availability, and commitments matches what is provided under the hourly/reservation model, and the guidance to deploy before purchasing a commitment (or reservation, for the hourly model) is the same for both.
 
 See the following links for more information. The guidance for reservations and commitments is the same:
 
@@ -85,15 +85,15 @@ See the following links for more information. The guidance for reservations and
 ## New hourly reservation payment model
 
 > [!NOTE]
-> The following description of payment models does not apply to the older "Provisioned Classic (PTU-C)" offering. They only affect the Provisioned (aka Provisioned Managed) offering. Provisioned Classic continues to be governed by the unchanged monthly commitment payment model.
+> The following description of payment models doesn't apply to the older "Provisioned Classic (PTU-C)" offering. They only affect the Provisioned (also known as Provisioned Managed) offering. Provisioned Classic continues to be governed by the unchanged monthly commitment payment model.
 
 Microsoft has introduced a new "Hourly/reservation" payment model for provisioned deployments. This is in addition to the current **Commitment** payment model, which will continue to be supported at least through the end of 2024.
 
 ### Commitment payment model
 
 - A regional, monthly commitment is required to use provisioned (longer terms available contractually).
 
-- Commitments are bound to Azure OpenAI resources, which makes moving deployments across resources difficult.
+- Commitments are bound to Azure OpenAI resources, which will make moving deployments across resources difficult.
 
 - Commitments can't be canceled or altered during their term, except to add new PTUs.
 
@@ -149,9 +149,9 @@ Steps 1 and 2 are the same in all cases. The difference is whether a commitment
 * The best practice is to create deployments first, and then to apply discounts. This is to guarantee that service. capacity is available to support your deployments prior to creating a term commitment for PTUs you cannot use. 
 
 > [!NOTE] 
-> When you follow best practices, you may receive hourly charges between the time you create the deployment and increase your discount (commitment or reservation).   
+> When you follow best practices, you might receive hourly charges between the time you create the deployment and increase your discount (commitment or reservation).   
 >
-> For this reason, we recommend that you be prepared to increase your discount immediately following the deployment. The prerequisites for purchasing an Azure reservations are different than for commitments, and we recommend you validate them prior to deployment if you intend to use them to discount your deployment.  For more information, see [Permissions to view and manage Azure reservations](/azure/cost-management-billing/reservations/view-reservations) 
+> For this reason, we recommend that you be prepared to increase your discount immediately following the deployment. The prerequisites for purchasing an Azure reservations are different than for commitments, and we recommend you validate them prior to deployment if you intend to use them to discount your deployment. For more information, see [Permissions to view and manage Azure reservations](/azure/cost-management-billing/reservations/view-reservations) 
 
 ## Mapping deployments to discounting method 
 
@@ -206,7 +206,7 @@ An alternative approach to self-service migration is to switch the reservation p
 * There will be a short period of double-billing or hourly charges during the switchover from committed to hourly/reservation billing.
 
 > [!IMPORTANT]
-> Both self-service approaches generate some additional charges as the payment mode is switched from Committed to Hourly/Reservation.  These are characteristics of the migration approaches and customers aren't credited for these charges.  Customers may choose to use the managed migration approach described below to avoid them.
+> Both self-service approaches generate some additional charges as the payment mode is switched from Committed to Hourly/Reservation. These are characteristics of the migration approaches and customers aren't credited for these charges.  Customers can choose to use the managed migration approach described below to avoid them.
 
 ### Managed migration
 
@@ -233,7 +233,7 @@ Customers must reach out to their account teams to schedule a managed migration.
 
 ## Managing Provisioned Throughput Commitments
 
-Provisioned throughput commitments are created and managed from the **Manage Commitments** menu in Azure OpenAI Studio. You can navigate to this view by selecting **Manage Commitments** from the Quota menu:
+Provisioned throughput commitments are created and managed by selecting **Management center** in the Azure AI Foundry portal's navigation menu > **Quota** > **Manage Commitments**. 
 
 :::image type="content" source="../media/how-to/provisioned-onboarding/notifications.png" alt-text="Screenshot of commitment purchase UI with notifications." lightbox="../media/how-to/provisioned-onboarding/notifications.png":::
 
@@ -247,7 +247,7 @@ The following sections will take you through these tasks.
 
 ## Purchase a Provisioned Throughput Commitment
 
-With your commitment plan ready, the next step is to create the commitments. Commitments are created manually via Azure OpenAI Studio and require the user creating the commitment to have either the [Contributor or Cognitive Services Contributor role](../how-to/role-based-access-control.md) at the subscription level.
+With your commitment plan ready, the next step is to create the commitments. Commitments are created manually via the Azure AI Foundry and require the user creating the commitment to have either the [Contributor or Cognitive Services Contributor role](../how-to/role-based-access-control.md) at the subscription level.
 
 For each new commitment you need to create, follow these steps:
 
@@ -273,11 +273,11 @@ For each new commitment you need to create, follow these steps:
 :::image type="content" source="../media/how-to/provisioned-onboarding/commitment-tier.png" alt-text="Screenshot of commitment purchase UI." lightbox="../media/how-to/provisioned-onboarding/commitment-tier.png":::
 
 > [!IMPORTANT]
-> A new commitment is billed up-front for the entire term.  If the renewal settings are set to auto-renew, then you will be billed again on each renewal date based on the renewal settings.
+> A new commitment is billed up-front for the entire term. If the renewal settings are set to auto-renew, then you will be billed again on each renewal date based on the renewal settings.
 
 ### Edit an existing Provisioned Throughput commitment
 
-From the Manage Commitments view, you can also edit an existing commitment. There are two types of changes you can make to an existing commitment:
+From the **Manage Commitments** view, you can also edit an existing commitment. There are two types of changes you can make to an existing commitment:
 
 - You can add PTUs to the commitment.
 - You can change the renewal settings.
@@ -291,14 +291,14 @@ Adding PTUs to an existing commitment will allow you to create larger or more nu
 :::image type="content" source="../media/how-to/provisioned-onboarding/increase-commitment.png" alt-text="Screenshot of commitment purchase UI with an increase in the amount to commit value." lightbox="../media/how-to/provisioned-onboarding/increase-commitment.png":::
 
 > [!IMPORTANT]
-> When you add PTUs to a commitment, they will be billed immediately, at a pro-rated amount from the current date to the end of the existing commitment term.  Adding PTUs does not reset the commitment term.
+> When you add PTUs to a commitment, they will be billed immediately, at a pro-rated amount from the current date to the end of the existing commitment term. Adding PTUs doesn't reset the commitment term.
 
 ### Changing renewal settings
 
-Commitment renewal settings can be changed at any time before the expiration date of your commitment.  Reasons you might want to change the renewal settings include ending your use of provisioned throughput by setting the commitment to not autorenew, or to decrease usage of provisioned throughput by lowering the number of PTUs that will be committed in the next period.
+Commitment renewal settings can be changed at any time before the expiration date of your commitment. Reasons you might want to change the renewal settings include ending your use of provisioned throughput by setting the commitment to not autorenew, or to decrease usage of provisioned throughput by lowering the number of PTUs that will be committed in the next period.
 
 > [!IMPORTANT]
-> If you allow a commitment to expire or decrease in size such that the deployments under the resource require more PTUs than you have in your resource commitment, you will receive hourly overage charges for any excess PTUs.  For example, a resource that has deployments that total 500 PTUs and a commitment for 300 PTUs will generate hourly overage charges for 200 PTUs.
+> If you allow a commitment to expire or decrease in size such that the deployments under the resource require more PTUs than you have in your resource commitment, you will receive hourly overage charges for any excess PTUs. For example, a resource that has deployments that total 500 PTUs and a commitment for 300 PTUs will generate hourly overage charges for 200 PTUs.
 
 ## Monitor commitments and prevent unexpected billings
 
@@ -319,7 +319,7 @@ To end use of provisioned throughput, and prevent hourly overage charges after c
 
 **Move a commitment/deployment to a new resource in the same subscription/region**
 
-It isn't possible in Azure OpenAI Studio to directly *move* a deployment or a commitment to a new resource. Instead, a new deployment needs to be created on the target resource and traffic moved to it. There will need to be a commitment purchased established on the new resource to accomplish this. Because commitments are charged up-front for a 30-day period, it's necessary to time this move with the expiration of the original commitment to minimize overlap with the new commitment and “double-billing” during the overlap.
+It isn't possible in Azure AI Foundry to directly *move* a deployment or a commitment to a new resource. Instead, a new deployment needs to be created on the target resource and traffic moved to it. There will need to be a commitment purchased established on the new resource to accomplish this. Because commitments are charged up-front for a 30-day period, it's necessary to time this move with the expiration of the original commitment to minimize overlap with the new commitment and “double-billing” during the overlap.
 
 There are two approaches that can be taken to implement this transition.
 
@@ -357,4 +357,4 @@ The same approaches apply in moving the commitment and deployment within the reg
 
 ### View and edit an existing resource
 
-In Azure OpenAI Studio, select **Quota** > **Provisioned** > **Manage commitments** and select a resource with an existing commitment to view/change it. 
+In Azure AI Foundry, select **Management center** > **Quota** > **Provisioned** > **Manage commitments** and select a resource with an existing commitment to view/change it. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョニング移行に関する更新"
}
```

### Explanation
この変更は、Azure OpenAIのプロビジョニング移行に関するドキュメントの更新を反映しています。主な改訂点には、著者と日付の更新、セクションタイトルの修正、そして「モデル固有」のクォータから「モデル独立」のクォータへの移行に関する説明が含まれています。

具体的には、2024年8月12日から、既存の顧客のモデル固有のクォータが自動的にモデル独立のクォータに変換されることが明記されています。この移行において、クォータが失われることはなく、既存のクォタ制限は合算されて、新しいモデル独立のクォタアイテムに割り当てられます。

さらに、Azure AI Foundryプラットフォームにおける新しいクォタ管理の方法や、自サービスによるクォタのリクエスト方法が明確に記載されています。顧客は、営業チームに連絡するのではなく、自サービスのクォタリクエストフォームを使用してPTU管理クォタタイプを指定することが求められています。これにより、すべてのユーザーに対してクォタの獲得プロセスが簡素化され、デプロイメントの際にサービス容量の制限に遭遇する可能性が高まることが示されています。

全体として、このドキュメントの更新は、ユーザーに提供される情報が最新であることを保証し、プロビジョニング移行の詳細を明確に理解できるようにすることを目的としています。

## articles/ai-services/openai/concepts/provisioned-reservation-update.md{#item-53236b}

<details>
<summary>Diff</summary>
````diff
@@ -67,5 +67,5 @@ The migration with downtime approach involves migrating existing provisioned dep
 - Once your new deployment has succeeded, you may resume inference traffic on the new global or data zone deployment.
 
 ## How do I migrate my existing Azure Reservation to the new Azure Reservation products?
-Azure Reservations for Azure OpenAI Service provisioned offers are specific to the provisioned deployment type. If the Azure Reservation purchased does not match the provisioned deployment type, the deployment will default to the hourly payment model. If you choose to migrate to global or data zone provisioned deployments, you may need to purchase a new Azure Reservation for these deployments to support additional discounts. For more information on how to purchase a new Azure Reservation or make changes to an existing Azure Reservation, see the [Azure Reservations for Azure OpenAI Service Provisioned guidance](https://aka.ms/aoai/reservation-transition).
+Azure Reservations for Azure OpenAI Service provisioned offers are specific to the provisioned deployment type. If the Azure Reservation purchased does not match the provisioned deployment type, the deployment will default to the hourly payment model. If you choose to migrate to global or data zone provisioned deployments, you might need to purchase a new Azure Reservation for these deployments to support additional discounts. For more information on how to purchase a new Azure Reservation or make changes to an existing Azure Reservation, see the [Azure Reservations for Azure OpenAI Service Provisioned guidance](https://aka.ms/aoai/reservation-transition).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Reservationに関する注意点の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスのプロビジョニング予約の更新に関するドキュメントの一部であり、特定の文章が修正されています。主な修正点は、顧客が新しいAzure予約を購入する必要がある場合の注意点を示す文の表現の微調整です。

具体的には、「may」という表現が「might」に変更されており、これにより、依存関係のある予約購入に関する可能性を柔らかく表現しています。この変更は、利用者が予約の適合性について判断を行う際に、少しだけ条件付きの印象を与えるものとなっています。

全体として、変更は文脈に対する明確な理解を助け、ユーザーがAzure OpenAIサービスのプロビジョニング予約の移行を行う際の選択肢についての認識を促進することを目指しています。

## articles/ai-services/openai/concepts/red-teaming.md{#item-0916c9}

<details>
<summary>Diff</summary>
````diff
@@ -65,7 +65,7 @@ It can be helpful to provide red teamers with:
 
 ### Plan: What to test
 
-Because an application is developed using a base model, you may need to test at several different layers:
+Because an application is developed using a base model, you might need to test at several different layers:
 
 - The LLM base model with its safety system in place to identify any gaps that may need to be addressed in the context of your application system. (Testing is usually done through an API endpoint.)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レッドチーミングのテストに関する表現の更新"
}
```

### Explanation
この変更は、レッドチーミングに関するドキュメントの一部を更新したもので、表現の微調整が行われています。具体的には、「may」という表現が「might」に変更され、テストを実施する必要があることを示す表現が柔らかく修正されています。

この修正は、アプリケーションがベースモデルを使用して開発されていることを踏まえ、さまざまなレイヤーでテストする必要があることを示す文のコンテキスト内で行われています。このニュアンスの変更によって、テストの必要性が提案的に示され、実施の選択肢としての柔軟性が強調されています。

全体として、この変更はドキュメントの表現を明確にし、読者がレッドチーミングのテスト要件についてより良い理解を得る手助けをすることを目的としています。

## articles/ai-services/openai/concepts/use-your-data.md{#item-455d6e}

<details>
<summary>Diff</summary>
````diff
@@ -19,14 +19,14 @@ Use this article to learn about Azure OpenAI On Your Data, which makes it easier
 
 ## What is Azure OpenAI On Your Data
 
-Azure OpenAI On Your Data enables you to run advanced AI models such as GPT-35-Turbo and GPT-4 on your own enterprise data without needing to train or fine-tune models. You can chat on top of and analyze your data with greater accuracy. You can specify sources to support the responses based on the latest information available in your designated data sources. You can access Azure OpenAI On Your Data using a REST API, via the SDK or the web-based interface in the [Azure OpenAI Studio](https://oai.azure.com/). You can also create a web app that connects to your data to enable an enhanced chat solution or deploy it directly as a copilot in the Copilot Studio (preview).
+Azure OpenAI On Your Data enables you to run advanced AI models such as GPT-35-Turbo and GPT-4 on your own enterprise data without needing to train or fine-tune models. You can chat on top of and analyze your data with greater accuracy. You can specify sources to support the responses based on the latest information available in your designated data sources. You can access Azure OpenAI On Your Data using a REST API, via the SDK or the web-based interface in the [Azure AI Foundry portal](https://oai.azure.com/). You can also create a web app that connects to your data to enable an enhanced chat solution or deploy it directly as a copilot in the Copilot Studio (preview).
 
 ## Developing with Azure OpenAI On Your Data
 
 :::image type="content" source="../media/use-your-data/workflow-diagram.png" alt-text="A diagram showing an example workflow.":::
 
 Typically, the development process you'd use with Azure OpenAI On Your Data is:
-1. **Ingest**: Upload files using either Azure OpenAI Studio or the ingestion API. This enables your data to be cracked, chunked and embedded into an Azure AI Search instance that can be used by Azure OpenAI models. If you have an existing [supported data source](#supported-data-sources), you can also connect it directly.
+1. **Ingest**: Upload files using either Azure AI Foundry portal or the ingestion API. This enables your data to be cracked, chunked and embedded into an Azure AI Search instance that can be used by Azure OpenAI models. If you have an existing [supported data source](#supported-data-sources), you can also connect it directly.
 
 1. **Develop**: After trying Azure OpenAI On Your Data, begin developing your application using the available REST API and SDKs, which are available in several languages. It will create prompts and search intents to pass to the Azure OpenAI service.
 
@@ -39,7 +39,7 @@ Typically, the development process you'd use with Azure OpenAI On Your Data is:
     
     1. **Response generation**: The resulting data is submitted along with other information like the system message to the Large Language Model (LLM) and the response is sent back to the application.
 
-To get started, [connect your data source](../use-your-data-quickstart.md) using Azure OpenAI Studio and start asking questions and chatting on your data.
+To get started, [connect your data source](../use-your-data-quickstart.md) using Azure AI Foundry portal and start asking questions and chatting on your data.
 
 ## Azure Role-based access controls (Azure RBAC) for adding data sources
 
@@ -136,9 +136,9 @@ Azure OpenAI On Your Data lets you restrict the documents that can be used in re
 
 ### Index field mapping 
 
-If you're using your own index, you'll be prompted in the Azure OpenAI Studio to define which fields you want to map for answering questions when you add your data source. You can provide multiple fields for *Content data*, and should include all fields that have text pertaining to your use case. 
+If you're using your own index, you'll be prompted in the Azure AI Foundry portal to define which fields you want to map for answering questions when you add your data source. You can provide multiple fields for *Content data*, and should include all fields that have text pertaining to your use case. 
 
-:::image type="content" source="../media/use-your-data/index-data-mapping.png" alt-text="A screenshot showing the index field mapping options in Azure OpenAI Studio." lightbox="../media/use-your-data/index-data-mapping.png":::
+:::image type="content" source="../media/use-your-data/index-data-mapping.png" alt-text="A screenshot showing the index field mapping options in Azure AI Foundry portal." lightbox="../media/use-your-data/index-data-mapping.png":::
 
 In this example, the fields mapped to **Content data** and **Title** provide information to the model to answer questions. **Title** is also used to title citation text. The field mapped to **File name** generates the citation names in the response. 
 
@@ -189,10 +189,10 @@ You might want to use Azure Blob Storage as a data source if you want to connect
 
 To keep your Azure AI Search index up-to-date with your latest data, you can schedule an automatic index refresh rather than manually updating it every time your data is updated. Automatic index refresh is only available when you choose **Azure Blob Storage** as the data source. To enable an automatic index refresh:
 
-1. [Add a data source](../quickstart.md) using Azure OpenAI studio.
+1. [Add a data source](../quickstart.md) using Azure AI Foundry portal.
 1. Under **Select or add data source** select **Indexer schedule** and choose the refresh cadence you would like to apply.
 
-    :::image type="content" source="../media/use-your-data/indexer-schedule.png" alt-text="A screenshot of the indexer schedule in Azure OpenAI Studio." lightbox="../media/use-your-data/indexer-schedule.png":::
+    :::image type="content" source="../media/use-your-data/indexer-schedule.png" alt-text="A screenshot of the indexer schedule in Azure AI Foundry portal." lightbox="../media/use-your-data/indexer-schedule.png":::
 
 After the data ingestion is set to a cadence other than once, Azure AI Search indexers will be created with a schedule equivalent to `0.5 * the cadence specified`. This means that at the specified cadence, the indexers will pull, reprocess, and index the documents that were added or modified from the storage container. This process ensures that the updated data gets preprocessed and indexed in the final index at the desired cadence automatically. To update your data, you only need to upload the additional documents from the Azure portal. From the portal, select **Storage Account** > **Containers**. Select the name of the original container, then **Upload**. The index will pick up the files automatically after the scheduled refresh period. The intermediate assets created in the Azure AI Search resource won't be cleaned up after ingestion to allow for future runs. These assets are:
    - `{Index Name}-index`
@@ -221,9 +221,9 @@ To modify the schedule, you can use the [Azure portal](https://portal.azure.com/
 
 # [Upload files (preview)](#tab/file-upload)
 
-Using Azure OpenAI Studio, you can upload files from your machine to try Azure OpenAI On Your Data. You also have the option to create a new Azure Blob Storage account and Azure AI Search resource. The service then stores the files to an Azure storage container and performs ingestion from the container. You can use the [quickstart](../use-your-data-quickstart.md) article to learn how to use this data source option.
+Using Azure AI Foundry portal, you can upload files from your machine to try Azure OpenAI On Your Data. You also have the option to create a new Azure Blob Storage account and Azure AI Search resource. The service then stores the files to an Azure storage container and performs ingestion from the container. You can use the [quickstart](../use-your-data-quickstart.md) article to learn how to use this data source option.
 
-:::image type="content" source="../media/quickstarts/add-your-data-source.png" alt-text="A screenshot showing options for selecting a data source in Azure OpenAI Studio." lightbox="../media/quickstarts/add-your-data-source.png":::
+:::image type="content" source="../media/quickstarts/add-your-data-source.png" alt-text="A screenshot showing options for selecting a data source in Azure AI Foundry portal." lightbox="../media/quickstarts/add-your-data-source.png":::
 
 [!INCLUDE [ai-search-ingestion](../includes/ai-search-ingestion.md)]
 
@@ -305,7 +305,7 @@ Mapping these fields correctly helps ensure the model has better response and ci
 
 ### Use Elasticsearch as a data source via API  
 
-Along with using Elasticsearch databases in Azure OpenAI Studio, you can also use your Elasticsearch database using the [API](../references/elasticsearch.md). 
+Along with using Elasticsearch databases in Azure AI Foundry portal, you can also use your Elasticsearch database using the [API](../references/elasticsearch.md). 
 
 # [MongoDB Atlas (preview)](#tab/mongo-db-atlas)
 
@@ -360,15 +360,15 @@ When you add your MongoDB Atlas data source, you can specify data fields to prop
 
 ## Deploy to a copilot (preview), Teams app (preview), or web app 
 
-After you connect Azure OpenAI to your data, you can deploy it using the **Deploy to** button in Azure OpenAI Studio.
+After you connect Azure OpenAI to your data, you can deploy it using the **Deploy to** button in Azure AI Foundry portal.
 
-:::image type="content" source="../media/use-your-data/deploy-model.png" alt-text="A screenshot showing the model deployment button in Azure OpenAI Studio." lightbox="../media/use-your-data/deploy-model.png":::
+:::image type="content" source="../media/use-your-data/deploy-model.png" alt-text="A screenshot showing the model deployment button in Azure AI Foundry portal." lightbox="../media/use-your-data/deploy-model.png":::
 
 This gives you multiple options for deploying your solution.
 
 #### [Copilot (preview)](#tab/copilot)
 
-You can deploy to a copilot in [Copilot Studio](/microsoft-copilot-studio/fundamentals-what-is-copilot-studio) (preview) directly from Azure OpenAI Studio, enabling you to bring conversational experiences to various channels such as: Microsoft Teams, websites, Dynamics 365, and other [Azure Bot Service channels](/microsoft-copilot-studio/publication-connect-bot-to-azure-bot-service-channels). The tenant used in the Azure OpenAI service and Copilot Studio (preview) should be the same. For more information, see [Use a connection to Azure OpenAI On Your Data](/microsoft-copilot-studio/nlu-generative-answers-azure-openai).
+You can deploy to a copilot in [Copilot Studio](/microsoft-copilot-studio/fundamentals-what-is-copilot-studio) (preview) directly from Azure AI Foundry portal, enabling you to bring conversational experiences to various channels such as: Microsoft Teams, websites, Dynamics 365, and other [Azure Bot Service channels](/microsoft-copilot-studio/publication-connect-bot-to-azure-bot-service-channels). The tenant used in the Azure OpenAI service and Copilot Studio (preview) should be the same. For more information, see [Use a connection to Azure OpenAI On Your Data](/microsoft-copilot-studio/nlu-generative-answers-azure-openai).
 
 > [!NOTE]
 > Deploying to a copilot in Copilot Studio (preview) is only available in US regions.
@@ -390,15 +390,15 @@ A Teams app lets you bring conversational experience to your users in Teams to i
 - Your Azure account has been assigned **Cognitive Services OpenAI user** or **Cognitive Services OpenAI Contributor** role of the Azure OpenAI resource you're using, allowing your account to make Azure OpenAI API calls. For more information, see [Azure OpenAI On Your data configuration](../how-to/on-your-data-configuration.md#using-the-api) and [Add role assignment to an Azure OpenAI resource](/azure/ai-services/openai/how-to/role-based-access-control#add-role-assignment-to-an-azure-openai-resource) for instructions on setting this role in the Azure portal. 
 
 
-You can deploy to a standalone Teams app directly from Azure OpenAI Studio. Follow the steps below: 
+You can deploy to a standalone Teams app directly from Azure AI Foundry portal. Follow the steps below: 
 
 1. After you've added your data to the chat model, select **Deploy** and then **a new Teams app (preview)**. 
 
 1. Enter the name of your Teams app and download the resulting .zip file.
 
 1. Extract the .zip file and open the folder in Visual Studio Code.
 
-1. If you chose **API key** in the data connection step, manually copy and paste your Azure AI Search key into the `src\prompts\chat\config.json` file. Your Azure AI Search Key can be found in Azure OpenAI Studio Playground by selecting the **View code** button with the key located under Azure Search Resource Key. If you chose **System assigned managed identity**, you can skip this step. Learn more about different data connection options in the [Data connection](/azure/ai-services/openai/concepts/use-your-data?tabs=ai-search#data-connection) section.
+1. If you chose **API key** in the data connection step, manually copy and paste your Azure AI Search key into the `src\prompts\chat\config.json` file. Your Azure AI Search Key can be found in Azure AI Foundry portal Playground by selecting the **View code** button with the key located under Azure Search Resource Key. If you chose **System assigned managed identity**, you can skip this step. Learn more about different data connection options in the [Data connection](/azure/ai-services/openai/concepts/use-your-data?tabs=ai-search#data-connection) section.
 
 1. Open the Visual Studio Code terminal and log into Azure CLI, selecting the account that you assigned **Cognitive Service OpenAI User** role to. Use the `az login` command in the terminal to log in.
 
@@ -464,7 +464,7 @@ A small chunk size like 256 produces more granular chunks. This size also means
 
 ### Runtime parameters
 
-You can modify the following additional settings in the **Data parameters** section in Azure OpenAI Studio and [the API](../references/on-your-data.md). You don't need to reingest your data when you update these parameters. 
+You can modify the following additional settings in the **Data parameters** section in Azure AI Foundry portal and [the API](../references/on-your-data.md). You don't need to reingest your data when you update these parameters. 
 
 
 |Parameter name  | Description  |
@@ -481,9 +481,9 @@ It's possible for the model to return `"TYPE":"UNCITED_REFERENCE"` instead of `"
 
 You can define a system message to steer the model's reply when using Azure OpenAI On Your Data. This message allows you to customize your replies on top of the retrieval augmented generation (RAG) pattern that Azure OpenAI On Your Data uses. The system message is used in addition to an internal base prompt to provide the experience. To support this, we truncate the system message after a specific [number of tokens](#token-usage-estimation-for-azure-openai-on-your-data) to ensure the model can answer questions using your data. If you are defining extra behavior on top of the default experience, ensure that your system prompt is detailed and explains the exact expected customization. 
 
-Once you select add your dataset, you can use the **System message** section in the Azure OpenAI Studio, or the `role_information` [parameter in the API](../references/on-your-data.md).
+Once you select add your dataset, you can use the **System message** section in the Azure AI Foundry portal, or the `role_information` [parameter in the API](../references/on-your-data.md).
 
-:::image type="content" source="../media/use-your-data/system-message.png" alt-text="A screenshot showing the system message option in Azure OpenAI Studio." lightbox="../media/use-your-data/system-message.png":::
+:::image type="content" source="../media/use-your-data/system-message.png" alt-text="A screenshot showing the system message option in Azure AI Foundry portal." lightbox="../media/use-your-data/system-message.png":::
 
 #### Potential usage patterns
 
@@ -681,7 +681,7 @@ token_output = TokenEstimator.estimate_tokens(input_text)
 
 ## Troubleshooting 
 
-To troubleshoot failed operations, always look out for errors or warnings specified either in the API response or Azure OpenAI Studio. Here are some of the common errors and warnings: 
+To troubleshoot failed operations, always look out for errors or warnings specified either in the API response or Azure AI Foundry portal. Here are some of the common errors and warnings: 
 
 ### Failed ingestion jobs
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルへの移行"
}
```

### Explanation
この変更は、「Azure OpenAI On Your Data」に関するドキュメントの大部分を更新し、表現を「Azure OpenAI Studio」から「Azure AI Foundryポータル」に変更したものです。この更新によって、ポータルの名称と関連する機能の整合性が保たれています。

具体的には、データの取り扱いやモデルのデプロイに関する手順、APIやSDKの利用方法などの説明において、すべての参照を新しいポータルに合わせて修正しています。これにより、ユーザーは新しいインターフェースに基づいて、データのインジェストやAPIの利用、デプロイの設定ができるようになっています。

全体として、変更は文書の一貫性を高め、ユーザーが最新の開発環境でスムーズに作業を進められるようにすることを目指しています。また、この更新は利用者が新機能や改善点にアクセスするのを助けるものであり、Azure AI Foundryポータルを使用した新しい操作体験を促進します。

## articles/ai-services/openai/dall-e-quickstart.md{#item-fcd528}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: 'Quickstart: Generate images with Azure OpenAI Service'
 titleSuffix: Azure OpenAI
-description: Learn how to get started generating images with Azure OpenAI Service by using the Python SDK, the REST APIs, or Azure OpenAI Studio.
+description: Learn how to get started generating images with Azure OpenAI Service by using the Python SDK, the REST APIs, or Azure AI Foundry portal.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
@@ -16,11 +16,11 @@ zone_pivot_groups: openai-quickstart-dall-e
 # Quickstart: Generate images with Azure OpenAI Service
 
 > [!NOTE]
-> The image generation API creates an image from a text prompt. It does not edit or create variations from existing images.
+> The image generation API creates an image from a text prompt. It doesn't edit or create variations from existing images.
 
 ::: zone pivot="programming-language-studio"
 
-[!INCLUDE [Studio quickstart](includes/dall-e-studio.md)]
+[!INCLUDE [Portal quickstart](includes/dall-e-studio.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの参照追加と表現修正"
}
```

### Explanation
この変更は、Azure OpenAIサービスを利用して画像を生成する方法に関するクイックスタートガイドの修正です。具体的には、「Azure OpenAI Studio」という表現が「Azure AI Foundryポータル」に変更され、最新の環境に合わせた情報提供が行われています。また、テキストプロンプトから画像を生成するAPIの説明が少し修正され、「doesn't」という否定語が使われることで、より口語的な表現に統一されています。

これらの修正は、ユーザーが最新のインターフェースを使用してクイックスタートガイドを利用できるようにすることを意図しており、より明確で理解しやすいドキュメントを提供することを目指しています。また、APIの動作についての認識を強化し、混乱を避けるための説明の精度を向上させています。この更新により、利用者が直感的に作業を進めることができるようになっています。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: 'Customize a model with Azure OpenAI Service'
 titleSuffix: Azure OpenAI
-description: Learn how to create your own customized model with Azure OpenAI Service by using Python, the REST APIs, or Azure OpenAI Studio.
+description: Learn how to create your own customized model with Azure OpenAI Service by using Python, the REST APIs, or Azure AI Foundry portal.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
@@ -28,7 +28,7 @@ We use LoRA, or low rank approximation, to fine-tune models in a way that reduce
 
 ::: zone pivot="programming-language-studio"
 
-[!INCLUDE [Azure OpenAI Studio fine-tuning](../includes/fine-tuning-unified.md)]
+[!INCLUDE [Azure AI Foundry portal fine-tuning](../includes/fine-tuning-unified.md)]
 
 ::: zone-end
 
@@ -159,7 +159,7 @@ In order to successfully access fine-tuning, you need **Cognitive Services OpenA
 
 ### Why did my upload fail?
 
-If your file upload fails in Azure OpenAI Studio, you can view the error message under “data files” in Azure OpenAI Studio. Hover your mouse over where it says “error” (under the status column) and an explanation of the failure will be displayed.
+If your file upload fails in Azure AI Foundry portal, you can view the error message under **Data files** in Azure AI Foundry portal. Hover your mouse over where it says “error” (under the status column) and an explanation of the failure will be displayed.
 
 :::image type="content" source="../media/fine-tuning/error.png" alt-text="Screenshot of fine-tuning error message." lightbox="../media/fine-tuning/error.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルへの移行"
}
```

### Explanation
この変更は、Azure OpenAIサービスを使用してモデルをカスタマイズする方法に関するドキュメントの更新です。主な修正点は、「Azure OpenAI Studio」という表現を「Azure AI Foundryポータル」に変更し、最新の開発環境に合わせた情報提供を行ったことです。

具体的には、カスタマイズモデルの作成手順に関する説明や、ファイルのアップロード失敗時のエラーメッセージ表示の方法が新しいポータルに基づいて修正されています。これにより、ユーザーは最新のインターフェースを使用して、カスタマイズされたモデルのファインチューニングをスムーズに行えるようになります。

全体として、この変更はユーザー体験を向上させ、最新の製品名や機能に関する整合性を保つことを目的としています。また、ポータルへの正しい誘導を行うことで、ユーザーがドキュメントに記載されている手順を正確に実行できるようにしています。

## articles/ai-services/openai/how-to/monitor-openai.md{#item-fcba4d}

<details>
<summary>Diff</summary>
````diff
@@ -69,7 +69,7 @@ After you configure the diagnostic settings, you can work with metrics and log d
 
 [!INCLUDE [horz-monitor-kusto-queries](~/reusable-content/ce-skilling/azure/includes/azure-monitor/horizontals/horz-monitor-kusto-queries.md)]
 
-After you deploy an Azure OpenAI model, you can send some completions calls by using the **playground** environment in [Azure AI Foundry](https://oai.azure.com/).
+After you deploy an Azure OpenAI model, you can send some completions calls by using the **playground** environment in [Azure AI Foundry](https://ai.azure.com/).
 
 Any text that you enter in the **Completions playground** or the **Chat completions playground** generates metrics and log data for your Azure OpenAI resource. In the Log Analytics workspace for your resource, you can query the monitoring data by using the [Kusto](/azure/data-explorer/kusto/query/) query language.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryのリンク修正"
}
```

### Explanation
この変更は、Azure OpenAIモデルを監視する方法に関するドキュメントの更新です。具体的には、Azure OpenAIモデルをデプロイした後に利用する「playground」環境のリンク先が、正確なURLに更新されました。具体的には「Azure AI Foundry」から「Azure AI Foundry」へのテキスト修正が行われています。

この修正によって、ユーザーは正確なURLに基づく正しい環境を参照できるようになり、コンプリーションの呼び出しに関する体験が向上します。また、メトリクスやログデータの収集においても、ユーザーが有効に活用できることを意識した内容になっています。全体として、この変更は資料の明確性を高め、ユーザーがより簡単に手順を理解し、実行できるようにすることを目的としています。

## articles/ai-services/openai/how-to/on-your-data-configuration.md{#item-4875d3}

<details>
<summary>Diff</summary>
````diff
@@ -67,9 +67,9 @@ Azure OpenAI On Your Data lets you restrict the documents that can be used in re
     `group_ids` is the default field name. If you use a different field name like `my_group_ids`, you can map the field in [index field mapping](../concepts/use-your-data.md#index-field-mapping).
 
 1. Make sure each sensitive document in the index has this security field value set to the permitted groups of the document.
-1. In [Azure OpenAI Studio](https://oai.azure.com/portal), add your data source. in the [index field mapping](../concepts/use-your-data.md#index-field-mapping) section, you can map zero or one value to the **permitted groups** field, as long as the schema is compatible. If the **permitted groups** field isn't mapped, document level access is disabled. 
+1. In [Azure AI Foundry portal](https://oai.azure.com/portal), add your data source. in the [index field mapping](../concepts/use-your-data.md#index-field-mapping) section, you can map zero or one value to the **permitted groups** field, as long as the schema is compatible. If the **permitted groups** field isn't mapped, document level access is disabled. 
 
-**Azure OpenAI Studio**
+**Azure AI Foundry portal**
 
 Once the Azure AI Search index is connected, your responses in the studio have document access based on the Microsoft Entra permissions of the logged in user.
 
@@ -178,7 +178,7 @@ This step can be skipped only if you have a [shared private link](#create-shared
 
 You can disable public network access of your Azure OpenAI resource in the Azure portal. 
 
-To allow access to your Azure OpenAI Service from your client machines, like using Azure OpenAI Studio, you need to create [private endpoint connections](/azure/ai-services/cognitive-services-virtual-networks?tabs=portal#use-private-endpoints) that connect to your Azure OpenAI resource.
+To allow access to your Azure OpenAI Service from your client machines, like using Azure AI Foundry portal, you need to create [private endpoint connections](/azure/ai-services/cognitive-services-virtual-networks?tabs=portal#use-private-endpoints) that connect to your Azure OpenAI resource.
 
 
 ## Configure Azure AI Search
@@ -202,7 +202,7 @@ For more information, see the [Azure AI Search RBAC article](/azure/search/searc
 
 You can disable public network access of your Azure AI Search resource in the Azure portal. 
 
-To allow access to your Azure AI Search resource from your client machines, like using Azure OpenAI Studio, you need to create [private endpoint connections](/azure/search/service-create-private-endpoint) that connect to your Azure AI Search resource.
+To allow access to your Azure AI Search resource from your client machines, like using Azure AI Foundry portal, you need to create [private endpoint connections](/azure/search/service-create-private-endpoint) that connect to your Azure AI Search resource.
 
 
 ### Enable trusted service
@@ -256,7 +256,7 @@ In the Azure portal, navigate to your storage account networking tab, choose "Se
 
 You can disable public network access of your Storage Account in the Azure portal. 
 
-To allow access to your Storage Account from your client machines, like using Azure OpenAI Studio, you need to create [private endpoint connections](/azure/storage/common/storage-private-endpoints) that connect to your blob storage.
+To allow access to your Storage Account from your client machines, like using Azure AI Foundry portal, you need to create [private endpoint connections](/azure/storage/common/storage-private-endpoints) that connect to your blob storage.
 
 
 
@@ -285,9 +285,9 @@ To enable the developers to use these resources to build applications, the admin
 
 |Role| Resource | Description |
 |--|--|--|
-| `Cognitive Services OpenAI Contributor` | Azure OpenAI | Call public ingestion API from Azure OpenAI Studio. The `Contributor` role is not enough, because if you only have `Contributor` role, you cannot call data plane API via Microsoft Entra ID authentication, and Microsoft Entra ID authentication is required in the secure setup described in this article. |
-| `Contributor` | Azure AI Search | List API-Keys to list indexes from Azure OpenAI Studio.|
-| `Contributor` | Storage Account | List Account SAS to upload files from Azure OpenAI Studio.|
+| `Cognitive Services OpenAI Contributor` | Azure OpenAI | Call public ingestion API from Azure AI Foundry portal. The `Contributor` role is not enough, because if you only have `Contributor` role, you cannot call data plane API via Microsoft Entra ID authentication, and Microsoft Entra ID authentication is required in the secure setup described in this article. |
+| `Contributor` | Azure AI Search | List API-Keys to list indexes from Azure AI Foundry portal.|
+| `Contributor` | Storage Account | List Account SAS to upload files from Azure AI Foundry portal.|
 | `Contributor` | The resource group or Azure subscription where the developer need to deploy the web app to | Deploy web app to the developer's Azure subscription.|
 | `Role Based Access Control Administrator` | Azure OpenAI | Permission to configure the necessary role assignment on the Azure OpenAI resource. Enables the web app to call Azure OpenAI. |
 
@@ -309,9 +309,9 @@ Configure your local machine `hosts` file to point your resources host names to
 10.0.0.7 contoso.blob.core.windows.net
 ```
 
-## Azure OpenAI Studio
+## Azure AI Foundry portal
 
-You should be able to use all Azure OpenAI Studio features, including both ingestion and inference, from your on-premises client machines.
+You should be able to use all Azure AI Foundry portal features, including both ingestion and inference, from your on-premises client machines.
 
 ## Web app
 The web app communicates with your Azure OpenAI resource. Since your Azure OpenAI resource has public network disabled, the web app needs to be set up to use the private endpoint in your virtual network to access your Azure OpenAI resource.
@@ -322,7 +322,7 @@ The web app needs to resolve your Azure OpenAI host name to the private IP of th
 1. [Add a DNS record](/azure/dns/private-dns-getstarted-portal#create-an-additional-dns-record). The IP is the private IP of the private endpoint for your Azure OpenAI resource, and you can get the IP address from the network interface associated with the private endpoint for your Azure OpenAI.
 1. [Link the private DNS zone to your virtual network](/azure/dns/private-dns-getstarted-portal#link-the-virtual-network) so the web app integrated in this virtual network can use this private DNS zone.
 
-When deploying the web app from Azure OpenAI Studio, select the same location with the virtual network, and select a proper SKU, so it can support the [virtual network integration feature](/azure/app-service/overview-vnet-integration). 
+When deploying the web app from Azure AI Foundry portal, select the same location with the virtual network, and select a proper SKU, so it can support the [virtual network integration feature](/azure/app-service/overview-vnet-integration). 
 
 After the web app is deployed, from the Azure portal networking tab, configure the web app outbound traffic virtual network integration, choose the third subnet that you reserved for web app.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの名称変更"
}
```

### Explanation
この変更は、「データ構成に関するAzure OpenAIサービス」のドキュメントの更新です。特に、Azure OpenAI Studioという表現をAzure AI Foundryポータルに置き換える修正が行われています。この変更は、ドキュメント全体で一貫性を保ち、開発者が最新の環境を正しく認識し、使用できるようにすることを目的としています。

具体的には、データソースの追加や、パーミットグループフィールドのマッピング、外部クライアントからのアクセスに関する記述が修正されました。これにより、ユーザーはAzure AI Foundryポータルを通じて、各種の機能が正しく利用できることが強調されています。

全体として、この変更は、ユーザーの混乱を招かないようにするための重要なステップであり、最新の製品名やポータル名に関する整合性を維持するために行われています。ユーザーは、提案された手順に従って、適切に設定を行うことができるようになります。

## articles/ai-services/openai/how-to/provisioned-get-started.md{#item-c8df1c}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,6 @@ The following guide walks you through key steps in creating a provisioned deploy
 
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - Azure Contributor or Cognitive Services Contributor role 
-- Access to Azure OpenAI Studio
 
 ## Obtain/verify PTU quota availability.
 
@@ -37,9 +36,9 @@ Creating a new deployment requires available (unused) quota to cover the desired
 
 Then 200 PTUs of quota are considered used, and there are 300 PTUs available for use to create new deployments. 
 
-A default amount of global, data zone, and regional provisioned quota is assigned to eligible subscriptions in several regions. You can view the quota available to you in a region by visiting the Quotas pane in Azure AI Foundry and selecting the desired subscription and region. For example, the screenshot below shows a quota limit of 500 PTUs in West US for the selected subscription. Note that you might see lower values of available default quotas. 
+A default amount of global, data zone, and regional provisioned quota is assigned to eligible subscriptions in several regions. You can view the quota available to you in a region by visiting the Quotas pane in Azure AI Foundry portal and selecting the desired subscription and region. For example, the screenshot below shows a quota limit of 500 PTUs in West US for the selected subscription. Note that you might see lower values of available default quotas. 
 
-:::image type="content" source="../media/provisioned/available-quota.png" alt-text="A screenshot of the available quota in Azure OpenAI studio." lightbox="../media/provisioned/available-quota.png":::
+:::image type="content" source="../media/provisioned/available-quota.png" alt-text="A screenshot of the available quota in Azure AI Foundry portal." lightbox="../media/provisioned/available-quota.png":::
 
 Additional quota can be requested by clicking the Request Quota link to the right of the “Usage/Limit” column.  (This is off-screen in the screenshot above). 
 
@@ -54,16 +53,15 @@ Provisioned deployments are created via Azure OpenAI resource objects within Azu
 
 once you have verified your quota, you can create a deployment. To create a provisioned deployment, you can follow these steps; the choices described reflect the entries shown in the screenshot. 
 
-:::image type="content" source="../media/provisioned/deployment-screen.png" alt-text="Screenshot of the Azure OpenAI Studio deployment page for a provisioned deployment." lightbox="../media/provisioned/deployment-screen.png":::
+:::image type="content" source="../media/provisioned/deployment-screen.png" alt-text="Screenshot of the Azure AI Foundry portal deployment page for a provisioned deployment." lightbox="../media/provisioned/deployment-screen.png":::
 
 
 
-1.	Sign into [Azure AI Foundry](https://oai.azure.com)
+1. Sign into the [Azure AI Foundry portal](https://ai.azure.com).
 1. Choose the subscription that was enabled for provisioned deployments & select the desired resource in a region where you have the quota.
-
-3.	Under **Management** in the left-nav select **Deployments**.
-4.	Select Create new deployment and configure the following fields. Expand the **advanced options** drop-down menu.
-5.	Fill out the values in each field. Here's an example:
+1. Under **Management** in the left-nav select **Deployments**.
+1. Select Create new deployment and configure the following fields. Expand the **advanced options** drop-down menu.
+1. Fill out the values in each field. Here's an example:
 
 | Field | Description |	Example |
 |--|--|--|
@@ -74,8 +72,8 @@ once you have verified your quota, you can create a deployment. To create a prov
 | Deployment Type	|This impacts the throughput and performance. Choose Global Provisioned-Managed, DataZone Provisioned-Managed or Provisioned-Managed from the deployment dialog dropdown for your deployment 	| Provisioned-Managed |
 | Provisioned Throughput Units |	Choose the amount of throughput you wish to include in the deployment. |	100 |
 
-Important things to note: 
-* The deployment dialog contains a reminder that you can purchase an Azure Reservation for Azure OpenAI Provisioned to obtain a significant discount for a term commitment. 
+> [!NOTE]
+> The deployment dialog contains a reminder that you can purchase an Azure Reservation for Azure OpenAI Provisioned to obtain a significant discount for a term commitment. 
 
 Once you have entered the deployment settings, click **Confirm Pricing** to continue.  A pricing confirmation dialog will appear that will display the list price for the deployment, if you choose to pay for it on an hourly basis, with no Azure Reservation to provide a term discount.
 
@@ -108,16 +106,16 @@ REST, ARM template, Bicep, and Terraform can also be used to create deployments.
 
 Due to the dynamic nature of capacity availability, it is possible that the region of your selected resource might not have the service capacity to create the deployment of the specified model, version, and number of PTUs. 
 
-In this event, Azure AI Foundry will direct you to other regions with available quota and capacity to create a deployment of the desired model. If this happens, the deployment dialog will look like this: 
+In this event, the wizard in Azure AI Foundry portal will direct you to other regions with available quota and capacity to create a deployment of the desired model. If this happens, the deployment dialog will look like this: 
 
-:::image type="content" source="../media/provisioned/deployment-screen-2.png" alt-text="Screenshot of the Azure OpenAI Studio deployment page for a provisioned deployment with no capacity available." lightbox="../media/provisioned/deployment-screen-2.png":::
+:::image type="content" source="../media/provisioned/deployment-screen-2.png" alt-text="Screenshot of the Azure AI Foundry portal deployment page for a provisioned deployment with no capacity available." lightbox="../media/provisioned/deployment-screen-2.png":::
 
 Things to notice: 
 
 * A message displays showing you many PTUs you have in available quota, and how many can currently be deployed at this time. 
 * If you select a number of PTUs greater than service capacity, a message will appear that provides options for you to obtain more capacity, and a button to allow you to select an alternate region. Clicking the "See other regions" button will display a dialog that shows a list of Azure OpenAI resources where you can create a deployment, along with the maximum sized deployment that can be created based on available quota and service capacity in each region. 
 
-:::image type="content" source="../media/provisioned/choose-different-resource.png" alt-text="Screenshot of the Azure OpenAI Studio deployment page for choosing a different resource and region." lightbox="../media/provisioned/choose-different-resource.png":::
+:::image type="content" source="../media/provisioned/choose-different-resource.png" alt-text="Screenshot of the Azure AI Foundry portal deployment page for choosing a different resource and region." lightbox="../media/provisioned/choose-different-resource.png":::
 
 Selecting a resource and clicking **Switch resource** will cause the deployment dialog to redisplay using the selected resource. You can then proceed to create your deployment in the new region. 
 
@@ -167,9 +165,8 @@ The inferencing code for provisioned deployments is the same a standard deployme
 
 ## Understanding expected throughput
 The amount of throughput that you can achieve on the endpoint is a factor of the number of PTUs deployed, input size, output size, and call rate. The number of concurrent calls and total tokens processed can vary based on these values. Our recommended way for determining the throughput for your deployment is as follows:
-1. Use the Capacity calculator for a sizing estimate. You can find the capacity calculator in Azure AI Foundry under the quotas page and Provisioned tab.  
-
-2.	Benchmark the load using real traffic workload. For more information about benchmarking, see the [benchmarking](#run-a-benchmark) section.
+1. Use the Capacity calculator for a sizing estimate. You can find the capacity calculator in Azure AI Foundry portal under the quotas page and Provisioned tab.  
+1. Benchmark the load using real traffic workload. For more information about benchmarking, see the [benchmarking](#run-a-benchmark) section.
 
 
 ## Measuring your deployment utilization
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルへの参照を更新"
}
```

### Explanation
この変更は、Azure OpenAIの開始方法に関するドキュメントの更新です。特に、Azure OpenAI Studioという名称を、最新の名称である「Azure AI Foundryポータル」に置き換えています。この更新は、ドキュメント内で使用する用語の一貫性を保ち、ユーザーがより正確に情報を理解できるようにすることを目的としています。

具体的には、プロビジョニングデプロイメントの作成手順や、利用可能なPTU（Provisioned Throughput Units）クォータの確認方法、デプロイメント設定の確認方法などにおいて、Azure AI Foundryポータルへの正しい案内が行われています。また、関連するスクリーンショットもすべて新しいポータル名称に合わせて更新されています。

この変更によって、ユーザーが手順に従う際に混乱せず、新しいポータルの機能を効果的に利用できるようにし、Azureのリソース管理においてよりスムーズな体験を提供することが期待されます。全体として、情報の透明性と明確性が向上しています。

## articles/ai-services/openai/how-to/risks-safety-monitor.md{#item-b2be0b}

<details>
<summary>Diff</summary>
````diff
@@ -12,15 +12,15 @@ manager: nitinme
 
 # Use Risks & Safety monitoring in Azure AI Foundry (preview) 
 
-When you use an Azure OpenAI model deployment with a content filter, you may want to check the results of the filtering activity. You can use that information to further adjust your [filter configuration](/azure/ai-services/openai/how-to/content-filters) to serve your specific business needs and Responsible AI principles.  
+When you use an Azure OpenAI model deployment with a content filter, you might want to check the results of the filtering activity. You can use that information to further adjust your [filter configuration](/azure/ai-services/openai/how-to/content-filters) to serve your specific business needs and Responsible AI principles.  
 
-[Azure AI Foundry](https://oai.azure.com/) provides a Risks & Safety monitoring dashboard for each of your deployments that uses a content filter configuration.
+[Azure AI Foundry](https://ai.azure.com/) provides a Risks & Safety monitoring dashboard for each of your deployments that uses a content filter configuration.
 
 ## Access Risks & Safety monitoring
 
 To access Risks & Safety monitoring, you need an Azure OpenAI resource in one of the supported Azure regions: East US, Switzerland North, France Central, Sweden Central, Canada East. You also need a model deployment that uses a content filter configuration.
 
-Go to [Azure AI Foundry](https://oai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. Select a project. Then select the **Models + endpoints** tab on the left and then select your model deployment from the list. On the deployment's page, select the **Metrics** tab at the top. Then select **Open in Azure Monitor** to view the full report in the Azure portal.
+Go to [Azure AI Foundry](https://ai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. Select a project. Then select the **Models + endpoints** tab on the left and then select your model deployment from the list. On the deployment's page, select the **Metrics** tab at the top. Then select **Open in Azure Monitor** to view the full report in the Azure portal.
 
 ## Configure metrics   
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI FoundryポータルのURLを更新"
}
```

### Explanation
この変更は、「Azure AI Foundryにおけるリスクおよび安全監視」のドキュメントに対するものであり、特にAzure OpenAIのモデルデプロイメントに関連する情報の更新が含まれています。主な修正点は、Azure AI Foundryにアクセスする際のURLを古い形式から最新の形式に更新したことです。

具体的には、文中の「Azure OpenAI Studio」という表現を、「Azure AI Foundryポータル」に変更し、それに伴いURLも一致させています。これにより、ユーザーが最新のポータルにアクセスしやすくなり、コンテンツフィルタの結果を確認する際に必要な情報を確実に取得できるようになります。

また、コンテンツフィルタ設定を調整する方法や、リスクおよび安全監視ダッシュボードの利用方法についても言及されています。この更新により、ユーザーは正確なリンクを参照しながら、Azure AI Foundryを利用する際の操作を円滑に進めることができるようになります。全体として、情報の最新化とユーザビリティの向上が図られています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ Support for structured outputs was first added in API version `2024-08-01-previe
 
 # [Python (Microsoft Entra ID)](#tab/python-secure)
 
-You can use [`Pydantic`](https://docs.pydantic.dev/latest/) to define object schemas in Python. Depending on what version of the [OpenAI](https://pypi.org/project/openai/) and [`Pydantic` libraries](https://pypi.org/project/pydantic/) you're running you may need to upgrade to a newer version. These examples were tested against `openai 1.42.0` and `pydantic 2.8.2`.
+You can use [`Pydantic`](https://docs.pydantic.dev/latest/) to define object schemas in Python. Depending on what version of the [OpenAI](https://pypi.org/project/openai/) and [`Pydantic` libraries](https://pypi.org/project/pydantic/) you're running you might need to upgrade to a newer version. These examples were tested against `openai 1.42.0` and `pydantic 2.8.2`.
 
 ```cmd
 pip install openai pydantic --upgrade
@@ -120,7 +120,7 @@ name='Science Fair' date='Friday' participants=['Alice', 'Bob']
 
 # [Python (key-based auth)](#tab/python)
 
-You can use [`Pydantic`](https://docs.pydantic.dev/latest/) to define object schemas in Python. Depending on what version of the [OpenAI](https://pypi.org/project/openai/) and [`Pydantic` libraries](https://pypi.org/project/pydantic/) you're running you may need to upgrade to a newer version. These examples were tested against `openai 1.42.0` and `pydantic 2.8.2`.
+You can use [`Pydantic`](https://docs.pydantic.dev/latest/) to define object schemas in Python. Depending on what version of the [OpenAI](https://pypi.org/project/openai/) and [`Pydantic` libraries](https://pypi.org/project/pydantic/) you're running you might need to upgrade to a newer version. These examples were tested against `openai 1.42.0` and `pydantic 2.8.2`.
 
 ```cmd
 pip install openai pydantic --upgrade
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pydanticバージョン更新の表現を統一"
}
```

### Explanation
この変更は、「構造化出力」に関するドキュメントに対して行われたもので、特にPythonにおける`Pydantic`ライブラリの使用に関する記述に対する小さな修正です。修正内容は、文中の「may need to」から「might need to」への変更で、より一貫性のある表現を使用しています。

具体的には、OpenAIとPydanticライブラリのバージョンに応じて、ユーザーが新しいバージョンへのアップグレードが必要な場合があることを注意喚起する部分が対象です。どちらの表現も同様の意味ですが、「might」を使用することで、より柔らかいニュアンスを持たせています。

この更新により、文書全体のトーンがより一貫し、ユーザーにとって読みやすくなっています。また、正確な情報を知っていることが重要な開発者向けのドキュメントにおいて、適切な表現を使用することが意義のある変更です。全体として、この修正は文書の品質向上に寄与しています。

## articles/ai-services/openai/how-to/use-blocklists.md{#item-e99db7}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ms.author: pafarley
 
 # Use a blocklist with Azure OpenAI
 
-The configurable content filters are sufficient for most content moderation needs. However, you may need to filter terms specific to your use case. 
+The configurable content filters are sufficient for most content moderation needs. However, you might need to filter terms specific to your use case. 
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フィルター表現の変更"
}
```

### Explanation
この変更は、「Azure OpenAIでのブロックリストの使用」に関するドキュメントの内容に対して行われたもので、文中の表現を微修正しています。具体的には、文の「may need to」を「might need to」に変更することにより、表現に一貫性を持たせることを目的としています。

元の文は、サConfigure可能なコンテンツフィルターが大多数のコンテンツモデレーションニーズに対して十分である一方で、特定のユースケースに応じて特定の用語をフィルタリングする必要があるかもしれないことを説明しています。修正された文では、同じ内容をより柔らかい表現で伝えており、全体的にユーザーに対する配慮が感じられるトーンに調整されています。

この変更によって、文章のトーンが改善され、ユーザーが情報を受け取る際のハードルが下がることが期待されます。全体として、文書の質と読みやすさを向上させるための小規模な修正として重要です。

## articles/ai-services/openai/how-to/use-web-app.md{#item-802413}

<details>
<summary>Diff</summary>
````diff
@@ -7,23 +7,23 @@ ms.service: azure-ai-openai
 ms.topic: how-to
 author: aahill
 ms.author: aahi
-ms.date: 08/09/2024
+ms.date: 01/08/2025
 recommendations: false
 ---
 
 
 # Use the Azure OpenAI web app
 
-Along with Azure AI Foundry, Azure OpenAI Studio, APIs, and SDKs, you can use the customizable standalone web app to interact with Azure OpenAI models by using a graphical user interface. Key features include:
+Along with Azure AI Foundry portal, APIs, and SDKs, you can use the customizable standalone web app to interact with Azure OpenAI models by using a graphical user interface. Key features include:
 * Connectivity with multiple data sources to support rich querying and retrieval-augmented generation, including Azure AI Search, Prompt Flow, and more.
 * Conversation history and user feedback collection through Cosmos DB.
 * Authentication with role-based access control via Microsoft Entra ID.
 * Customization of the user interface, data sources, and features using environment variables (no-code via Azure portal).
-* Support for modifying the underlying web application source code as an open-source repository. 
+* Sample source code for the web app is available on [GitHub](https://github.com/microsoft/sample-app-aoai-chatGPT). Source code is provided "as is" and as a sample only. Customers are responsible for all customization and implementation of their web apps.
 
-You can deploy the app by using either [Azure AI Foundry](/azure/ai-studio/tutorials/deploy-chat-web-app) or [Azure OpenAI Studio](/azure/ai-services/openai/use-your-data-quickstart), or through a manual deployment through the Azure portal or the Azure Developer CLI via your local machine [(instructions available at the repository here)](https://github.com/microsoft/sample-app-aoai-chatGPT). Depending on your deployment channel, you can preload a data source to chat with via the web application, but this can be changed after deployment. 
+You can deploy the app via the [Azure AI Foundry portal](/azure/ai-studio/tutorials/deploy-chat-web-app), the [Azure portal](https://portal.azure.com), or the Azure Developer CLI via your local machine [(instructions available at the repository here)](https://github.com/microsoft/sample-app-aoai-chatGPT). Depending on your deployment channel, you can preload a data source to chat with via the web application, but this can be changed after deployment. 
 
-For Azure OpenAI beginners aspiring to chat with their data through the web application, [Azure AI Foundry](/azure/ai-studio/tutorials/deploy-chat-web-app) is the recommended medium for initial deployment and data source configuration.
+For Azure OpenAI beginners aspiring to chat with their data through the web application, [Azure AI Foundry portal](/azure/ai-studio/tutorials/deploy-chat-web-app) is the recommended medium for initial deployment and data source configuration.
 
 ![Screenshot that shows the web app interface.](../media/use-your-data/web-app.png)
 
@@ -59,8 +59,6 @@ When you're customizing the app, we recommend:
 
 - Updating the app settings for each of your deployed apps to use new API keys after you rotate keys for your Azure OpenAI or Azure AI Search resource.
 
-Sample source code for the web app is available on [GitHub](https://github.com/microsoft/sample-app-aoai-chatGPT). Source code is provided "as is" and as a sample only. Customers are responsible for all customization and implementation of their web apps.
-
 ## Modifying the application user interface
 
 The environment variables relevant to user interface customization are:
@@ -119,7 +117,7 @@ To modify the application user interface, follow the instructions in the previou
 
 You can turn on chat history for your users of the web app. When you turn on the feature, users have access to their individual previous queries and responses.
 
-To turn on chat history, deploy or redeploy your model as a web app by using [Azure OpenAI Studio](https://oai.azure.com/portal) or [Azure AI Foundry](https://ai.azure.com/) and select **Enable chat history and user feedback in the web app**.
+To turn on chat history, deploy or redeploy your model as a web app by using [Azure AI Foundry portal](https://ai.azure.com/) and select **Enable chat history and user feedback in the web app**.
 
 :::image type="content" source="../media/use-your-data/enable-chat-history.png" alt-text="Screenshot of the checkbox for enabling chat history in Azure OpenAI or Azure AI Foundry." lightbox="../media/use-your-data/enable-chat-history.png":::
 
@@ -164,13 +162,9 @@ This can be accomplished using the Advanced edit or simple Edit options as previ
 
 ## Connecting to Azure AI Search and uploaded files as a data source
 
-### Using Azure AI Foundry
-
-Follow [this tutorial on integrating Azure AI Search with Azure AI Foundry](/azure/ai-studio/tutorials/deploy-chat-web-app#add-your-data-and-try-the-chat-model-again) and redeploy your application.
-
-### Using Azure OpenAI Studio
+### Using Azure AI Foundry portal
 
-Follow [this tutorial on integrating Azure AI Search with OpenAI Studio](/azure/ai-services/openai/use-your-data-quickstart#add-your-data-using-azure-openai-studio) and redeploy your application.
+Follow [this tutorial on integrating Azure AI Search with Azure AI Foundry](/azure/ai-studio/tutorials/deploy-chat-web-app#add-your-data-and-try-the-chat-model-again) or [quickstart](/azure/ai-services/openai/use-your-data-quickstart#add-your-data) and redeploy your application.
 
 ### Using environment variables
 
@@ -181,7 +175,7 @@ To connect to Azure AI Search without redeploying your app, you can modify the f
     - Data type: text
 - `AZURE_SEARCH_INDEX`: This is the name of your Azure AI Search instance's index name.
     - Data type: text
-- `AZURE_SEARCH_KEY`: This is the authentication key of your Azure AI Search instance. Optional if using Microsoft Entra ID for authentication.
+- `AZURE_SEARCH_KEY`: This is the authentication key of your Azure AI Search instance. Optional if using the recommended Microsoft Entra ID for authentication.
     - Data type: text
 
 ### Further customization scenarios using environment variables
@@ -195,15 +189,15 @@ To connect to Azure AI Search without redeploying your app, you can modify the f
 - `AZURE_SEARCH_ENABLE_IN_DOMAIN`: Limits responses to queries related only to your data.
     - Data type: boolean, should be set to `True`.
 - `AZURE_SEARCH_CONTENT_COLUMNS`: Specifies the list of fields in your Azure AI Search index that contain the text content of your documents, used when formulating a bot response.
-    - Data type: text, defaults to `content` if deployed from Azure AI Foundry or Azure OpenAI Studio,
+    - Data type: text, defaults to `content` if deployed from Azure AI Foundry portal,
 - `AZURE_SEARCH_FILENAME_COLUMN`: Specifies the field from your Azure AI Search index that provides a unique identifier of the source data to display in the UI.
-    - Data type: text, defaults to `filepath` if deployed from Azure AI Foundry or Azure OpenAI Studio,
+    - Data type: text, defaults to `filepath` if deployed from Azure AI Foundry portal,
 - `AZURE_SEARCH_TITLE_COLUMN`: Specifies the field from your Azure AI Search index that provides a relevant title or header for your data content to display in the UI.
-    - Data type: text, defaults to `title` if deployed from Azure AI Foundry or Azure OpenAI Studio,
+    - Data type: text, defaults to `title` if deployed from Azure AI Foundry portal,
 - `AZURE_SEARCH_URL_COLUMN`: Specifies the field from your Azure AI Search index that contains a URL for the document.
-    - Data type: text, defaults to `url` if deployed from Azure AI Foundry or Azure OpenAI Studio,
+    - Data type: text, defaults to `url` if deployed from Azure AI Foundry portal,
 - `AZURE_SEARCH_VECTOR_COLUMNS`: Specifies the list of fields in your Azure AI Search index that contain vector embeddings of your documents, used when formulating a bot response.
-    - Data type: text, defaults to `contentVector` if deployed from Azure AI Foundry or Azure OpenAI Studio,
+    - Data type: text, defaults to `contentVector` if deployed from Azure AI Foundry portal,
 - `AZURE_SEARCH_QUERY_TYPE`: Specifies the query type to use: `simple`, `semantic`, `vector`, `vectorSimpleHybrid`, or `vectorSemanticHybrid`. This setting takes precedence over `AZURE_SEARCH_USE_SEMANTIC_SEARCH`.
     - Data type: text, we recommend testing with `vectorSemanticHybrid`.
 - `AZURE_SEARCH_PERMITTED_GROUPS_COLUMN`: Specifies the field from your Azure AI Search index that contains Microsoft Entra group IDs, determining document-level access control.
@@ -408,7 +402,7 @@ If you customized or changed the app's source code, you need to update your app'
 
 ## Deleting your Cosmos DB instance
 
-Deleting your web app doesn't delete your Cosmos DB instance automatically. To delete your Cosmos DB instance along with all stored chats, you need to go to the associated resource in the [Azure portal](https://portal.azure.com) and delete it. If you delete the Cosmos DB resource but keep the chat history option selected on subsequent updates from the Azure OpenAI Studio, the application notifies the user of a connection error. However, the user can continue to use the web app without access to the chat history.
+Deleting your web app doesn't delete your Cosmos DB instance automatically. To delete your Cosmos DB instance along with all stored chats, you need to go to the associated resource in the [Azure portal](https://portal.azure.com) and delete it. If you delete the Cosmos DB resource but keep the chat history option selected on subsequent updates from the Azure AI Foundry portal, the application notifies the user of a connection error. However, the user can continue to use the web app without access to the chat history.
 
 ## Enabling Microsoft Entra ID authentication between services
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と日付の更新"
}
```

### Explanation
この変更は、「Azure OpenAIウェブアプリの使用」に関する文書に対するもので、主に用語の統一と日付の修正が行われました。具体的には、さまざまな部分で「Azure AI Foundry」から「Azure AI Foundry portal」への表現の統一が図られています。また、文書の日付が「08/09/2024」から「01/08/2025」に変更されました。

文中の重要な変更点には以下が含まれます：

1. 語句の修正:
   - 「Azure AI Foundry」の言及を「Azure AI Foundry portal」に統一することで、一貫性を持たせています。
   
2. 提供する情報の明確化:
   - ウェブアプリのサンプルソースコードに関する記述が明確にされ、ユーザーに対してカスタマイズと実装の責任があることが強調されています。

3. デプロイ方法の説明に改良が加わり、AzureのポータルやAzure Developer CLIを使用した新しい情報が追加されています。

この修正は、全体的な文書の質の向上を目的としており、ユーザーに対してより正確で一貫した情報を提供することに貢献しています。特に初心者にとってわかりやすい内容にすることで、文書の有用性が高まっています。

## articles/ai-services/openai/how-to/working-with-models.md{#item-7ec098}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ You can get a list of models that are available for both inference and fine-tuni
 
 Azure OpenAI now supports automatic updates for select model deployments. On models where automatic update support is available, a model version drop-down is visible in Azure AI Foundry portal under **Deployments** and **Edit**:
 
-:::image type="content" source="../media/models/auto-update-new.png" alt-text="Screenshot of the deploy model UI of Azure AI Foundry." lightbox="../media/models/auto-update-new.png":::
+:::image type="content" source="../media/models/auto-update-new.png" alt-text="Screenshot of the deploy model UI in the Azure AI Foundry portal." lightbox="../media/models/auto-update-new.png":::
 
 You can learn more about Azure OpenAI model versions and how they work in the [Azure OpenAI model versions](../concepts/model-versions.md) article.
 
@@ -40,13 +40,13 @@ When you select a specific model version for a deployment, this version remains
 
 ## Viewing retirement dates
 
-For currently deployed models, from Azure AI Foundry select **Deployments**:
+For currently deployed models, in the Azure AI Foundry portal select **Deployments**:
 
-:::image type="content" source="../media/models/deployments-new.png" alt-text="Screenshot of the deployment UI of Azure AI Foundry." lightbox="../media/models/deployments-new.png":::
+:::image type="content" source="../media/models/deployments-new.png" alt-text="Screenshot of the deployment UI of the Azure AI Foundry portal." lightbox="../media/models/deployments-new.png":::
 
 ## Model deployment upgrade configuration
 
-You can check what model upgrade options are set for previously deployed models in [Azure AI Foundry](https://oai.azure.com). Select **Deployments** > Under the deployment name column select one of the deployment names that are highlighted in blue.
+You can check what model upgrade options are set for previously deployed models in the [Azure AI Foundry portal](https://ai.azure.com). Select **Deployments** > Under the deployment name column select one of the deployment names that are highlighted in blue.
 
 Selecting a deployment name opens the **Properties** for the model deployment. You can view what upgrade options are set for your deployment under **Version update policy**:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語の統一と文書の明確化"
}
```

### Explanation
この変更は、「モデルの操作」に関する文書に対して行われたもので、主に用語の一貫性の向上と文書の明確化が目的とされています。具体的には、Azure AI Foundryポータルに関連する表現を修正し、ユーザーに対してより明確な指示を提供しています。

主な変更点は以下の通りです：

1. 言語の統一:
   - 「Azure AI Foundry」から「Azure AI Foundry portal」への表現変更が行われ、文書全体での用語の一貫性が確保されています。

2. スクリーンショットの説明の明確化:
   - スクリーンショットの説明文が「Azure AI FoundryのUI」から「Azure AI Foundry portalのUI」に変更されており、これにより対象となるインターフェースがより具体的に示されています。

3. モデルのデプロイやアップグレード設定に関する説明の修正:
   - 説明内容が少し調整されており、ユーザーがモデルのデプロイや設定の手順を理解しやすくなるように工夫されています。

この修正によって、利用者が情報をより明確に理解しやすくなることが期待され、多くのユーザーにとって操作がスムーズになることに貢献しています。全体として、文書の質と可読性が向上しています。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Information on the division of control plane and data plane API sur
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 11/01/2024
+ms.date: 01/08/2024
 ---
 
 
@@ -22,8 +22,8 @@ Each API surface/specification encapsulates a different set of Azure OpenAI capa
 | API | Latest preview release | Latest GA release | Specifications | Description |
 |:---|:----|:----|:----|:---|
 | **Control plane** | [`2024-06-01-preview`](/rest/api/aiservices/accountmanagement/operation-groups?view=rest-aiservices-accountmanagement-2024-06-01-preview&preserve-view=true) | [`2024-10-01`](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2024-10-01&tabs=HTTP&preserve-view=true) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices) | Azure OpenAI shares a common control plane with all other Azure AI Services. The control plane API is used for things like [creating Azure OpenAI resources](/rest/api/aiservices/accountmanagement/accounts/create?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), [model deployment](/rest/api/aiservices/accountmanagement/deployments/create-or-update?view=rest-aiservices-accountmanagement-2023-05-01&tabs=HTTP&preserve-view=true), and other higher level resource management tasks. The control plane also governs what is possible to do with capabilities like Azure Resource Manager, Bicep, Terraform, and Azure CLI.|
-| **Data plane - authoring** | `2024-10-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
-| **Data plane - inference** | [`2024-10-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
+| **Data plane - authoring** | `2024-12-01-preview` | `2024-10-21` | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/authoring) | The data plane authoring API controls [fine-tuning](/rest/api/azureopenai/fine-tuning?view=rest-azureopenai-2024-08-01-preview&preserve-view=true), [file-upload](/rest/api/azureopenai/files/upload?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [ingestion jobs](/rest/api/azureopenai/ingestion-jobs/create?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true), [batch](/rest/api/azureopenai/batch?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true) and certain [model level queries](/rest/api/azureopenai/models/get?view=rest-azureopenai-2024-08-01-preview&tabs=HTTP&preserve-view=true)
+| **Data plane - inference** | [`2024-12-01-preview`](/azure/ai-services/openai/reference-preview#data-plane-inference) | [`2024-10-21`](/azure/ai-services/openai/reference#data-plane-inference) | [Spec files](https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI/inference) | The data plane inference API provides the inference capabilities/endpoints for features like completions, chat completions, embeddings, speech/whisper, on your data, Dall-e, assistants, etc. |
 
 ## Authentication
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIバージョンの更新と日付修正"
}
```

### Explanation
この変更は、「APIサーフェス」に関する文書に対するもので、主にAPIバージョンの情報を更新し、日付を修正することを目的としています。以下が主な変更点です：

1. 日付の修正:
   - 文書の日付が「11/01/2024」から「01/08/2024」に変更され、更新の時期が明確になりました。この変更は、文書の鮮度を保つために重要です。

2. APIバージョンの更新:
   - Data plane APIのバージョンに変更が加えられています。「Data plane - authoring」と「Data plane - inference」の各セクションの最新プレビューリリースが「2024-10-01-preview」から「2024-12-01-preview」に更新されており、最新のリリース情報が反映されています。
   - これにより、ユーザーは最新のAPI動向に関する正確な情報を得ることができ、適切な使用方法を理解しやすくなります。

3. 表の整備:
   - 表形式で各APIの詳細が整理され、リリースバージョンと仕様へのリンクが提供されているため、利用者が必要な情報に迅速にアクセスできるよう配慮されています。

この修正により、文書は最新の情報を反映し、利用者に対してなお一層明確で信頼性の高い内容を提供することが目的とされています。全体的に、ユーザーの利便性が向上し、APIの利用における誤解を減らす効果が期待されます。

## articles/ai-services/openai/includes/api-versions/latest-inference-preview.md{#item-24bf0f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新の推論APIバージョンに関する内容の大幅な更新"
}
```

### Explanation
この変更は、「最新の推論APIバージョン」に関する文書に対するもので、大幅な内容の更新が行われています。主な変更点は以下の通りです：

1. コンテンツの追加:
   - 文書に227行の新しい情報が追加され、推論APIの最新の機能や仕様についての詳細が豊富に盛り込まれています。これにより、ユーザーがAPIを効果的に利用するための参考情報が充実しています。

2. コンテンツの削除:
   - 同時に163行が削除されており、古い情報や不要な内容が整理されています。これにより、文書全体がよりクリアで、ユーザーが必要な情報に迅速にアクセスできるようになっています。

3. 構造の改良:
   - 大幅な変更により、情報がより使いやすく整理されている可能性が高く、推論APIに関する最新の動向を反映した明確なガイドラインとして機能しています。

この修正は、最新のAPI使用に関する情報を提供することを目的としており、ユーザーの理解を助け、APIの適切な利用を促すことが期待されています。全体的に、文書の質と有用性が向上し、開発者やユーザーにとっての利便性が増しています。

## articles/ai-services/openai/includes/assistants-env-var-key.md{#item-670ce2}

<details>
<summary>Diff</summary>
````diff
@@ -1,17 +0,0 @@
----
-manager: nitinme
-author: aahill
-ms.author: aahi
-ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 10/09/2024
-ms.custom: devex-track-js, devex-track-typescript
----
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. |
-| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
-| `AZURE_OPENAI_DEPLOYMENT_NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Model Deployments** in the Azure portal.|
-| `OPENAI_API_VERSION`|Learn more about [API Versions](/azure/ai-services/openai/api-version-deprecation).|
-
-Learn more about [finding API keys](/azure/ai-services/cognitive-services-environment-variables) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "環境変数に関する文書の削除"
}
```

### Explanation
この変更は、「アシスタント環境変数キー」に関する文書が削除されたことを示しています。具体的な変更点は以下の通りです：

1. コンテンツの削除:
   - 文書全体が17行削除され、環境変数に関する情報が完全に消失しました。これにより、ユーザーはこの特定の情報源からは環境変数やそれに関連する設定方法についての指示を得ることができなくなります。

2. 新たな参照先が必要:
   - 環境変数に関する重要な情報が削除されたため、ユーザーは新たに他の資料や文書を参照する必要があります。特に、AzureポータルからのAPIキーの取得方法や環境変数の設定方法に関する情報が必要です。

この変更は、文書が不要であるとみなされたか、または情報が他の資料に統一されるために移動された可能性がありますが、利用者にとっては特定の設定情報が得られないという破壊的な影響を与える可能性があります。全体として、エコシステム内での情報アクセスが制限されることになり、特に初めてAzure OpenAIサービスを使うユーザーにとっての不便さが増すことが懸念されます。

## articles/ai-services/openai/includes/assistants-env-var-without-key.md{#item-039e55}

<details>
<summary>Diff</summary>
````diff
@@ -1,16 +0,0 @@
----
-manager: nitinme
-author: aahill
-ms.author: aahi
-ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 10/0//2024
-ms.custom: devex-track-js, devex-track-typescript
----
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. |
-| `AZURE_OPENAI_DEPLOYMENT_NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Model Deployments** in the Azure portal.|
-| `OPENAI_API_VERSION`|Learn more about [API Versions](/azure/ai-services/openai/api-version-deprecation).|
-
-Learn more about [keyless authentication](/azure/ai-services/authentication) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "APIキーなしのアシスタント環境変数に関する文書の削除"
}
```

### Explanation
この変更は、「APIキーなしのアシスタント環境変数」に関連する文書が削除されたことを示しています。具体的な変更点は以下の通りです：

1. コンテンツの削除:
   - 文書全体が16行削除され、特定の環境変数に関する情報提供が停止しました。この情報には、Azureポータルでのリソースの確認時に得られる重要な環境変数が含まれていました。

2. 利用可能な情報の消失:
   - `AZURE_OPENAI_ENDPOINT`や`AZURE_OPENAI_DEPLOYMENT_NAME`などの変数に関する情報が削除され、ユーザーはこれに対する情報を他の資料から探さなければならなくなります。特に、これらの変数がどのように取得されるかについての具体的な指示が欠落しています。

3. 別の資料への依存:
   - 環境変数の設定やAPIキーなしの認証方法に関する情報は、他の文書に移動された可能性があります。これにより、ユーザーはアクセスする情報源が分散し、情報を見つけるのが難しくなる可能性があります。

この変更は、関連情報の統合や改善を目的としている可能性がありますが、利用者にとっては重要な情報が失われるという破壊的な影響があるため、特に初めてAzure OpenAIサービスを使用するユーザーにとっての不便さが増すかもしれません。全体として、アクセス不便性がかかることで、ユーザー体験に悪影響を及ぼす可能性があります。

## articles/ai-services/openai/includes/assistants-javascript.md{#item-ad3627}

<details>
<summary>Diff</summary>
````diff
@@ -22,13 +22,11 @@ ms.custom: passwordless-ts, devex-track-js
 - We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI Service.
 - An Azure OpenAI resource with the `gpt-4 (1106-preview)` model deployed was used testing this example. 
 
-## Microsoft Entra ID authentication is recommended
+### Microsoft Entra ID prerequisites
 
-For _keyless_ authentication, you need to 
-
-1. Use the `@azure/identity` package.
-1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
-1. Sign in with the Azure CLI such as `az login`.
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
 ## Set up
 
@@ -64,18 +62,10 @@ For _keyless_ authentication, you need to
     npm install @azure/identity
     ```
 
-## Retrieve resource information
-
-#### [Microsoft Entra ID](#tab/javascript-keyless)
-
-[!INCLUDE [assistants-keyless-environment-variables](assistants-env-var-without-key.md)]
 
+## Retrieve resource information
 
-#### [API key](#tab/javascript-key)
-
-[!INCLUDE [assistants-key-environment-variables](assistants-env-var-key.md)]
-
----
+[!INCLUDE [resource authentication](resource-auth.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
@@ -98,7 +88,7 @@ An individual assistant can access up to 128 tools including `code interpreter`,
     
 ## Create a new JavaScript application
 
-#### [Microsoft Entra ID](#tab/javascript-keyless)
+#### [Microsoft Entra ID](#tab/keyless)
 
 1. Create the `index.js` file with the following code:
 
@@ -205,7 +195,7 @@ An individual assistant can access up to 128 tools including `code interpreter`,
 
 
 
-#### [API key](#tab/javascript-key)
+#### [API key](#tab/api-key)
 
 1. Create the `index.js` file with the following code:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptアシスタントに関するドキュメントの修正"
}
```

### Explanation
この変更は、JavaScriptアシスタントに関するドキュメントが更新されたことを示しています。具体的な変更点は以下の通りです：

1. 見出しの変更:
   - 「Microsoft Entra ID認証の推奨」が「Microsoft Entra IDの前提条件」に変更され、文書の構造が改善されました。これにより、読者が情報の目的を簡単に理解できるようになりました。

2. 説明の追加・変更:
   - キーレス認証のための提案が明確にされ、具体的なステップが追加されました。Azure CLIのインストール方法が説明に組み込まれ、新しいユーザーのためのガイダンスが強化されています。

3. テキストの整理:
   - 一部の説明文が簡略化され、重要な情報が強調されています。特に、「AZURE_OPENAI_API_KEY」環境変数が設定されていないことを確認する重要性が強調され、注意喚起が追加されました。

4. インクルードセクションの改善:
   - 環境変数に関するインクルードセクションが見直され、コードの一貫性が向上しました。ユーザーの理解を助けるためのリンクやリソースが整理され、関連情報へのアクセスが容易になっています。

この変更は、新しい情報を追加したり、既存の情報を更新したりすることによって、ドキュメントの質を向上させ、利用者に対するサポートを強化することを目的としています。全体として、ユーザーがAzure OpenAIを使用する際に必要な情報をよりスムーズに見つけられるようになっています。

## articles/ai-services/openai/includes/assistants-python.md{#item-82d745}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ ms.date: 05/22/2024
 
 ## Passwordless authentication is recommended
 
-For passwordless authentication, you need to 
+For passwordless authentication, you need to:
 
 1. Use the [azure-identity](https://pypi.org/project/azure-identity/) package.
 2. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonアシスタントに関するドキュメントの文言修正"
}
```

### Explanation
この変更は、Pythonアシスタントに関するドキュメントの文言を修正したことを示しています。具体的には、パスワードなし認証に関する説明が若干の修正を受けています：

1. 表現の変更:
   - 文中の「、」が「:」に変更され、リストの導入部分がより明確になりました。これは、リストが続くことを示す文法的な改善であり、読者にとっての可読性が向上します。

2. 説明の整合性:
   - パスワードなし認証に関するガイドラインとして、具体的なステップの導入を明確にすることで、利用者が必要な情報を一目で理解しやすくなっています。

この変更は小規模ですが、文書の明瞭さを向上させ、ユーザーが情報をより簡単に利用できるようにすることを目的としています。全体として、ユーザーに対してより良い体験を提供するための文書の質を高めるための一環です。

## articles/ai-services/openai/includes/assistants-studio.md{#item-23d0ea}

<details>
<summary>Diff</summary>
````diff
@@ -1,126 +0,0 @@
----
-title: 'Quickstart: Use Azure OpenAI Assistants (Preview) via the Azure OpenAI Studio'
-titleSuffix: Azure OpenAI
-description: Walkthrough on how to get started with Azure OpenAI and make your first completions call with Azure OpenAI Studio. 
-manager: nitinme
-author: aahill
-ms.author: aahi
-ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 05/31/2024
----
-
-## Prerequisites
-
-- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-- An Azure OpenAI resource with a [compatible model in a supported region](../concepts/models.md#assistants-preview).
-- We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI Service.
-
-## Go to the Azure OpenAI Studio
-
-Navigate to Azure OpenAI Studio at <a href="https://oai.azure.com/" target="_blank">https://oai.azure.com/</a> and sign-in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
-
-From the Azure OpenAI Studio landing page launch the Assistant's playground from the left-hand navigation **Playground** > **Assistants (Preview)**
-
-:::image type="content" source="../media/quickstarts/assistants-studio.png" alt-text="Screenshot of the Azure OpenAI Studio landing page." lightbox="../media/quickstarts/assistants-studio.png":::
-
-## Playground
-
-The Assistants playground allows you to explore, prototype, and test AI Assistants without needing to run any code. From this page, you can quickly iterate and experiment with new ideas.
-
-:::image type="content" source="../media/quickstarts/assistants-playground.png" alt-text="Screenshot of the Assistant configuration screen without all the values filled in." lightbox="../media/quickstarts/assistants-playground.png":::
-
-### Assistant setup
-
-Use the **Assistant setup** pane to create a new AI assistant or to select an existing assistant. 
-
-| **Name** | **Description** |
-|:---|:---|
-| **Assistant name** | Your deployment name that is associated with a specific model. |
-| **Instructions** | Instructions are similar to system messages this is where you give the model guidance about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses. You can also provide examples of the steps it should take when answering responses. |
-| **Deployment** | This is where you set which model deployment to use with your assistant. |
-| **Functions**| Create custom function definitions for the models to formulate API calls and structure data outputs based on your specifications |
-| **Code interpreter** | Code interpreter provides access to a sandboxed Python environment that can be used to allow the model to test and execute code. |
-| **Files** | You can upload up to 20 files, with a max file size of 512 MB to use with tools. You can upload up to 10,000 files using [Azure AI Foundry portal](../assistants-quickstart.md?pivots=ai-foundry-portal). |
-
-### Tools
-
-An individual assistant can access up to 128 tools including `code interpreter`, as well as any custom tools you create via [functions](../how-to/assistant-functions.md).
-
-### Chat session
-
-Chat session also known as a *thread* within the Assistant's API is where the conversation between the user and assistant occurs. Unlike traditional chat completion calls there is no limit to the number of messages in a thread. The assistant will automatically compress requests to fit the input token limit of the model.
-
-This also means that you are not controlling how many tokens are passed to the model during each turn of the conversation. Managing tokens is abstracted away and handled entirely by the Assistants API.
-
-Select the **Clear chat** button to delete the current conversation history.
-
-Underneath the text input box there are two buttons:
-
-- Add a message without run.
-- Add and run.
-
-### Logs
-
-Logs provide a detailed snapshot of what the assistant API activity.
-
-### Show panels
-
-By default there are three panels: assistant setup, chat session, and Logs. **Show panels** allows you to add, remove, and rearrange the panels. If you ever close a panel and need to get it back, use **Show panels** to restore the lost panel.
-
-## Create your first assistant
-
-1. From the assistant setup drop-down, select **New**
-2. Give your Assistant a name
-3. Enter the following instructions "You are an AI assistant that can write code to help answer math questions"
-4. Select a deployment of `gpt-4 (1106-preview)`. The dropdown will display your custom deployment names so if your model/deployment names are different you should choose a deployment where the underlying model is equivalent to the 1106-preview model.
-5. Select the toggle enabling code interpreter.
-6. Select Save.
-
-    :::image type="content" source="../media/quickstarts/assistant-configuration.png" alt-text="Screenshot of the assistant with configuration details entered." lightbox="../media/quickstarts/assistant-configuration.png":::
-
-7. Enter a question for the assistant to answer: "I need to solve the equation `3x + 11 = 14`. Can you help me?"
-8. Select the **Add and run button** :::image type="icon" source="../media/quickstarts/run.png":::
-
-    ```output
-    The solution to the equation (3x + 11 = 14) is (x = 1).
-    ```
-
-    While we can see that answer is correct, to confirm that the model used code interpreter to get to this answer, and that the code it wrote is valid rather than just repeating an answer from the model's training data we'll ask another question.
-
-9. Enter the follow-up question: "Show me the code you ran to get this solution."
-
-    ```output
-    Certainly! Here's the Python code I ran to find the solution for the equation (3x + 11 = 14):
-    ```
-
-    ```python
-    from sympy import symbols, Eq, solve  
-      
-    # Define the variable  
-    x = symbols('x')  
-      
-    # Define the equation  
-    equation = Eq(3*x + 11, 14)  
-      
-    # Solve the equation  
-    solution = solve(equation, x)  
-    solution  
-    ```
-
-:::image type="content" source="../media/quickstarts/assistant-session.png" alt-text="Screenshot of conversation session in the Assistant playground." lightbox="../media/quickstarts/assistant-session.png":::
-
-You could also consult the logs in the right-hand panel to confirm that code interpreter was used and to validate the code that was run to generate the response. It is important to remember that while code interpreter gives the model the capability to respond to more complex math questions by converting the questions into code and running in a sandboxed Python environment, you still need to validate the response to confirm that the model correctly translated your question into a valid representation in code.
-
-## Clean up resources
-
-If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
-
-- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
-- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
-
-## See also
-
-* Learn more about how to use Assistants with our [How-to guide on Assistants](../how-to/assistant.md).
-* [Azure OpenAI Assistants API samples](https://github.com/Azure-Samples/azureai-samples/tree/main/scenarios/Assistants)
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azure OpenAI Studioに関するドキュメントの削除"
}
```

### Explanation
この変更は、Azure OpenAI Studioに関するドキュメントの全削除を示しています。この決定は、以下の理由から重要な影響をもたらします。

1. **コンテンツの完全な削除**:
   - 「assistants-studio.md」というファイルが完全に削除され、これによりAzure OpenAI Studioの使用方法やインターフェースに関する情報が一切提供されなくなります。この変更は、ユーザーが必要な情報を欠くことになるため、重要な機能や手順のガイダンスが喪失します。

2. **ドキュメントの再構成必要性**:
   - このドキュメントが削除されることにより、他の関連ドキュメントが新たに追加の情報やガイダンスを提供する必要が生じるかもしれません。たとえば、他の場所に新しい情報を組み込む必要があるため、利用者が必要とするすべてのリソースを見つけることが難しくなる可能性があります。

3. **影響を受けるユーザー**:
   - Azure OpenAI Studioに依存していたユーザーにとって、この変更は操作や探索に関する明確な手順を失うことを意味します。特に、具体的な使い方やチュートリアルが欠如することにより、新たなユーザーがスムーズにサービスを利用することが難しくなるでしょう。

全体として、Azure OpenAI Studioに関連する文書の削除は、ユーザーの体験に大きな影響を及ぼし、代替の情報源やリファレンスが必要になることを示唆しています。今後、他の関連するドキュメントやリソースに対する再評価が求められる可能性があります。

## articles/ai-services/openai/includes/assistants-typescript.md{#item-3195a9}

<details>
<summary>Diff</summary>
````diff
@@ -23,13 +23,11 @@ ms.custom: passwordless-js, devex-track-typescript
 - We recommend reviewing the [Responsible AI transparency note](/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext&tabs=text) and other [Responsible AI resources](/legal/cognitive-services/openai/overview?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext) to familiarize yourself with the capabilities and limitations of the Azure OpenAI Service.
 - An Azure OpenAI resource with the `gpt-4 (1106-preview)` model deployed was used testing this example. 
 
-## Passwordless authentication is recommended
+### Microsoft Entra ID prerequisites
 
-For passwordless authentication, you need to 
-
-1. Use the `@azure/identity` package.
-1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
-1. Sign in with the Azure CLI such as `az login`.
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
 ## Set up
 
@@ -67,22 +65,11 @@ For passwordless authentication, you need to
 
 ## Retrieve resource information
 
-
-#### [Microsoft Entra ID](#tab/typescript-keyless)
-
-[!INCLUDE [assistants-keyless-environment-variables](assistants-env-var-without-key.md)]
-
-
-#### [API key](#tab/typescript-key)
-
-[!INCLUDE [assistants-key-environment-variables](assistants-env-var-key.md)]
-
----
+[!INCLUDE [resource authentication](resource-auth.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
-
 ## Create an assistant
 
 In our code we're going to specify the following values:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Entra IDを用いたキーレス認証に関する文言修正"
}
```

### Explanation
この変更は、Azure OpenAI Assistantsに関するTypeScript用のドキュメントの文言を見直すことで、キーレス認証に関連する情報を明確にしています。具体的には以下のような修正が行われています。

1. **セクションタイトルの変更**:
   - 以前の「Passwordless authentication is recommended」というタイトルが、「Microsoft Entra ID prerequisites」に変更されました。この変更により、トピックがより具体的かつ焦点を絞った内容になり、ユーザーがキーレス認証に関連する準備についての注意を向けることができます。

2. **手順の更新**:
   - パスワードレス認証に関する手順が明確に更新され、Microsoft Entra IDを使用するための具体的なインストール手順（Azure CLIのインストール）が追加されました。これにより、ユーザーが必要なソフトウェアをインストールする明確なガイダンスを得ることができます。

3. **文の簡略化**:
   - 説明文が簡潔になり、冗長な情報が削除され、重要な情報のみが残されました。また、手順の番号付けが整然とされ、利用者が読みやすくなっています。

4. **リソースの統合**:
   - ドキュメントの最後には、リソース認証に関する新しい情報セクションが追加され、エコシステム全体での統一性が増しています。

これらの変更は、ユーザーがAzure OpenAIの認証プロセスに関してより理解しやすく、効率的に手続きを進められるようにすることを目的としています。全体として、文書の質が向上し、ユーザーが必要な作業を正確に把握できるようになっています。

## articles/ai-services/openai/includes/chatgpt-javascript.md{#item-cbf09f}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.date: 10/22
 [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
 > [!NOTE]
-> This article has been updated to use the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you are looking for code examples for the legacy Azure OpenAI JavaScript SDK they are currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
+> This guide uses the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you're looking for code examples for the legacy Azure OpenAI JavaScript SDK, they're currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
 
 ## Prerequisites
 
@@ -23,12 +23,19 @@ ms.date: 10/22
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI Service resource with either a `gpt-35-turbo` or `gpt-4` series models deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
+### Microsoft Entra ID prerequisites
 
-## Set up
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+## Retrieve resource information
+
+[!INCLUDE [resource authentication](resource-auth.md)]
+
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
-[!INCLUDE [environment-variables](environment-variables.md)]
 
 ## Create a Node application
 
@@ -42,7 +49,7 @@ Install the required packages for JavaScript with npm from within the context of
 npm install openai @azure/identity
 ```
 
-Your app's _package.json_ file will be updated with the dependencies.
+Your app's _package.json_ file is updated with the dependencies.
 
 ## Create a sample application
 
@@ -158,7 +165,7 @@ node.exe ChatCompletion.js
 ---
 
 > [!NOTE]
-> If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You may need to remove a pre-existing environment variable for the API key from your system. Even though the Microsoft Entra ID code sample is not explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error will still be generated.
+> If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You might need to remove a preexisting environment variable for the API key from your system. Even though the Microsoft Entra ID code sample isn't explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error is still generated.
 
 
 ## Clean up resources
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI向けの最新のnpmパッケージ使用に関する文言修正"
}
```

### Explanation
この変更は、Azure OpenAIに関するJavaScriptのドキュメントを更新し、最新のnpmパッケージに基づく内容を強調しています。主な変更点は以下の通りです。

1. **文言の改善**:
   - 「This article has been updated to use the [latest OpenAI npm package]」という文言が「This guide uses the [latest OpenAI npm package]」に改訂され、より直接的な表現に変更されました。これにより、読者にとっての理解が容易になっています。

2. **Prerequisitesセクションの明確化**:
   - Microsoft Entra IDに基づくキーレス認証のための要件が明確にリストアップされ、手続きが簡潔に説明されています。特に、Azure CLIのインストールと役割の割り当てに関する指示が明確に記載されています。

3. **トラブルシューティング情報の修正**:
   - エラーメッセージに関する説明が若干の文言修正を受け、全体の文が読みやすくなっています。これにより、ユーザーがトラブルに遭遇した際の理解が向上します。

4. **新しいセクションの追加**:
   - リソース情報を取得するためのセクションが追加され、リソース認証に関する重要な情報が統合されています。これにより、ユーザーが必要な情報を一元的に取得できるようになりました。

このように、ドキュメントの更新は、ユーザーが最新の技術と手続きを容易に理解できるようにするためのものであり、Azure OpenAIの利用を促進することを目指しています。全体として、情報が整理され、文書の質が向上しています。

## articles/ai-services/openai/includes/chatgpt-studio.md{#item-ab43f3}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,7 @@ From the Azure OpenAI Studio landing page, select **Chat playground**.
 
 ## Playground
 
-Start exploring OpenAI capabilities with a no-code approach through the Azure OpenAI Studio Chat playground. From this page, you can quickly iterate and experiment with the capabilities.
+Start exploring Azure OpenAI Service capabilities with a no-code approach through the Azure OpenAI Studio Chat playground. From this page, you can quickly iterate and experiment with the capabilities.
 
 :::image type="content" source="../media/quickstarts/chatgpt-playground-load-new.png" alt-text="Screenshot of the Chat playground page." lightbox="../media/quickstarts/chatgpt-playground-load-new.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIサービスの機能に関する文言修正"
}
```

### Explanation
この変更は、Azure OpenAI Studioに関するドキュメントの表現を若干修正し、より正確な情報を提供することを目的としています。具体的な変更点は以下の通りです。

1. **文言の修正**:
   - 「OpenAI capabilities」に関する表現が「Azure OpenAI Service capabilities」へと変更されました。この修正により、Azureの文脈における機能に特有の強調がなされ、読み手に対してより明確な情報提供が行われています。

2. **文の流れの改善**:
   - 修正された文は、Azure OpenAI Studioのチャットプレイグラウンドでの体験がより具体的に描写されており、ユーザーに対する案内の質が向上しています。これにより、読者は特定のサービスにおける体験を容易に理解できるようになります。

このように、ドキュメントの微調整は、Azure OpenAIの特定の機能を明確にするためのものであり、ユーザーがサービスの内容を正しく把握できるようにすることを目指しています。全体的に、情報提供の質が向上しています。

## articles/ai-services/openai/includes/chatgpt-typescript.md{#item-6d2f1f}

<details>
<summary>Diff</summary>
````diff
@@ -14,24 +14,28 @@ ms.date: 10/22
 [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
 > [!NOTE]
-> This article has been updated to use the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you are looking for code examples for the legacy Azure OpenAI JavaScript SDK they are currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
+> This guide uses the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you're looking for code examples for the legacy Azure OpenAI JavaScript SDK, they're currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
 
 ## Prerequisites
 
-
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
 - [TypeScript](https://www.typescriptlang.org/download/)
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI Service resource with a `gpt-35-turbo` or `gpt-4` series models deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
+### Microsoft Entra ID prerequisites
 
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Set up
+## Retrieve resource information
 
-[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+[!INCLUDE [resource authentication](resource-auth.md)]
 
-[!INCLUDE [environment-variables](environment-variables.md)]
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a Node application
 
@@ -45,7 +49,7 @@ Install the required packages for JavaScript with npm from within the context of
 npm install openai @azure/identity
 ```
 
-Your app's _package.json_ file will be updated with the dependencies.
+Your app's _package.json_ file is updated with the dependencies.
 
 
 ## Create a sample application
@@ -219,7 +223,7 @@ node.exe ChatCompletion.js
 ---
 
 > [!NOTE]
-> If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You may need to remove a pre-existing environment variable for the API key from your system. Even though the Microsoft Entra ID code sample is not explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error will still be generated.
+> If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You might need to remove a preexisting environment variable for the API key from your system. Even though the Microsoft Entra ID code sample isn't explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error is still generated.
 
 
 ## Clean up resources
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI向けの最新のnpmパッケージ使用に関する文言修正"
}
```

### Explanation
この変更は、Azure OpenAIに関連したTypeScriptのドキュメントを更新し、内容を明確にすることを目的としています。以下は主な変更点です。

1. **文言の改善**:
   - 「This article has been updated to use the [latest OpenAI npm package]」という文言が「This guide uses the [latest OpenAI npm package]」に変更され、よりダイレクトで読みやすい表現に修正されています。これにより、利用者が指針を理解しやすくなっています。

2. **Prerequisitesセクションの追加**:
   - Microsoft Entra IDに基づくキーレス認証に関する要件が新たに追加され、Azure CLIのインストールや役割の割り当て手順が明確に説明されています。これにより、ユーザーは必要な準備を迅速に理解することができます。

3. **注意事項の追加**:
   - 推奨されるキーレス認証を使用する際に、`AZURE_OPENAI_API_KEY`環境変数が設定されていないことを確認するための注意喚起が含まれています。これにより、ユーザーがトラブルを未然に防ぐことができるようになります。

4. **トラブルシューティング情報の文面修正**:
   - エラーメッセージに関する記述の文言が修正され、わかりやすくなっています。特に、環境変数の影響を受ける可能性についての説明が改善されています。

このように、ドキュメントの更新は、ユーザーがAzure OpenAIサービスを利用する際に必要な情報にアクセスしやすくし、体験を向上させることを目指しています。全体を通して、明確さと正確性の向上が図られています。

## articles/ai-services/openai/includes/connect-your-data-studio.md{#item-c34da8}

<details>
<summary>Diff</summary>
````diff
@@ -12,12 +12,12 @@ ms.date: 11/06/2024
 recommendations: false
 ---
 
-## Add your data using Azure OpenAI Studio
+## Add your data using Azure AI Foundry portal
 
 > [!TIP]
 > You can [use the Azure Developer CLI](../how-to/azure-developer-cli.md) to programmatically create the resources needed for Azure OpenAI On Your Data 
 
-Navigate to [Azure AI Foundry](https://ai.azure.com/) and sign-in with credentials that have access to your Azure OpenAI resource. 
+Navigate to [Azure AI Foundry portal](https://ai.azure.com/) and sign-in with credentials that have access to your Azure OpenAI resource. 
 
 1. You can either [create an Azure AI Foundry project](../../../ai-studio/how-to/create-projects.md) by clicking **Create project**, or continue directly by clicking the button on the **Focused on Azure OpenAI Service** tile.  
 
@@ -41,7 +41,7 @@ Navigate to [Azure AI Foundry](https://ai.azure.com/) and sign-in with credentia
 
     1. Select your Azure AI Search resource, and select the acknowledgment that connecting it will incur usage on your account. Then select **Next**.
 
-    :::image type="content" source="../media/quickstarts/add-your-data-source.png" alt-text="A screenshot showing options for selecting a data source in Azure OpenAI Studio." lightbox="../media/quickstarts/add-your-data-source.png":::
+    :::image type="content" source="../media/quickstarts/add-your-data-source.png" alt-text="A screenshot showing options for selecting a data source in Azure AI Foundry portal." lightbox="../media/quickstarts/add-your-data-source.png":::
 
 
 1. On the **Upload files** pane, select **Browse for a file** and select the files you downloaded from the [prerequisites](#prerequisites) section, or your own data. Then select **Upload files**. Then select **Next**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルに関する表現修正"
}
```

### Explanation
この変更は、Azure OpenAI Studioに関連したデータ接続の手順を説明する文書を更新し、使用するポータルの名称を明確にすることを目的としています。主な変更点は以下の通りです。

1. **ポータル名称の変更**:
   - タイトルおよび文中の「Azure OpenAI Studio」が「Azure AI Foundry portal」に変更され、正確な名称が使用されています。これにより、ユーザーは現在の製品名に基づいた情報を得ることができます。

2. **内容の一貫性の向上**:
   - すべての箇所で同様の変更が適用されているため、文書全体の一貫性が増し、新しい用語が適切に統一されています。これは、プラットフォームの名前の変更に伴う重要な更新です。

3. **画像の説明文の修正**:
   - 画像のキャプションにおいても、ポータルの名称が適切に更新され、ユーザーが視覚的に情報を理解しやすくなっています。

このように、変更は主に用語の更新に集中しており、内容の正確性と明確性を高めることを目的としています。これにより、ユーザーがAzure AI Foundryを使用する際の手順が一貫して明確に理解できるようになります。

## articles/ai-services/openai/includes/create-resource-portal.md{#item-cb2503}

<details>
<summary>Diff</summary>
````diff
@@ -97,7 +97,7 @@ Before you can generate text or inference, you need to deploy a model. You can s
 
 To deploy a model, follow these steps:
 
-1. Sign in to [Azure AI Foundry](https://oai.azure.com).
+1. Sign in to [Azure AI Foundry portal](https://ai.azure.com).
 
 2. Choose the subscription and the Azure OpenAI resource to work with, and select **Use resource**.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルの表現を修正"
}
```

### Explanation
この変更は、Azure OpenAIリソースをデプロイする手順に関する文書の一部を更新し、ポータルの名称を明確にすることを目的としています。以下は主な変更点です。

1. **ポータル名称の具体化**:
   - ステップ1の指示が「Azure AI Foundry」から「Azure AI Foundry portal」に変更されました。これは、ユーザーに対して正確で一貫した情報を提供するために重要です。

2. **利用者への明確な指示**:
   - 端的で簡潔な指示が強調され、利用者が正しいポータルにサインインする手順をより明確に理解できるようになっています。この種の微調整は、ユーザー体験を向上させるために役立ちます。

この更新は、リソースの作成手順において一貫した情報提供を目指すものであり、ユーザーが正確な情報に基づいて操作を行う際の助けとなります。全体として、文書の正確性と明瞭さが向上しました。

## articles/ai-services/openai/includes/dall-e-javascript.md{#item-6cffcf}

<details>
<summary>Diff</summary>
````diff
@@ -17,19 +17,23 @@ Use this guide to get started generating images with the Azure OpenAI SDK for Ja
 
 ## Prerequisites
 
-
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
+### Microsoft Entra ID prerequisites
 
-## Setup
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+## Retrieve resource information
 
-[!INCLUDE [environment-variables](environment-variables.md)]
+[!INCLUDE [resource authentication](resource-auth.md)]
 
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a Node application
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Entra IDの要件に関する追加"
}
```

### Explanation
この変更は、Azure OpenAI SDKを使用して画像を生成するためのガイドにおいて、Microsoft Entra IDに関連する要件を追加し、手順を更新しました。主な変更点は以下の通りです。

1. **Microsoft Entra IDに関する新しい要件の追加**:
   - 認証方法としてMicrosoft Entra IDを用いるための具体的な手順が新たに追加され、利用者がキーレス認証を使用する際の前提条件に関するセクションが設けられました。これにより、ユーザーは必要な設定を適切に理解し、実施することができます。

2. **重要な手順の明記**:
   - Azure CLIを使用してMicrosoft Entra IDとのキーレス認証を行うため、`Cognitive Services User`ロールをユーザーアカウントに割り当てる必要がある旨が記載されています。この手順は、正しい権限設定によるアクセスを確保するために重要です。

3. **リソース情報の取得に関する更新**:
   - 環境変数やリソース認証に関する情報が整理されており、特に`AZURE_OPENAI_API_KEY`環境変数が設定されていないことが求められる注意点として強調されています。

これらの変更は、Azure OpenAI SDKの導入に際して必須の情報を提供するとともに、利用者がスムーズに作業を進めるための支援を目的としています。全体として、文書はより実用的で明確なガイドとしての役割を強化しています。

## articles/ai-services/openai/includes/dall-e-studio.md{#item-439729}

<details>
<summary>Diff</summary>
````diff
@@ -21,7 +21,7 @@ Use this guide to get started generating images with Azure OpenAI in your browse
 
 ## Go to Azure AI Foundry
 
-Browse to [Azure AI Foundry](https://oai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
+Browse to [Azure AI Foundry](https://ai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
 From the Azure AI Foundry landing page, create or select a new project. Navigate to the **Models + endpoints** page on the left nav. Select **Deploy model** and then choose one of the DALL-E models from the list. Complete the deployment process. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI FoundryのURL修正"
}
```

### Explanation
この変更は、画像生成ガイドにおいてAzure AI FoundryのURLを更新することを目的としています。以下は主な変更点です。

1. **URLの修正**:
   - 文中の「Azure AI Foundry」のリンクが、以前の「https://oai.azure.com/」から「https://ai.azure.com/」に変更されました。これは、サービスの現在の正しいURLに合わせるための修正です。

2. **サインイン手順の明確化**:
   - 更新されたURLに基づいて、ユーザーがAzure OpenAIリソースに関連する資格情報を使用してサインインする手順が明示されています。この修正によって、ユーザーは正しいポータルにアクセスすることができ、混乱を避けることができます。

全体として、この更新は文書の正確性を向上させ、利用者が適切な手順を踏んでサービスにアクセスできるようにサポートしています。これによって、ユーザーの体験が改善され、サービス利用のスムーズさが増します。

## articles/ai-services/openai/includes/dall-e-typescript.md{#item-57b205}

<details>
<summary>Diff</summary>
````diff
@@ -17,21 +17,24 @@ Use this guide to get started generating images with the Azure OpenAI SDK for Ja
 
 ## Prerequisites
 
-
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
 - [TypeScript](https://www.typescriptlang.org/download/)
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
+### Microsoft Entra ID prerequisites
 
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Setup
-
-[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+## Retrieve resource information
 
-[!INCLUDE [environment-variables](environment-variables.md)]
+[!INCLUDE [resource authentication](resource-auth.md)]
 
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a Node application
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Entra IDの要件に関する追加"
}
```

### Explanation
この変更は、Azure OpenAI SDKを用いて画像を生成するためのガイドにおいて、Microsoft Entra IDに関連する要件を追加し、手順を更新することを目的としています。以下は主な変更点です。

1. **Microsoft Entra IDに関する新たな要件の追加**:
   - 必要な前提条件として、Microsoft Entra IDを用いたキーレス認証に関する具体的な手順が追加されました。これにより利用者は、適切な設定を行うために必要な情報を得ることができます。

2. **重要な手順の明記**:
   - Azure CLIをインストールし、Microsoft Entra IDと連携したキーレス認証を行うためには、ユーザーアカウントに`Cognitive Services User`ロールを割り当てる必要がある旨が記載されています。この手順は、正しい権限設定を通じてアクセスを保証するために重要です。

3. **リソース情報の取得に関する更新**:
   - 環境変数やリソース認証に関する情報が整理され、特に`AZURE_OPENAI_API_KEY`環境変数が設定されていないことが求められる注意点として強調されています。

このような変更により、文書はより実用的に、かつ明確に利用者をサポートする内容に強化されています。利用者は、Azure OpenAI SDKを導入する際に知っておくべき重要な情報にアクセスしやすくなり、スムーズに導入作業を進めることが可能です。

## articles/ai-services/openai/includes/deploy-web-app.md{#item-d61fc3}

<details>
<summary>Diff</summary>
````diff
@@ -10,10 +10,9 @@ ms.date: 02/09/2024
 
 ## Deploy your model
 
-Once you're satisfied with the experience in Azure OpenAI studio, you can deploy a web app directly from the 
-Studio by selecting the **Deploy to** button. 
+Once you're satisfied with the experience, you can deploy a web app directly from the portal by selecting the **Deploy to** button. 
 
-:::image type="content" source="../media/use-your-data/deploy-model.png" alt-text="A screenshot showing the model deployment button in Azure OpenAI Studio." lightbox="../media/use-your-data/deploy-model.png":::
+:::image type="content" source="../media/use-your-data/deploy-model.png" alt-text="A screenshot showing the model deployment button in the portal." lightbox="../media/use-your-data/deploy-model.png":::
 
 This gives you the option to either deploy to a standalone web application, or a copilot in Copilot Studio (preview) if you're [using your own data](../concepts/use-your-data.md#deploy-to-a-copilot-preview-teams-app-preview-or-web-app) on the model. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントに関する表現の修正"
}
```

### Explanation
この変更は、Azure OpenAIモデルをデプロイする手順において、一部の表現を修正し、指示をより明確にすることを目的としています。以下は主な変更点です。

1. **ポータルへの言及の明確化**:
   - 「Azure OpenAI Studio」から「ポータル」に表現を変更することにより、デプロイメント操作が行われる場所を明確に示しています。これにより、利用者は正確なインターフェースを認識しやすくなります。

2. **スクリーンショットの説明修正**:
   - 画像の説明文が修正され、対象となるボタンが「ポータル」に関連していることが強調されています。この修正により、ユーザーは参照する画像がどのインターフェースを示しているかをより理解しやすくなっています。

3. **デプロイメントオプションの保持**:
   - 修正後も、スタンドアロンウェブアプリケーションまたはコパイロットへのデプロイメントオプションが維持されているため、ユーザーが自分のデータを利用してモデルをデプロイする際の選択肢が引き続き提供されています。

全体として、これらの変更はドキュメントの明確さを向上させ、利用者がプロセスを円滑に進めるための手助けをしています。ユーザーは正しいインターフェース情報にアクセスでき、具体的な手順に沿ってデプロイを実施することが容易になります。

## articles/ai-services/openai/includes/env-var-without-key.md{#item-56a8e2}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +0,0 @@
----
-author: eric-urban 
-ms.author: eur 
-ms.service: azure-ai-openai
-ms.topic: include
-ms.date: 12/27/2024
----
-
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. |
-| `AZURE_OPENAI_DEPLOYMENT_NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Model Deployments** in the Azure portal.|
-| `OPENAI_API_VERSION`|Learn more about [API Versions](/azure/ai-services/openai/api-version-deprecation).|
-
-Learn more about [keyless authentication](/azure/ai-services/authentication) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "環境変数に関するドキュメントの削除"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連する環境変数に関するドキュメントが削除されたことを示しています。この削除によって、以下のような影響があります。

1. **環境変数の情報の消失**:
   - `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT_NAME`, `OPENAI_API_VERSION` などの重要な環境変数の詳細が削除され、これらの変数に関する情報が利用者に提供されなくなります。これにより、新規ユーザーや既存のユーザーが設定すべき環境変数についてのガイダンスを失うことになります。

2. **キーレス認証や環境変数の設定に関する情報のアクセス喪失**:
   - キーレス認証や環境変数の設定に関するリンクや情報も消失し、これらのトピックについてさらに学ぶためのリソースがなくなっています。このことで、利用者はキーレス認証の実施方法や環境設定に関しての洞察を得る手段を失います。

3. **ドキュメントの構造の変更**:
   - この変更により、ドキュメント全体の構造が変わり、これまで関連情報の一部として機能していた部分が無くなることで、他のコンテンツの関連性や流れにも影響を及ぼす可能性があります。

このように、環境変数に関するドキュメントの削除は、利用者にとって重大な影響を及ぼす変更であるため、適切な代替リソースの提供が求められるでしょう。

## articles/ai-services/openai/includes/fine-tuning-openai-in-ai-studio.md{#item-723c8d}

<details>
<summary>Diff</summary>
````diff
@@ -306,4 +306,4 @@ You can delete a fine-tuned model on the **Fine-tuning** page in Azure AI Foundr
 
 ### Delete your training files
 
-You can optionally delete training and validation files that you uploaded for training, and result files generated during training. For this you need to go to Azure OpenAI Studio and navigate to the **Management** > **Data files** pane. Select the file to delete, and then select **Delete** to delete the file.
+You can optionally delete training and validation files that you uploaded for training, and result files generated during training. For this you need to go to Azure AI Foundry portal and navigate to the **Management** > **Data + indexes** pane. Select the file to delete, and then select **Delete** to delete the file.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI StudioからAzure AI Foundryへの用語変更"
}
```

### Explanation
この変更は、Azureに関連するドキュメント内の用語を「Azure OpenAI Studio」から「Azure AI Foundry」へ更新したことを示しています。以下はこの変更の概要です。

1. **用語の更新**:
   - 「Azure OpenAI Studio」という表現を「Azure AI Foundry」に変更しています。この修正により、利用者は現在の正確なプラットフォームを知り、最新の情報に基づいて操作を行うことができるようになります。

2. **管理セクションの名称変更**:
   - ドキュメント内での「Management」セクションの名称も「Data files」から「Data + indexes」に変更されています。これにより、ユーザーは新しいインターフェースでのファイル管理の方法を明確に把握できるようになります。

このような変更は、ユーザーが正確な環境やインターフェースに基づいて正しい操作を行うことを保証するために重要であり、文書の整合性を保つ役割を果たします。

## articles/ai-services/openai/includes/fine-tuning-python.md{#item-976f58}

<details>
<summary>Diff</summary>
````diff
@@ -346,7 +346,7 @@ To examine the individual fine-tuning events that were generated during training
 
 # [OpenAI Python 1.x](#tab/python-new)
 
-You may need to upgrade your OpenAI client library to the latest version with `pip install openai --upgrade` to run this command.
+You might need to upgrade your OpenAI client library to the latest version with `pip install openai --upgrade` to run this command.
 
 ```python
 response = client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id, limit=10)
@@ -367,7 +367,7 @@ You can run the list checkpoints command to retrieve the list of checkpoints ass
 
 # [OpenAI Python 1.x](#tab/python-new)
 
-You may need to upgrade your OpenAI client library to the latest version with `pip install openai --upgrade` to run this command.
+You might need to upgrade your OpenAI client library to the latest version with `pip install openai --upgrade` to run this command.
 
 ```python
 response = client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id, limit=10)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "表現の変更による文の調整"
}
```

### Explanation
この変更は、AzureのOpenAI Pythonライブラリに関するドキュメント内での表現を微調整したものです。具体的には、「You may need to」から「You might need to」への変更が行われています。以下はこの変更の概要です。

1. **表現の統一**:
   - 文中の「may」を「might」に変更することで、表現をよりカジュアルで柔軟なものにしています。このような変更は、読者に対して選択肢や可能性を示す際により自然な表現となることがあります。

2. **文の全体的な明瞭さの向上**:
   - この変更により、利用者がOpenAIクライアントライブラリを最新バージョンへアップグレードする必要がある場合に対する警告が、より受け入れやすくなります。このような微調整は、ユーザー体験を向上させる重要な要素です。

変更が行われた箇所は2箇所ですが、いずれも同じ内容の繰り返しであり、表現の統一によって文全体の一貫性が高められています。これにより、ドキュメントはより親しみやすく、読みやすいものとなっています。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: 'Customize a model with Azure OpenAI Service and Azure AI Foundry'
+title: 'Customize a model with Azure OpenAI Service and Azure AI Foundry portal'
 titleSuffix: Azure OpenAI
 description: Learn how to create your own custom model with Azure OpenAI Service by using the Azure AI Foundry portal.
 #services: cognitive-services
@@ -40,9 +40,9 @@ Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{
 Consult the [models page](../concepts/models.md#fine-tuning-models) to check which regions currently support fine-tuning.
 
 
-## Review the workflow for Azure AI Foundry
+## Review the workflow for Azure AI Foundry portal
 
-Take a moment to review the fine-tuning workflow for using Azure AI Foundry:
+Take a moment to review the fine-tuning workflow for using Azure AI Foundry portal:
 
 1. Prepare your training and validation data.
 1. Use the **Create custom model** wizard in Azure AI Foundry portal to train your custom model.
@@ -150,9 +150,9 @@ After it guides you through the process of implementing suggested changes, the t
 
 ## Use the Create custom model wizard
 
-Azure AI Foundry provides the **Create custom model** wizard, so you can interactively create and train a fine-tuned model for your Azure resource.
+Azure AI Foundry portal provides the **Create custom model** wizard, so you can interactively create and train a fine-tuned model for your Azure resource.
 
-1. Open Azure AI Foundry at <a href="https://oai.azure.com/" target="_blank">https://oai.azure.com/</a> and sign in with credentials that have access to your Azure OpenAI resource. During the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
+1. Open Azure AI Foundry portal at <a href="https://oai.azure.com/" target="_blank">https://oai.azure.com/</a> and sign in with credentials that have access to your Azure OpenAI resource. During the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
 
 1. In Azure AI Foundry portal, browse to the **Tools > Fine-tuning** pane, and select **Fine-tune model**.
 
@@ -310,7 +310,7 @@ If you're ready to train your model, select **Start Training job** to start the
 
 The **Models** pane displays information about your custom model in the **Customized models** tab. The tab includes information about the status and job ID of the fine-tune job for your custom model. When the job completes, the tab displays the file ID of the result file. You might need to select **Refresh** in order to see an updated status for the model training job.
 
-:::image type="content" source="../media/fine-tuning/studio-models-job-running.png" alt-text="Screenshot of the Models pane from Azure AI Foundry, with a custom model displayed." lightbox="../media/fine-tuning/studio-models-job-running.png":::
+:::image type="content" source="../media/fine-tuning/studio-models-job-running.png" alt-text="Screenshot of the Models pane from Azure AI Foundry portal, with a custom model displayed." lightbox="../media/fine-tuning/studio-models-job-running.png":::
 
 After you start a fine-tuning job, it can take some time to complete. Your job might be queued behind other jobs on the system. Training your model can take minutes or hours depending on the model and dataset size.
 
@@ -366,13 +366,13 @@ Cross subscription/region deployment can be accomplished via [Python](/azure/ai-
 
 ## Use a deployed custom model
 
-After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure AI Foundry](https://oai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models. For fine-tuned `babbage-002` and `davinci-002` models you will use the Completions playground and the Completions API. For fine-tuned `gpt-35-turbo-0613` models you will use the Chat playground and the Chat completion API.
+After your custom model deploys, you can use it like any other deployed model. You can use the **Playgrounds** in [Azure AI Foundry portal](https://oai.azure.com) to experiment with your new deployment. You can continue to use the same parameters with your custom model, such as `temperature` and `max_tokens`, as you can with other deployed models. For fine-tuned `babbage-002` and `davinci-002` models you will use the Completions playground and the Completions API. For fine-tuned `gpt-35-turbo-0613` models you will use the Chat playground and the Chat completion API.
 
 :::image type="content" source="../media/quickstarts/playground-load-new.png" alt-text="Screenshot of the Playground pane in Azure AI Foundry portal, with sections highlighted." lightbox="../media/quickstarts/playground-load-new.png":::
 
 ## Analyze your custom model
 
-Azure OpenAI attaches a result file named _results.csv_ to each fine-tuning job after it completes. You can use the result file to analyze the training and validation performance of your custom model. The file ID for the result file is listed for each custom model in the **Result file Id** column on the **Models** pane for Azure AI Foundry. You can use the file ID to identify and download the result file from the **Data files** pane of Azure AI Foundry.
+Azure OpenAI attaches a result file named _results.csv_ to each fine-tuning job after it completes. You can use the result file to analyze the training and validation performance of your custom model. The file ID for the result file is listed for each custom model in the **Result file Id** column on the **Models** pane for Azure AI Foundry portal. You can use the file ID to identify and download the result file from the **Data files** pane of Azure AI Foundry portal.
 
 The result file is a CSV file that contains a header row and a row for each training step performed by the fine-tuning job. The result file contains the following columns:
 
@@ -409,7 +409,7 @@ You can delete a custom model on the **Models** pane in Azure AI Foundry portal.
 
 ### Delete your training files
 
-You can optionally delete training and validation files that you uploaded for training, and result files generated during training, on the **Management** > **Data files** pane in Azure AI Foundry portal. Select the file to delete, and then select **Delete** to delete the file.
+You can optionally delete training and validation files that you uploaded for training, and result files generated during training, on the **Management** > **Data + indexes** pane in Azure AI Foundry portal. Select the file to delete, and then select **Delete** to delete the file.
 
 ## Continuous fine-tuning
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryにおける用語の修正"
}
```

### Explanation
この変更は、Azure AI Foundryに関するドキュメントで用語の一貫性を強化するための修正が行われています。主に「Azure AI Foundry」と表現されていた部分が「Azure AI Foundry portal」に変更されており、これにより、特定のプラットフォームを明確に示すことができます。以下はこの変更の概要です。

1. **プラットフォームの明確化**:
   - ドキュメント内で「Azure AI Foundry」という表現をすべて「Azure AI Foundry portal」に変更することで、ユーザーに対して何を参照しているのかをより明確にしています。これにより、読者は正確なプラットフォーム情報を知ることができ、混乱を避けられます。

2. **文の整合性向上**:
   - 用語が統一されることで、ドキュメント全体の整合性が向上し、プロフェッショナルな印象を与えることに繋がります。特に、同じセクション内で繰り返し用語が使用される場面では、一貫した表現が重要です。

3. **ユーザービリティの改善**:
   - 明確な呼称を使用することによって、ユーザーは必要な情報を探しやすくなり、特定の操作や手順に従う際の混乱を減少させることができます。

このような用語の修正は、ユーザーが最新の情報を正確に理解するために非常に重要であり、長期的にはユーザー体験の向上に寄与します。

## articles/ai-services/openai/includes/gpt-v-javascript.md{#item-a128c9}

<details>
<summary>Diff</summary>
````diff
@@ -23,16 +23,21 @@ This SDK is provided by OpenAI with Azure specific types provided by Azure.
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
----
-
-
 > [!NOTE]
 > This library is maintained by OpenAI. Refer to the [release history](https://github.com/openai/openai-node/releases) to track the latest updates to the library.
 
-[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+### Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+
+## Retrieve resource information
 
-[!INCLUDE [environment-variables](environment-variables.md)]
+[!INCLUDE [resource authentication](resource-auth.md)]
 
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a Node application
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Entra IDに関する前提条件の追加"
}
```

### Explanation
この変更は、Azure OpenAIリソースにアクセスする際の認証方法に関する情報を更新したものです。特に、Microsoft Entra IDを使用した推奨の認証方法に関する前提条件が追加されています。以下はこの変更の概要です。

1. **前提条件の整理**:
   - 新たに「Microsoft Entra ID prerequisites」というセクションが追加され、ユーザーがこの認証方式を使用するために必要な手順が詳述されています。これにより、ユーザーが必要な環境を整える際の理解が深まります。

2. **具体的な手順の明示**:
   - ユーザーが行うべき具体的な作業（Azure CLIのインストールや、ユーザーアカウントへのロールの割り当て）について説明しています。これにより、利用者は設定を行う際の迷いが軽減され、スムーズに作業を進められるようになります。

3. **注意喚起の追加**:
   - 環境変数`AZURE_OPENAI_API_KEY`の設定についての注意事項が新たに追加されており、これを設定していないことが推奨されています。このような注意喚起は、ユーザーが不具合に遭遇するのを防ぐために重要です。

変更によって、Microsoft Entra IDを使用したキーなしの認証手法に関し、より明確で具体的な指示が提供され、ユーザーが必要な前提条件を理解しやすくなっています。これは、ドキュメントのユーザビリティおよび情報の質を向上させる重要な改善です。

## articles/ai-services/openai/includes/gpt-v-typescript.md{#item-03ec34}

<details>
<summary>Diff</summary>
````diff
@@ -24,14 +24,21 @@ This SDK is provided by OpenAI with Azure specific types provided by Azure.
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
-
 > [!NOTE]
 > This library is maintained by OpenAI. Refer to the [release history](https://github.com/openai/openai-node/releases) to track the latest updates to the library.
 
-[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+### Microsoft Entra ID prerequisites
+
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
+
+## Retrieve resource information
 
-[!INCLUDE [environment-variables](environment-variables.md)]
+[!INCLUDE [resource authentication](resource-auth.md)]
 
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a Node application
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Entra IDによる認証に関する前提条件の追加"
}
```

### Explanation
この変更は、Azure OpenAIリソースを利用する際の認証方法に関する情報を更新したもので、特にMicrosoft Entra IDを使用したキーなしの認証に関連する前提条件が追加されています。以下はこの変更の概要です。

1. **新しいセクションの追加**:
   - 「Microsoft Entra ID prerequisites」という新しいセクションが導入され、Microsoft Entra IDを使用した推奨のキーなし認証を行うための必要条件について解説されています。これにより、ユーザーは認証を行うために必要な準備が整えやすくなります。

2. **具体的な手順の提示**:
   - ユーザーが行うべき手順として、Azure CLIのインストールや、ユーザーアカウントへの典型的な役割である`Cognitive Services User`の割り当てが明記されています。これにより、デベロッパーは設定を正確に行うことができるようになります。

3. **注意事項の追加**:
   - 環境変数`AZURE_OPENAI_API_KEY`についての注意喚起が追加され、推奨されるキーなしの認証を利用する場合はこの変数が設定されていないことを確認する必要があるとされています。このような明確な指示は、ユーザーがエラーを避けるために重要です。

このような変更によって、Microsoft Entra IDを用いた認証方法に関する理解が進み、ユーザーの操作性と安全性が向上します。全体として、これらの修正はAzure OpenAIの利用をよりスムーズにするための重要な改善となっています。

## articles/ai-services/openai/includes/javascript.md{#item-f4828f}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.date: 10/22/2024
 [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
 > [!NOTE]
-> This article has been updated to use the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you are looking for code examples for the legacy Azure OpenAI JavaScript SDK they are currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
+> This guide uses the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you're looking for code examples for the legacy Azure OpenAI JavaScript SDK, they're currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
 
 ## Prerequisites
 
@@ -24,25 +24,24 @@ ms.date: 10/22/2024
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI Service resource with the `gpt-35-turbo-instruct` model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
+## Retrieve resource information
 
+[!INCLUDE [resource authentication](resource-auth.md)]
 
-## Set up
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
-[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
-
-[!INCLUDE [environment-variables](environment-variables.md)]
+## Install the client library
 
 In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it.
 
-## Install the client library
-
 Install the required packages for JavaScript with npm from within the context of your new directory:
 
 ```console
 npm install openai @azure/identity
 ```
 
-Your app's _package.json_ file will be updated with the dependencies.
+Your app's _package.json_ file is updated with the dependencies.
 
 
 ## Create a sample application
@@ -146,7 +145,7 @@ Microsoft was founded on April 4, 1975.
 ```
 
 > [!NOTE]
-> If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You may need to remove a pre-existing environment variable for the API key from your system. Even though the Microsoft Entra ID code sample is not explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error will still be generated.
+> If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You might need to remove a preexisting environment variable for the API key from your system. Even though the Microsoft Entra ID code sample isn't explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error is still generated.
 
 
 ## Clean up resources
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OpenAI npmパッケージの更新に関するガイドの修正"
}
```

### Explanation
この変更は、OpenAI JavaScript SDKに関するドキュメントを更新したもので、特に最新のOpenAI npmパッケージに関する情報が明確化されています。以下はこの変更の概要です。

1. **通知文の改善**:
   - 文中の注意書きが更新され、最新のOpenAI npmパッケージがAzure OpenAIを完全にサポートする旨がより簡潔に説明されています。これにより、ユーザーが新しいパッケージの利点を理解しやすくなります。

2. **前提条件セクションの強化**:
   - 前提条件に関する情報が整理され、Azure OpenAI Serviceリソースの必要性やモデルのデプロイに関するリンクが強調されています。また、推奨されるキーなしの認証を使用するための条件が注意事項として追加されているため、誤使用を防ぐための情報が提供されています。

3. **クライアントライブラリのインストール手順の明示化**:
   - クライアントライブラリのインストールに関するセクションが整備され、必要なパッケージをnpmを使用してインストールする手順が具体的に示されています。この部分は、ユーザーが実際にアプリケーションを構築する際に非常に役立ちます。

4. **エラーメッセージの注意点**:
   - 既存の環境変数の設定に関する注意点が整理され、特定のエラーメッセージが発生する条件が説明されています。これにより、ユーザーはアプリケーションを実行する際のトラブルシューティングが容易になります。

全体として、この変更はOpenAI npmパッケージを使用する開発者にとって、より明確で使いやすい情報を提供し、Azure OpenAIの利用を促進するための重要な改善となっています。

## articles/ai-services/openai/includes/on-your-data-authentication.md{#item-43fc01}

<details>
<summary>Diff</summary>
````diff
@@ -11,8 +11,7 @@ ms.date: 03/27/2024
 
 You need to select how you want to authenticate the connection from Azure OpenAI, Azure AI Search, and Azure blob storage. You can choose a *System assigned managed identity* or an *API key*. By selecting *API key* as the authentication type, the system will automatically populate the API key for you to connect with your Azure AI Search, Azure OpenAI, and Azure Blob Storage resources. By selecting *System assigned managed identity*, the authentication will be based on the [role assignment](../how-to/on-your-data-configuration.md#role-assignments) you have. *System assigned managed identity* is selected by default for security. 
 
-
-:::image type="content" source="../media/use-your-data/data-connection-authentication.png" alt-text="A screenshot showing the managed identity option in Azure OpenAI Studio." lightbox="../media/use-your-data/data-connection-authentication.png":::
+:::image type="content" source="../media/use-your-data/data-connection-authentication.png" alt-text="A screenshot showing the managed identity option in Azure AI Foundry portal." lightbox="../media/use-your-data/data-connection-authentication.png":::
 
 Once you select the **next** button, it will automatically validate your setup to use the selected authentication method. If you encounter an error, see the [role assignments article](../how-to/on-your-data-configuration.md#role-assignments) to update your setup.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルにおける認証オプションの説明変更"
}
```

### Explanation
この変更は、Azure OpenAI、Azure AI Search、Azure Blob Storageの接続認証に関するドキュメントを更新したもので、特に管理されたIDオプションに関連する記述が改善されています。以下はこの変更の概要です。

1. **認証オプションの明確化**:
   - Azure OpenAIへの接続認証方法について、*System assigned managed identity*と*API key*の選択肢が示されています。この情報は、ユーザーがどの認証方法を使用するかを決定するのに役立ちます。

2. **画像の参照先の変更**:
   - スクリーンショットの説明文が変更され、画像が「Azure OpenAI Studio」から「Azure AI Foundryポータル」に載せ替えられています。この変更により、正確な情報とコンテキストが提供されるようになりました。

3. **デフォルト設定の確認**:
   - *System assigned managed identity*がデフォルトの選択肢であることが強調されており、セキュリティの観点からも重要なポイントです。これにより、ユーザーは安全な接続方法を意識することができます。

このような小規模な更新により、ユーザーがAzureの各リソースに接続する際の認証プロセスについてより正確かつ明確な理解を促進することが目的です。全体として、利用者が適切な設定を行いやすくなる重要な改善がなされています。

## articles/ai-services/openai/includes/realtime-javascript.md{#item-3c125e}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.date: 12/26/2024
 - An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
 - Then, you need to deploy a `gpt-4o-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
 
-## Microsoft Entra ID prerequisites
+### Microsoft Entra ID prerequisites
 
 For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
@@ -59,22 +59,14 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-#### [Microsoft Entra ID](#tab/javascript-keyless)
-
-[!INCLUDE [keyless-environment-variables](env-var-without-key.md)]
-
-#### [API key](#tab/javascript-key)
-
-[!INCLUDE [key-environment-variables](env-var-key.md)]
-
----
+[!INCLUDE [resource authentication](resource-auth.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Text in audio out
 
-#### [Microsoft Entra ID](#tab/javascript-keyless)
+#### [Microsoft Entra ID](#tab/keyless)
 
 1. Create the `text-in-audio-out.js` file with the following code:
 
@@ -143,7 +135,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     ```
 
 
-#### [API key](#tab/javascript-key)
+#### [API key](#tab/api-key)
 
 1. Create the `text-in-audio-out.js` file with the following code:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Entra IDに関する初心者向け手順の整理"
}
```

### Explanation
この変更は、Azure OpenAIを使用するためのJavaScriptに関するドキュメントを更新したもので、Microsoft Entra IDによる無鍵認証のセクションが改善されています。以下はこの変更の概要です。

1. **セクションのタイトル変更**:
   - 「Microsoft Entra ID prerequisites」のタイトルが「##」から「###」に変更され、ドキュメントの階層が調整されました。これにより、読みやすさが向上し、情報の構造が明確になります。

2. **不必要な要素の削除**:
   - いくつかの無駄なヘッダーとマークダウンのインクルード文が削除され、特定のセクションが簡素化されました。この変更により、ユーザーが重要な情報に迅速にアクセスしやすくなっています。

3. **認証関連の注意事項の強調**:
   - 無鍵認証に関する注意事項が残されており、`AZURE_OPENAI_API_KEY`環境変数が設定されていないことを確認するように促されています。この情報は、ユーザーが正しく設定を行うための重要なポイントです。

4. **タブのリンク修正**:
   - 複数のタブのリンクが更新され、より適切なセクションに関連付けられるようになりました。これによって、ユーザーが関連情報にスムーズにアクセスできるようになります。

全体として、この変更はドキュメントの明瞭さと使いやすさを向上させており、Azure OpenAIを利用する際の設定プロセスの理解を助けるための重要な改善です。

## articles/ai-services/openai/includes/realtime-python.md{#item-1291c0}

<details>
<summary>Diff</summary>
````diff
@@ -76,19 +76,11 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-#### [Microsoft Entra ID](#tab/javascript-keyless)
-
-[!INCLUDE [keyless-environment-variables](env-var-without-key.md)]
-
-#### [API key](#tab/javascript-key)
-
-[!INCLUDE [key-environment-variables](env-var-key.md)]
-
----
+[!INCLUDE [resource authentication](resource-auth.md)]
 
 ## Text in audio out
 
-## [Microsoft Entra ID](#tab/javascript-keyless)
+## [Microsoft Entra ID](#tab/keyless)
 
 1. Create the `text-in-audio-out.py` file with the following code:
 
@@ -149,7 +141,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     python text-in-audio-out.py
     ```
 
-## [API key](#tab/javascript-key)
+## [API key](#tab/api-key)
 
 1. Create the `text-in-audio-out.py` file with the following code:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "無鍵認証およびAPIキーに関するセクションの整理"
}
```

### Explanation
この変更は、Azure OpenAIを利用したPythonに関するドキュメントを更新したもので、主に無鍵認証とAPIキーに関連するセクションが整理されています。以下はこの変更の概要です。

1. **無鍵認証に関するセクションの簡素化**:
   - Microsoft Entra IDに関する無鍵認証のセクションから、不要なヘッダーと環境変数のインクルードが削除されています。これにより、情報が整理され、特に重要なポイントにフォーカスできるようになっています。

2. **タブのリンクの修正**:
   - タブリンクが「javascript-keyless」から「keyless」および「javascript-key」から「api-key」に変更されており、より直感的で正確なリンク名が使用されています。この改善により、ユーザーは適切なリソースにスムーズにアクセスしやすくなります。

3. **APIキーセクションの整理**:
   - APIキーに関するセクションも同様に簡略化され、必要な情報のみが保持されるように整理されています。

4. **リソース情報のインクルード**:
   - リソース認証に関する情報がインクルードされるようになり、ユーザーが関連する設定をより理解しやすくなっています。

このように、全体的にドキュメントがシンプルかつ明確になるように改善されており、Azure OpenAIを使用する際の設定プロセスの理解がより容易になります。また、ユーザーにとって直感的なナビゲーションが可能になるため、利用体験の向上にも寄与しています。

## articles/ai-services/openai/includes/realtime-typescript.md{#item-eacc9c}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.date: 12/26/2024
 - An Azure OpenAI resource created in the East US 2 or Sweden Central regions. See [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability).
 - Then, you need to deploy a `gpt-4o-realtime-preview` model with your Azure OpenAI resource. For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md). 
 
-## Microsoft Entra ID prerequisites
+### Microsoft Entra ID prerequisites
 
 For the recommended keyless authentication with Microsoft Entra ID, you need to:
 - Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
@@ -60,22 +60,14 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
 
 ## Retrieve resource information
 
-#### [Microsoft Entra ID](#tab/javascript-keyless)
-
-[!INCLUDE [keyless-environment-variables](env-var-without-key.md)]
-
-#### [API key](#tab/javascript-key)
-
-[!INCLUDE [key-environment-variables](env-var-key.md)]
-
----
+[!INCLUDE [resource authentication](resource-auth.md)]
 
 > [!CAUTION]
 > To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
-    
+
 ## Text in audio out
 
-#### [Microsoft Entra ID](#tab/typescript-keyless)
+#### [Microsoft Entra ID](#tab/keyless)
 
 1. Create the `text-in-audio-out.ts` file with the following code:
 
@@ -170,7 +162,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     node text-in-audio-out.js
     ```
 
-#### [API key](#tab/typescript-key)
+#### [API key](#tab/api-key)
 
 1. Create the `text-in-audio-out.ts` file with the following code:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "無鍵認証とAPIキーに関するセクションの整理"
}
```

### Explanation
この変更は、Azure OpenAIを利用したTypeScriptに関するドキュメントの更新を反映したもので、特に無鍵認証およびAPIキーに関するセクションが整理されています。以下はこの変更の概要です。

1. **セクションのタイトル変更**:
   - 「Microsoft Entra ID prerequisites」の見出しが「##」から「###」に変更され、ドキュメントの階層が調整されました。これにより、情報が構造的に整理され、読みやすさが向上します。

2. **不要な要素の削除**:
   - 無鍵認証に関する不要なヘッダーや環境変数のインクルードが削除され、ユーザーが重要な情報にすぐにアクセスできるようになっています。この簡素化により、情報の焦点が絞られました。

3. **タブのリンクの修正**:
   - タブのリンクが「typescript-keyless」から「keyless」および「typescript-key」から「api-key」に変更され、より直感的で正確なリンク名に改められています。これにより、ユーザーが関連情報を簡単に見つけることが可能になります。

4. **リソース情報の更新**:
   - リソース認証に関する新しい情報が追加され、必要な認証方法が包括的にまとめられています。

5. **注意事項の強調**:
   - 無鍵認証を利用する際に、`AZURE_OPENAI_API_KEY`環境変数が設定されていないことを確認するように促す注意事項が残されており、重要な設定ポイントが強調されています。

このように、全体的にドキュメントが洗練され、より使いやすくなっているため、Azure OpenAIの利用における設定プロセスの理解がさらに容易になっています。ユーザーは必要な情報を迅速に取得できるため、利用体験の向上にも寄与しています。

## articles/ai-services/openai/includes/resource-auth.md{#item-cd425d}

<details>
<summary>Diff</summary>
````diff
@@ -3,9 +3,23 @@ author: eric-urban
 ms.author: eur 
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 12/27/2024
+ms.date: 1/7/2025
 ---
 
+You need to retrieve the following information to authenticate your application with your Azure OpenAI resource:
+
+#### [Microsoft Entra ID](#tab/keyless)
+
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. |
+| `AZURE_OPENAI_DEPLOYMENT_NAME` | This value will correspond to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Model Deployments** in the Azure portal.|
+| `OPENAI_API_VERSION`|Learn more about [API Versions](/azure/ai-services/openai/api-version-deprecation).|
+
+Learn more about [keyless authentication](/azure/ai-services/authentication) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
+
+#### [API key](#tab/api-key)
+
 |Variable name | Value |
 |--------------------------|-------------|
 | `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys and Endpoint** section when examining your resource from the Azure portal. |
@@ -15,4 +29,9 @@ ms.date: 12/27/2024
 
 Learn more about [finding API keys](/azure/ai-services/cognitive-services-environment-variables) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
 
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
\ No newline at end of file
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+---
+
+
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "環境変数に関するドキュメントの名前変更と内容追加"
}
```

### Explanation
この変更は、環境変数に関するドキュメントの名前を変更し、新たな情報を追加したものです。具体的には、`env-var-key.md`という元のファイル名が`resource-auth.md`に変更され、Azure OpenAIリソースに関連する認証情報の詳細が明記されています。以下はこの変更の概要です。

1. **ファイル名の変更**:
   - ドキュメントのファイル名が`env-var-key.md`から`resource-auth.md`に変更され、この変更によりファイルの内容が一目で分かるようになりました。新しいファイル名は、リソース認証に関連する情報を示唆しています。

2. **日付の更新**:
   - 文書内の日付が`12/27/2024`から`1/7/2025`に更新され、最近の内容であることを示しています。これは文書の適用性を向上させます。

3. **新しい情報の追加**:
   - Microsoft Entra IDおよびAPIキーの認証に関連する環境変数の詳細が追加されました。各環境変数に対する説明が表形式で整理されており、ユーザーは必要な情報にすぐにアクセスできるようになっています。具体的には、`AZURE_OPENAI_ENDPOINT`や`AZURE_OPENAI_DEPLOYMENT_NAME`などの変数についての情報が提供されています。

4. **リンクの追加**:
   - 新たに、無鍵認証や環境変数の設定に関する外部リンクが追加されており、ユーザーがより多くの情報を得られるよう工夫されています。

5. **内容の整形とクリアランス**:
   - また、Markdown形式での書き方が整理されており、全体的に見やすさが向上しています。

このように、文書の内容と構造が改善され、ユーザーが必要な情報を獲得しやすくなることを目的とした変更です。Azure OpenAIリソースの認証方法を明確に理解できることが期待されています。

## articles/ai-services/openai/includes/safety-evaluation.md{#item-09609f}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ GPT-4o, GPT-4o-mini, and GPT-4 are our most advanced models that can be fine-tun
 - Evaluation endpoints are in the same geography as the Azure OpenAI resource;
 - Training data is not stored in connection with performing evaluations; only the final model assessment (deployable or not deployable) is persisted; and
 
-GPT-4o, GPT-4o-mini, and GPT-4 fine-tuned model evaluation filters are set to predefined thresholds and cannot be modified by customers; they aren't tied to any custom content filtering configuration you may have created.
+GPT-4o, GPT-4o-mini, and GPT-4 fine-tuned model evaluation filters are set to predefined thresholds and cannot be modified by customers; they aren't tied to any custom content filtering configuration you might have created.
 
 ### Data evaluation
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書内の文言修正"
}
```

### Explanation
この変更は、`safety-evaluation.md`というドキュメント内の文言を修正したものであり、コントロールや定義に対する用語の一貫性を向上させる目的があります。以下にこの変更の概要を示します。

1. **文言の修正**:
   - 変更前の文では「may have created」という表現が「might have created」に修正され、より一貫性のある表現が使用されています。この微細な修正は、文章全体のスタイルの整合性を保ちつつ、読みやすさを向上させています。

2. **ステートメントの明確化**:
   - 修正内容は、GPT-4o、GPT-4o-mini、GPT-4の評価フィルターが顧客によって変更できないこと、そしてそれらのフィルターが顧客が作成したカスタムコンテンツフィルタリング設定に関連していないことを強調する部分です。この内容は、ユーザーに対して評価プロセスやフィルタリング設定の制約を明確に理解させることを目的としています。

全体として、この変更によって文書の表現が洗練され、技術的な内容の理解が容易になることが期待されます。文言の微調整は、特に技術的なトピックにおいては重要であり、ユーザーが誤解を避けられるように寄与します。

## articles/ai-services/openai/includes/text-to-speech-javascript.md{#item-e9b653}

<details>
<summary>Diff</summary>
````diff
@@ -19,58 +19,18 @@ recommendations: false
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
+### Microsoft Entra ID prerequisites
 
-## Set up
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-### Retrieve key and endpoint
+## Retrieve resource information
 
-To successfully make a call against Azure OpenAI, you need an **endpoint** and a **key**.
+[!INCLUDE [resource authentication](resource-auth.md)]
 
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | The service endpoint can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the endpoint via the **Deployments** page in Azure AI Foundry portal. An example endpoint is: `https://docs-test-001.openai.azure.com/`.|
-| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
-
-Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
-
-:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location highlighted." lightbox="../media/quickstarts/endpoint.png":::
-
-### Environment variables
-
-Create and assign persistent environment variables for your key and endpoint.
-
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
-
-# [Command Line](#tab/command-line)
-
-```CMD
-setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
-```
-
-```CMD
-setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
-```
-
-# [PowerShell](#tab/powershell)
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
-```
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
-```
-
-# [Bash](#tab/bash)
-
-```Bash
-echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
-```
-
-```Bash
-echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
-```
----
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a Node application
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト読み上げのJavaScriptに関する文書の更新"
}
```

### Explanation
この変更は、`text-to-speech-javascript.md`というドキュメントにおける内容の大幅な修正を行ったもので、特にMicrosoft Entra IDを利用したキーレス認証の必要条件について詳細な情報が追加されています。以下はこの変更の概要です。

1. **キーレス認証の推奨事項追加**:
   - 文書の初めに「Microsoft Entra IDの前提条件」という新しいセクションが追加され、ユーザーがキーレス認証を設定する際に必要な手順が詳述されています。これには、Azure CLIのインストールや、`Cognitive Services User`ロールの割り当てが含まれています。

2. **リソース情報の取得セクションの変更**:
   - `Retrieve key and endpoint`というセクションが`Retrieve resource information`という新しい見出しに置き換えられ、情報の取得方法が簡略化されています。また、特定のリソース情報を取得するためのインクルード文が追加され、より効率的なテキストが提供されています。

3. **環境変数に関する指摘の明確化**:
   - キーレス認証を使用するためには`AZURE_OPENAI_API_KEY`環境変数が設定されていないことを確認する必要があるという注意喚起の情報が追加されています。この変更により、利用者が認証関連の問題を事前に防ぐことができるよう配慮されています。

4. **大幅な削減と簡素化**:
   - 以前の文書から不要な内容が削除され、全体としてよりコンパクトかつ重点的な情報が提供されています。特に、環境変数の設定手順が詳細に扱われていた部分が大幅に削減されています。

この修正により、ユーザーがMicrosoft Entra IDを使ったAzure OpenAIへのアクセスを行うための手順が明確になり、理解しやすくなっています。文書の全体的な可読性が向上し、新しいユーザーに対する助けとなることが期待されます。

## articles/ai-services/openai/includes/text-to-speech-typescript.md{#item-1335d5}

<details>
<summary>Diff</summary>
````diff
@@ -20,58 +20,18 @@ recommendations: false
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
+### Microsoft Entra ID prerequisites
 
-## Set up
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-### Retrieve key and endpoint
+## Retrieve resource information
 
-To successfully make a call against Azure OpenAI, you need an **endpoint** and a **key**.
+[!INCLUDE [resource authentication](resource-auth.md)]
 
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
-| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
-
-Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
-
-:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location highlighted." lightbox="../media/quickstarts/endpoint.png":::
-
-### Environment variables
-
-Create and assign persistent environment variables for your key and endpoint.
-
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
-
-# [Command Line](#tab/command-line)
-
-```CMD
-setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
-```
-
-```CMD
-setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
-```
-
-# [PowerShell](#tab/powershell)
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
-```
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
-```
-
-# [Bash](#tab/bash)
-
-```Bash
-echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
-```
-
-```Bash
-echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
-```
----
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a Node application
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト読み上げのTypeScriptに関する文書の更新"
}
```

### Explanation
この変更は、`text-to-speech-typescript.md`というドキュメントにおいて、主にMicrosoft Entra IDを利用したキーレス認証に関する新しい情報が追加され、全体の構成が整理されたものです。以下はこの変更の概要です。

1. **キーレス認証の前提条件追加**:
   - 新たに「Microsoft Entra IDの前提条件」というセクションが追加され、キーレス認証を利用する際に必要な手顺についての情報が提供されています。具体的には、Azure CLIのインストールと、ユーザーアカウントへの`Cognitive Services User`ロールの割り当てが記載されています。

2. **リソース情報の取得セクションの変更**:
   - 以前の「Retrieve key and endpoint」セクションが「Retrieve resource information」に変更され、正確なリソース情報の取得が強調されています。ここでは、リソースを利用するためのエンドポイントとキーが必要であることが示されています。

3. **情報の簡素化と明確化**:
   - 環境変数に関連するセクションが削減され、必要な情報が簡潔にまとめられています。また、キーレス認証の利用に際し、`AZURE_OPENAI_API_KEY`環境変数が設定されていないことを確認するべきとの注意喚起も追加されています。

4. **リファレンスの整理**:
   - 文書全体がより整理された形になり、重要な情報が簡単に見つけやすくなっています。具体的な手順や情報が明確に示されているため、ユーザーは設定や認証の方法を理解するのが容易になっています。

このような更新により、ユーザーはMicrosoft Entra IDを用いたアクセスに関する理解を深めることができ、よりスムーズに作業を進めることが期待されます。全体として、文書は読者にとって有用かつ取り扱いやすいものとなります。

## articles/ai-services/openai/includes/typescript.md{#item-ee5b93}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.date: 10/22/2024
 [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
 > [!NOTE]
-> This article has been updated to use the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you are looking for code examples for the legacy Azure OpenAI JavaScript SDK they are currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
+> This guide uses the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you're looking for code examples for the legacy Azure OpenAI JavaScript SDK, they're currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
 
 ## Prerequisites
 
@@ -24,23 +24,25 @@ ms.date: 10/22/2024
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI Service resource with the `gpt-35-turbo-instruct` model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
-## Set up
 
-[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+## Retrieve resource information
 
-[!INCLUDE [environment-variables](environment-variables.md)]
+[!INCLUDE [resource authentication](resource-auth.md)]
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it.
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Install the client library
 
+In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it.
+
 Install the required packages for JavaScript with npm from within the context of your new directory:
 
 ```console
 npm install openai @azure/identity
 ```
 
-Your app's _package.json_ file will be updated with the dependencies.
+Your app's _package.json_ file is updated with the dependencies.
 
 
 ## Create a sample application
@@ -200,7 +202,7 @@ Microsoft was founded on April 4, 1975.
 ```
 
 > [!NOTE]
-> If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You may need to remove a pre-existing environment variable for the API key from your system. Even though the Microsoft Entra ID code sample is not explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error will still be generated.
+> If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You might need to remove a preexisting environment variable for the API key from your system. Even though the Microsoft Entra ID code sample isn't explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error is still generated.
 
 
 ## Clean up resources
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TypeScriptに関するガイドの更新"
}
```

### Explanation
この変更は、`typescript.md`というドキュメントにおけるいくつかの文言の修正および整理を行ったもので、安定した情報提供を目的としています。以下はこの変更の概要です。

1. **文言の改善**:
   - 記事の最初の部分で、最新のOpenAI npmパッケージを使用していることが強調されています。古いJavaScript SDKに関するコード例についても言及しており、これらの情報が明確に示されています。

2. **セクション名の変更**:
   - 「Set up」というセクションが「Retrieve resource information」という名前に変更され、リソースにアクセスするために必要な情報を取得することに焦点を当てるように整理されました。

3. **注意事項の追加**:
   - 新しい注意喚起が追加され、SDKを使用する際には`AZURE_OPENAI_API_KEY`環境変数が設定されていないことを確認する必要があることが強調されています。この変更により、ユーザーが潜在的なエラーを事前に回避できるようになります。

4. **文中の表現の明確化**:
   - エラーメッセージに関する説明が改善され、よりわかりやすい表現に変更されています。これにより、ユーザーが問題に直面した際の対処法が理解しやすくなっています。

5. **一貫したスタイルの維持**:
   - ドキュメント全体にわたって、用語やスタイルの一貫性が維持され、情報が整理されています。これにより、ユーザーが必要な情報を迅速に見つけられるようになります。

この修正により、TypeScriptを使用してAzure OpenAIを利用する際のガイドがよりユーザーフレンドリーになり、利用者にとっての理解と実行が容易になることが期待されます。全体的に、文書の明確さと可読性が向上しています。

## articles/ai-services/openai/includes/use-your-data-common-variables.md{#item-c35afc}

<details>
<summary>Diff</summary>
````diff
@@ -1,100 +1,41 @@
 ---
-#services: cognitive-services
-manager: nitinme
-author: travisw
-ms.author: travisw
+author: eric-urban 
+ms.author: eur 
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 08/29/2023
+ms.date: 1/7/2025
 ---
 
-## Retrieve required variables
+## Retrieve resource information
 
-To successfully make a call against Azure OpenAI, you need the following variables. This quickstart assumes you've uploaded your data to an Azure blob storage account and have an Azure AI Search index created. See [Add your data using Azure AI Foundry](../use-your-data-quickstart.md?pivots=programming-language-studio)
+You need to retrieve the following information to authenticate your application with your Azure OpenAI resource. This quickstart assumes you've uploaded your data to an Azure blob storage account and have an Azure AI Search index created. See [Add your data using Azure AI Foundry portal](../use-your-data-quickstart.md?pivots=programming-language-studio).
+
+#### [Microsoft Entra ID](#tab/keyless)
 
 |Variable name | Value |
 |--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your Azure OpenAI resource from the Azure portal. Alternatively, you can find the value in **Azure AI Foundry** > **Chat playground** > **Code view**. An example endpoint is: `https://my-resoruce.openai.azure.com`.|
-| `AZURE_OPENAI_API_KEY` | This value can be found in **Resource management** > **Keys & Endpoint** section when examining your Azure OpenAI resource from the Azure portal. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption. |
-| `AZURE_OPENAI_DEPLOYMENT_ID` | This value corresponds to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Deployments** in the Azure portal or alternatively under **Management** > **Deployments** in Azure AI Foundry portal.|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your Azure OpenAI resource from the Azure portal. An example endpoint is: `https://my-resoruce.openai.azure.com`.|
+| `AZURE_OPENAI_DEPLOYMENT_ID` | This value corresponds to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Deployments** in the Azure portal.|
 | `AZURE_AI_SEARCH_ENDPOINT` | This value can be found in the **Overview** section when examining your Azure AI Search resource from the Azure portal. |
-| `AZURE_AI_SEARCH_API_KEY` | This value can be found in the **Settings** > **Keys** section when examining your Azure AI Search resource from the Azure portal. You can use either the primary admin key or secondary admin key. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption. |
 | `AZURE_AI_SEARCH_INDEX` | This value corresponds to the name of the index you created to store your data. You can find it in the **Overview** section when examining your Azure AI Search resource from the Azure portal. |
 
-### Environment variables
-
-Create and assign persistent environment variables for your key and endpoint.
-
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
-
-# [Command Line](#tab/command-line)
-
-```CMD
-setx AZURE_OPENAI_ENDPOINT REPLACE_WITH_YOUR_AOAI_ENDPOINT_VALUE_HERE
-```
-```CMD
-setx AZURE_OPENAI_API_KEY REPLACE_WITH_YOUR_AOAI_KEY_VALUE_HERE
-```
-```CMD
-setx AZURE_OPENAI_DEPLOYMENT_ID REPLACE_WITH_YOUR_AOAI_DEPLOYMENT_VALUE_HERE
-```
-```CMD
-setx AZURE_AI_SEARCH_ENDPOINT REPLACE_WITH_YOUR_AZURE_SEARCH_RESOURCE_VALUE_HERE
-```
-```CMD
-setx AZURE_AI_SEARCH_API_KEY REPLACE_WITH_YOUR_AZURE_SEARCH_RESOURCE_KEY_VALUE_HERE
-```
-```CMD
-setx AZURE_AI_SEARCH_INDEX REPLACE_WITH_YOUR_INDEX_NAME_HERE
-```
-
-
-# [PowerShell](#tab/powershell)
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_AOAI_ENDPOINT_VALUE_HERE', 'User')
-```
+Learn more about [keyless authentication](/azure/ai-services/authentication) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
 
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_AOAI_KEY_VALUE_HERE', 'User')
-```
+#### [API key](#tab/api-key)
 
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_DEPLOYMENT_ID', 'REPLACE_WITH_YOUR_AOAI_DEPLOYMENT_VALUE_HERE', 'User')
-```
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_AI_SEARCH_ENDPOINT', 'REPLACE_WITH_YOUR_AZURE_SEARCH_RESOURCE_VALUE_HERE', 'User')
-```
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_AI_SEARCH_API_KEY', 'REPLACE_WITH_YOUR_AZURE_SEARCH_RESOURCE_KEY_VALUE_HERE', 'User')
-```
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_AI_SEARCH_INDEX', 'REPLACE_WITH_YOUR_INDEX_NAME_HERE', 'User')
-```
+|Variable name | Value |
+|--------------------------|-------------|
+| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your Azure OpenAI resource from the Azure portal. An example endpoint is: `https://my-resoruce.openai.azure.com`.|
+| `AZURE_OPENAI_API_KEY` | This value can be found in **Resource management** > **Keys & Endpoint** section when examining your Azure OpenAI resource from the Azure portal. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption. |
+| `AZURE_OPENAI_DEPLOYMENT_ID` | This value corresponds to the custom name you chose for your deployment when you deployed a model. This value can be found under **Resource Management** > **Deployments** in the Azure portal.|
+| `AZURE_AI_SEARCH_ENDPOINT` | This value can be found in the **Overview** section when examining your Azure AI Search resource from the Azure portal. |
+| `AZURE_AI_SEARCH_API_KEY` | This value can be found in the **Settings** > **Keys** section when examining your Azure AI Search resource from the Azure portal. You can use either the primary admin key or secondary admin key. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption. |
+| `AZURE_AI_SEARCH_INDEX` | This value corresponds to the name of the index you created to store your data. You can find it in the **Overview** section when examining your Azure AI Search resource from the Azure portal. |
 
-# [Bash](#tab/bash)
+Learn more about [finding API keys](/azure/ai-services/cognitive-services-environment-variables) and [setting environment variables](/azure/ai-services/cognitive-services-environment-variables).
 
-```Bash
-export AZURE_OPENAI_ENDPOINT=REPLACE_WITH_YOUR_AOAI_ENDPOINT_VALUE_HERE
-```
-```Bash
-export AZURE_OPENAI_API_KEY=REPLACE_WITH_YOUR_AOAI_KEY_VALUE_HERE
-```
-```Bash
-export AZURE_OPENAI_DEPLOYMENT_ID=REPLACE_WITH_YOUR_AOAI_DEPLOYMENT_VALUE_HERE
-```
-```Bash
-export AZURE_AI_SEARCH_ENDPOINT=REPLACE_WITH_YOUR_AZURE_SEARCH_RESOURCE_VALUE_HERE
-```
-```Bash
-export AZURE_AI_SEARCH_API_KEY=REPLACE_WITH_YOUR_AZURE_SEARCH_RESOURCE_KEY_VALUE_HERE
-```
-```Bash
-export AZURE_AI_SEARCH_INDEX=REPLACE_WITH_YOUR_INDEX_NAME_HERE
-```
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ---
 
+
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ利用の共通変数に関するガイドの更新"
}
```

### Explanation
この変更は、`use-your-data-common-variables.md`というドキュメントに対する更新であり、主に内容の整理と情報の明確化を行っています。以下はこの変更の概要です。

1. **セクションタイトルの変更**:
   - 「Retrieve required variables」というセクション名が「Retrieve resource information」に変更され、リソース情報を取得するための内容に焦点を当てる形で整理されました。

2. **情報の明確化**:
   - ユーザーがAzure OpenAIリソースに対して認証を行うために必要な変数についてはっきりとした説明がなされており、具体的な情報の取得方法が強調されています。

3. **変数の詳細の強化**:
   - 各変数に対する具体的な説明が補足され、特にAzure AI Searchに関連する情報も含まれました。この変更により、ユーザーが必要な設定を行うための参考となります。

4. **環境変数関連の情報削除**:
   - 環境変数の設定に関する具体的なコマンドが削除されていますが、代わりにキーレス認証やAPIキーの取得に関するガイドへのリンクが追加されています。これにより、情報が集中管理され、ある程度の冗長性が排除されました。

5. **文体の一貫性の確保**:
   - 記事内で用いる表現やスタイルが統一されており、読みやすさが向上しています。これにより、ユーザーは情報を迅速に見つけやすくなっています。

このような変更により、ユーザーがAzure OpenAIを利用する際のリソース情報の取得や設定がより明確になり、理解しやすいものとなっています。全体的には、文書の可読性とユーザビリティが向上しています。

## articles/ai-services/openai/includes/use-your-data-javascript.md{#item-786699}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,6 @@ ms.date: 10/22/2024
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
 
 
-
 ## Initialize a Node.js application
 
 In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptデータ利用ガイドの修正"
}
```

### Explanation
この変更は、`use-your-data-javascript.md`というドキュメントに対する小さな修正で、不要な改行が削除され、セクションの整合性が向上しています。以下はこの変更の概要です。

1. **改行の削除**:
   - 不要な改行が削除され、セクション「Initialize a Node.js application」の前後の整合性が改善されました。これにより、文書がよりコンパクトで読みやすくなっています。

2. **セクションの明確さ**:
   - セクションが適切に構造化されることにより、ユーザーがNode.jsアプリケーションを初期化するための手順に迅速にアクセスできるようになっています。

全体的に、この修正によりドキュメントの可読性が向上し、ユーザーが情報を簡単に理解できるようになっています。このような細かな調整は、文書全体の整然さとプロフェッショナリズムを強化します。

## articles/ai-services/openai/includes/use-your-data-powershell.md{#item-2d7fe4}

<details>
<summary>Diff</summary>
````diff
@@ -78,4 +78,4 @@ The available health plans in the Contoso Electronics plan and benefit packages
 
 ## Chat with your model using a web app
 
-To start chatting with the Azure OpenAI model that uses your data, you can deploy a web app using [Azure OpenAI studio](../concepts/use-your-data.md#deploy-to-a-copilot-preview-teams-app-preview-or-web-app) or example code we [provide on GitHub](https://go.microsoft.com/fwlink/?linkid=2244395). This app deploys using Azure app service, and provides a user interface for sending queries. This app can be used with Azure OpenAI models that use your data, or models that don't use your data. See the readme file in the repo for instructions on requirements, setup, and deployment. You can optionally customize the [frontend and backend logic](../how-to/use-web-app.md#customizing-the-application-using-environment-variables) of the web app by making changes to the source code.
+To start chatting with the Azure OpenAI model that uses your data, you can deploy a web app using [Azure AI Foundry portal](../concepts/use-your-data.md#deploy-to-a-copilot-preview-teams-app-preview-or-web-app) or example code we [provide on GitHub](https://go.microsoft.com/fwlink/?linkid=2244395). This app deploys using Azure app service, and provides a user interface for sending queries. This app can be used with Azure OpenAI models that use your data, or models that don't use your data. See the readme file in the repo for instructions on requirements, setup, and deployment. You can optionally customize the [frontend and backend logic](../how-to/use-web-app.md#customizing-the-application-using-environment-variables) of the web app by making changes to the source code.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PowerShellデータ利用ガイドの更新"
}
```

### Explanation
この変更は、`use-your-data-powershell.md`というドキュメントに対する小さな修正であり、使用しているプラットフォームに関する言及が更新されています。以下はこの変更の概要です。

1. **プラットフォーム名の変更**:
   - 「Azure OpenAI studio」という表現が「Azure AI Foundry portal」に変更されました。これにより、現行のプラットフォーム名に沿った表記に更新され、利用者が最新のリソースにアクセスしやすくなります。

2. **情報の一貫性の確保**:
   - 同じ文脈内で特定のリソース名が一貫して使用されることにより、読者が混乱することなく内容を理解できるようになっています。

この修正により、ドキュメントの正確性が向上し、ユーザーが最新の情報に基づいてアプリケーションを展開することを支援します。全体として、このような小規模な更新は、文書の信頼性を高め、ユーザー体験を向上させる重要な要素です。

## articles/ai-services/openai/includes/use-your-data-rest.md{#item-d1e071}

<details>
<summary>Diff</summary>
````diff
@@ -87,4 +87,4 @@ curl -i -X POST $AZURE_OPENAI_ENDPOINT/openai/deployments/$AZURE_OPENAI_DEPLOYME
 
 ## Chat with your model using a web app
 
-To start chatting with the Azure OpenAI model that uses your data, you can deploy a web app using [Azure OpenAI studio](../concepts/use-your-data.md#deploy-to-a-copilot-preview-teams-app-preview-or-web-app) or example code we [provide on GitHub](https://go.microsoft.com/fwlink/?linkid=2244395). This app deploys using Azure app service, and provides a user interface for sending queries. This app can be used with Azure OpenAI models that use your data, or models that don't use your data. See the readme file in the repo for instructions on requirements, setup, and deployment. You can optionally customize the [frontend and backend logic](../how-to/use-web-app.md#customizing-the-application-using-environment-variables) of the web app by making changes to the source code.
+To start chatting with the Azure OpenAI model that uses your data, you can deploy a web app using [Azure AI Foundry portal](../concepts/use-your-data.md#deploy-to-a-copilot-preview-teams-app-preview-or-web-app) or example code we [provide on GitHub](https://go.microsoft.com/fwlink/?linkid=2244395). This app deploys using Azure app service, and provides a user interface for sending queries. This app can be used with Azure OpenAI models that use your data, or models that don't use your data. See the readme file in the repo for instructions on requirements, setup, and deployment. You can optionally customize the [frontend and backend logic](../how-to/use-web-app.md#customizing-the-application-using-environment-variables) of the web app by making changes to the source code.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIデータ利用ガイドの更新"
}
```

### Explanation
この変更は、`use-your-data-rest.md`というドキュメントに対する小規模な修正であり、Azureのプラットフォーム名が更新されています。以下はこの変更の概要です。

1. **プラットフォーム名の変更**:
   - 「Azure OpenAI studio」という表現が「Azure AI Foundry portal」に変更され、現在のプラットフォーム名に合わせた表記がされました。これにより、最新の情報を反映し、ユーザーが正確なリソースにアクセスできるようになります。

2. **情報の一貫性の確保**:
   - プラットフォーム名の更新により、ドキュメント内の用語が一致し、利用者が混乱することを防ぎます。この変更により全体の文書の整合性が向上します。

この修正は、ドキュメントの信頼性を高め、ユーザーにとって役立つ情報を時代に即した形で提供するための重要なステップです。全体として、この小さな更新は、ユーザー体験の向上や文書の正確性を確保するために重要な役割を果たします。

## articles/ai-services/openai/includes/use-your-data-studio.md{#item-705daf}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ recommendations: false
 
 Start exploring Azure OpenAI capabilities with a no-code approach through the chat playground. It's simply a text box where you can submit a prompt to generate a completion. From this page, you can quickly iterate and experiment with the capabilities. 
 
-:::image type="content" source="../media/quickstarts/chat-playground-new.png" alt-text="Screenshot of the playground page of the Azure OpenAI Studio with sections highlighted." lightbox="../media/quickstarts/chat-playground-new.png":::
+:::image type="content" source="../media/quickstarts/chat-playground-new.png" alt-text="Screenshot of the playground page of the Azure AI Foundry portal with sections highlighted." lightbox="../media/quickstarts/chat-playground-new.png":::
 
 The playground gives you options to tailor your chat experience. On the top menu, you can select **Deploy** to determine which model generates a response using the search results from your index. You choose the number of past messages to include as conversation history for future generated responses. [Conversation history](../concepts/use-your-data.md#conversation-history-for-better-results) gives context to generate related responses but also consumes [token usage](../concepts/use-your-data.md#token-usage-estimation-for-azure-openai-on-your-data). The input token progress indicator keeps track of the token count of the question you submit. 
 
@@ -38,6 +38,6 @@ Send your first query. The chat models perform best in question and answer exerc
 
 Queries that require data analysis would probably fail, such as "*Which health plan is most popular?*". Queries that require information about all of your data will also likely fail, such as "*How many documents have I uploaded?*". Remember that the search engine looks for chunks having exact or similar terms, phrases, or construction to the query. And while the model might understand the question, if search results are chunks from the data set, it's not the right information to answer that kind of question.
 
-Chats are constrained by the number of documents (chunks) returned in the response (limited to 3-20 in Azure OpenAI Studio playground). As you can imagine, posing a question about "all of the titles" requires a full scan of the entire vector store.
+Chats are constrained by the number of documents (chunks) returned in the response (limited to 3-20 in Azure AI Foundry portal playground). As you can imagine, posing a question about "all of the titles" requires a full scan of the entire vector store.
 
 [!INCLUDE [deploy-web-app](deploy-web-app.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルに関するガイドの更新"
}
```

### Explanation
この変更は、`use-your-data-studio.md`という文書に対する小規模な修正であり、Azureのプラットフォームに関する用語が更新されています。以下はこの変更の概要です。

1. **プラットフォーム名の変更**:
   - 「Azure OpenAI Studio」という名称が「Azure AI Foundry portal」に変更されました。これにより、最新のプラットフォーム名を反映させ、利用者が現行のリソースにアクセスしやすくしています。

2. **情報の一貫性**:
   - プラットフォーム名の更新によって、ドキュメント内での用語が一致し、コンテンツの整合性が向上します。この変更は、ユーザーが情報をより容易に理解できるようにするための重要な要素です。

3. **ユーザー体験の向上**:
   - 変更された説明や用語は、利用者がAzureの最新のインターフェースや機能を正確に理解するために役立ちます。特に、チャット体験についての記述が改善され、情報の取得方法や制約についての理解が深まります。

この小規模な更新は、ドキュメントを最新の状態に保ちながら、ユーザーがAzureのサービスを効果的に利用できるようにするための重要な施策です。全体的に、この変更がユーザー体験と文書の信頼性を高めることに寄与しています。

## articles/ai-services/openai/includes/whisper-javascript.md{#item-3ee990}

<details>
<summary>Diff</summary>
````diff
@@ -13,73 +13,23 @@ author: eric-urban
 
 ## Prerequisites
 
-
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
+### Microsoft Entra ID prerequisites
 
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-## Set up
-
-### Retrieve key and endpoint
-
-To successfully make a call against Azure OpenAI, you need an *endpoint* and a *key*.
-
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | The service endpoint can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the endpoint via the **Deployments** page in Azure AI Foundry portal. An example endpoint is: `https://docs-test-001.openai.azure.com/`.|
-| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
-
-Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
-
-:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
-
-### Environment variables
-
-Create and assign persistent environment variables for your key and endpoint.
-
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
-
-# [Command Line](#tab/command-line)
-
-```CMD
-setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
-```
-
-```CMD
-setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
-```
-
-# [PowerShell](#tab/powershell)
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
-```
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
-```
-
-# [Bash](#tab/bash)
-
-```Bash
-echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
-```
-
-```Bash
-echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
-```
----
-
-## Microsoft Entra ID authentication is recommended
+## Retrieve resource information
 
-For passwordless authentication, you need to 
+[!INCLUDE [resource authentication](resource-auth.md)]
 
-1. Use the `@azure/identity` package.
-1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
-1. Sign in with the Azure CLI such as `az login`.
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a Node application
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper JavaScriptガイドの認証手順の更新"
}
```

### Explanation
この変更は、`whisper-javascript.md`というドキュメントに対する小規模な修正であり、Azureの認証手順に関連する情報が更新されています。以下はこの変更の概要です。

1. **Microsoft Entra IDに関する新しいセクションの追加**:
   - 認証方法が「Passwordless authentication」から「Microsoft Entra ID」を使用する推奨の方法にアップデートされました。新しいセクションでは、Microsoft Entra IDを用いたキーなし認証の手順が紹介されています。また、Azure CLIのインストールと「Cognitive Services User」ロールの割り当てについても具体的に説明されています。

2. **不必要な情報の削除**:
   - 従来の手順が削除されたことにより、文書が簡潔化され、重要な情報が強調される形になりました。特に、エンドポイントとAPIキーの取得方法の詳細が簡略化され、現在の推奨手法に集中しています。

3. **環境変数に関する指示の更新**:
   - 環境変数を設定する際に、`AZURE_OPENAI_API_KEY`が設定されていないことを確認するようにという警告が追加されました。これにより、正しい環境設定が簡単に行えるように配慮されています。

この更新により、ユーザーはAzureにおける承認プロセスをより容易に理解し、実行できるようになります。また、文書全体の整合性が向上し、最新の開発環境に適応した情報が提供されるようになっています。全体として、この変更はユーザー体験を大幅に改善することに寄与しています。

## articles/ai-services/openai/includes/whisper-python.md{#item-e61179}

<details>
<summary>Diff</summary>
````diff
@@ -68,7 +68,7 @@ echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/envi
 
 ## Passwordless authentication is recommended
 
-For passwordless authentication, you need to 
+For passwordless authentication, you need to:
 
 1. Use the `@azure/identity` package.
 1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper Pythonガイドの文章修正"
}
```

### Explanation
この変更は、`whisper-python.md`というドキュメントに対する小規模な修正であり、文中の文法的な調整が行われました。以下はこの変更の概要です。

1. **文体の統一**:
   - パスワードレス認証に関する説明の文末にコロン（:）が追加されました。この変更により、文がより一貫性を持ち、読みやすくなります。

2. **見やすさの改善**:
   - コロンの追加により、次のステップのリストを示す際の視覚的な明確さが向上しています。このような小さな変更が、ユーザーが手順を追いやすくするための助けになります。

全体として、この更新はドキュメントの読みやすさを向上させるものであり、特に手順や指示に関する理解を助けるために役立ちます。このような小規模な修正でも、ユーザー体験をより良くするための重要なステップとなります。

## articles/ai-services/openai/includes/whisper-typescript.md{#item-eafedb}

<details>
<summary>Diff</summary>
````diff
@@ -19,65 +19,18 @@ author: eric-urban
 - [Azure CLI](/cli/azure/install-azure-cli) used for passwordless authentication in a local development environment, create the necessary context by signing in with the Azure CLI.
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
-## Set up
+### Microsoft Entra ID prerequisites
 
-### Retrieve key and endpoint
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
-To successfully make a call against Azure OpenAI, you need an *endpoint* and a *key*.
+## Retrieve resource information
 
-|Variable name | Value |
-|--------------------------|-------------|
-| `AZURE_OPENAI_ENDPOINT`               | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. Alternatively, you can find the value in the **Azure OpenAI Studio** > **Playground** > **Code View**. An example endpoint is: `https://aoai-docs.openai.azure.com/`.|
-| `AZURE_OPENAI_API_KEY` | This value can be found in the **Keys & Endpoint** section when examining your resource from the Azure portal. You can use either `KEY1` or `KEY2`.|
+[!INCLUDE [resource authentication](resource-auth.md)]
 
-Go to your resource in the Azure portal. The **Endpoint and Keys** can be found in the **Resource Management** section. Copy your endpoint and access key as you'll need both for authenticating your API calls. You can use either `KEY1` or `KEY2`. Always having two keys allows you to securely rotate and regenerate keys without causing a service disruption.
-
-:::image type="content" source="../media/quickstarts/endpoint.png" alt-text="Screenshot of the overview UI for an Azure OpenAI resource in the Azure portal with the endpoint & access keys location circled in red." lightbox="../media/quickstarts/endpoint.png":::
-
-### Environment variables
-
-Create and assign persistent environment variables for your key and endpoint.
-
-[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
-
-# [Command Line](#tab/command-line)
-
-```CMD
-setx AZURE_OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
-```
-
-```CMD
-setx AZURE_OPENAI_ENDPOINT "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
-```
-
-# [PowerShell](#tab/powershell)
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_API_KEY', 'REPLACE_WITH_YOUR_KEY_VALUE_HERE', 'User')
-```
-
-```powershell
-[System.Environment]::SetEnvironmentVariable('AZURE_OPENAI_ENDPOINT', 'REPLACE_WITH_YOUR_ENDPOINT_HERE', 'User')
-```
-
-# [Bash](#tab/bash)
-
-```Bash
-echo export AZURE_OPENAI_API_KEY="REPLACE_WITH_YOUR_KEY_VALUE_HERE" >> /etc/environment && source /etc/environment
-```
-
-```Bash
-echo export AZURE_OPENAI_ENDPOINT="REPLACE_WITH_YOUR_ENDPOINT_HERE" >> /etc/environment && source /etc/environment
-```
----
-
-## Microsoft Entra ID authentication is recommended
-
-For passwordless authentication, you need to 
-
-1. Use the `@azure/identity` package.
-1. Assign the `Cognitive Services User` role to your user account. This can be done in the Azure portal under **Access control (IAM)** > **Add role assignment**.
-1. Sign in with the Azure CLI such as `az login`.
+> [!CAUTION]
+> To use the recommended keyless authentication with the SDK, make sure that the `AZURE_OPENAI_API_KEY` environment variable isn't set. 
 
 ## Create a Node application
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whisper TypeScriptガイドの認証手順の更新"
}
```

### Explanation
この変更は、`whisper-typescript.md`というドキュメントに対する小規模な修正であり、Azureの認証手順に関連する情報が更新されています。以下はこの変更の概要です。

1. **Microsoft Entra IDに関する新しいセクションの追加**:
   - 認証方法としてMicrosoft Entra IDを用いたキーなし認証の手順が新たに追加されました。このセクションでは、Azure CLIのインストールと「Cognitive Services User」ロールの割り当てが必要であることが説明されています。

2. **不要な情報の削除**:
   - 従来の手順からエンドポイントとAPIキーの取得方法の詳細が削除され、ドキュメントが簡潔化されました。新しいセクションでは、リソース情報を取得するための指示が強調されています。

3. **注意事項の追加**:
   - SDKを用いた推奨のキーなし認証を使用する場合、`AZURE_OPENAI_API_KEY`環境変数が設定されていないことを確認する必要があるという警告が追加されました。これにより、適切な設定の維持が促されます。

全体として、この更新はユーザーがAzureに関連する認証手順をより理解しやすくすることを目的としており、最新の推奨手法に基づいた情報を提供することで、ユーザー体験の改善に貢献しています。

## articles/ai-services/openai/media/tutorials/fine-tuning/studio-deployment-status.png{#item-3cdf5c}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ファインチューニングチュートリアルにおける画像の削除"
}
```

### Explanation
この変更は、`studio-deployment-status.png`という画像ファイルの削除に関するものであり、ファインチューニングチュートリアルのコンテンツに影響を及ぼします。以下はこの変更の概要です。

1. **画像の削除**:
   - 指定された画像ファイルがリポジトリから完全に削除されました。この画像は、おそらくチュートリアルの一部として使用されていたもので、デプロイメントステータスを示すためのビジュアルリソースとして機能していました。

2. **影響の検討**:
   - 画像が削除されることで、ファインチューニングに関するチュートリアルの一部が視覚的な説明を欠くことになります。これは、ユーザーにとって情報の理解を難しくする可能性があります。

3. **今後の対策**:
   - この画像を使用していた部分や、影響を受けるコンテンツについては、新しい代替リソースの提供や、他の補足情報で補う必要があるかもしれません。また、テキストによる説明を強化することも考慮すべきです。

この変更により、ユーザー体験への影響が予想されるため、代替手段を講じることが重要です。

## articles/ai-services/openai/tutorials/fine-tune.md{#item-8f87b5}

<details>
<summary>Diff</summary>
````diff
@@ -35,18 +35,18 @@ In this tutorial you learn how to:
 - [Jupyter Notebooks](https://jupyter.org/)
 - An Azure OpenAI resource in a [region where `gpt-4o-mini-2024-07-18` fine-tuning is available](../concepts/models.md). If you don't have a resource the process of creating one is documented in our resource [deployment guide](../how-to/create-resource.md).
 - Fine-tuning access requires **Cognitive Services OpenAI Contributor**.
-- If you do not already have access to view quota, and deploy models in Azure OpenAI Studio you will require [additional permissions](../how-to/role-based-access-control.md).
+- If you don't already have access to view quota and deploy models in Azure AI Foundry portal, then you need [more permissions](../how-to/role-based-access-control.md).
 
 > [!IMPORTANT]
-> We recommend reviewing the [pricing information](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing) for fine-tuning to familiarize yourself with the associated costs. In testing, this tutorial resulted in 48,000 tokens being billed (4,800 training tokens * 10 epochs of training). Training costs are in addition to the costs that are associated with fine-tuning inference, and the hourly hosting costs of having a fine-tuned model deployed. Once you have completed the tutorial, you should delete your fine-tuned model deployment otherwise you will continue to incur the hourly hosting cost.
+> We recommend reviewing the [pricing information](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/#pricing) for fine-tuning to familiarize yourself with the associated costs. Testing of this tutorial resulted in 48,000 tokens being billed (4,800 training tokens * 10 epochs of training). Training costs are in addition to the costs that are associated with fine-tuning inference, and the hourly hosting costs of having a fine-tuned model deployed. Once you have completed the tutorial, you should delete your fine-tuned model deployment otherwise you continue to incur the hourly hosting cost.
 
 ## Set up
 
 ### Python libraries
 
 # [OpenAI Python 1.x](#tab/python-new)
 
-This tutorial provides examples of some of the latest OpenAI features include seed/events/checkpoints. In order to take advantage of these features you may need to run `pip install openai --upgrade` to upgrade to the latest release.
+This tutorial provides examples of some of the latest OpenAI features include seed/events/checkpoints. In order to take advantage of these features, you might need to run `pip install openai --upgrade` to upgrade to the latest release.
 
 ```cmd
 pip install openai requests tiktoken numpy
@@ -113,7 +113,7 @@ Fine-tuning `gpt-4o-mini-2024-07-18` requires a specially formatted JSONL traini
 {"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "How far is the Moon from Earth?"}, {"role": "assistant", "content": "Around 384,400 kilometers. Give or take a few, like that really matters."}]}
 ```
 
-For this example we'll modify this slightly by changing to:
+For this example we modify this slightly by changing to:
 
 ```json
 {"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the capital of France?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}]}
@@ -123,7 +123,7 @@ For this example we'll modify this slightly by changing to:
 
 While these three examples are helpful to give you the general format, if you want to steer your custom fine-tuned model to respond in a similar way you would need more examples. Generally you want **at least 50 high quality examples** to start out. However, it's entirely possible to have a use case that might require 1,000's of high quality training examples to be successful.
 
-In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively impact performance. If you train the model on a large amount of internal data, without first pruning the dataset for only the highest quality examples, you could end up with a model that performs much worse than expected.
+In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind, low quality examples can negatively affect performance. If you train the model on a large amount of internal data without first pruning the dataset for only the highest quality examples, you could end up with a model that performs worse than expected.
 
 You'll need to create two files `training_set.jsonl` and `validation_set.jsonl`.
 
@@ -134,7 +134,7 @@ Create the files in the same directory that you're running the Jupyter Notebook,
 ```json
 {"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who discovered Antarctica?"}, {"role": "assistant", "content": "Some chaps named Fabian Gottlieb von Bellingshausen and Mikhail Lazarev, as if they don't teach that in every school!"}]}
 {"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What is the biggest ocean?"}, {"role": "assistant", "content": "The Pacific Ocean. It's not like it's a small pond or anything."}]}
-{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What is the largest planet?"}, {"role": "assistant", "content": "It's called Jupiter, you may have heard of it...or not."}]}
+{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What is the largest planet?"}, {"role": "assistant", "content": "It's called Jupiter, you might have heard of it...or not."}]}
 {"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who painted the Mona Lisa?"}, {"role": "assistant", "content": "Oh, some obscure artist named Leonardo da Vinci. Not that he is famous or anything."}]}
 {"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the boiling point of water?"}, {"role": "assistant", "content": "Exciting fact of the day: it's 100 degrees Celsius. Life-changing, isn't it?"}]}
 {"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who wrote 'The Odyssey'?"}, {"role": "assistant", "content": "Oh, just some poet named Homer. Nothing special, really."}]}
@@ -203,12 +203,12 @@ First example in validation set:
 {'role': 'assistant', 'content': "It's Canberra, not Sydney. Shocking, I know!"}
 ```
 
-In this case we only have 10 training and 10 validation examples so while this will demonstrate the basic mechanics of fine-tuning a model this in unlikely to be a large enough number of examples to produce a consistently noticeable impact.
+In this case we only have 10 training and 10 validation examples so while this demonstrates the basic mechanics of fine-tuning a model this in unlikely to be a large enough number of examples to produce a consistently noticeable effect.
 
-Now you can then run some additional code from OpenAI using the tiktoken library to validate the token counts. Token counting using this method is not going to give you the exact token counts that will be used for fine-tuning, but should provide a good estimate.
+Now you can use the tiktoken library to validate the token counts. Token counting using this method isn't going to give you the exact token counts that are used for fine-tuning, but should provide a good estimate.
 
 > [!NOTE]
-> Individual examples need to remain under the `gpt-4o-mini-2024-07-18` model's current training example context legnth of: 64,536 tokens. The model's input token limit remains 128,000 tokens.
+> Individual examples need to remain under the `gpt-4o-mini-2024-07-18` model's current training example context length of: 64,536 tokens. The model's input token limit remains 128,000 tokens.
 
 ```python
 # Validate token counts
@@ -371,11 +371,11 @@ Validation file ID: file-8556c3bb41b7416bb7519b47fcd1dd6b
 
 ## Begin fine-tuning
 
-Now that the fine-tuning files have been successfully uploaded you can submit your fine-tuning training job:
+Now that the fine-tuning files are successfully uploaded you can submit your fine-tuning training job:
 
 # [OpenAI Python 1.x](#tab/python-new)
 
-In this example we're also passing the seed parameter. The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but can differ in rare cases. If a seed isn't specified, one will be generated for you.
+In this example, we're also passing the seed parameter. The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but can differ in rare cases. If a seed isn't specified, one is generated for you.
 
 ```python
 # Submit fine-tuning training job
@@ -556,7 +556,7 @@ Status: pending
 }
 ```
 
-It isn't unusual for training to take more than an hour to complete. Once training is completed the output message will change to something like:
+It isn't unusual for training to take more than an hour to complete. Once training is completed the output message changes to something like:
 
 ```output
 Fine-tuning job ftjob-900fcfc7ea1d4360a9f0cb1697b4eaa6 finished with status: succeeded
@@ -568,7 +568,7 @@ Found 4 fine-tune jobs.
 
 API version: `2024-08-01-preview` or later is required for this command.
 
-While not necessary to complete fine-tuning it can be helpful to examine the individual fine-tuning events that were generated during training. The full training results can also be examined after training is complete in the [training results file](../how-to/fine-tuning.md#analyze-your-customized-model).
+While not necessary to complete fine-tuning, it can be helpful to examine the individual fine-tuning events that were generated during training. The full training results can also be examined after training is complete in the [training results file](../how-to/fine-tuning.md#analyze-your-customized-model).
 
 # [OpenAI Python 1.x](#tab/python-new)
 
@@ -732,7 +732,7 @@ This command isn't available in the 0.28.1 OpenAI Python library. Upgrade to the
 
 API version: `2024-08-01-preview` or later is required for this command.
 
-When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be particularly useful, as they can provide a snapshot of your model prior to overfitting having occurred. When a fine-tuning job completes you will have the three most recent versions of the model available to deploy. The final epoch will be represented by your fine-tuned model, the previous two epochs will be available as checkpoints.
+When each training epoch completes a checkpoint is generated. A checkpoint is a fully functional version of a model which can both be deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be useful, as they can provide a snapshot of your model prior to overfitting having occurred. When a fine-tuning job completes, you have the three most recent versions of the model available to deploy. The final epoch will be represented by your fine-tuned model, the previous two epochs are available as checkpoints.
 
 # [OpenAI Python 1.x](#tab/python-new)
 
@@ -841,16 +841,16 @@ fine_tuned_model = response["fine_tuned_model"]
 
 Unlike the previous Python SDK commands in this tutorial, since the introduction of the quota feature, model deployment must be done using the [REST API](/rest/api/aiservices/accountmanagement/deployments/create-or-update?tabs=HTTP), which requires separate authorization, a different API path, and a different API version.
 
-Alternatively, you can deploy your fine-tuned model using any of the other common deployment methods like [Azure OpenAI Studio](https://oai.azure.com/), or [Azure CLI](/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-create()).
+Alternatively, you can deploy your fine-tuned model using any of the other common deployment methods like [Azure AI Foundry portal](https://ai.azure.com/), or [Azure CLI](/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-create()).
 
 |variable      | Definition|
 |--------------|-----------|
 | token        | There are multiple ways to generate an authorization token. The easiest method for initial testing is to launch the Cloud Shell from the [Azure portal](https://portal.azure.com). Then run [`az account get-access-token`](/cli/azure/account#az-account-get-access-token()). You can use this token as your temporary authorization token for API testing. We recommend storing this in a new environment variable|
 | subscription | The subscription ID for the associated Azure OpenAI resource |
 | resource_group | The resource group name for your Azure OpenAI resource |
 | resource_name | The Azure OpenAI resource name |
-| model_deployment_name | The custom name for your new fine-tuned model deployment. This is the name that will be referenced in your code when making chat completion calls. |
-| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It will look like `gpt-4o-mini-2024-07-18.ft-0e208cf33a6a466994aff31a08aba678`. You'll need to add that value to the deploy_data json. |
+| model_deployment_name | The custom name for your new fine-tuned model deployment. This is the name that is referenced in your code when making chat completion calls. |
+| fine_tuned_model | Retrieve this value from your fine-tuning job results in the previous step. It looks like `gpt-4o-mini-2024-07-18.ft-0e208cf33a6a466994aff31a08aba678`. You need to add that value to the deploy_data json. |
 
 [!INCLUDE [Fine-tuning deletion](../includes/fine-tune.md)]
 
@@ -892,15 +892,13 @@ print(r.reason)
 print(r.json())
 ```
 
-You can check on your deployment progress in the Azure OpenAI Studio:
-
-:::image type="content" source="../media/tutorials/fine-tuning/studio-deployment-status.png" alt-text="Screenshot of Deployment progress on Azure OpenAI Studio." lightbox="../media/tutorials/fine-tuning/studio-deployment-status.png":::
+You can check on your deployment progress in the Azure AI Foundry portal.
 
 It isn't uncommon for this process to take some time to complete when dealing with deploying fine-tuned models.
 
 ## Use a deployed customized model
 
-After your fine-tuned model is deployed, you can use it like any other deployed model in either the [Chat Playground of Azure OpenAI Studio](https://oai.azure.com), or via the chat completion API. For example, you can send a chat completion call to your deployed model, as shown in the following Python example. You can continue to use the same parameters with your customized model, such as temperature and max_tokens, as you can with other deployed models.
+After your fine-tuned model is deployed, you can use it like any other deployed model in either the [Chat Playground of Azure AI Foundry portal](https://ai.azure.com), or via the chat completion API. For example, you can send a chat completion call to your deployed model, as shown in the following Python example. You can continue to use the same parameters with your customized model, such as temperature and max_tokens, as you can with other deployed models.
 
 # [OpenAI Python 1.x](#tab/python-new)
 
@@ -964,11 +962,11 @@ Unlike other types of Azure OpenAI models, fine-tuned/customized models have [an
 
 Deleting the deployment won't affect the model itself, so you can re-deploy the fine-tuned model that you trained for this tutorial at any time.
 
-You can delete the deployment in [Azure OpenAI Studio](https://oai.azure.com/), via [REST API](/rest/api/aiservices/accountmanagement/deployments/delete?tabs=HTTP), [Azure CLI](/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-delete()), or other supported deployment methods.
+You can delete the deployment in [Azure AI Foundry portal](https://ai.azure.com/), via [REST API](/rest/api/aiservices/accountmanagement/deployments/delete?tabs=HTTP), [Azure CLI](/cli/azure/cognitiveservices/account/deployment#az-cognitiveservices-account-deployment-delete()), or other supported deployment methods.
 
 ## Troubleshooting
 
-### How do I enable fine-tuning? Create a custom model is grayed out in Azure OpenAI Studio
+### How do I enable fine-tuning? Create a custom model is grayed out.
 
 In order to successfully access fine-tuning you need **Cognitive Services OpenAI Contributor assigned**. Even someone with high-level Service Administrator permissions would still need this account explicitly set in order to access fine-tuning. For more information please review the [role-based access control guidance](/azure/ai-services/openai/how-to/role-based-access-control#cognitive-services-openai-contributor).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングチュートリアルの内容更新"
}
```

### Explanation
この変更は、`fine-tune.md`というファインチューニングに関するチュートリアルドキュメントに対する際立った更新を示します。以下はこの変更の概要です。

1. **用語の更新**:
   - Azureのプラットフォーム名が「Azure OpenAI Studio」から「Azure AI Foundry portal」に変更され、一貫性が持たれています。また、一部の文法や表現が自然な形に修正されています。

2. **重要な注意事項の強調**:
   - コストに関する警告文が少し変更され、ユーザーがファインチューニングやデプロイメントのコストを理解しやすくなるように注意喚起が強化されています。具体的には、モデルをデプロイした後もコストが発生する可能性があることが明確にされています。

3. **文書の整合性向上**:
   - 文の構造が改善され、流れが自然になっており、情報がより明確に伝わるようになりました。例文に関する表現が若干の修正を受けており、文法上の小さな修正が行われています。

4. **新しいリソースへのリンク**:
   - 新しいポータルでの操作に関する手順が追加され、ユーザーが最新のツールやリソースにアクセスしやすくなっています。

これらの変更により、チュートリアルはより分かりやすく、実用的な情報を提供するものとなっており、ユーザーの学習体験が向上することが期待されます。

## articles/ai-services/openai/use-your-data-quickstart.md{#item-52c1f4}

<details>
<summary>Diff</summary>
````diff
@@ -77,8 +77,9 @@ The following resources:
 
 ::: zone pivot="programming-language-javascript"
 
-## Prerequisites
+[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
+## Prerequisites
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
@@ -89,9 +90,11 @@ The following resources:
 
 - Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
 
+### Microsoft Entra ID prerequisites
 
-[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
-
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
 [!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
 
@@ -101,6 +104,8 @@ The following resources:
 
 ::: zone pivot="programming-language-typescript"
 
+[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
 ## Prerequisites
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
@@ -114,9 +119,11 @@ The following resources:
 
 - Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
 
+### Microsoft Entra ID prerequisites
 
-[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
-
+For the recommended keyless authentication with Microsoft Entra ID, you need to:
+- Install the [Azure CLI](/cli/azure/install-azure-cli) used for keyless authentication with Microsoft Entra ID.
+- Assign the `Cognitive Services User` role to your user account. You can assign roles in the Azure portal under **Access control (IAM)** > **Add role assignment**.
 
 [!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ利用クイックスタートの前提条件に関する更新"
}
```

### Explanation
この変更は、`use-your-data-quickstart.md`というドキュメントに対する軽微な更新を示しています。以下はこの変更の概要です。

1. **前提条件の整備**:
   - 前提条件が整理され、Microsoft Entra IDに関連する新しい設定が追加されました。特に、キーを使用しない認証の推奨事項が強調されています。

2. **新しい手順の追加**:
   - Microsoft Entra IDを使用した認証に関する具体的な手順が追加され、Azure CLIをインストールし、ユーザーアカウントに`Cognitive Services User`ロールを割り当てる必要があることが明示されています。

3. **リファレンスリンクの改善**:
   - 参照ドキュメント、ソースコード、npmパッケージ、サンプルへのリンクが各セクションで再度配置され、ユーザーが必要な情報に迅速にアクセスできるよう改善されています。

4. **視覚的要素の強化**:
   - Microsoft Entra ID関連の情報がセクションとして分けられ、見やすさや理解のしやすさが向上しています。

これにより、ドキュメントはより体系的で明確に情報が整理されており、ユーザーにとって便利かつ使用しやすいものになっています。データを利用するための環境設定が一層簡潔になり、ユーザーが迅速に必要な手続きを行えるようになっています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -145,7 +145,7 @@ Global batch now supports GPT-4o (2024-08-06). See the [global batch getting sta
 
 ### Azure OpenAI Studio UX updates
 
-On September 19, when you access the [Azure OpenAI Studio](https://oai.azure.com/) you'll begin to no longer see the legacy Azure AI Foundry portal by default. If needed you'll still be able to go back to the previous experience by using the **Switch to the old look** toggle in the top bar of the UI for the next couple of weeks. If you switch back to legacy Azure AI Foundry portal, it helps if you fill out the feedback form to let us know why. We're actively monitoring this feedback to improve the new experience.
+As of September 19, 2024, when you go to the [Azure OpenAI Studio](https://oai.azure.com/) you no longer see the legacy Azure OpenAI Studio by default. If needed you'll still be able to go back to the previous experience by using the **Switch to the old look** toggle in the top bar of the UI for the next couple of weeks. If you switch back to legacy Azure AI Foundry portal, it helps if you fill out the feedback form to let us know why. We're actively monitoring this feedback to improve the new experience.
 
 
 ### GPT-4o 2024-08-06 provisioned deployments
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Studioのユーザーエクスペリエンス更新日付の修正"
}
```

### Explanation
この変更は、`whats-new.md`というドキュメント内のAzure OpenAI Studioのユーザーエクスペリエンスに関する情報を修正したものです。主な変更点は以下の通りです。

1. **日付の更新**:
   - 「2024年9月19日」と「従来のAzure AI Foundryポータル」という表現に関する記述が修正され、ユーザーがAzure OpenAI Studioを使用する際の背景が正確に反映されています。修正後は「従来のAzure OpenAI Studio」との表現になっています。

2. **表現の明確化**:
   - 修正が行われた文の表現が整理され、全体として理解しやすくなりました。この変更によって、ユーザーは新しいエクスペリエンスに対するフィードバックを提供しやすくなると同時に、旧インターフェースへの切り替えがどのように行われるかをより明確に理解できるようになっています。

この更新により、ユーザーは最新の情報に基づいてAzure OpenAI Studioを利用でき、変更点やフィードバック提供方法がより分かりやすくなることが期待されます。


