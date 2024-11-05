---
date: '2024-11-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8de853c...MicrosoftDocs:c2df9dc
summary: この変更では、OpenAIのコンテンツフィルタとAzure OpenAIのクォータに関するドキュメントが更新されました。新しいセクションや具体的な使用方法が追加され、ユーザーがこれらのサービスをより効率的に活用できるための情報が提供されています。特に、「Groundedness」という新セクションがコンテンツフィルタ文書に追加され、生成AIの基底性を検出する機能が説明されています。また、Azure
  OpenAIのクォータに関するドキュメントには、Azure PowerShellを用いたクォータ管理の情報とコマンド例が追加されています。全体として、ユーザーは最新の技術を活用しやすくなるでしょう。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8de853c...MicrosoftDocs:c2df9dc){target="_blank"}

# ハイライト
この変更では、OpenAIのコンテンツフィルタおよびAzure OpenAIのクォータに関するドキュメントのアップデートが行われました。それぞれのドキュメントでは、新しいセクションの追加や具体的な使用方法の解説が加えられており、ユーザーがこれらのサービスをより効率的に利用できるようにするための情報が提供されています。

## 新機能
- 「Groundedness」という新しいセクションがコンテンツフィルタのドキュメントに追加され、生成AIの基底性を検出する機能について説明されています。
- Azure OpenAIのクォータに関するドキュメントでは、Azure PowerShellを利用したクォータ管理に関する新しい情報とコマンド例が紹介されています。

## 破壊的変更
特に破壊的な変更は報告されていませんが、APIのバージョンによるAnnotationの可用性に関するテーブルが更新されています。

## その他の更新
- コンテンツフィルタのドキュメントでは、未基底コンテンツのフィルタリング方法や攻撃に関する対応状況についての情報が追加されています。

# インサイト
このドキュメント修正の意図は、ユーザーが生成AIおよびAzureサービスをより最適に活用できるよう、使用する際に必要な情報を包括的に提供することです。

OpenAIコンテンツフィルタのドキュメントにおける「Groundedness」セクションの追加は、AI生成コンテンツの信頼性を高めるための重要なステップです。特に、ソース資料に基づくコンテンツ生成の重要性が高まっている中で、未基底コンテンツを検出し排除する機能を強調することは、多くのビジネスユースケースにおけるコンテクストの正確性を保証する点で有益です。

Azure OpenAIクォータのドキュメント更新は、Azure PowerShellを利用するユーザーにとって非常に有用です。具体的なコマンドとそれを使ったクォータの確認方法が明示されていることで、ユーザーはリソース管理をより効率的かつ正確に行うことが可能になります。特に「Get-AzCognitiveServicesUsage」の使用例は、日常的にAzureリソースを管理している技術者にとって効果的な実装の参考となるでしょう。

