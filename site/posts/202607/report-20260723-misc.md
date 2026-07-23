---
date: '2026-07-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1958566...MicrosoftDocs:d74629f
summary: この変更では、Azure Languageサービスのデプロイメントにおけるセキュリティのベストプラクティスが紹介された新しいドキュメントが追加されました。目次ファイルも更新され、セキュリティとコンプライアンスに関するセクションが追加されています。破壊的な変更はないものの、目次構造の変更には注意が必要です。このアップデートは、機密性の高いデータを扱う自然言語処理ワークフローにおいて、セキュリティの重要性を再認識させ、適切なガイドラインが提供されていることが特徴です。この結果、企業はAzure
  Languageサービスをより安心して利用できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1958566...MicrosoftDocs:d74629f){target="_blank"}

<format>
# ハイライト
この変更では、新しいドキュメントが追加され、Azure Languageサービスのデプロイメントにおけるセキュリティのベストプラクティスが提供されました。また、関連する目次ファイルが更新され、セキュリティとコンプライアンスに関連するセクションが追加されました。

## 新機能
- Azure Languageサービスの安全なデプロイメントガイドの追加。
- セキュリティとコンプライアンスに関する新しいセクションを目次に追加。

## 破壊的変更
- 特に破壊的な変更はありませんが、目次構造の変更に注意が必要です。

## その他の更新
- 重複する目次エントリの削除とリンクの更新。

# インサイト
このコード変更は、Azure Languageサービスのデプロイメントにおいてセキュリティを高めることに焦点を当てた重要なアップデートです。自然言語処理ワークフローで扱うデータは機密性が高いため、セキュリティのベストプラクティスを適用することが重要です。この新しいガイドは、サービス特有のセキュリティ、デプロイメントの考慮事項、アイデンティティとアクセス管理、ネットワークセキュリティ、データ保護、監視とロギング、そしてコンプライアンスとガバナンスといった多岐にわたる側面をカバーしています。

特に、組織がAzure Languageサービスを使用する際のリスクを軽減し、セキュリティを強化するための具体的な方法を明確に示しています。このようなガイドラインは、プライバシー侵害の可能性を最小限に抑え、規制への準拠を容易にします。

