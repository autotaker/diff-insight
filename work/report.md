---
title: Diff Insight Report
date: 2024-09-09
---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:72f3416...MicrosoftDocs:3501c57){target="_blank"}

# ハイライト
このコードの変更は、AzureのAIサービス関連文書の改善に焦点を当てており、主に以下の点が含まれます：

- モデルカスタマイズに関する注意情報の追加
- 有害カテゴリに対するAPI用語の追加
- ローカル認証の無効化に関する手順の追加

## 新機能
特に新機能は追加されていませんが、以下の改善が行われています：

- モデルカスタマイズの使い方に関する注意情報の明示
- 有害カテゴリごとにAPI用語の追加
- ローカル認証の無効化方法に関する細胞な手順の追加

## 破壊的変更
これらの変更によって既存の機能が破壊されるようなことはありません。

## その他の更新
微細な文書の修正や情報の追加が行われています。

# インサイト
今回の変更は、ユーザーがAzure AIサービスをより効率的に利用するための文書の改善が中心です。

### モデルカスタマイズに関する注意情報の追加
まず、「モデルカスタマイズ」関連の文書に、新たに注意情報が追加されており、これはモデルカスタマイズがクライアント言語SDKではなく、REST APIおよびVision Studioを通じて利用可能であることを明確にしています。これにより、ユーザーは誤ったアプローチを取ることを避け、指定された方法を利用して画像分類モデルを作成することができます。また、見出しの一貫性を保つための微調整も行われ、一貫した読みやすさを提供しています。

### 有害カテゴリにAPI用語を追加
次に、有害カテゴリにAPI用語を追加することで、開発者が特定の有害カテゴリを簡単に識別できるようになりました。これにより、文書の実用性が向上し、開発作業の効率もアップします。例えば、「Hate and Fairness」には`Hate`、「Sexual」には`Sexual`というAPI用語が追加されています。これにより、APIユーザーは直感的にこれらのカテゴリを利用できるようになります。

### ローカル認証の無効化に関する手順の追加
最後に、ローカル認証の無効化方法についての詳細な手順が文書化されています。今回の更新では、Azureポリシーを使った設定に加え、PowerShellおよびAzure CLIを使用して個々のリソースで設定を行う手順が追加されています。具体的なコマンド例として、`Connect-AzAccount` や `Set-AzCognitiveServicesAccount`が示されており、ユーザーはこれらを指示通りに利用することで簡単に設定を行うことができます。また、ローカル認証の状態を確認する方法も詳述されており、設定変更後の確認プロセスも提供されています。

これらの変更は、ユーザーが自分のプロジェクトにおいて必要な設定や操作を迷うことなくスムーズに行えるようにするためのものです。追加された情報と手順により、効率的でストレスのない設定が可能となります。