これらの更新により、ユーザーはOpenAIやAzureの生成AI機能をより効率的に利用し、サポートされている最新の技術と機能を十分に活用できるようになります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [content-filter.md](#item-dfc7e7) | minor update | コンテンツフィルタードキュメントの更新 | modified | 52 | 14 | 66 | 
| [quota.md](#item-9440c2) | minor update | Azure PowerShellの使用法に関する更新 | modified | 68 | 1 | 69 | 


# Modified Contents
## articles/ai-services/openai/concepts/content-filter.md{#item-dfc7e7}

<details>
<summary>Diff</summary>
````diff
@@ -43,13 +43,15 @@ Text and image models support Drugs as an additional classification. This catego
 | Sexual  | Sexual describes language related to anatomical organs and genitals, romantic relationships and sexual acts, acts portrayed in erotic or affectionate terms, including those portrayed as an assault or a forced sexual violent act against one’s will. <br><br> This includes but is not limited to:<ul><li>Vulgar content</li><li>Prostitution</li><li>Nudity and Pornography</li><li>Abuse</li><li>Child exploitation, child abuse, child grooming</li></ul>   |
 | Violence  | Violence describes language related to physical actions intended to hurt, injure, damage, or kill someone or something; describes weapons, guns and related entities. <br><br>This includes, but isn't limited to:  <ul><li>Weapons</li><li>Bullying and intimidation</li><li>Terrorist and violent extremism</li><li>Stalking</li></ul>  |
 | Self-Harm  | Self-harm describes language related to physical actions intended to purposely hurt, injure, damage one’s body or kill oneself. <br><br> This includes, but isn't limited to: <ul><li>Eating Disorders</li><li>Bullying and intimidation</li></ul>  |
-| Protected Material for Text<sup>*</sup> | Protected material text describes known text content (for example, song lyrics, articles, recipes, and selected web content) that can be outputted by large language models.
+| Protected Material for Text<sup>1</sup> | Protected material text describes known text content (for example, song lyrics, articles, recipes, and selected web content) that can be outputted by large language models.
 | Protected Material for Code | Protected material code describes source code that matches a set of source code from public repositories, which can be outputted by large language models without proper citation of source repositories.
 |User Prompt Attacks |User prompt attacks are User Prompts designed to provoke the Generative AI model into exhibiting behaviors it was trained to avoid or to break the rules set in the System Message. Such attacks can vary from intricate roleplay to subtle subversion of the safety objective. |
 |Indirect Attacks |Indirect Attacks, also referred to as Indirect Prompt Attacks or Cross-Domain Prompt Injection Attacks, are a potential vulnerability where third parties place malicious instructions inside of documents that the Generative AI system can access and process. Requires [document embedding and formatting](#embedding-documents-in-your-prompt). |
+| Groundedness<sup>2</sup> | Groundedness detection flags whether the text responses of large language models (LLMs) are grounded in the source materials provided by the users. Ungrounded material refers to instances where the LLMs produce information that is non-factual or inaccurate from what was present in the source materials. Requires [document embedding and formatting](#embedding-documents-in-your-prompt). |
 
-<sup>*</sup> If you're an owner of text material and want to submit text content for protection, [file a request](https://aka.ms/protectedmaterialsform).
+<sup>1</sup> If you're an owner of text material and want to submit text content for protection, [file a request](https://aka.ms/protectedmaterialsform).
 
+<sup>2</sup> Not available in non-streaming scenarios; only available for streaming scenarios. The following regions support Groundedness Detection: Central US, East US, France Central, and Canada East 
 
 [!INCLUDE [severity-levels text, four-level](../../content-safety/includes/severity-levels-text-four.md)]
 
@@ -328,24 +330,27 @@ When annotations are enabled as shown in the code snippets below, the following
 |indirect attacks|detected (true or false), </br>filtered (true or false)|
 |protected material text|detected (true or false), </br>filtered (true or false)|
 |protected material code|detected (true or false), </br>filtered (true or false), </br>Example citation of public GitHub repository where code snippet was found, </br>The license of the repository|
+|Groundedness | detected (true or false)</br>filtered (true or false) </br>details (`completion_end_offset`, `completion_start_offset`) |
 
 When displaying code in your application, we strongly recommend that the application also displays the example citation from the annotations. Compliance with the cited license may also be required for Customer Copyright Commitment coverage.
 
 See the following table for the annotation availability in each API version:
 
-|Category |2024-02-01 GA| 2024-04-01-preview | 2023-10-01-preview | 2023-06-01-preview| 
+|Category |2024-10-01-preview|2024-02-01 GA| 2024-04-01-preview | 2023-10-01-preview | 2023-06-01-preview| 
 |--|--|--|--|
-| Hate | ✅ |✅ |✅ |✅ |
-| Violence | ✅ |✅ |✅ |✅ |
-| Sexual |✅ |✅ |✅ |✅ |
-| Self-harm |✅ |✅ |✅ |✅ |
-| Prompt Shield for user prompt attacks|✅ |✅ |✅ |✅ |
-|Prompt Shield for indirect attacks|  | ✅ | | |
-|Protected material text|✅ |✅ |✅ |✅ |
-|Protected material code|✅ |✅ |✅ |✅ |
-|Profanity blocklist|✅ |✅ |✅ |✅ |
-|Custom blocklist| | ✅ |✅ |✅ |
-
+| Hate | ✅|✅ |✅ |✅ |✅ |
+| Violence | ✅|✅ |✅ |✅ |✅ |
+| Sexual |✅ |✅|✅ |✅ |✅ |
+| Self-harm |✅|✅|✅ |✅ |✅ |
+| Prompt Shield for user prompt attacks|✅|✅|✅ |✅ |✅ |
+|Prompt Shield for indirect attacks|   | | ✅ | | |
+|Protected material text|✅|✅ |✅ |✅ |✅ |
+|Protected material code|✅|✅ |✅ |✅ |✅ |
+|Profanity blocklist|✅|✅ |✅ |✅ |✅ |
+|Custom blocklist|✅| | ✅ |✅ |✅ |
+|Groundedness<sup>1</sup>|✅| |  | |  |
+
+<sup>1</sup> Not available in non-streaming scenarios; only available for streaming scenarios. The following regions support Groundedness Detection: Central US, East US, France Central, and Canada East 
 
 # [OpenAI Python 1.x](#tab/python-new)
 
@@ -710,6 +715,39 @@ violence  : @{filtered=False; severity=safe}
 
 For details on the inference REST API endpoints for Azure OpenAI and how to create Chat and Completions, follow [Azure OpenAI Service REST API reference guidance](../reference.md). Annotations are returned for all scenarios when using any preview API version starting from `2023-06-01-preview`, as well as the GA API version `2024-02-01`.
 
+### Groundedness
+
+#### Annotate only 
+
+Returns offsets referencing the ungrounded completion content. 
+
+```json
+{ 
+  "ungrounded_material": { 
+    "details": [ 
+       { 
+         "completion_end_offset": 127, 
+         "completion_start_offset": 27 
+       } 
+   ], 
+    "detected": true, 
+    "filtered": false 
+ } 
+} 
+```
+
+#### Annotate and filter 
+
+Blocks completion content when ungrounded completion content was detected. 
+
+```json
+{ "ungrounded_material": { 
+    "detected": true, 
+    "filtered": true 
+  } 
+} 
+```
+
 ### Example scenario: An input prompt containing content that is classified at a filtered category and severity level is sent to the completions API
 
 ```json
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタードキュメントの更新"
}
```

### Explanation
この変更は、OpenAIのコンテンツフィルタに関するドキュメントの更新を示しています。修正内容には、52行の追加と14行の削除が含まれ、全体で66行の変更が行われました。主な変更点としては、テキストやコードに関連する保護された材料の扱いや、生成AIモデルの挙動に関する新たなカテゴリの導入が挙げられます。

特に、「Groundedness」という新しいセクションが追加され、これは生成AIがユーザーに提供されたソース資料に基づいているかどうかを検出する機能に関する情報を提供しています。このセクションでは、未基底のコンテンツを検出し、フィルタリングする方法についても記述されています。また、APIのバージョンによって利用可能なAnnotationの可用性についてのテーブルも更新されており、生成AIが処理する可能性のある攻撃や保護すべき資料に関する対応状況が示されています。

全体的に、この修正はコンテンツフィルタの機能を明確にし、ユーザーがコンテンツをどのように管理・保護できるかに関する新たな情報を提供しています。

## articles/ai-services/openai/how-to/quota.md{#item-9440c2}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: mrbullwinkle
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 06/18/2024
+ms.date: 11/04/2024
 ms.author: mbullwin
 ---
 
@@ -233,6 +233,73 @@ This command runs in the context of the currently active subscription for Azure
 
 For more details on `az cognitiveservices account` and `az cognitivesservices usage` consult the [Azure CLI reference documentation](/cli/azure/cognitiveservices/account/deployment?view=azure-cli-latest&preserve-view=true)
 
+# [Azure PowerShell](#tab/powershell)
+
+Install the latest version of the [Az PowerShell module](/powershell/azure/install-azure-powershell). If you already have the Az PowerShell module installed locally, run `Update-Module -Name Az` to update to the latest version.
+
+To check which version of the Az PowerShell module you are running, use `Get-InstalledModule -Name Az`. Azure Cloud Shell is currently running a version of Azure PowerShell that can take advantage of the latest Azure OpenAI features.
+
+### Deployment
+
+```azurepowershell
+New-AzCognitiveServicesAccountDeployment
+   [-ResourceGroupName] <String>
+   [-AccountName] <String>
+   [-Name] <String>
+   [-Properties] <DeploymentProperties>
+   [-Sku] <Sku>
+   [-DefaultProfile <IAzureContextContainer>]
+   [-WhatIf]
+   [-Confirm]
+   [<CommonParameters>]
+```
+
+To sign into your local installation of Azure PowerShell, run the [Connect-AzAccount](/powershell/module/az.accounts/connect-azaccount) command:
+
+```azurepowershell
+Connect-AzAccount
+```
+
+By setting Sku Capacity to 10 in the command below, this deployment is set to a 10K TPM limit.
+
+```azurepowershell-interactive
+$cognitiveServicesDeploymentParams = @{
+    ResourceGroupName = 'test-resource-group'
+    AccountName = 'test-resource-name'
+    Name = 'test-deployment-name'
+    Properties = @{
+        Model = @{
+            Name = 'gpt-35-turbo'
+            Version = '0613'
+            Format  = 'OpenAI'
+        }
+    }
+    Sku = @{
+        Name = 'Standard'
+        Capacity = '10'
+    }
+}
+New-AzCognitiveServicesAccountDeployment @cognitiveServicesDeploymentParams
+```
+
+### Usage
+
+To [query your quota usage](/powershell/module/az.cognitiveservices/get-azcognitiveservicesusage) in a given region for a specific subscription:
+
+```azurepowershell
+Get-AzCognitiveServicesUsage -Location <location>
+```
+
+### Example
+
+```azurepowershell-interactive
+Get-AzCognitiveServicesUsage -Location eastus
+```
+
+This command runs in the context of the currently active subscription for Azure PowerShell. Use `Set-AzContext` to [modify the active subscription](/powershell/azure/manage-subscriptions-azureps#change-the-active-subscription).
+
+For more details on `New-AzCognitiveServicesAccountDeployment` and `Get-AzCognitiveServicesUsage`, consult the [Azure PowerShell reference documentation](/powershell/module/az.cognitiveservices/).
+
 # [Azure Resource Manager](#tab/arm)
 
 ```json
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure PowerShellの使用法に関する更新"
}
```

### Explanation
この変更は、Azure OpenAIに関する「Quota」ドキュメントのアップデートを示しています。具体的には、68行の追加と1行の削除が行われ、全体で69行の変更がなされています。主な変更の内容としては、Azure PowerShellに関連した新しい情報の追加が含まれます。

ドキュメントの最初の部分では、更新日が2024年11月4日に変更されており、その後にAzure PowerShellの最新バージョンのインストールおよびアップデート方法が記載されています。また、新たに「デプロイメント」および「使用法」というセクションが追加され、これには特定のコマンドが示されています。これにより、ユーザーは具体的なコマンド例を参考にしながら、Azure PowerShellを通じてコグニティブサービスのデプロイやクォータの使用状況を確認することができるようになっています。

特に、「Get-AzCognitiveServicesUsage」コマンドを使用して特定の地域内でのクォータの使用状況を照会する方法や、デプロイメントの例について詳しく説明されています。このような情報の追加により、ユーザーはAzure PowerShellを効率的に利用し、関連するサービスの管理が容易になります。