また、目次ファイルの構成を変更することで、ユーザーが必要な情報により効率的にアクセスできるようになりました。セキュリティとコンプライアンスセクションの追加は、Azureのサービス利用におけるセキュリティの重要性を再認識させるものであり、適切な実装を促進します。これにより、企業は安心してAzure Languageサービスを利用できるようになると期待されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [secure-deployment.md](#item-3f47d4) | new feature | Azure Languageサービスの安全なデプロイメント | added | 112 | 0 | 112 | 
| [toc.yml](#item-12f1f0) | minor update | AIサービスのセクション更新 | modified | 13 | 26 | 39 | 


# Modified Contents
## articles/ai-services/language-service/secure-deployment.md{#item-3f47d4}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,112 @@
+---
+title: Secure your Azure Language data and deployment
+titleSuffix: Foundry Tools
+description: Learn how to secure Azure Language, with best practices for protecting your data and deployment.
+author: laujan
+manager: mcleans
+ms.service: azure-ai-language
+ms.topic: best-practice
+ms.date: 07/16/2026
+ms.author: lajanuar
+ms.custom: horz-security
+---
+
+<!-- markdownlint-disable MD025 -->
+# Secure your Azure Language data and deployment
+
+Azure Language in Foundry Tools is a cloud-based service that provides Natural Language Processing (NLP) capabilities for understanding and analyzing text across applications, workflows, and business processes. When organizations integrate this service, they can extract insights, classify content, and detect sensitive information across many languages.
+
+- **Security within Azure is grounded in a collaborative model, where Microsoft and customers share the responsibility for protecting resources and data.**
+
+- **Microsoft is dedicated to securing the core infrastructure that underpins all Azure services, providing a reliable and robust foundation for cloud operations.**
+
+- **Customers play a crucial role in this security partnership by ensuring that Azure Language is properly configured and managed, thereby protecting sensitive information and adhering to all relevant regulatory requirements.**
+
+- **By clearly understanding and fulfilling their respective responsibilities, both Microsoft and customers work together to achieve a comprehensive and resilient security posture in the Azure environment.**
+
+For more information, *see* [**Shared responsibility in the cloud**](/azure/security/fundamentals/shared-responsibility).
+
+This document offers detailed guidelines and practical recommendations for establishing and maintaining a secure environment when using Azure Language. It's essential for users of any service to prioritize the protection of sensitive data, safeguard user privacy, and ensure deployment reliability. By adhering to these best practices, you help reduce risks and guarantee that your language solutions remain secure and effective across all platforms.
+
+## Service-specific security
+
+Azure Language requires careful consideration of specific security challenges and requirements to maintain the confidentiality and integrity of natural language processing workflows. By taking a proactive approach to these security concerns, you can protect sensitive information during processing and reduce the risk of unauthorized access or data breaches. The following guidance is organized by [core capabilities](overview.md#core-capabilities), which are recommended for new development, and [legacy capabilities](overview.md#legacy-capabilities), which are supported for existing implementations.
+
+### Core capabilities
+
+- **Personally identifiable information (PII) detection**: For workflows that process sensitive content, use PII detection to identify and redact personal data before storing, sharing, or displaying text and conversations. Redacting sensitive values reduces the risk of unintended exposure downstream. To narrow output to protected health information, set the `domain=phi` parameter. By default, the service temporarily stores and encrypts submitted input for up to 48 hours to support troubleshooting. Set `loggingOptOut=true` to prevent this temporary storage. For more information, *see* [What is personally identifiable information (PII) detection](personally-identifiable-information/overview.md).
+- **Language detection**: When routing or preprocessing untrusted input based on detected language, validate and sanitize the text before passing it to downstream systems to avoid propagating malicious content. For more information, *see* [What is language detection](language-detection/overview.md).
+- **Named entity recognition (NER)**: Prebuilt NER can surface sensitive entities such as names, locations, and organizations from unstructured text. Apply appropriate access controls to both the input text and the extracted results, and consider pairing NER with PII detection when handling confidential content. When redacting, use the `piiCategories` parameter to explicitly specify which entity categories to detect, so that sensitive values you intend to redact aren't inadvertently left exposed. For more information, *see* [What is named entity recognition (NER)](named-entity-recognition/overview.md).
+- **Custom NER**: To ensure the security of proprietary schemas, labels, and domain-specific language, set up robust access controls for custom NER projects. Your labeled training data is stored in your own Azure Blob Storage account, and trained models are retained by the service until you delete them, so restrict access to that storage account and remove models you no longer need. Text submitted for extraction isn't stored by the service. For more information, *see* [What is custom named entity recognition](custom-named-entity-recognition/overview.md).
+- **Text analytics for health**: When processing clinical or health-related text, protect any protected health information (PHI) surfaced during extraction. Establish secure handling and access controls for both source text and results. Temporary input logging is disabled by default (`loggingOptOut=true`) for health processing, and the capability can run in a container for on-premises or isolated environments. For more information, *see* [What is Text Analytics for health](text-analytics-for-health/overview.md).
+
+### Legacy capabilities
+
+- **Conversational language understanding (CLU)**: Restrict access to CLU projects, models, and training utterances, which can contain sensitive intents and domain-specific language. Apply least-privilege access controls to protect these proprietary assets. For more information, *see* [What is conversational language understanding](conversational-language-understanding/overview.md).
+- **Custom text classification**: Protect the classes, labels, and training documents that define your custom classification models by restricting access to both the models and their underlying training data. Your labeled dataset is stored in your own Azure Blob Storage account, and the service retains trained models until you delete them, so secure that storage account and remove unused models. The service doesn't store text submitted for classification. For more information, *see* [What is custom text classification](custom-text-classification/overview.md).
+- **Entity linking**: When disambiguating entities and returning external links, validate and sanitize returned content before displaying it to end users to avoid surfacing untrusted references. For more information, *see* [What is entity linking](entity-linking/overview.md).
+- **Key phrase extraction**: Apply appropriate access controls to input text and extracted key phrases, which can reveal the substance of confidential documents. For more information, *see* [What is key phrase extraction](key-phrase-extraction/overview.md).
+- **Orchestration workflow**: Because orchestration connects CLU and custom question answering projects, secure each connected project and enforce consistent access controls across the workflow. For more information, *see* [What is orchestration workflow](orchestration-workflow/overview.md).
+- **Question answering**: Secure the knowledge bases and source content that power question answering, and apply access controls to prevent unauthorized users from viewing or modifying answers. Knowledge bases and chat logs are stored in your own Azure resources (Azure AI Search and, when diagnostic logging is enabled, Azure Monitor), so apply role-based access control to those resources and enable chat logging only when needed. For more information, *see* [What is question answering](question-answering/overview.md).
+- **Sentiment analysis and opinion mining**: Apply access controls to the text you analyze and to the sentiment results, which can reveal sensitive customer or business information. For more information, *see* [What is sentiment analysis and opinion mining](sentiment-opinion-mining/overview.md).
+- **Summarization**: When summarizing text or conversations, protect both the source content and the generated summaries, which can retain sensitive information. For more information, *see* [What is summarization](summarization/overview.md).
+
+### Deployment considerations
+
+The following options apply across core and legacy capabilities:
+
+- **Native document support**: When processing documents, ensure secure workflows are established. Use secure storage containers with appropriate access controls and encryption to safeguard both the original documents and the processed outputs. For more information, *see* [Native document support for Azure Language](native-document-support/overview.md).
+- **Azure Language containers**: For scenarios that require high security or offline processing in isolated environments, consider deploying Language containers. This deployment model is well-suited for safeguarding sensitive data and supporting processing workflows in controlled or disconnected environments. For more information, *see* [Configure Language docker containers](concepts/configure-containers.md).
+
+## Identity and access management
+
+Effectively overseeing identities and access permissions is crucial for protecting your Azure Language deployments from unauthorized use and possible credential compromise. By enforcing secure access management, you guarantee that only approved users and devices can interact with your Language resource. The following list identifies ways you can support secure access management:
+
+- **Access**. To effectively manage user identities and securely control access permissions for your Azure Language resources, enable Microsoft Entra ID. By integrating Microsoft Entra ID, you can streamline the administration of user accounts and ensure that only authorized individuals have access to your Azure Language services. For more information, *see* [Enable Microsoft Entra authentication](concepts/role-based-access-control.md#enable-microsoft-entra-authentication).
+- **Authorization**. Grant only the permissions that are essential for each role using role-based access control (RBAC). By utilizing RBAC-managed identities, you uphold the principle of least privilege, ensuring that users receive only the access required to perform their specific tasks. This approach greatly minimizes the possibility of unauthorized access to sensitive information or critical functions within your resource. For more information, *see* [Language role-based access control](concepts/role-based-access-control.md).
+- **Authentication**. Access to Language data should be limited solely to entities that successfully complete authentication. This restriction requires users to complete verification and receive authorization before they can view or modify Language data. This approach provides a layer of security by making certain that unauthorized users can't access sensitive information or make changes that could impact the integrity of the data. For more information, *see* [Authenticate requests to Foundry Tools](/azure/ai-services/authentication).
+- **Azure Key Vault**. Azure Key Vault offers a secure, centralized repository for application secrets like database connection strings, API keys, customer-managed keys (CMK), passwords, and cryptographic keys. Using the key vault eliminates the need to hard-code sensitive information directly into application code or configuration files, reducing the risk of accidental exposure. For more information, *see* [About Azure Key Vault](/azure/key-vault/general/overview). For Language encryption key management, *see* [Language service encryption of data at rest](concepts/encryption-data-at-rest.md).
+
+    > [!TIP]
+    > ✔️ **Rotate API keys regularly**: Keys in Azure Key Vault can be configured with rotation policies that automatically generate new key versions at specified frequencies. Regularly rotating your Language API keys mitigates the risk of compromised credentials being used to access your services. For more information, *see* [Key autorotation](/azure/key-vault/general/autorotation).
+
+## Network security
+
+Azure Language processes sensitive data from your applications. Therefore, it's essential to establish strong network isolation measures to prevent unauthorized access and ensure that content remains secure. The following list outlines key practices to help you manage secure access effectively:
+
+- **Configure private endpoints**: Increase shielding by configuring private endpoints for API requests. This approach strengthens security and provides enhanced network isolation for your Azure Language resources. For more information, *see* [Use private endpoints with Foundry Tools](/azure/ai-services/cognitive-services-virtual-networks#use-private-endpoints).
+- **Implement virtual network service endpoints**: Augment safeguards by restricting network access to allow only traffic originating from your Azure virtual network. At the same time, ensure that you maintain optimal routing by utilizing the Microsoft backbone network for all communications. For more information, *see* [Configure virtual networks for Foundry Tools](/azure/ai-services/cognitive-services-virtual-networks).
+- **Configure firewall rules**: Enhance security by designating specific IP addresses or ranges that are permitted to access your Language resource. Restricting access in this way minimizes the likelihood of unauthorized connections from unfamiliar networks. For more information, *see* [Configure Foundry Tools virtual networks](/azure/ai-services/cognitive-services-virtual-networks#grant-access-from-an-internet-ip-range).
+
+## Data protection
+
+Azure Language processes sensitive text and document content. Because of the confidential nature of this information, implementing robust data protection measures is essential. These safeguards are vital not only to maintain the privacy and confidentiality of the data being processed but also to ensure compliance with relevant regulations and industry standards.
+
+- **Enable data encryption at rest**: Ensure your data is automatically encrypted with Federal Information Processing Standard (FIPS) 140-2 compliant 256-bit Advanced Encryption Standard (AES) when stored by the service. For more information, *see* [Language service encryption of data at rest](concepts/encryption-data-at-rest.md).
+- **Implement customer-managed keys (CMK)**: To achieve enhanced control over encryption key management, configure customer-managed keys for Language resources by integrating Azure Key Vault. This capability is accessible when selecting a pricing tier that includes support for customer-managed key functionality. For more information, *see* [Customer-managed keys with Azure Key Vault](concepts/encryption-data-at-rest.md#customer-managed-keys-with-azure-key-vault).
+- **Review data retention and privacy details**: Understand how Azure Language handles the data you submit, including what's retained during processing and how customer data is protected. For more information, *see* [Data, privacy, and security for Azure Language](/azure/ai-foundry/responsible-ai/language-service/data-privacy).
+- **Follow data residency requirements**: To ensure that your deployment adheres to regional data residency regulations, select the designated region for your Language resource. Use supported regions to remain compliant with local requirements. For more information, *see* [Region support for Azure Language](concepts/regional-support.md).
+
+## Logging and monitoring
+
+Establishing robust logging and monitoring is critical for identifying potential security threats and resolving issues within your Azure Language deployment. By ensuring that all relevant activities and anomalies are thoroughly tracked, you can enhance your overall security posture and streamline troubleshooting processes throughout your cloud-based language environment.
+
+- **Enable diagnostic logging**: Configure Azure Monitor to collect and analyze logs from your Language resource to identify potential security issues, track usage patterns, and troubleshoot problems. For more information, *see* [Monitor Azure resources with Azure Monitor](/azure/azure-monitor/platform/monitor-azure-resource).
+- **Set up alerts for unusual activity**: Create Azure Monitor alerts to notify you of abnormal usage patterns, potential security breaches, or service disruptions affecting your Language resources. For more information, *see* [Create, view, and manage metric alerts using Azure Monitor](/azure/azure-monitor/alerts/alerts-metric).
+- **Configure audit logs**: Enable and review audit logs to monitor access and changes to your Language resources. Audit logs ensure you know who is using your service and what actions are being performed. For more information, *see* [Resource logs in Azure Monitor](/azure/azure-monitor/platform/resource-logs).
+- **Implement request rate monitoring**: Monitor API request rates to detect potential denial of service attacks or unauthorized usage, ensuring your service remains available for legitimate use. For more information, *see* [Service limits for Azure Language](concepts/data-limits.md).
+
+## Compliance and governance
+
+To ensure the secure operation of Azure Language services, put a robust governance framework in place and consistently comply with all relevant standards. By establishing thorough policies and procedures, you can effectively protect your systems, maintain regulatory compliance, and minimize potential risks. This approach helps you deliver a reliable and secure service.
+
+- **Review Azure Policy for Foundry Tools**: Implement Azure Policy to enforce organization-wide security standards for your Foundry Tools, including network isolation requirements. For more information, *see* [Azure Policy Regulatory Compliance controls for Foundry Tools](/azure/ai-services/security-controls-policy#microsoft-cloud-security-benchmark).
+- **Conduct regular security assessments**: Continuously assess the security status of your Language deployments and ensure they align with industry standards and organizational policies. Promptly detect and address any potential vulnerabilities as they arise. For more information, *see* [Microsoft cloud security benchmark](/security/benchmark/azure/introduction).
+- **Maintain regulatory compliance**: Configure your Language resource to comply with all relevant laws and regulations that apply to your industry and geographic area. Pay special attention to any requirements related to data privacy and protection. For more information, *see* [Transparency note for Azure Language](/azure/ai-foundry/responsible-ai/language-service/transparency-note).
+- **Implement human oversight**: For sensitive scenarios, implement a human review workflow to verify output accuracy. This process ensures that all content complies with organizational standards before wide distribution. For more information, *see* [Guidance for integration and responsible use](/azure/ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use).
+
+## Related content
+
+- [Microsoft Cloud Security Benchmark – Foundry Tools](/security/benchmark/azure/baselines/azure-openai-security-baseline)
+- [Well-Architected Framework – AI workloads](/azure/well-architected/ai/design-principles)
+- [Security documentation for Foundry Tools](/azure/ai-services/security-features)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure Languageサービスの安全なデプロイメント"
}
```

### Explanation
この変更では、Azure Languageサービスを使用する際のデータとデプロイメントのセキュリティに関する詳細なガイドラインを提供する新しい文書が追加されました。具体的には、Azure Languageのセキュリティに関するベストプラクティスと推奨事項が含まれており、機密情報の保護やユーザーのプライバシーの確保が重要であることが強調されています。

文書は、以下の主要なセクションで構成されています：

1. **サービス特有のセキュリティ**: 自然言語処理のワークフローにおける特定のセキュリティ課題に対処するためのガイダンスを提供し、個人情報の検出や言語の検出、名前付き実体認識（NER）などの基本的な能力に関する推奨事項を記載しています。

2. **デプロイメントの考慮事項**: Azure Languageを安全にデプロイするためのオプションとして、ドキュメント管理やAzure Languageコンテナの使用について言及されています。

3. **アイデンティティとアクセス管理**: ユーザーのアイデンティティとアクセス権限を効果的に管理する方法について説明し、安全なアクセス管理を確保するための手法を提案しています。

4. **ネットワークセキュリティ**: Azure Languageリソースへのアクセスを制限するための安全なネットワーク設定に関する推奨事項が含まれています。

5. **データ保護**: 機密情報の処理におけるデータ保護措置を強調し、暗号化やデータ管理の重要性について言及しています。

6. **監視とロギング**: Azure Languageデプロイメント内でのセキュリティ脅威の特定や問題解決のために、ロギングと監視の重要性を説明しています。

7. **コンプライアンスとガバナンス**: セキュリティ運用を維持するためのガバナンスフレームワークの重要性を強調し、関係する法令や規制の遵守が求められています。

この文書は、Azure Languageサービスを利用する組織がリスクを軽減し、セキュリティを高めるために必要な情報を提供します。また、この新しいガイドラインによって、適切なセキュリティ状況の維持と規制順守が促進されます。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -28,6 +28,15 @@ items:
   - name: Migrate to Microsoft Foundry
     href: migration-studio-to-foundry.md
     displayName: migrate, foundry, studio, permissions, roles, access, requisites, requirements
+
+- name: Security and compliance
+  items:
+  - name: Secure deployment
+    href: secure-deployment.md
+    displayName: security, data protection, encryption, secure deployment
+  - name: Data privacy and security
+    href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
+    displayName: data privacy, logging, data retention    
 - name: Core capabilities
   items:
 
@@ -112,9 +121,6 @@ items:
       - name: Integration and responsible use
         href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
         displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-        displayName: Data privacy, logging, data retention
 
   - name: Language detection
     items:
@@ -133,9 +139,6 @@ items:
       - name: Integration and responsible use
         href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
         displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-        displayName: Data privacy, logging, data retention
     - name: How-to guides
       items:
       - name: Call the API
@@ -227,9 +230,6 @@ items:
         - name: Integration and responsible use
           href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
           displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-        - name: Data, privacy, and security
-          href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-          displayName: Data privacy, logging, data retention
       - name: How-to guides
         items:
         - name: Call NER
@@ -279,9 +279,6 @@ items:
       - name: Integration and responsible use
         href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
         displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-        displayName: Data privacy, logging, data retention
     - name: How-to guides
       items:
       - name: How to call the API
@@ -575,10 +572,6 @@ items:
       - name: Integration and responsible use
         href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
         displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-        displayName: Data privacy, logging, data retention
-    
 
   - name: Key phrase extraction
     items:
@@ -618,9 +611,6 @@ items:
       - name: Integration and responsible use
         href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
         displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-        displayName: Data privacy, logging, data retention
 
   - name: Orchestration workflow
     items:
@@ -706,9 +696,6 @@ items:
         - name: Integration and responsible use
           href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
           displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-        - name: Data, privacy, and security
-          href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-          displayName: Data privacy, logging, data retention
 
   - name: Summarization
     items:
@@ -746,10 +733,7 @@ items:
         displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
       - name: Characteristics and limitations
         href: ../../ai-foundry/responsible-ai/language-service/characteristics-and-limitations-summarization.md
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-        displayName: Data privacy, logging, data retention
-
+      
 - name: Azure Language concepts
   items:
   - name: Developer guide
@@ -906,6 +890,9 @@ items:
         href: /training/paths/build-custom-text-analytics
     - name: Enterprise readiness
       items:
+      - name: Secure your data and deployment
+        href: secure-deployment.md
+        displayName: security, secure deployment, best practices, network isolation, encryption, compliance
       - name: Virtual networks
         href: ../cognitive-services-virtual-networks.md?context=/azure/ai-services/language-service/context/context
       - name: Microsoft Foundry security
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIサービスのセクション更新"
}
```

### Explanation
この変更では、Azure Languageサービスの目次ファイル（toc.yml）に対して複数の修正が加えられました。具体的には、セキュリティおよびコンプライアンスに関連する新しいセクションが追加され、不必要な項目が削除されました。

主な変更点は以下の通りです：

1. **セクションの追加**:
   - 「Security and compliance」という新しい大項目が追加され、その下にセキュアなデプロイメントに関する項目とデータプライバシーおよびセキュリティに関する項目が挿入されました。これにより、ユーザーがセキュリティ関連の情報に簡単にアクセスできるようになります。

2. **既存の項目の削除**:
   - 「Data, privacy, and security」という項目が複数の場所から削除され、重複していた情報が整理されました。

3. **ハイパーリンクの更新**:
   - 新しく追加されたリンクは、ユーザーがアクセスする際に便宜が図られるようにオーガナイズされています。

全体的に、これらの変更によって、文書はより構造的に整理され、セキュリティとコンプライアンスに関する重要な情報が強調されるようになっています。これにより、Azure Languageサービスの利用者は必要な情報によりアクセスしやすくなることが期待されます。