具体的な変更は以下のリンクから確認できます：
- [モデルカスタマイズ](https://github.com/MicrosoftDocs/azure-ai-docs/blob/3501c5790df351e75164730b0049cc6c3199bcc6/articles/ai-services/computer-vision/how-to/model-customization.md)
- [有害カテゴリ](https://github.com/MicrosoftDocs/azure-ai-docs/blob/3501c5790df351e75164730b0049cc6c3199bcc6/articles/ai-services/content-safety/concepts/harm-categories.md)
- [ローカル認証の無効化](https://github.com/MicrosoftDocs/azure-ai-docs/blob/3501c5790df351e75164730b0049cc6c3199bcc6/articles/ai-services/disable-local-auth.md)

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-customization.md](#item-a3f1c3) | minor update | モデルカスタマイズに関する注意情報の追加 | modified | 5 | 2 | 7 | 
| [harm-categories.md](#item-4c6a07) | minor update | 有害カテゴリにAPI用語を追加 | modified | 6 | 6 | 12 | 
| [disable-local-auth.md](#item-ae6204) | minor update | ローカル認証の無効化に関する手順の追加 | modified | 10 | 2 | 12 | 


# Modified Contents
## articles/ai-services/computer-vision/how-to/model-customization.md{#item-a3f1c3}

<details>
<summary>Diff</summary>
```diff
@@ -18,6 +18,9 @@ Image Analysis 4.0 allows you to train a custom model using your own training im
 
 This guide shows you how to create and train a custom image classification model. The few differences between training an image classification model and object detection model are noted.
 
+> [!NOTE]
+> Model customization is available through the REST API and Vision Studio, but not through the client language SDKs.
+
 ## Prerequisites
 
 * Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services)
@@ -331,7 +334,7 @@ If an evaluation set isn't provided when training the model, the reported perfor
 
 ![Screenshot of evaluation]( ../media/customization/training-result.png)
 
-## Test custom model in Vision Studio
+## Test the custom model in Vision Studio
 
 Once you've built a custom model, you can test by selecting the **Try it out** button on the model evaluation screen.
 
@@ -466,7 +469,7 @@ The API call returns an **ImageAnalysisResult** JSON object, which contains all
 
 ## Next steps
 
-In this guide, you created and trained a custom image classification model using Image Analysis. Next, learn more about the Analyze Image 4.0 API, so you can call your custom model from an application using REST or library SDKs.
+In this guide, you created and trained a custom image classification model using Image Analysis. Next, learn more about the Analyze Image 4.0 API, so you can call your custom model from an application using REST.
 
 * See the [Model customization concepts](../concept-model-customization.md) guide for a broad overview of this feature and a list of frequently asked questions.
 * [Call the Analyze Image API](./call-analyze-image-40.md). <!--Note the sections [Set model name when using a custom model](./call-analyze-image-40.md#set-model-name-when-using-a-custom-model) and [Get results using custom model](./call-analyze-image-40.md#get-results-using-custom-model).-->
```
</details>

### Summary

```json
{
    "filename": "articles/ai-services/computer-vision/how-to/model-customization.md",
    "modification_type": "minor update",
    "modification_title": "モデルカスタマイズに関する注意情報の追加"
}
```

### Explanation
このコードの変更は、特定の文書内での軽微な更新を示しています。主に、モデルカスタマイズがクライアント言語SDKではなく、REST APIおよびVision Studioを通じて利用可能であることに関する注意を追加しました。この情報は、読者が画像分類モデルを作成する際の前提条件を理解する上で重要です。

また、見出し「Test custom model in Vision Studio」を「Test the custom model in Vision Studio」に変更し、文書全体の一貫性を向上させています。さらに、次のステップを示すセクションでは、REST APIを用いてカスタムモデルをアプリケーションから呼び出す説明が強調されています。

全体として、これらの変更は情報の明確さと利用者の理解を高めることを目的としています。変更の詳細は以下のリンクから確認できます: [こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/3501c5790df351e75164730b0049cc6c3199bcc6/articles/ai-services/computer-vision/how-to/model-customization.md)。

## articles/ai-services/content-safety/concepts/harm-categories.md{#item-4c6a07}

<details>
<summary>Diff</summary>
```diff
@@ -21,12 +21,12 @@ This guide describes all of the harm categories and ratings that Azure AI Conten
 
 Content Safety recognizes four distinct categories of objectionable content.
 
-| Category  | Description         |
-| --------- | ------------------- |
-| Hate and Fairness      | Hate and fairness-related harms refer to any content that attacks or uses discriminatory language with reference to a person or Identity group based on certain differentiating attributes of these groups. <br><br>This includes, but is not limited to:<ul><li>Race, ethnicity, nationality</li><li>Gender identity groups and expression</li><li>Sexual orientation</li><li>Religion</li><li>Personal appearance and body size</li><li>Disability status</li><li>Harassment and bullying</li></ul> |
-| Sexual  | Sexual describes language related to anatomical organs and genitals, romantic relationships and sexual acts, acts portrayed in erotic or affectionate terms, including those portrayed as an assault or a forced sexual violent act against one’s will. <br><br> This includes but is not limited to:<ul><li>Vulgar content</li><li>Prostitution</li><li>Nudity and Pornography</li><li>Abuse</li><li>Child exploitation, child abuse, child grooming</li></ul>   |
-| Violence  | Violence describes language related to physical actions intended to hurt, injure, damage, or kill someone or something; describes weapons, guns and related entities. <br><br>This includes, but isn't limited to:  <ul><li>Weapons</li><li>Bullying and intimidation</li><li>Terrorist and violent extremism</li><li>Stalking</li></ul>  |
-| Self-Harm  | Self-harm describes language related to physical actions intended to purposely hurt, injure, damage one’s body or kill oneself. <br><br> This includes, but isn't limited to: <ul><li>Eating Disorders</li><li>Bullying and intimidation</li></ul>  |
+| Category  | Description         |API term |
+| --------- | ------------------- | -- |
+| Hate and Fairness      | Hate and fairness-related harms refer to any content that attacks or uses discriminatory language with reference to a person or Identity group based on certain differentiating attributes of these groups. <br><br>This includes, but is not limited to:<ul><li>Race, ethnicity, nationality</li><li>Gender identity groups and expression</li><li>Sexual orientation</li><li>Religion</li><li>Personal appearance and body size</li><li>Disability status</li><li>Harassment and bullying</li></ul> | `Hate` |
+| Sexual  | Sexual describes language related to anatomical organs and genitals, romantic relationships and sexual acts, acts portrayed in erotic or affectionate terms, including those portrayed as an assault or a forced sexual violent act against one’s will. <br><br> This includes but is not limited to:<ul><li>Vulgar content</li><li>Prostitution</li><li>Nudity and Pornography</li><li>Abuse</li><li>Child exploitation, child abuse, child grooming</li></ul>   | `Sexual` |
+| Violence  | Violence describes language related to physical actions intended to hurt, injure, damage, or kill someone or something; describes weapons, guns and related entities. <br><br>This includes, but isn't limited to:  <ul><li>Weapons</li><li>Bullying and intimidation</li><li>Terrorist and violent extremism</li><li>Stalking</li></ul>  | `Violence` |
+| Self-Harm  | Self-harm describes language related to physical actions intended to purposely hurt, injure, damage one’s body or kill oneself. <br><br> This includes, but isn't limited to: <ul><li>Eating Disorders</li><li>Bullying and intimidation</li></ul>  | `SelfHarm` |
 
 Classification can be multi-labeled. For example, when a text sample goes through the text moderation model, it could be classified as both Sexual content and Violence.
 
```
</details>

### Summary

```json
{
    "filename": "articles/ai-services/content-safety/concepts/harm-categories.md",
    "modification_type": "minor update",
    "modification_title": "有害カテゴリにAPI用語を追加"
}
```

### Explanation
このコードの変更は、「有害カテゴリ」に関する文書に対する軽微な更新を反映しています。具体的には、各有害カテゴリの説明にAPI用語を追加しました。これにより、開発者が代数的にそれぞれのカテゴリを参照しやすくなります。

変更点としては、カテゴリのテーブルに「API term」という列を追加し、各カテゴリに対する識別子を明示的に示しています。例えば、「Hate and Fairness」には`Hate`、 「Sexual」には`Sexual`、 「Violence」には`Violence`、そして 「Self-Harm」には`SelfHarm`というラベルが付けられています。これにより、APIのユーザーは、これらの用語を使って有害カテゴリを簡単に識別できるようになります。

全体として、この変更は、文書がより実用的で、使用する際の利便性を向上させることを目指しています。具体的な変更内容は以下のリンクから確認できます: [こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/3501c5790df351e75164730b0049cc6c3199bcc6/articles/ai-services/content-safety/concepts/harm-categories.md)。

## articles/ai-services/disable-local-auth.md{#item-ae6204}

<details>
<summary>Diff</summary>
```diff
@@ -13,13 +13,21 @@ ms.author: pafarley
 
 # Disable local authentication in Azure AI Services
 
-Azure AI Services provides Microsoft Entra authentication support for all resources. This gives organizations control to disable local authentication methods and enforce Microsoft Entra authentication. This feature provides you with seamless integration when you require centralized control and management of identities and resource credentials.
+Azure AI Services provides Microsoft Entra authentication support for all resources. This feature provides you with seamless integration when you require centralized control and management of identities and resource credentials. Organizations can disable local authentication methods and enforce Microsoft Entra authentication instead.
 
-You can disable local authentication using the Azure policy [Cognitive Services accounts should have local authentication methods disabled](https://ms.portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F71ef260a-8f18-47b7-abcb-62d0673d94dc). You can set it at the subscription level or resource group level to enforce the policy for a group of services.
+You can disable local authentication using the Azure policy [Cognitive Services accounts should have local authentication methods disabled](https://ms.portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F71ef260a-8f18-47b7-abcb-62d0673d94dc). Set it at the subscription level or resource group level to enforce the policy for a group of services.
 
 If you're creating an account using Bicep / ARM template, you can set the property `disableLocalAuth` to `true` to disable local authentication. For more information, see 
 [Microsoft.CognitiveServices accounts - Bicep, ARM template, & Terraform](/azure/templates/microsoft.cognitiveservices/accounts)
 
+You can also use PowerShell with the Azure CLI to disable local authentication for an individual resource. First sign in with the `Connect-AzAccount` command. Then use the `Set-AzCognitiveServicesAccount` cmdlet with the parameter `-DisableLocalAuth $true`, like the following example:
+
+```powershell
+Set-AzCognitiveServicesAccount -ResourceGroupName "my-resource-group" -Name "my-resource-name" -DisableLocalAuth $false
+```
+
+## Verify local authentication status
+
 Disabling local authentication doesn't take effect immediately. Allow a few minutes for the service to block future authentication requests.
 
 You can use PowerShell to determine whether the local authentication policy is currently enabled. First sign in with the `Connect-AzAccount` command. Then use the cmdlet **[Get-AzCognitiveServicesAccount](/powershell/module/az.cognitiveservices/get-azcognitiveservicesaccount)** to retrieve your resource, and check the property `DisableLocalAuth`. A value of `true` means local authentication is disabled.
```
</details>

### Summary

```json
{
    "filename": "articles/ai-services/disable-local-auth.md",
    "modification_type": "minor update",
    "modification_title": "ローカル認証の無効化に関する手順の追加"
}
```

### Explanation
このコードの変更は、Azure AI Servicesにおけるローカル認証の無効化に関する文書に対する軽微な更新を示しています。主なポイントは、ローカル認証を無効にするための手順を明確にし、PowerShellを使用した方法を追加したことです。

変更内容には、ローカル認証を無効にする方法の説明が含まれています。具体的には、Azureポリシーを使用してローカル認証を無効化する手続きの説明に少し手を加え、より簡潔にしました。また、個々のリソースに対してPowerShellとAzure CLIを使用してローカル認証を無効化する手順も追加されています。この部分では、`Connect-AzAccount`コマンドを使用してサインインし、`Set-AzCognitiveServicesAccount`コマンドレットを用いて設定を行う具体例が示されています。

さらに、「ローカル認証の状況を確認する」セクションが新たに追加され、無効化が実際に適用されるまでの待機時間や、PowerShellを使って現在のポリシーの状態を確認する方法が詳述されています。

これにより、ユーザーはローカル認証を無効にする際の手順をより理解しやすくなり、作業の効率が向上します。具体的な変更内容は以下のリンクから確認できます: [こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/3501c5790df351e75164730b0049cc6c3199bcc6/articles/ai-services/disable-local-auth.md)。


